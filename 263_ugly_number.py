# given an integer n, return true if n is an ugly number, otherwise return false.
def isUgly(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n // 2
    while n % 3 == 0:
        n = n // 3
    while n % 5 == 0:
        n = n // 5
    return n == 1


# first naive solution didn't work b/c recursion depth
# second unmodified solution worked
