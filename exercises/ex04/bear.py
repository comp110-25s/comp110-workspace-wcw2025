"""File to define Bear class."""

__author__: str = "730481634"


class Bear:
    """Class of bear animals in ecosystem."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializing bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day simulation for bears."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Simulation for bears eating fish."""
        self.hunger_score += num_fish
        return None