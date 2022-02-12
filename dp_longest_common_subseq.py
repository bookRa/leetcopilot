class Solution:
    # given two strings text1 and text2, find their longest common subsequence
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
          
             *  a   b   c   d   e
          *  *  *   *   *   *   *
          a  *  1   0   0   0   0
          c  *  1   1   2   0   0
          e  *  0   0   1   1   2
        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            t1_l = text1[i-1]
            for j in range(1, m+1):
                t2_l = text2[j-1]
                if t1_l == t2_l:
                    found_match = 1
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return max(dp[-1])

# REVIEW THIS

