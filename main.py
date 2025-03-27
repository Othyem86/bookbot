def main() -> None:
    book_file_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    print(book_text)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

main()