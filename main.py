def get_book_text(file_path):
    try:
        with open(file_path) as f:
            book_text = f.read()
        return book_text
    except FileNotFoundError:
        print("frankenstein book not found")

def count_words(text):
    return text.split()

if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    count_of_words = count_words(get_book_text(book_path))
    print(len(count_of_words))
