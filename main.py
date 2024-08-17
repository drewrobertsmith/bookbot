def main():
    book_path = "./books/frankenstein.txt"
    body_text = get_book_contents(book_path)
    words = get_number_of_words(body_text)
    characters = get_character_counts(body_text)
    report = generate_word_and_character_report(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for dict in report:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print("--- End report ---")


def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(body_text):
    number_of_words = 0
    words = body_text.split()
    for word in words:
        number_of_words += 1
    return number_of_words

# MUCH SLOWER
# Issues: creating new full copy of the text in memory by lowercasing entire string, .update() creates a new dict each time, .count() scans entire string
# def get_character_counts(body_text):
#     character_dict = {}
#     lowered_string = body_text.lower()
#     for character in lowered_string:
#         character_dict.update({character: lowered_string.count(character)})
#         print(character)
#     return character_dict

def get_character_counts(body_text):
    char = {}
    for c in body_text:
        lower = c.lower()
        if lower in char:
            char[lower] += 1
        else:
            char[lower] = 1
    return char

def generate_word_and_character_report(character_dict):
    list_of_dicts = []
    for k in character_dict:
        if k.isalpha():
            list_of_dicts.append({
                "char" : k,
                "num" : character_dict[k]
                })
    def sort_on(dict):
        return dict["num"]
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
    # for dict in list_of_dicts:
    #     (f"The '{dict['char']}' character was found {dict['num']} times")
main()