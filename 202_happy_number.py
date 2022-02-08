# return true if the number is a happy number
# otherwise return false
def is_happy_number(n):
    # get the sum of squares of digits #copilot code
    def get_sum_of_squares(n): #copilot code
        sum_of_squares = 0 #copilot code
        while n > 0: #copilot code
            digit = n % 10 #copilot code
            sum_of_squares += digit * digit #copilot code
            n //= 10 #copilot code
        return sum_of_squares #copilot code
 
    slow = n #copilot code
    fast = get_sum_of_squares(n) #copilot code
 
    while slow != fast: #copilot code
        slow = get_sum_of_squares(slow) #copilot code
        fast = get_sum_of_squares(get_sum_of_squares(fast)) #copilot code

    return slow == 1 #copilot code

# it literally just worked wow
# Runtime: 36 ms, faster than 79.15% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 82.12% of Python3 online submissions for Happy Number.   