def main() -> None:
    print("--- Welcome to Bookbot 9000 ---")

    while True:
        print("Type in the path to a text file to analyse its contents")
        print("Type in 'q' to quit")
        book_path = input("> ").lower()
        if book_path == "q":
            break    
        analyse_book(book_path)

def analyse_book(book_path: str) -> None:
    try:
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_num_letters(text)
    
        print()
        print(f"--- Begin report of '{book_path}'... ---")
        print(f"{num_words} words found in the document")
        print()
        for char in chars_dict:
            if char.isalpha():
                print(f"The '{char}' character was found {chars_dict[char]} times")
        print()
        print(f"--- End report ---")
        print()
    except Exception as e:
        print()
        print("Text could not be analised.")
        print(f"Error message: {e}")



def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_num_letters(text: str) -> dict[str, int]:
    num_chars = {}
    for char in text:
        c = char.lower()
        if c not in num_chars:
            num_chars[c] = 0
        num_chars[c] += 1
    return dict(sorted(num_chars.items()))


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


main()