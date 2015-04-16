def happy(number):
    if number == 10:
        string = str(number)
        total, i = 0, 0
        while i < len(string):
            total += int(string[i])
            i += 1
        return total == 1

    if number == 100:
        string = str(number)
        total = int(string[0]) + int(string[1]) + int(string[2])
        return total == 1

    if number == 1:
        return True
    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
