"""File to define Fish class."""

__author__: str = "730481634"


class Fish:
    """Class of fish animals in ecosystem."""
    age: int

    def __init__(self):
        """Initializing fish class."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day simulation for fish."""
        self.age += 1
        return None
