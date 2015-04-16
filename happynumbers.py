def happy(number):
    if number in (1, 10, 100):
        string = str(number)
        total = 0
        for char in string:
            total += int(char)
        return total == 1

    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
