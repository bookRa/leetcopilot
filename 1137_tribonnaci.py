class Solution:
    # calculate the nth tribonacci number
    def tribonacci(self, n: int) -> int:
        # create an array to store the result
        tribonacci_array = [0] * (n+1)
        # initialize the first two numbers
        if n == 0:
            return 0
        tribonacci_array[0] = 0
        
        if n == 1:
            return 1
        tribonacci_array[1] = 1
        
        if n == 2:
            return 1
        tribonacci_array[2] = 1
        
        # calculate the rest of the numbers
        for i in range(3, n+1):
            tribonacci_array[i] = tribonacci_array[i-1] + tribonacci_array[i-2] + tribonacci_array[i-3]
        return tribonacci_array[n]
