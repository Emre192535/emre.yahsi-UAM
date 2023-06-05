"""
Exercise 170, pp_170.py

Modify the exercise 160 - print to the terminal the list of the 10 the longest words in the given text, you still have to implement
a function get_text() to get text from file.

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters
The longest word in the file 'shakespeare.txt' is '726002026compuservecom' with the length of 22 characters

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
    """Failed to process Shakespeare text"""

    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(
            f"{self.__doc__}: {msg}" if msg else self.__doc__,
            *args,
            **kwargs,
        )


class ShakespeareLoadTextException(ShakespeareDefaultException):
    """Failed to load text file"""


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
    Find the longest word in a text file.

    Usage:
    ```
    shp: Shakespeare = Shakespeare(inp)
    longest: list[tuple[str, int]] = shp.map_longest())
    print(longest[0])
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
    def _remove_punctuation(text: str, remove_space: bool = False) -> str:
        """
        Return a string without punctuation.

        Args:
            text (str): Any string with or without the punctuation.
            remove_space (bool, optional): If True, spaces are removed. Defaults to False.

        Returns:
            str: String without punctuation.
        """
        return "".join(
            i for i in text if i not in punctuation and not (remove_space and i == " ")
        )

    @timeit
    def map_longest(self, remove_punctuation: bool = True) -> list[tuple[str, int]]:
        """
        Return a list of words and their lengths.

        Each tuple consists of word and its length.

        Args:
            remove_punctuation (bool, optional): If True, punctuation will be removed. Defaults to True.

        Returns:
            list[tuple[str, int]]: A list of tuples corresponding to individual words (word, length).
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
        return text_tuples


def print_word_length_list(
    tuples: list[tuple[str, int]],
    amount: int = 10,
    remove_punctuation=False,
) -> None:
    """
    Print top X tuples. Each tuple consists of word and its length.

    _extended_summary_

    Args:
        tuples (list[tuple[str, int]]): List of tuples (word, length).
        amount (int, optional): The amount of words to be printed. Defaults to 10.
        remove_punctuation (bool, optional): Whether to print that punctuation was removed. Defaults to False.
    """
    print(
        "Top longest words (punctuation ",
        "removed" if remove_punctuation else "included",
        "):",
        sep="",
    )
    count: int = 1
    while count < amount + 1:
        print(f"{count}. '{tuples[count][0]}' ({tuples[count][1]} characters)")
        count += 1
    return None


def print_result(filepath: str, number: int = 10) -> None:
    """
    Print results to console, catching all exceptions.
    """
    try:
        shp: Shakespeare = Shakespeare(filepath)
        res_tuples: list[tuple[str, int]] = shp.map_longest(remove_punctuation=False)
        res_tuples_no_punct: list[tuple[str, int]] = shp.map_longest(
            remove_punctuation=True
        )
        print(
            f"The longest word in the file '{shp.filepath}' is '{res_tuples[0][0]}' "
            f"with the length of {res_tuples[0][1]} characters (punctuation included)."
        )
        print_word_length_list(res_tuples, remove_punctuation=False)
        print(
            f"The longest word in the file '{shp.filepath}' is '{res_tuples_no_punct[0][0]}' "
            f"with the length of {res_tuples_no_punct[0][1]} characters (punctuation removed)."
        )
        print_word_length_list(res_tuples_no_punct, remove_punctuation=True)
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
        description="Find the longest word in a text file.",
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
