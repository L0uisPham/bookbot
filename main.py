from stats import words_count, char_counts, format_results
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        return content


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    # print(get_book_text("books/frankenstein.txt"))
    # print(f"{words_count(text)} words found in the document")
    # print(char_counts(text))
    format_results(dict=char_counts(text), counts=words_count(text), path=sys.argv[1])
