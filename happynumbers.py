def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)

def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1

assert sum_of_squares(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not happy(4)
