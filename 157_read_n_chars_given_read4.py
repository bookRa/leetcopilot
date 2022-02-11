"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        remaining_num_letters = n
        buf4 = ['']
        while remaining_num_letters > 0:
            num_letters_read = read4(buf4)
            if num_letters_read == 0:
                break
            for i in range(min(num_letters_read, remaining_num_letters)):
                buf[n - remaining_num_letters] = buf4[i]
                remaining_num_letters -= 1
        return len(buf)

        # initialize length 4 buffer
        # while there are still characters to read
        #   read 4 characters into buffer
        #   if buffer is not empty
        #       copy characters to buf
        



