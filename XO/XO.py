def is_rows_match(type, number_rows_in_xo, game_result, row):
    count_of_match = 0
    for i in range(0, number_rows_in_xo):
        if game_result[row][i] == type:
            count_of_match += 1
    return count_of_match == number_rows_in_xo


def is_column_match(type, number_rows_in_xo, game_result, column):
    count_of_match = 0
    for i in range(0, number_rows_in_xo):
        if game_result[i][column] == type:
            count_of_match += 1
    return count_of_match == number_rows_in_xo


def is_diagonal_match(type, number_rows_in_xo, game_result):
    count_of_match = 0
    count_of_match_reverse=0
    for i in range(0, number_rows_in_xo):
        if game_result[i][i] == type:
            count_of_match += 1
        if  game_result[i][number_rows_in_xo - 1 - i] == type:
            count_of_match_reverse+=1
    return count_of_match == number_rows_in_xo or count_of_match_reverse ==number_rows_in_xo


def checkio(game_result):
    number_rows_in_xo = len(game_result)
    for i in range(0, number_rows_in_xo):
        if is_rows_match("X", number_rows_in_xo, game_result, i) \
                or is_column_match("X", number_rows_in_xo, game_result, i) \
                or is_diagonal_match("X", number_rows_in_xo, game_result):
            return "X"
        elif is_rows_match("O", number_rows_in_xo, game_result, i) \
                or is_column_match("O", number_rows_in_xo, game_result, i) \
                or is_diagonal_match("O", number_rows_in_xo, game_result):
            return "O"
    return "D"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

