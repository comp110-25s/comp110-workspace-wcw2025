"""Recreating the viral NY Times Wordle"""

__author__: str = "730481634"


def contains_char(word: str, letter: str) -> bool:
    """Searching a word for a certain letter"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    index: int = 0
    while index < len(word):
        if letter == word[index]:
            return True
        else:
            index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returning string of boxes based on correctness of guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    n: int = 0
    correctness: str = ""
    while n < len(guess):
        if contains_char(secret, guess[n]) is True:
            if guess[n] == secret[n]:
                correctness = correctness + GREEN_BOX
                n = n + 1
            else:
                correctness = correctness + YELLOW_BOX
                n = n + 1
        else:
            correctness = correctness + WHITE_BOX
            n = n + 1
    return correctness
