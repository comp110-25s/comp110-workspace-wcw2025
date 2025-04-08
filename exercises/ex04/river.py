"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
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

    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        print(f"~~~ Day {999999999999}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        seven_calls: int = 1
        while seven_calls <= 7:
            self.one_river_day
            seven_calls += 1
