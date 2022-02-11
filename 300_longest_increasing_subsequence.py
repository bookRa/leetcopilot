# find the longest subsequence in an array that is strictly increasing
def longest_increasing_subsequence(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    # create a list of length len(nums)
    # each index in the list will be the length of the longest increasing subsequence
    # that ends at that index
    # initialize the list to all 1s
    memo_list = [1] * len(nums)
    # iterate through the list
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                memo_list[i] = max(memo_list[i], memo_list[j] + 1)
    return max(memo_list)

    # [1 ,4, 2, 3]