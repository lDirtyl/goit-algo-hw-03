import argparse
import shutil
from pathlib import Path

def parse_argv():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Папка з файлами для копіювання"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("dist"),
        help="Папка для відсортованих файлів",
    )
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)
        else:
            extension = item.suffix[1:]  
            if extension == "":  
                extension = "no_extension"
            folder = dst / extension  
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy2(item, folder)

def main():
    args = parse_argv()
    print(f"Вхідні аргументи: {args}")
    if not args.source.exists():
        print(f"Джерельна директорія не існує: {args.source}")
        return
    if not args.source.is_dir():
        print(f"Вказаний шлях не є директорією: {args.source}")
        return
    args.output.mkdir(exist_ok=True, parents=True)
    recursive_copy(args.source, args.output)

if __name__ == "__main__":
    main()
