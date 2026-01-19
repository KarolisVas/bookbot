def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))