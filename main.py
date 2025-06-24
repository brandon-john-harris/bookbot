import sys
from stats import split_text, character_count, sort_on


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    my_text = get_book_text(book)
    num_words = split_text(my_text)
    characters = character_count(my_text)
    character_report = []
    for character, num in characters.items():
        if character.isalpha():
            character_report.append({"character": character, "num": num})
    character_report.sort(reverse=True, key=sort_on)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_dict in character_report:
        print(f"{character_dict['character']}: {character_dict['num']}")
    print("============= END ===============")


main()

exit()
