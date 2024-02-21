def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char in chars_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {chars_dict[char]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    num_chars = {}
    for char in text:
        c = char.lower()
        if c not in num_chars:
            num_chars[c] = 0
        num_chars[c] += 1
    return num_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()