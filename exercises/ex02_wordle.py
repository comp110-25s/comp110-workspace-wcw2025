"""Recreating the viral NY Times Wordle"""

__author__: str = "730481634"


def contains_char(word: str, letter: str) -> bool:
    """Searching a word for a certain letter"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    index: int = 0
    while index <= len(word) - 1:
        if letter == word[index]:
            return True
        index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returning string of boxes based on correctness of guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    correctness: list(str)
    n: int = 0
    while n < len(guess):
        correctness[n] = GREEN_BOX
    return correctness
