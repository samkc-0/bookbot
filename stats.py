from typing import Any


report_template = """============ BOOKBOT ============
Analyzing book found at {}...
----------- Word Count ----------
Found {} total words
--------- Character Count -------
{}
============= END ===============
"""


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    counts = {}
    for c in text.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts


def sort_characters_by_count(char_counts: dict[str, int]) -> list[dict]:
    counts = [{"char": key, "num": value} for key, value in char_counts.items()]
    counts.sort(key=lambda c: c["num"])
    return counts


def format_report(path: str, word_count: int, char_counts: list[dict]) -> str:
    char_count_lines = "\n".join(f"{c['char']}: {c['num']}" for c in char_counts)
    return report_template.format(path, word_count, char_count_lines)
