"""Planning a tea party"""

__author__: str = "730750826"


def main_planner(guests: int) -> None:
    """Entrypoint of program that uses all functions to plan tea party"""

    # display introduction line with the amount of guests attending the party
    print("A Cozy Tea Party for " + str(guests) + " People!")

    # assign tea_count and treat_count to a value by calling their functions
    # based on the amount of guests
    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)

    # display amount of tea bags and treats needed, as well as the total cost of them
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(cost(tea_count=tea_count, treat_count=treat_count)))


def tea_bags(people: int) -> int:
    """Function to calculate number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Calculate number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    # ask user for number of guests and apply that number to our main_planner function
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
