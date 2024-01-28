import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли та сортує їх за розширенням.")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-d", "--destination", type=Path, default=Path("dist"), help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()


def recursive_copy(source: Path, destination: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, destination)
            else:
                file_extension = el.suffix[1:]  # отримуємо розширення файлу
                folder = destination / file_extension
                folder.mkdir(exist_ok=True)
                shutil.copy(el, folder)
    except Exception as e:
        print(f"Помилка обробки директорії {source}: {e}")

def main():
    args = parse_argv()
    
    try:
        # Рекурсивне копіювання файлів
        recursive_copy(args.source, args.destination)
        print("Копіювання файлів та сортування за розширенням завершено успішно.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()