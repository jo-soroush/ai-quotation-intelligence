"""Static import-direction check for every classified package module.

This does not inspect dynamic imports, runtime objects, or semantic misuse.
"""

import ast
from importlib.util import resolve_name
from pathlib import Path

import pytest


PACKAGE_NAME = "ai_quotation_intelligence"
REPOSITORY = Path(__file__).resolve().parents[1]
PACKAGE = REPOSITORY / "src" / PACKAGE_NAME
EVALUATION_PACKAGE = REPOSITORY / "evaluation"
CORE = "CORE"
PROVIDER = "PROVIDER"
AGENT_TOOL = "AGENT_TOOL"
AGENT = "AGENT"
REVIEW = "REVIEW"
EXPORT = "EXPORT"
APPLICATION_BOUNDARY = "APPLICATION_BOUNDARY"
SUPPORT = "SUPPORT"
CATEGORIES = {CORE, PROVIDER, AGENT_TOOL, AGENT, REVIEW, EXPORT, APPLICATION_BOUNDARY, SUPPORT}
FORBIDDEN_FROM_CORE = {PROVIDER, AGENT_TOOL, AGENT, REVIEW, EXPORT, APPLICATION_BOUNDARY}
# C10 may orchestrate C09 and call Core's existing calculation/domain owners.
# C08's adapter is injected through a provider-neutral client protocol, so
# Agent requires no Provider or Support import permission.
# C11 review may use Core contracts/arithmetic only; Agent, Agent Tool,
# Provider, Support, Core, and future Application modules cannot import Review.
# C12 export needs only C11's held approval gate and Core's domain/arithmetic;
# no other existing category except C13's application adapter may import Export.
# C13 uses an injected C10 runner protocol; only Core, Review, and Export are imported.
# C16 permits an exact observability-only Support module import from the
# application/agent/tool boundaries, without granting general Support access.
ALLOWED_LOCAL_DEPENDENCIES = {
    CORE: {CORE, SUPPORT},
    SUPPORT: {SUPPORT},
    PROVIDER: {CORE, SUPPORT},
    AGENT_TOOL: {CORE},
    AGENT: {CORE, AGENT_TOOL},
    REVIEW: {CORE},
    EXPORT: {CORE, REVIEW},
    APPLICATION_BOUNDARY: {CORE, REVIEW, EXPORT},
}
# boto3 is declared in pyproject.toml; botocore is its imported SDK boundary.
PROVIDER_SDK_ROOTS = {"boto3", "botocore"}

# This is a complete classification, not a scan list. Discovery below fails
# when a new or moved Python file is not classified, including __init__.py.
MODULE_CATEGORIES = {
    "__init__.py": CORE,
    "domain/__init__.py": CORE,
    "domain/models.py": CORE,
    "data/__init__.py": CORE,
    "data/synthetic_history.py": CORE,
    "calculation.py": CORE,
    "comparison.py": CORE,
    "retrieval.py": CORE,
    "risk_evidence.py": CORE,
    "storage_contract.py": CORE,
    "bedrock.py": PROVIDER,
    "s3_storage.py": PROVIDER,
    "agent_tools.py": AGENT_TOOL,
    "quotation_agent.py": AGENT,
    "human_review.py": REVIEW,
    "excel_export.py": EXPORT,
    "api.py": APPLICATION_BOUNDARY,
    "config.py": SUPPORT,
    "logging_config.py": SUPPORT,
}

# C17 is a separate offline owner, not a production architecture category.
# Keep its complete module inventory explicit so new files cannot appear
# without an architecture decision and test update.
EVALUATION_MODULES = {"__init__.py", "c17.py"}


def _module_name(relative_path: str) -> str:
    parts = list(Path(relative_path).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join((PACKAGE_NAME, *parts))


def _import_targets(tree: ast.AST, source_module: str, is_package: bool) -> list[str]:
    targets: list[str] = []
    source_package = source_module if is_package else source_module.rpartition(".")[0]
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            targets.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                base = resolve_name("." * node.level + base, source_package)
            targets.append(base)
            targets.extend(f"{base}.{alias.name}" for alias in node.names if alias.name != "*")
    return targets


def _local_category(target: str, modules: dict[str, str]) -> str | None:
    parts = target.split(".")
    while parts:
        category = modules.get(".".join(parts))
        if category is not None:
            return category
        parts.pop()
    return None


def _validate_policy(policy: dict[str, set[str]]) -> None:
    assert set(policy) == CATEGORIES, "architecture policy must cover every category"
    assert all(targets <= CATEGORIES for targets in policy.values()), "unknown policy target category"
    reachable = {CORE}
    pending = [CORE]
    while pending:
        for target in policy[pending.pop()] - reachable:
            reachable.add(target)
            pending.append(target)
    assert not reachable & FORBIDDEN_FROM_CORE, "unsafe dependency policy: Core can reach a forbidden category"


def validate_architecture(
    package: Path,
    categories: dict[str, str],
    policy: dict[str, set[str]] = ALLOWED_LOCAL_DEPENDENCIES,
) -> None:
    _validate_policy(policy)
    discovered = {path.relative_to(package).as_posix() for path in package.rglob("*.py")}
    missing = discovered - categories.keys()
    stale = categories.keys() - discovered
    assert not missing and not stale, (
        f"unclassified modules: {sorted(missing)}; stale classifications: {sorted(stale)}"
    )
    invalid = {path: category for path, category in categories.items() if category not in CATEGORIES}
    assert not invalid, f"invalid architecture categories: {invalid}"

    modules = {_module_name(path): category for path, category in categories.items()}
    assert len(modules) == len(categories), "module names must be unique"
    violations: list[str] = []
    for relative_path, category in sorted(categories.items()):
        source_module = _module_name(relative_path)
        source = (package / relative_path).read_text(encoding="utf-8")
        for target in _import_targets(
            ast.parse(source, filename=relative_path),
            source_module,
            relative_path.endswith("/__init__.py") or relative_path == "__init__.py",
        ):
            external_provider = target.split(".")[0] in PROVIDER_SDK_ROOTS
            target_category = _local_category(target, modules)
            c16_logging_only = (
                category in {APPLICATION_BOUNDARY, AGENT, AGENT_TOOL}
                and (target == f"{PACKAGE_NAME}.logging_config"
                     or target.startswith(f"{PACKAGE_NAME}.logging_config."))
            )
            if (external_provider and category != PROVIDER) or (
                target_category is not None and target_category not in policy[category]
                and not c16_logging_only
            ):
                violations.append(f"{relative_path} -> {target}")

    assert not violations, "forbidden architecture imports: " + ", ".join(violations)


def _fixture_package(tmp_path: Path) -> tuple[Path, dict[str, str]]:
    package = tmp_path / PACKAGE_NAME
    package.mkdir()
    (package / "__init__.py").write_text("", encoding="utf-8")
    return package, {"__init__.py": CORE}


def _add_module(package: Path, relative_path: str, source: str = "") -> None:
    path = package / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(source, encoding="utf-8")


def test_actual_package_tree_has_complete_classification_and_valid_imports() -> None:
    validate_architecture(PACKAGE, MODULE_CATEGORIES)


def test_c17_evaluation_owner_is_complete_and_outside_production_package() -> None:
    discovered = {
        path.relative_to(EVALUATION_PACKAGE).as_posix()
        for path in EVALUATION_PACKAGE.rglob("*.py")
    }
    assert discovered == EVALUATION_MODULES
    assert not (PACKAGE / "evaluation").exists()


def test_production_runtime_does_not_import_offline_evaluation() -> None:
    violations: list[str] = []
    for relative_path in sorted(MODULE_CATEGORIES):
        source = (PACKAGE / relative_path).read_text(encoding="utf-8")
        module = _module_name(relative_path)
        targets = _import_targets(
            ast.parse(source, filename=relative_path),
            module,
            relative_path.endswith("/__init__.py") or relative_path == "__init__.py",
        )
        if any(target == "evaluation" or target.startswith("evaluation.") for target in targets):
            violations.append(relative_path)
    assert not violations, f"production modules import evaluation: {violations}"


def test_c17_evaluation_has_no_provider_sdk_or_production_boundary_dependency() -> None:
    source = (EVALUATION_PACKAGE / "c17.py").read_text(encoding="utf-8")
    targets = _import_targets(ast.parse(source, filename="evaluation/c17.py"), "evaluation.c17", False)
    forbidden = {
        "boto3", "botocore", "ai_quotation_intelligence.bedrock",
        "ai_quotation_intelligence.api", "ai_quotation_intelligence.s3_storage",
    }
    violations = sorted(
        target for target in targets
        if any(target == item or target.startswith(f"{item}.") for item in forbidden)
    )
    assert not violations, f"evaluation imports live/provider boundary: {violations}"


@pytest.mark.parametrize("source_path,category", [
    ("api.py", APPLICATION_BOUNDARY),
    ("quotation_agent.py", AGENT),
    ("agent_tools.py", AGENT_TOOL),
])
def test_c16_allows_only_logging_support_import(tmp_path: Path, source_path: str, category: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, source_path, "from .logging_config import emit_event\n")
    _add_module(package, "logging_config.py", "import logging\n")
    _add_module(package, "config.py", "")
    categories.update({source_path: category, "logging_config.py": SUPPORT, "config.py": SUPPORT})
    validate_architecture(package, categories)
    _add_module(package, source_path, "from .config import load_settings\n")
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


def test_human_review_is_separate_authority_with_core_only_dependency() -> None:
    assert MODULE_CATEGORIES["human_review.py"] == REVIEW
    assert ALLOWED_LOCAL_DEPENDENCIES[REVIEW] == {CORE}
    validate_architecture(PACKAGE, MODULE_CATEGORIES)
    for category in CATEGORIES - {REVIEW, EXPORT, APPLICATION_BOUNDARY}:
        assert REVIEW not in ALLOWED_LOCAL_DEPENDENCIES[category]


def test_excel_export_has_only_review_and_core_dependencies() -> None:
    assert MODULE_CATEGORIES["excel_export.py"] == EXPORT
    assert ALLOWED_LOCAL_DEPENDENCIES[EXPORT] == {CORE, REVIEW}
    validate_architecture(PACKAGE, MODULE_CATEGORIES)
    for category in CATEGORIES - {EXPORT, APPLICATION_BOUNDARY}:
        assert EXPORT not in ALLOWED_LOCAL_DEPENDENCIES[category]


def test_api_least_privilege_and_no_reverse_authority() -> None:
    assert MODULE_CATEGORIES["api.py"] == APPLICATION_BOUNDARY
    assert ALLOWED_LOCAL_DEPENDENCIES[APPLICATION_BOUNDARY] == {CORE, REVIEW, EXPORT}
    for category in CATEGORIES - {APPLICATION_BOUNDARY}:
        assert APPLICATION_BOUNDARY not in ALLOWED_LOCAL_DEPENDENCIES[category]
    validate_architecture(PACKAGE, MODULE_CATEGORIES)


def test_s3_storage_reuses_provider_with_only_existing_core_support_directions() -> None:
    assert MODULE_CATEGORIES["storage_contract.py"] == CORE
    assert MODULE_CATEGORIES["s3_storage.py"] == PROVIDER
    assert ALLOWED_LOCAL_DEPENDENCIES[PROVIDER] == {CORE, SUPPORT}
    assert PROVIDER not in ALLOWED_LOCAL_DEPENDENCIES[CORE]
    assert PROVIDER not in ALLOWED_LOCAL_DEPENDENCIES[REVIEW]
    assert PROVIDER not in ALLOWED_LOCAL_DEPENDENCIES[EXPORT]
    assert PROVIDER not in ALLOWED_LOCAL_DEPENDENCIES[APPLICATION_BOUNDARY]
    validate_architecture(PACKAGE, MODULE_CATEGORIES)


@pytest.mark.parametrize("source_path,category", [
    ("calculation.py", CORE), ("human_review.py", REVIEW),
    ("excel_export.py", EXPORT), ("api.py", APPLICATION_BOUNDARY),
    ("agent_tools.py", AGENT_TOOL), ("quotation_agent.py", AGENT),
    ("config.py", SUPPORT),
])
def test_nonprovider_boundaries_cannot_import_s3_adapter(
    tmp_path: Path, source_path: str, category: str,
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, source_path, "from .s3_storage import S3StorageAdapter\n")
    _add_module(package, "s3_storage.py")
    categories.update({source_path: category, "s3_storage.py": PROVIDER})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source", [
    "from .bedrock import BedrockConverseAdapter\n",
    "from .agent_tools import AgentTools\n",
    "from .quotation_agent import QuotationAgent\n",
    "from .config import Settings\n",
    "import boto3\n",
])
def test_api_rejects_provider_tool_support_or_sdk_import(tmp_path: Path, source: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "api.py", source)
    for path, category in (("bedrock.py", PROVIDER), ("agent_tools.py", AGENT_TOOL),
                           ("quotation_agent.py", AGENT),
                           ("config.py", SUPPORT)):
        _add_module(package, path)
        categories[path] = category
    categories["api.py"] = APPLICATION_BOUNDARY
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source", [
    "from .quotation_agent import QuotationAgent\n",
    "from .agent_tools import AgentTools\n",
    "from .bedrock import BedrockConverseAdapter\n",
    "from .config import Settings\n",
    "import boto3\n",
])
def test_export_rejects_agent_tool_provider_and_support_imports(
    tmp_path: Path, source: str,
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "excel_export.py", source)
    for name, category in (
        ("quotation_agent.py", AGENT), ("agent_tools.py", AGENT_TOOL),
        ("bedrock.py", PROVIDER), ("config.py", SUPPORT),
    ):
        _add_module(package, name)
        categories[name] = category
    categories["excel_export.py"] = EXPORT
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source_path,category", [
    ("calculation.py", CORE), ("human_review.py", REVIEW),
    ("quotation_agent.py", AGENT), ("agent_tools.py", AGENT_TOOL),
    ("config.py", SUPPORT), ("bedrock.py", PROVIDER),
])
def test_other_categories_cannot_import_export(
    tmp_path: Path, source_path: str, category: str,
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, source_path, "from .excel_export import export_approved_quote\n")
    _add_module(package, "excel_export.py")
    categories.update({source_path: category, "excel_export.py": EXPORT})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source_path,category", [
    ("quotation_agent.py", AGENT),
    ("agent_tools.py", AGENT_TOOL),
    ("bedrock.py", PROVIDER),
    ("config.py", SUPPORT),
])
def test_nonreview_boundaries_cannot_import_human_approval(
    tmp_path: Path, source_path: str, category: str
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, source_path, "from .human_review import ReviewSession\n")
    _add_module(package, "human_review.py")
    categories.update({source_path: category, "human_review.py": REVIEW})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


def test_review_cannot_import_agent_or_provider_sdk(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "human_review.py", "from .quotation_agent import QuotationAgent\nimport boto3\n")
    _add_module(package, "quotation_agent.py")
    categories.update({"human_review.py": REVIEW, "quotation_agent.py": AGENT})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("relative_path", ["new_core.py", "new_package/__init__.py"])
def test_unclassified_new_module_fails_closed(tmp_path: Path, relative_path: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, relative_path)
    with pytest.raises(AssertionError, match="unclassified modules"):
        validate_architecture(package, categories)


@pytest.mark.parametrize(
    ("target_path", "target_category", "import_statement"),
    [
        ("bedrock_adapter.py", PROVIDER, "from ai_quotation_intelligence import bedrock_adapter"),
        ("agent_tools.py", AGENT_TOOL, "import ai_quotation_intelligence.agent_tools"),
        ("quotation_agent.py", AGENT, "from .. import quotation_agent"),
        ("human_review.py", REVIEW, "from .. import human_review"),
        ("tooling/__init__.py", AGENT_TOOL, "from ai_quotation_intelligence import tooling"),
        ("api.py", APPLICATION_BOUNDARY, "from ai_quotation_intelligence.api import route"),
        ("excel_export.py", EXPORT, "from .. import excel_export"),
    ],
)
def test_core_rejects_each_forbidden_local_boundary(
    tmp_path: Path, target_path: str, target_category: str, import_statement: str
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "domain/__init__.py", import_statement + "\n")
    _add_module(package, target_path)
    categories.update({"domain/__init__.py": CORE, target_path: target_category})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("import_statement", ["import boto3", "from botocore.config import Config"])
def test_core_rejects_provider_sdk_imports(tmp_path: Path, import_statement: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "calculation.py", import_statement + "\n")
    categories["calculation.py"] = CORE
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


def test_classified_package_reexport_cannot_hide_provider_import(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "bedrock_adapter.py")
    _add_module(package, "domain/__init__.py", "from .. import bedrock_adapter\n")
    categories.update({"bedrock_adapter.py": PROVIDER, "domain/__init__.py": CORE})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


def test_root_package_reexport_cannot_hide_provider_import(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "__init__.py", "from . import bedrock_adapter\n")
    _add_module(package, "bedrock_adapter.py")
    categories["bedrock_adapter.py"] = PROVIDER
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize(
    ("target_path", "target_category"),
    [
        ("bedrock_adapter.py", PROVIDER),
        ("agent_tools.py", AGENT_TOOL),
        ("quotation_agent.py", AGENT),
        ("human_review.py", REVIEW),
        ("api.py", APPLICATION_BOUNDARY),
        ("excel_export.py", EXPORT),
    ],
)
def test_support_cannot_launder_forbidden_dependency_to_core(
    tmp_path: Path, target_path: str, target_category: str
) -> None:
    package, categories = _fixture_package(tmp_path)
    target_name = Path(target_path).stem
    _add_module(package, "config.py", f"from . import {target_name}\n")
    _add_module(package, "calculation.py", f"from ai_quotation_intelligence.config import {target_name}\n")
    _add_module(package, target_path)
    categories.update({"config.py": SUPPORT, "calculation.py": CORE, target_path: target_category})
    with pytest.raises(AssertionError, match=rf"config.py -> ai_quotation_intelligence.{target_name}"):
        validate_architecture(package, categories)


def test_support_package_reexport_cannot_launder_provider(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "support/__init__.py", "from .. import bedrock_adapter\n")
    _add_module(package, "calculation.py", "from .support import bedrock_adapter\n")
    _add_module(package, "bedrock_adapter.py")
    categories.update({
        "support/__init__.py": SUPPORT,
        "calculation.py": CORE,
        "bedrock_adapter.py": PROVIDER,
    })
    with pytest.raises(AssertionError, match="support/__init__.py -> ai_quotation_intelligence.bedrock_adapter"):
        validate_architecture(package, categories)


def test_support_rejects_provider_sdk_import(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "config.py", "import boto3\n")
    categories["config.py"] = SUPPORT
    with pytest.raises(AssertionError, match="config.py -> boto3"):
        validate_architecture(package, categories)


def test_legitimate_core_to_support_and_support_imports_pass(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "config.py", "import logging\nfrom .logging_config import configure_logging\n")
    _add_module(package, "logging_config.py", "import logging\n")
    _add_module(package, "calculation.py", "from .config import Settings\n")
    categories.update({"config.py": SUPPORT, "logging_config.py": SUPPORT, "calculation.py": CORE})
    validate_architecture(package, categories)


def test_policy_self_check_rejects_support_tunnel_even_without_import(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    weakened = {category: set(targets) for category, targets in ALLOWED_LOCAL_DEPENDENCIES.items()}
    weakened[SUPPORT].add(PROVIDER)
    with pytest.raises(AssertionError, match="unsafe dependency policy"):
        validate_architecture(package, categories, weakened)


def test_agent_tool_may_delegate_to_core(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "agent_tools.py", "from .comparison import compare_historical_quotes\n")
    _add_module(package, "comparison.py")
    categories.update({"agent_tools.py": AGENT_TOOL, "comparison.py": CORE})
    validate_architecture(package, categories)


def test_agent_tool_rejects_unused_support_dependency(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "agent_tools.py", "from .config import Settings\n")
    _add_module(package, "config.py")
    categories.update({"agent_tools.py": AGENT_TOOL, "config.py": SUPPORT})
    with pytest.raises(AssertionError, match="agent_tools.py -> ai_quotation_intelligence.config"):
        validate_architecture(package, categories)


def test_agent_may_use_only_existing_core_and_agent_tool_owners(tmp_path: Path) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "quotation_agent.py",
                "from .calculation import calculate_quote\nfrom .agent_tools import AgentTools\n")
    _add_module(package, "calculation.py")
    _add_module(package, "agent_tools.py")
    categories.update({"quotation_agent.py": AGENT, "calculation.py": CORE, "agent_tools.py": AGENT_TOOL})
    validate_architecture(package, categories)


@pytest.mark.parametrize(("target", "category"), [
    ("bedrock.py", PROVIDER),
    ("config.py", SUPPORT),
    ("human_review.py", REVIEW),
])
def test_agent_rejects_unused_provider_and_support_dependencies(
    tmp_path: Path, target: str, category: str
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "quotation_agent.py", f"from . import {Path(target).stem}\n")
    _add_module(package, target)
    categories.update({"quotation_agent.py": AGENT, target: category})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source", ["import boto3\n", "from botocore.config import Config\n"])
def test_agent_rejects_provider_sdk_imports(tmp_path: Path, source: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "quotation_agent.py", source)
    categories["quotation_agent.py"] = AGENT
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize(("source_path", "category"), [
    ("agent_tools.py", AGENT_TOOL),
    ("bedrock.py", PROVIDER),
])
def test_agent_tool_and_provider_cannot_depend_on_agent(
    tmp_path: Path, source_path: str, category: str
) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "quotation_agent.py")
    _add_module(package, source_path, "from .quotation_agent import QuotationAgent\n")
    categories.update({"quotation_agent.py": AGENT, source_path: category})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


@pytest.mark.parametrize("source", [
    "from .bedrock import BedrockConverseAdapter\n",
    "import boto3\n",
    "from botocore.config import Config\n",
])
def test_agent_tool_rejects_provider_and_sdk_imports(tmp_path: Path, source: str) -> None:
    package, categories = _fixture_package(tmp_path)
    _add_module(package, "agent_tools.py", source)
    _add_module(package, "bedrock.py")
    categories.update({"agent_tools.py": AGENT_TOOL, "bedrock.py": PROVIDER})
    with pytest.raises(AssertionError, match="forbidden architecture imports"):
        validate_architecture(package, categories)


def test_c15_deployment_composition_has_no_reverse_or_storage_dependency() -> None:
    """C15 lives outside the application package; no owner imports it back."""
    root = PACKAGE.parents[1]
    entrypoint = root / "deployment" / "lambda_handler.py"
    imports = _import_targets(ast.parse(entrypoint.read_text()), "deployment.lambda_handler", False)
    expected = {
        f"{PACKAGE_NAME}.agent_tools", f"{PACKAGE_NAME}.api",
        f"{PACKAGE_NAME}.bedrock", f"{PACKAGE_NAME}.config",
        f"{PACKAGE_NAME}.quotation_agent",
    }
    local = {target for target in imports if target.startswith(f"{PACKAGE_NAME}.")}
    assert local & expected == expected
    assert all(target in expected or any(target.startswith(f"{module}.") for module in expected)
               for target in local)
    assert not any("s3_storage" in target or "storage_contract" in target for target in imports)
    for module in PACKAGE.rglob("*.py"):
        targets = _import_targets(ast.parse(module.read_text()), _module_name(module.relative_to(PACKAGE).as_posix()), False)
        assert not any(target == "deployment" or target.startswith("deployment.") for target in targets)
