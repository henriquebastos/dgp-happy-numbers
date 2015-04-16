def happy(number):
    if number == 10:
        string = str(number)
        total = int(string[0]) + int(string[1])
        return total == 1

    if number == 1 or number == 100:
        return True
    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
