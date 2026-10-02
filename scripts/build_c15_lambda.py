"""Build a Linux-compatible C15 Lambda ZIP locally; never contacts AWS.

The only network-capable step is pip's package-index download. No cloud API
is invoked. The output must not already exist, preventing silent overwrite.
"""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "deployment" / "requirements-lambda.txt"
SOURCE = ROOT / "src" / "ai_quotation_intelligence"
ENTRYPOINT = ROOT / "deployment" / "lambda_handler.py"


def build(output: Path) -> None:
    output = output.resolve()
    if output.exists():
        raise ValueError("deployment artifact already exists")
    if sys.version_info[:2] != (3, 13):
        raise RuntimeError("C15 package build requires Python 3.13")
    with tempfile.TemporaryDirectory(prefix="aqi-c15-package-") as temp:
        package = Path(temp) / "package"
        package.mkdir()
        subprocess.run(
            [
                sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
                "--no-cache-dir", "--no-deps", "--only-binary=:all:",
                "--platform=manylinux2014_x86_64", "--implementation=cp",
                "--python-version=3.13", "--abi=cp313", "--target", str(package),
                "-r", str(LOCK),
            ],
            check=True,
        )
        shutil.copytree(
            SOURCE, package / SOURCE.name,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
        shutil.copy2(ENTRYPOINT, package / "lambda_handler.py")
        with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob("*")):
                relative = path.relative_to(package)
                if path.is_file() and "__pycache__" not in relative.parts and path.suffix != ".pyc" and relative.parts[0] != "bin":
                    archive.write(path, relative.as_posix())
    with ZipFile(output) as archive:
        bad = archive.testzip()
        if bad is not None:
            output.unlink()
            raise RuntimeError("deployment ZIP integrity check failed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build(args.output)
    print(f"Built local C15 package: {args.output.resolve()}")


if __name__ == "__main__":
    main()
