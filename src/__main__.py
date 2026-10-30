import fire
import chunking

from src.cli import RagCLI
from pathlib import Path


def main() -> None:
    # fire.Fire(RagCLI)
    files: list[Path] = chunking.list_files()
    print(f"Number of files: {len(files)}")

    if files:
        print(f"First file: {files[0].as_posix()}")

    failed = 0
    for f in files:
        if chunking.read_file(f.as_posix()) is None:
            failed += 1
    print(f"Unreadable files: {failed}")


if __name__ == "__main__":
    main()
