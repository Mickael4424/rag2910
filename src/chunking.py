from pathlib import Path
from typing import List


ALLOWED_EXTENSIONS = {".py", ".md", ".txt"}


def list_files(root: str = "data/raw") -> List[Path]:
    files: List[Path] = []
    for path in Path(root).rglob("*"):
        if path.is_file() and path.suffix in ALLOWED_EXTENSIONS:
            files.append(path)
    return sorted(files)


def read_file(path: Path) -> str | None:
    try:
        with open(path, "r", encoding="utf-8", newline="") as file:
            return file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error: cannot read {path}: {error}")
        return None
