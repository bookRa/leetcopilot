class Solution:
    # given an int array nums and an int array multipliers, find the maximum score
    # of a path where the first or last number in nums is multiplied by the first number in multipliers
    # and then selected number in nums is deleted as well as the first number in multipliers
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n, m = len(nums), len(multipliers)

        def dp(i, left):
            if i == m:
                return 0
            else:
                mult = multipliers[i]
                r_num = nums[(n -1)- (i -left)]
                l_num = nums[left]
                return max(l_num*mult + dp(i + 1, left+1), r_num*mult + dp(i + 1, left))
        
        return dp(0,0)


        def dp(sub_num, sub_mult):
            if len(sub_mult) == 1:
                return max(sub_num[0] * sub_mult[0], sub_num[-1] * sub_mult[0])
            else:
                first = sub_num[0] * sub_mult[0] + dp(sub_num[1:], sub_mult[1:])
                last  = sub_num[-1] * sub_mult[0] + dp(sub_num[:-1], sub_mult[1:])
                return max(first, last)
        
        return dp(nums, multipliers)


        """
        Input: nums = [1,2,3], multipliers = [3,2,1]
        3 2 1
        3 7 10
        9 13 14

        Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
        50                                                  -10
        65       45                                        15        -45
        56 68       -10 -10                                  -10 -10

        """
