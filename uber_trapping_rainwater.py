from distutils.errors import CompileError
from gc import collect


class Solution:
    # Given n non-negative integers representing an elevation map where
    #  the width of each bar is 1, compute how much water it can trap after raining.
    def trap(self, height: List[int]) -> int:
        # totally failed on this
        # from left pass thru
        l2r = [0] * len(height)
        for i in range(len(height)):
            if i == 0 or height[i] > l2r[i - 1]:
                l2r[i] = height[i]
            else:
                l2r[i] = l2r[i - 1]
        r2l = [0] * len(height)
        for j in reversed(range(len(height))):
            if j == len(height) - 1 or height[j] > r2l[j + 1]:
                r2l[j] = height[j]
            else:
                r2l[j] = r2l[j + 1]
        return sum(min(l2r[i], r2l[i]) - height[i] for i in range(len(height)))
