"""
Exercise 190

https://www.w3schools.com/python/python_regex.asp

Using RE find all the 5-characters length

Think about the following Special Sequences
\b
\w
{}


`\b` matches at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters or underscores, i.e., any character that can appear in a Python identifier. The `\b` symbol is used to match word boundaries.

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes".

"""
import logging
import re
from dataclasses import dataclass


@dataclass
class Foo:
    filepath: str
    start_line: int = 0

    def _get_text(self) -> str:
        """
        Load a text file and return its content as string from specific line onwards.

        Returns:
            str: String representation of the text file.
        """
        try:
            with open(self.filepath, mode="r", encoding="utf-8") as f:
                return "".join(f.readlines()[self.start_line :])
        except Exception as e:
            logging.warning(f"File '{self.filepath}' couldn't be opened ({e}).")
            return ""

    @property
    def words(self) -> list[str]:
        """
        Get 5 letter words from text file.

        Returns:
            list[str]: List containing 5 letter words (can be empty).
        """
        l_split: list[str] = re.findall(r"\b\w{5}\b", self._get_text())
        return l_split


def main() -> None:
    # setup logger
    logging.basicConfig(
        datefmt="%G-%m-%d %T",
        format="%(asctime)s [%(levelname)s] %(filename)s : %(funcName)s() (%(lineno)d) - %(message)s",
        level=logging.DEBUG,
    )
    while True:
        while True:
            filename: str = input("Enter filename: ")
            if filename:
                break
            logging.warning("No filename provided.")
        while True:
            start: str = input("Enter line to start from: ")
            if not start:
                logging.warning("No filename provided.")
                continue
            try:
                i_start: int = int(start)
            except ValueError as e:
                logging.warning(f"Invalid mode provided ({e})")
            else:
                break
        f: Foo = Foo(filename, i_start)
        print(f.words)
    return None


if __name__ == "__main__":
    main()
