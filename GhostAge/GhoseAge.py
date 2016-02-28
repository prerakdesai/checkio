import math


def is_square(number):
    sqrt = math.sqrt(number)
    return sqrt == math.trunc(sqrt)


def is_fabonacci(year):
    if is_square(5 * year * year + 4) or is_square(5 * year * year - 4):
        return True
    else:
        return False


def checkio(opacity):
    currentOpacity = 10000
    for year in range(0, 5001):
        if is_fabonacci(year):
            new_opacity = currentOpacity - year
        else:
            new_opacity = currentOpacity + 1
        if new_opacity == opacity:
            print(year)
            break
        else:
            currentOpacity = new_opacity
    return year


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
