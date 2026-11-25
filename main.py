"""The 3 AM Excuse — make.fun entry.

Writes one line: the excuse a hardware wallet gives for refusing to sign
a transaction at 3 AM.
"""

import os

LINE = "No. I guard these keys all night so your 3 AM self can't spend what your 9 AM self earned. Sunrise, or nothing."

assert 1 <= len(LINE) < 200, f"line length {len(LINE)} out of range"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
