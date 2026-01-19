from stats import count_words
from stats import count_characters
from stats import sort_dictionary

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
    counted_chars = count_characters(text)
    sorted_chars = sort_dictionary(counted_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(count_of_words)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
