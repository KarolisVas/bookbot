from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    try:
        with open(file_path) as f:
            book_text = f.read()
        return book_text
    except FileNotFoundError:
        print("frankenstein book not found")

if __name__ == '__main__':
    text = get_book_text("books/frankenstein.txt")
    count_of_words = count_words(text)
    print(f"Found {len(count_of_words)} total words")
    print(count_characters(text))