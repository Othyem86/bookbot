from stats import *

def main() -> None:
    book_file_path = "./books/frankenstein.txt"
    text = get_book_text(book_file_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_chars = get_num_characters(text)
    print(num_chars)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


main()