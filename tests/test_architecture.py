"""Static import-direction check for every classified package module.

This does not inspect dynamic imports, runtime objects, or semantic misuse.
"""

import ast
from importlib.util import resolve_name
from pathlib import Path

import pytest


PACKAGE_NAME = "ai_quotation_intelligence"
PACKAGE = Path(__file__).resolve().parents[1] / "src" / PACKAGE_NAME
CORE = "CORE"
PROVIDER = "PROVIDER"
AGENT_TOOL = "AGENT_TOOL"
APPLICATION_BOUNDARY = "APPLICATION_BOUNDARY"
SUPPORT = "SUPPORT"
CATEGORIES = {CORE, PROVIDER, AGENT_TOOL, APPLICATION_BOUNDARY, SUPPORT}
FORBIDDEN_FROM_CORE = {PROVIDER, AGENT_TOOL, APPLICATION_BOUNDARY}
# Empty future-category policies are deliberate: their dependency directions
# must be approved with the owning Card, not guessed by this governance change.
ALLOWED_LOCAL_DEPENDENCIES = {
    CORE: {CORE, SUPPORT},
    SUPPORT: {SUPPORT},
    PROVIDER: {CORE, SUPPORT},
    AGENT_TOOL: set(),
    APPLICATION_BOUNDARY: set(),
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
    "bedrock.py": PROVIDER,
    "config.py": SUPPORT,
    "logging_config.py": SUPPORT,
}


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
            if (external_provider and category != PROVIDER) or (
                target_category is not None and target_category not in policy[category]
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
        ("quotation_agent.py", AGENT_TOOL, "from .. import quotation_agent"),
        ("tooling/__init__.py", AGENT_TOOL, "from ai_quotation_intelligence import tooling"),
        ("api.py", APPLICATION_BOUNDARY, "from ai_quotation_intelligence.api import route"),
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
        ("api.py", APPLICATION_BOUNDARY),
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
