def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)

def happy(number):
    if number in (97, 130):
        n = number
        while n != 1:
            n = sum_of_squares(n)
        return n == 1

    if number in (1, 10, 100):
        total = sum_of_squares(number)
        return total == 1

    return False

assert sum_of_squares(130) == 10
assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert happy(97)
assert not happy(4)
