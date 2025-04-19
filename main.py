from stats import get_word_count, char_count, report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book = sys.argv[1]

def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_string = get_book_text(book)
    report(get_word_count(book_string), char_count(book_string), book)
main()