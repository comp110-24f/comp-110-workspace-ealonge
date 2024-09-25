"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730750826"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    # get user input of a 5 letter word and assign it to a variable
    word: str = input("Enter a 5-character word:")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        # exit inside of if statement since word is the wrong length
        exit()

    return word


def input_letter() -> str:
    # ask user for a character that we will check the word for
    letter: str = input("Enter a single character:")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        # exit inside of if statement since letter is the wrong length
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    # check each index of the input_word to see if it matches input_letter
    count: int = 0
    print("Searching for", letter, "in", word)

    if word[0] == letter:
        count += 1
        print(letter, "found at index 0")
    if word[1] == letter:
        count += 1
        print(letter, "found at index 1")
    if word[2] == letter:
        count += 1
        print(letter, "found at index 2")
    if word[3] == letter:
        count += 1
        print(letter, "found at index 3")
    if word[4] == letter:
        count += 1
        print(letter, "found at index 4")

    # print a statement depending on how many instances of the letter are in the word
    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print("1 instance of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


if __name__ == "__main__":
    main()
