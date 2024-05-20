import sys
from pathlib import Path
from colorama import Fore, Style

def list_files_and_directories(directory_path, indent=0):
    directory = Path(directory_path)
    if not directory.is_dir():
        print(f"{Fore.RED}Error: {directory_path} is not a valid directory.{Style.RESET_ALL}")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{'  ' * indent}📁 {item.name}{Style.RESET_ALL}")
            list_files_and_directories(item, indent + 1)
        else:
            print(f"{Fore.GREEN}{'  ' * indent}📄 {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory_path>")
    else:
        list_files_and_directories(sys.argv[1])