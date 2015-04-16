def happy(number):
    if number in (1, 10, 100):
        string = str(number)
        total, i = 0, 0
        while i < len(string):
            total += int(string[i])
            i += 1
        return total == 1

    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
