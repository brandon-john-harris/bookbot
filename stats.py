def split_text(text):
    words = text.split()
    return len(words)


def character_count(text):
    text_lower = text.lower()
    character_dict = {}
    for character in text_lower:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict


def sort_on(items):
    return items["num"]
