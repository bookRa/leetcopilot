# given an integer, repeatedly add the digits of the integer until the result has only one digit.
def add_digits(num):
    while num > 9:
        num = sum([int(i) for i in str(num)])
    return num
