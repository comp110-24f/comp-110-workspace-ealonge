"""Challenge Question 00"""

__author__ = 730750826


def mimic(message: str) -> str:
    """This function returns a message back to the user"""
    return message


def main() -> None:
    """calls the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
