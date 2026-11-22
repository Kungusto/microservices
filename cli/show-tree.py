from pathlib import Path

CORE_DIR = Path(__file__).parent.parent

excluded_dirs = {
    ".venv",
    "__pycache__",
    ".git",
}


def show_tree(directory: Path, prefix: str = ""):
    children = sorted(
        (
            path
            for path in directory.iterdir()
            if not (
                path.is_dir()
                and (path.name in excluded_dirs or path.name.startswith("."))
            )
        ),
        key=lambda p: (not p.is_dir(), p.name.lower()),
    )

    for index, path in enumerate(children):
        is_last = index == len(children) - 1

        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{path.name}{'/' if path.is_dir() else ''}")

        if path.is_dir():
            extension = "    " if is_last else "│   "
            show_tree(path, prefix + extension)


def main():
    print(f"{CORE_DIR.name}/")
    show_tree(CORE_DIR)


if __name__ == "__main__":
    main()
