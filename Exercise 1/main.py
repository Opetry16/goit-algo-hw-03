import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("dist"), help="Шлях до директорії призначення"
    )
    return parser.parse_args()

def recursive_copy(source: Path, output: Path):
    try:
        output.mkdir(exist_ok=True, parents=True)
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, output)
            else:
                folder_name = el.suffix.lstrip('.')  # використовуємо розширення як ім'я піддиректорії
                folder = output / folder_name
                folder.mkdir(exist_ok=True)
                shutil.copy(el, folder)
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)
    print("Копіювання та сортування завершено.")

if __name__ == "__main__":
    main()