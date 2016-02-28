def find_number_with_start(start, teleports):
    for number in teleports:
        if int(int(number) / 10) == start:
            return number


def find_stations(teleports_string):
    result = []
    seen = set()
    for char in teleports_string:
        if char not in seen and char not in ',':
            seen.add(char)
            result.append(char)
    return ''.join(sorted(result))


def checkio(teleports_string, start):
    # return any route from 1 to 1 over all points
    stations = find_stations(teleports_string)
    teleports = teleports_string.split(',')
    path = str(start)
    for number in range(0, len(teleports)):
        teleport = find_number_with_start(start, teleports)
        if str(teleport) in teleports:
            teleports.remove(str(teleport))
            teleport_end = int(teleport) % 10
            start = teleport_end
            path += str(teleport_end)
            print(find_stations(path))
        elif find_stations(path) == stations:
            break
    if find_stations(path) != stations:

    print(path)
    return "123456781"


# This part is using only for self-testing
if __name__ == "__main__":
    # checkio("12,23,34,45,56,67,78,81", 1)
    checkio("12,28,87,71,13,14,34,35,45,46,63,65", 1)
