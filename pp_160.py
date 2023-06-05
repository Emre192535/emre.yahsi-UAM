"""
Exercise 160, pp_160.py

Task is the same as in exercise 40 - finding the longest word in the given text, but additionally you have to implement a function get_text().
The new function should return the text from a file,
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message
e.g. after punctuation removal
The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with the length of 25 characters

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters

use map function together with lambda

Exception handling should be implemented.
Implement the possibility of entering file_path from command line
"""
import logging
from argparse import ArgumentParser
from dataclasses import dataclass, field
from functools import wraps
from string import punctuation
from time import perf_counter


class ShakespeareDefaultException(Exception):
    """Failed to process Shakespeare text:"""

    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(
            f"{self.__doc__} {msg}" if msg else self.__doc__,
            *args,
            **kwargs,
        )


class ShakespeareLoadTextException(ShakespeareDefaultException):
    """Failed to load text file:"""


def timeit(func):
    """
    Calculate how much time it took to run a function in seconds.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start: float = perf_counter()
        result = func(*args, **kwargs)
        logging.debug(
            f"{func.__name__} took {perf_counter() - start:.6f} second(s) to complete."
        )
        return result

    return wrapper


@dataclass
class Shakespeare:
    """
    Find the most commonly occurring word in a text file.

    Usage:
    ```
    shp: Shakespeare = Shakespeare(inp)
    print(shp.get_longest())
    shp.print_result()
    ```
    """

    filepath: str
    text: str = field(init=False)

    def __post_init__(self) -> None:
        self.text = self._load_text(self.filepath)

    @staticmethod
    def _load_text(filepath: str) -> str:
        """
        Load a text file and return its content as string.

        Args:
            filepath (str): Path to the text file (e.g., "file.txt").

        Raises:
            ShakespeareLoadTextException: Couldn't load text for whatever reason.

        Returns:
            str: String representation of the text file.
        """
        if not filepath:
            logging.warning("Please provide a filepath.")
            raise
        try:
            with open(filepath, mode="r", encoding="utf-8") as f:
                r: str = f.read()
        except Exception as e:
            logging.warning(f"File '{filepath}' couldn't be opened ({e}).")
            raise ShakespeareLoadTextException(e)
        else:
            logging.info(
                f"Successfully loaded a file '{filepath}' ({len(r):,} characters)."
            )
            return r

    @staticmethod
    def _remove_punctuation(text: str) -> str:
        """
        Return a string without punctuation.

        Args:
            text (str): Any string with or without the punctuation.

        Returns:
            str: String without punctuation.
        """
        return "".join(i for i in text if i not in punctuation)

    @timeit
    def get_longest(self, remove_punctuation: bool = True) -> tuple[str, int]:
        """
        Return the longest word in the text and its length.

        Args:
            remove_punctuation (bool, optional): If True, punctuation will be removed. Defaults to True.

        Returns:
            tuple[str, int]: A tuple containing the longest word and its length.
        """
        text: str = self.text.lower()
        if remove_punctuation:
            # before: int = len(text)
            text = self._remove_punctuation(text)
            # logging.debug(f"Removed punctuation: {before:,} -> {len(text):,} characters")
        text_split: list[str] = text.split()
        logging.debug(f"Split text into '{len(text_split):,}' words.")
        text_tuples: list[tuple[str, int]] = list(
            map(lambda x: (x, len(x)), text_split)
        )
        text_tuples.sort(key=lambda x: x[1], reverse=True)
        return text_tuples[0]


def print_result(filepath: str) -> None:
    """
    Print results to console, catching all exceptions.
    """
    try:
        shp: Shakespeare = Shakespeare(filepath)
        res: tuple[str, int] = shp.get_longest(remove_punctuation=False)
        res_no_punct: tuple[str, int] = shp.get_longest(remove_punctuation=True)
        print(
            f"The longest word in the file '{shp.filepath}' is '{res[0]}' "
            f"with the length of {res[1]} characters (punctuation included)."
        )
        print(
            f"The longest word in the file '{shp.filepath}' is '{res_no_punct[0]}' "
            f"with the length of {res_no_punct[1]} characters (punctuation removed)."
        )
    except Exception as e:
        logging.error(f"Caught {type(e).__name__}: {e}")
    return None


def main() -> None:
    # setup logger
    logging.basicConfig(
        datefmt="%G-%m-%d %T",
        format="%(asctime)s [%(levelname)s] %(filename)s : %(funcName)s() (%(lineno)d) - %(message)s",
        level=logging.DEBUG,
    )
    parser: ArgumentParser = ArgumentParser(
        prog="Shakespeare",
        description="Find the most commonly occurring word in a text file.",
    )
    # usage: python3 pp_160.py --filepath shakespeare.txt
    parser.add_argument(
        "-f",
        "--filepath",
        help="Path to the text file.",
    )
    args = parser.parse_args()
    if args.filepath:
        logging.debug(f"Received filepath as a command-line argument: {args.filepath}")
        print_result(filepath=args.filepath)
    else:
        logging.debug(
            "No filepath provided as a command-line argument, running interactively."
        )
        while True:
            while True:
                inp: str = input("Enter the file to load: ")
                if inp:
                    break
                print("You provided nothing!")
            print_result(inp)
    return None


if __name__ == "__main__":
    main()
