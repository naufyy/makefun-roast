"""One satirical sentence roasting lawmakers who regulate the internet
but cannot convert a file to PDF.

166 characters: the morning is spent regulating the internet, the
afternoon on hold with IT, and the office PDF converter turns out to
be a man named Dave.
"""

from pathlib import Path

ENTRY = (
    "He spent the morning regulating the internet and the afternoon on "
    "hold with IT because his PDF converter, the one his office has used "
    "since 2019, is a man named Dave."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 320:
        raise ValueError(f"entry must be 1-320 characters, got {len(ENTRY)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
