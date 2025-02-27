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
