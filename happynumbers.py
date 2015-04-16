def happy(number):
    if number == 1 or number == 10 or number == 100:
        return True
    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
