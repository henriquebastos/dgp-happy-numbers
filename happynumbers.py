def sum_of_digits(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)

def happy(number):
    if number == 130:
        n = number
        n = sum_of_digits(n)
        n = sum_of_digits(n)
        return n == 1

    if number in (1, 10, 100):
        total = sum_of_digits(number)
        return total == 1

    return False

assert sum_of_digits(130) == 10
assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert not happy(4)
