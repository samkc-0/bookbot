from pathlib import Path
from stats import count_words, count_characters, sort_characters_by_count, format_report


def get_book_text(file_path: Path) -> str:
    return file_path.read_text()


def main():
    book_path = Path(".") / "books" / "frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = sort_characters_by_count(count_characters(text))
    report = format_report(str(book_path), word_count, char_counts)
    print(report)


if __name__ == "__main__":
    main()
