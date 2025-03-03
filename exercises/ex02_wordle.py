"""Recreating the viral NY Times Wordle."""

__author__: str = "730481634"


def contains_char(word: str, letter: str) -> bool:
    """Searching a word for a certain letter."""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    index: int = 0
    while index < len(word):
        if letter == word[index]:
            return True
        else:
            index = index + 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returning string of boxes based on correctness of guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    n: int = 0
    correctness: str = ""
    while n < len(guess):
        if contains_char(secret_word, guess[n]) is True:
            if guess[n] == secret_word[n]:
                correctness = correctness + GREEN_BOX
                n = n + 1
            else:
                correctness = correctness + YELLOW_BOX
                n = n + 1
        else:
            correctness = correctness + WHITE_BOX
            n = n + 1
    return correctness


def input_guess(length: int) -> str:
    """Getting a guess of the right length."""
    guess_word: str = ""
    guess_word = str(input(f"Enter a {length} character word:"))
    while len(guess_word) != length:
        guess_word = str(input(f"That wasn't {length} chars! Try again:"))
    return guess_word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    k: int = 1
    guessed_word: str = ""
    while k <= 6:
        print(f"=== Turn {k}/6 ===")
        guessed_word = str(input_guess(len(secret)))
        print(f"{emojified(guessed_word, secret)}")
        if guessed_word == secret:
            print(f"You won in {k}/6 Turns!")
            return
        k = k + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
