import sys
from pathlib import Path
from colorama import init, Fore

init()


def directory_structure(directory_path, indent=0):
    try:
        directory = Path(directory_path)

        print(Fore.LIGHTYELLOW_EX + "📦" + directory.name)

        for file in directory.iterdir():
            if file.is_file():
                print(Fore.BLUE + " " * indent + "┣ 📜" + file.name)
            elif file.is_dir():

                directory_structure(file, indent + 2)

    except FileNotFoundError:
        print(Fore.RED + "Error: Directory not found.")
    except PermissionError:
        print(Fore.RED + "Error: Permission denied.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python main.py pictures")
        sys.exit(1)

    directory_path = sys.argv[1]
    directory_structure(directory_path)
