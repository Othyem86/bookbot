
def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_characters(text: str) -> dict[str, int]:
    num_characters = {}
    for char in text.lower():
        if (char not in num_characters):
            num_characters[char] = 1
            continue
        num_characters[char] += 1
    return num_characters