def main():
    book_path = "./books/frankenstein.txt"
    body_text = get_book_contents(book_path)
    words = get_number_of_words(body_text)
    characters = get_character_counts(body_text)
    print(characters)


def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(body_text):
    number_of_words = 0
    words = body_text.split()
    for word in words:
        number_of_words += 1
    return number_of_words

def get_character_counts(body_text):
    character_dict = {}
    lowered_string = body_text.lower()
    for character in lowered_string:
        character_dict.update({character: lowered_string.count(character)})
        print(character)
    return character_dict

main()