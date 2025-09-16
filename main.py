import sys
from pathlib import Path
from stats import count_words, count_characters, sort_characters_by_count, format_report


def get_book_text(file_path: Path) -> str:
    return file_path.read_text()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        book_path = Path(book_path)
    except ValueError:
        print(f"Error: {book_path} is not a valid path")
        sys.exit(1)
    if not Path(book_path).is_file():
        print(f"Error: {book_path} is not a file")
        sys.exit(1)
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = sort_characters_by_count(count_characters(text))
    report = format_report(str(book_path), word_count, char_counts)
    print(report)


if __name__ == "__main__":
    main()
