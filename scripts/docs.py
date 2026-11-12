import shutil
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "cp" / "docs"
SOURCE = DOCS / "source"
BUILD = DOCS / "build"
DATA = DOCS.parent / "cellprofiler" / "data"
SYNCED = ("help", "images")


def clean():
    for name in SYNCED:
        shutil.rmtree(SOURCE / name, ignore_errors=True)
    shutil.rmtree(BUILD, ignore_errors=True)


def sync():
    for name in SYNCED:
        shutil.rmtree(SOURCE / name, ignore_errors=True)
        shutil.copytree(DATA / name, SOURCE / name)


def build(builder, extra):
    sync()
    return subprocess.call(
        [sys.executable, "-m", "sphinx", "-M", builder, str(SOURCE), str(BUILD), *extra]
    )


def main(argv):
    target = argv[0] if argv else "html"
    if target == "clean":
        clean()
        return 0
    return build(target, argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
