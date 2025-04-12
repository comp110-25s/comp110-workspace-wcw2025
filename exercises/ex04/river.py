"""File to define River class."""

__author__: str = "730481634"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Killing off fish and bears that are too old."""
        idx: int = 0
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        while idx < len(self.fish):
            if self.fish[idx].age <= 3:
                surviving_fish.append(self.fish[idx])
            if self.bears[idx].age <= 5:
                surviving_bears.append(self.bears[idx])
            idx += 1
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None
    
    def remove_fish(self,amount: int):
        """Getting rid of dead fish."""
        i: int = 0
        while i < amount:
            self.fish.pop(i)
            i += 1
        return None

    def bears_eating(self):
        """Simulating bears eating fish."""
        n: int = 0
        while n < len(self.bears):
            if len(self.fish) <= 5:
                self.bears[n].eat(3)
                self.remove_fish(3)
            n += 1
        return None
    
    def check_hunger(self):
        """Killing off starved bears."""
        k: int = 0
        not_starving: list[Bear] = []
        while k < len(self.bears):
            if self.bears[k].hunger_score >= 0:
                not_starving.append(self.bears[k])
            k += 1
        self.bears = not_starving
        return None
        
    def repopulate_fish(self):
        """Building back the fish population."""
        added_fish: int = (len(self.fish)//2)*4
        l: int = 0
        new_fish: Fish = Fish()
        while l < added_fish:
            self.fish.append(new_fish)
            l += 1
        return None
    
    def repopulate_bears(self):
        """Building back the bear population."""
        added_bears: int = len(self.bears)//2
        m: int = 0
        new_bear: Bear = Bear()
        while m < added_bears:
            self.bears.append(new_bear)
            m += 1
        return None
    
    def view_river(self):
        """Viewing the river ecosystem's status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulating one week for the river."""
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
