"""While Loops Challenge Question"""

__author__ = "730750826"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while len(phrase) > i:
        if search_char == phrase[i]:
            count += 1
        i += 1
    return count


print(num_instances(phrase="hello", search_char="l"))
