
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




def char_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict[str, int]]:
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list