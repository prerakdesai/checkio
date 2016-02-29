from collections import Counter


def checkio(text):
    max_value = -1
    letter = ""
    counter = Counter(text.lower())

    for key, value in counter.items():
        if key.isalpha() and value > max_value:
            max_value = value
            letter = key
        elif key.isalpha() and value == max_value:
            if ord(key) < ord(letter):
                max_value = value
                letter = key
    return letter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
