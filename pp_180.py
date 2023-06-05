"""
Exercise 180, pp_180.py

Modify the exercise 170 - you still print to the terminal the list of the 10 the longest words in the given text, you still have to implement
a function get_text().
But additionally, text analysis should start at specific line.
Implement the possibility to decide if text should be analyzed without or with punctuation and from which line number the analysis should start. Pass these arguments from command line.

On the beginning of the program a message should appear.

e.g. without punctuation removal
    ###############################################
    Text analyzer - finds 10 the longest words
    Do you want to analyze text as it is or you want to remove punctuation before?
    Press 1 if text as it is
    Press 2 if program should firstly remove punctuation
    ###############################################


-->  1
The longest word in the file 'shakespeare.txt' is 'swart-complexioned' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

use map function together with lambda, readline() method

Exception handling should be implemented.
Implement the possibility of entering "file_path" and "start_line"  from command line
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
    start_line: int = 0
    text: str = field(init=False)

    def __post_init__(self) -> None:
        self.text = self._load_text(self.filepath, self.start_line)

    @staticmethod
    def _load_text(filepath: str, start_line: int) -> str:
        """
        Load a text file and return its content as string.

        Args:
            filepath (str): Path to the text file (e.g., "file.txt").
            start_line (int): Line to begin from.

        Raises:
            ShakespeareLoadTextException: Couldn't load text for whatever reason.

        Returns:
            str: String representation of the text file.
        """
        try:
            with open(filepath, mode="r", encoding="utf-8") as f:
                r: str = "".join(f.readlines()[start_line:])
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


def _print_word_length_list(
    tuples: list[tuple[str, int]],
    amount: int = 10,
    remove_punctuation=False,
) -> None:
    """
    Print top X tuples.

    Each tuple consists of word and its length.

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


def print_result(
    filepath: str, start_line: int, remove_punctuation: bool = False
) -> None:
    """
    Print results to console, catching all exceptions.
    """
    try:
        shp: Shakespeare = Shakespeare(filepath, start_line=start_line)
        res_tuples: list[tuple[str, int]] = shp.map_longest(
            remove_punctuation=remove_punctuation
        )
        print(
            f"The longest word in the file '{shp.filepath}' is '{res_tuples[0][0]}' "
            f"with the length of {res_tuples[0][1]} characters."
        )
        _print_word_length_list(res_tuples, remove_punctuation=remove_punctuation)
    except Exception as e:
        logging.error(f"Caught {type(e).__name__}: {e}")
    return None


def get_input() -> tuple[bool, str]:
    """
    Get mode and filename from stdin.

    Returns:
        tuple[bool, str]: Tuple (remove_punctuation, filename).
    """
    while True:
        mode: str = input("Enter the mode: ")
        if not mode:
            logging.warning("You provided no number!")
        else:
            try:
                i_mode: int = int(mode)
            except ValueError as e:
                logging.warning(f"Invalid mode provided ({e})")
            else:
                if i_mode == 1 or i_mode == 2:
                    break
                else:
                    logging.warning("Mode should be 1 or 2.")
    while True:
        filename: str = input("Enter the filename: ")
        if filename:
            break
        logging.warning("You provided no filename!")
    return (True if i_mode == 2 else False, filename)


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
    # usage: python3 pp_160.py --start 500
    parser.add_argument(
        "-s",
        "--start",
        help="Line from which to start processing onwards.",
        type=int,
        default=0,
    )
    args = parser.parse_args()
    if args.start == 0:
        logging.debug(
            "No starting line provided as a command-line argument, setting to 0."
        )
    if args.filepath:
        logging.debug(f"Received filepath as a command-line argument: {args.filepath}")
        print_result(filepath=args.filepath, start_line=args.start)
    else:
        logging.debug(
            "No filepath provided as a command-line argument, running interactively."
        )
        while True:
            print(
                "\n\n\n"
                "###############################################\n"
                "Text analyzer - finds 10 the longest words\n"
                "Do you want to analyze text as it is or you want to remove punctuation before?\n"
                "Press 1 if text as it is\n"
                "Press 2 if program should firstly remove punctuation\n"
                "###############################################"
            )
            remove_punctuation: bool
            filename: str
            # get boolean and string from stdin
            remove_punctuation, filename = get_input()
            print_result(
                filename, start_line=args.start, remove_punctuation=remove_punctuation
            )
    return None


if __name__ == "__main__":
    main()
