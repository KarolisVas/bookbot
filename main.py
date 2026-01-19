from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(file_path):
    try:
        with open(file_path) as f:
            book_text = f.read()
        return book_text
    except FileNotFoundError:
        print("book not found")
        sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    count_of_words = count_words(text)
    counted_chars = count_characters(text)
    sorted_chars = sort_dictionary(counted_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {len(count_of_words)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
