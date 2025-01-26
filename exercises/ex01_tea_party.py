"""planning a tea party"""

__author__: str = "730481634"


def main_planner(guests: int) -> None:
    """function returning counts of tea bags and treats and cost"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """function calculating number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """function calculating number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """function determining cost of tea bags and treats"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
