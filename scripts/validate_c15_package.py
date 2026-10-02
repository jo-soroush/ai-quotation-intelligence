"""Validate a locally built C15 Lambda ZIP without contacting AWS."""

import argparse
from email.parser import Parser
from pathlib import Path
import subprocess
import tempfile
from zipfile import BadZipFile, ZipFile

from pip._vendor.packaging.markers import default_environment
from pip._vendor.packaging.requirements import Requirement
from pip._vendor.packaging.utils import canonicalize_name


REQUIRED = {
    "lambda_handler.py",
    "ai_quotation_intelligence/api.py",
    "ai_quotation_intelligence/bedrock.py",
    "ai_quotation_intelligence/excel_export.py",
}
PACKAGES = ("mangum/", "fastapi/", "openpyxl/", "boto3/", "botocore/", "pydantic/")
LOCK = Path(__file__).resolve().parents[1] / "deployment" / "requirements-lambda.txt"


def _validate_dependency_closure(archive: ZipFile) -> None:
    """Check the package's own metadata, not the developer environment."""

    installed: dict[str, tuple[str, list[str]]] = {}
    for name in archive.namelist():
        if not name.endswith(".dist-info/METADATA"):
            continue
        metadata = Parser().parsestr(archive.read(name).decode("utf-8"))
        distribution = metadata.get("Name")
        version = metadata.get("Version")
        if not distribution or not version:
            raise ValueError("malformed packaged distribution metadata")
        key = canonicalize_name(distribution)
        if key in installed:
            raise ValueError("duplicate packaged distribution")
        installed[key] = (version, metadata.get_all("Requires-Dist", []))

    pinned: dict[str, str] = {}
    for line in LOCK.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        distribution, separator, version = line.partition("==")
        if not separator or not distribution or not version:
            raise ValueError("invalid Lambda dependency snapshot")
        pinned[canonicalize_name(distribution)] = version
    if {name: version for name, (version, _) in installed.items()} != pinned:
        raise ValueError("packaged distributions differ from runtime dependency snapshot")

    target = default_environment()
    target.update({"python_version": "3.13", "python_full_version": "3.13.0",
                   "sys_platform": "linux", "platform_system": "Linux",
                   "platform_machine": "x86_64", "extra": ""})
    for _, requirements in installed.values():
        for raw in requirements:
            requirement = Requirement(raw)
            if requirement.marker is not None and not requirement.marker.evaluate(target):
                continue
            required = installed.get(canonicalize_name(requirement.name))
            if required is None or required[0] not in requirement.specifier:
                raise ValueError("incomplete or incompatible Lambda runtime dependency closure")


_RUNTIME_SMOKE = '''
import json
import sys
sys.path.insert(0, "/var/task")
import boto3
boto3.client = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("AWS client forbidden during health"))
import mangum, fastapi, starlette, ai_quotation_intelligence
import lambda_handler
event = {
    "version": "2.0", "routeKey": "GET /health", "rawPath": "/health",
    "rawQueryString": "", "headers": {"host": "local.invalid"},
    "requestContext": {"accountId": "000000000000", "apiId": "local",
        "domainName": "local.invalid", "http": {"method": "GET", "path": "/health",
        "protocol": "HTTP/1.1", "sourceIp": "127.0.0.1", "userAgent": "local"},
        "requestId": "local", "routeKey": "GET /health", "stage": "$default",
        "time": "02/Oct/2026:00:00:00 +0000", "timeEpoch": 0},
    "body": None, "isBase64Encoded": False,
}
response = lambda_handler.handler(event, None)
assert response["statusCode"] == 200 and json.loads(response["body"]) == {"status": "ok"}, response
print("C15_PACKAGED_HANDLER_AND_HEALTH: PASS")
'''


def runtime_smoke(path: Path) -> None:
    """Run the extracted Linux package without host packages or network."""

    validate(path)
    with tempfile.TemporaryDirectory(prefix="aqi-c15-runtime-smoke-") as directory:
        with ZipFile(path) as archive:
            archive.extractall(directory)
        result = subprocess.run(
            ["docker", "run", "--rm", "--pull", "never", "--platform", "linux/amd64", "--network", "none",
             "--read-only", "-v", f"{directory}:/var/task:ro", "-w", "/var/task",
             "python:3.13-slim", "python", "-I", "-S", "-B", "-c", _RUNTIME_SMOKE],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0 or "C15_PACKAGED_HANDLER_AND_HEALTH: PASS" not in result.stdout:
            raise ValueError("isolated Lambda handler/health runtime smoke failed")
        print(result.stdout.strip())


def validate(path: Path) -> None:
    try:
        with ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise ValueError("corrupt Lambda ZIP")
            names = set(archive.namelist())
            if not REQUIRED <= names:
                raise ValueError("missing application or handler module")
            if not all(any(name.startswith(prefix) for name in names) for prefix in PACKAGES):
                raise ValueError("missing required runtime dependency")
            binaries = [name for name in names if name.startswith("pydantic_core/") and name.endswith(".so")]
            if len(binaries) != 1 or not archive.read(binaries[0]).startswith(b"\x7fELF"):
                raise ValueError("Pydantic Core is not a Linux binary")
            if not any(name.startswith("mangum-") and name.endswith("LICENSE") for name in names):
                raise ValueError("Mangum license is missing from package")
            if any(name.startswith(("tests/", ".aws/", "deployment/")) or
                   (name.endswith((".env", ".pem", ".key", ".pyc")) and
                    name != "botocore/cacert.pem") or
                   "/__pycache__/" in name for name in names):
                raise ValueError("non-runtime or sensitive file in package")
            _validate_dependency_closure(archive)
    except BadZipFile as exc:
        raise ValueError("invalid Lambda ZIP") from exc


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("--runtime-smoke", action="store_true",
                        help="also import and invoke /health inside isolated Linux Python 3.13")
    args = parser.parse_args()
    validate(args.zip_path)
    if args.runtime_smoke:
        runtime_smoke(args.zip_path)
    print("C15_LAMBDA_PACKAGE_VALIDATION: PASS")


if __name__ == "__main__":
    main()
