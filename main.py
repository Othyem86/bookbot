import sys
import os
from stats import *


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    if (not os.path.exists(file_path)):
        print(f"ERROR: File {file_path} could not be found")
        sys.exit(1)
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    print_report(file_path, num_words, num_chars)
    sys.exit(0)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def print_report(
        book_path: str,
        num_words: int,
        chars_sorted_list: dict[str, int]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = char_dict_to_sorted_list(chars_sorted_list)
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()