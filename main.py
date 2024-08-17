def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_contents(book_path)
    words = get_number_of_words(text)
    print(words)

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(body_text):
    number_of_words = 0
    words = body_text.split()
    for word in words:
        number_of_words += 1
    return number_of_words

main()