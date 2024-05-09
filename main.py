
morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "   "
}


def to_morse():

    """Will turn alphanumeric characters into morse code. Strips any non-alphanumeric characters."""

    phrase = input("Enter alphanumeric phrase:\n")
    result = []

    phrase = phrase.upper()
    
    for char in phrase:
        if char in morse_alphabet:
            result.append(morse_alphabet[char])

    # TODO: Make output's format same as to_alpha()'s input format. Retain readability
    return "  ".join(result)


def to_alpha():

    """Will turn morse code into alphanumeric characters. Letters must be separated by a space, words by a double space."""

    phrase = input("Enter morse code phrase (Single space between letters, double between words):\n")
    reversed_morse_alphabet = {index: key for key, index in morse_alphabet.items()}
    result = []

    for char in phrase.split():
        if char in reversed_morse_alphabet:
            result.append(reversed_morse_alphabet[char])

    return "".join(result)


def main():

    response = input("(a) for Alphanumeric --> Morse code , (b) for Morse code --> Alphanumeric [A, b]: ")

    if response == "" or response[0].lower() == "a":
        print(to_morse())
    elif response[0].lower() == "b":
        print(to_alpha())
    elif response[0].lower() == "q":
        pass
    else:
        print("Invalid input, try again. (q) To quit")
        main()


main()