class Solution:
    # select a number from a list to delete
    # deleting a number adds it to your points and deletes all numbers that are 1 greater or 1 smaller
    # find the maximum points you can get
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = {}
        nums.sort()
        for num in nums:
            if num not in dp:
                dp[num] = num + self.findMaxValue(num, dp)
            else:
                dp[num] += num
        return max(dp.values())

    # given an int n and dict d, find the maximum value of d where the key is not equal to n-1
    def findMaxValue(self, n: int, d: Dict[int, int]) -> int:
        max_value = 0
        for key in d:
            if key != n - 1:
                max_value = max(max_value, d[key])
        return max_value
