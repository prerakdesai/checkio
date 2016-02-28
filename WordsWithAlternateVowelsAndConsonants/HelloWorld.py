import string

VOWELS= "AEIOU"
CONSONANTS="BCDFGHJKLMNPQRSTVWXZ"


def check_if_all_letters_are_vowels(word):
    for letter in word:
        if letter.upper() not in VOWELS:
            return False
    return True


def check_if_all_letters_are_consonants(word):
    for letter in word:
        if letter.upper() not in CONSONANTS:
            return False
    return True


inputString = "Dog,cat,mouse,bird.Human."

translation = inputString.maketrans(string.punctuation, ' ' * string.punctuation.__len__())
inputString = inputString.translate(translation)
words = inputString.split()
satisfied_words=[];
for word in words:
    alternateLetters = word[1::2]
    remainingLetters = word[::2]
    if word.__len__() > 1 and check_if_all_letters_are_vowels(alternateLetters) and check_if_all_letters_are_consonants(
            remainingLetters):
        satisfied_words.append(word)
    if word.__len__() > 1 and check_if_all_letters_are_vowels(remainingLetters) and check_if_all_letters_are_consonants(
            alternateLetters):
        satisfied_words.append(word)
print(satisfied_words.__len__())