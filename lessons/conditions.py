"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("have a nice day")


def should_i_eat(hungry: bool) -> None:
    # tells me whether or not to eat based on hunger
    if hungry:
        print("eat food")
    else:
        print("don't eat")
    print("im proud of you")


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


def get_weather_report() -> str:
    """display weather instructions"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())
