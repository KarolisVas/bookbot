def get_book_text(file_path):
    try:
        with open(file_path) as f:
            book_text = f.read()
        return book_text
    except FileNotFoundError:
        print("frankenstein book not found")

if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))
