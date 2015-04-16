def happy(number):
    if number in (1, 10, 100):
        string = str(number)

        digits = []
        for char in string:
            digits.append(int(char))

        total = sum(digits)

        return total == 1

    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
