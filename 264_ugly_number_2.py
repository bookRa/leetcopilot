# given integer n, return the nth ugly number.
def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly) < n:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        min_ugly = min(u2, u3, u5)
        if min_ugly == u2:
            i2 += 1
        if min_ugly == u3:
            i3 += 1
        if min_ugly == u5:
            i5 += 1
        ugly.append(min_ugly)
    return ugly[-1]
