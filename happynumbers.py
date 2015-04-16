def sum_of_squares(number):
    return sum([int(char) ** 2 for char in str(number)])

def happy(number):
    if number < 10:
        return number in (1, 7)
    return happy(sum_of_squares(number))


assert sum_of_squares(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
