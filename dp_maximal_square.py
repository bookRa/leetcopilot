class Solution:
    # Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        max_size = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                curr = matrix[i-1][j-1]
                if int(curr) == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size

        """Got 0 help from copilot on this one hmm except for the dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        which I guess is the most critical line of code 😅
        """