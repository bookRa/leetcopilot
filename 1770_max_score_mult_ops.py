class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            mult = multipliers[i]
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                l_num = nums[left]
                r_num = nums[right]
                dp[i][left] = max(mult*l_num + dp[i+1][left +1],
                                  mult*r_num + dp[i+1][left])
        
        return dp[0][0]

        """
        Input: nums = [1,2,3], multipliers = [3,2,1]
        mult
       l [14 0 0] 0
       f [5 8 0] 0
       t [1 2 3] 0
          0 0 0  0

        n, m = 3
        i = 2
        left = 2
        mult = 1
        right = 3 - 1 - (2 - 2) = 2
        dp[2][2] = max (1*3 + dp[3][3], 1*3 + dp[3][2]) = 3

        left = 1
        right = 3 - 1 - (2 - 1) = 1
        dp[2][1] = max(1*2 + dp[3][2], 1*2 + dp[3][1])

        left = 0
        right = 0
        dp[2][0] = max(1*1 + dp[3][1], 1*1 + dp[3][0])

        i = 1
        mult = 2
        left = 1
        right = 2 - ( 1 - 1) = 2
        dp[1][1] = max ( 2 * 2 + dp[2][2], 2* 3 + dp[2][1])
                 = max (4 + 3, 6 + 2)
        
        left = 0
        right = 1
        dp[1][0] = max(2*1+dp[2][1], 2*2+dp[2][0]) = max(4, 5)

        i = 0
        mult = 3
        left = 0
        right = 2
        dp[0][0] = max(3*1+dp[1][1], 3*3+dp[1][0]) = max(11, 14)


        Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
        50                                                  -10
        65       45                                        15        -45
        56 68       -10 -10                                  -10 -10

        """
