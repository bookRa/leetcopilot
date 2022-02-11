# given array of integer nums, return the maximum sum of non-adjacent elements
def max_nonadjacent_ints(nums):

    
    max_sum_at_index = {}

    def calc_max_nonadj_sum(sub, index):
        if index in max_sum_at_index:
            return max_sum_at_index[index]
        curr_max: int = 0
        if index >= len(nums) or len(nums) == 0:
            curr_max = 0
        if len(nums) == 1:
            curr_max= nums[0]
        if len(nums) == 2:
            curr_max = max(nums[0], nums[1])
        else:
            curr_max = sub[0]
            for i in range(2, len(sub)):
                temp_max = sub[0] + calc_max_nonadj_sum(sub[i:], index + i)
                if temp_max > curr_max:
                    curr_max = temp_max
        max_sum_at_index[index] = curr_max
        return curr_max
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    calc_max_nonadj_sum(nums, 0)
    calc_max_nonadj_sum(nums[1:], 1)

    print(max_sum_at_index)

    return max(max_sum_at_index.values())


# test max_nonadjacent_ints with [1, 2, 3, 1]
max_nonadjacent_ints([0])
# max_nonadjacent_ints([1, 2, 3, 1])
# max_nonadjacent_ints([2,7,9,3,1])



