from stats import *

def main() -> None:
    book_file_path = "./books/frankenstein.txt"
    text = get_book_text(book_file_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    print_report(book_file_path, num_words, num_chars)


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