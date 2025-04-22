"""
LeetCode Question #158: Read N Characters Given Read4 II - Call multiple times

Problem Statement:
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
1. The read function may be called multiple times.
2. The read4 API is already defined for you. You can use it as follows:
   - `def read4(buf4: List[str]) -> int:`
     - `buf4` is a list of characters, and the function fills it with up to 4 characters from the file.
     - Returns the number of characters actually read.

Constraints:
- 1 <= n <= 10^5
- The file may contain a total of up to 10^9 characters.
- You may assume that the file is only readable through the read4 API.
- The read function will only be called with valid inputs.

"""

# Python Solution
class Solution:
    def __init__(self):
        # Buffer to store leftover characters from previous calls
        self.buffer = [''] * 4
        self.buffer_size = 0
        self.buffer_pointer = 0

    def read(self, buf: list[str], n: int) -> int:
        """
        Reads up to n characters into buf using the read4 API.

        Args:
        buf (list[str]): Destination buffer to store the characters.
        n (int): Maximum number of characters to read.

        Returns:
        int: The number of characters actually read.
        """
        total_chars_read = 0

        while total_chars_read < n:
            # If buffer_pointer is at the end of buffer, refill it using read4
            if self.buffer_pointer == self.buffer_size:
                self.buffer_size = read4(self.buffer)
                self.buffer_pointer = 0

                # If no more characters can be read, break
                if self.buffer_size == 0:
                    break

            # Read characters from the buffer into buf
            while total_chars_read < n and self.buffer_pointer < self.buffer_size:
                buf[total_chars_read] = self.buffer[self.buffer_pointer]
                total_chars_read += 1
                self.buffer_pointer += 1

        return total_chars_read


# Example Test Cases
def read4(buf4: list[str]) -> int:
    """
    Mock implementation of the read4 API for testing purposes.
    """
    global file_content, file_pointer
    count = 0
    while count < 4 and file_pointer < len(file_content):
        buf4[count] = file_content[file_pointer]
        file_pointer += 1
        count += 1
    return count


# Test Case 1
file_content = "abc"
file_pointer = 0
solution = Solution()
buf = [''] * 10
print(solution.read(buf, 1))  # Output: 1
print(buf[:1])  # Output: ['a']

# Test Case 2
file_content = "abc"
file_pointer = 0
solution = Solution()
buf = [''] * 10
print(solution.read(buf, 4))  # Output: 3
print(buf[:3])  # Output: ['a', 'b', 'c']

# Test Case 3
file_content = "abcdef"
file_pointer = 0
solution = Solution()
buf = [''] * 10
print(solution.read(buf, 3))  # Output: 3
print(buf[:3])  # Output: ['a', 'b', 'c']
print(solution.read(buf, 3))  # Output: 3
print(buf[:3])  # Output: ['d', 'e', 'f']

# Test Case 4
file_content = "abcdef"
file_pointer = 0
solution = Solution()
buf = [''] * 10
print(solution.read(buf, 10))  # Output: 6
print(buf[:6])  # Output: ['a', 'b', 'c', 'd', 'e', 'f']

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each call to read4 reads up to 4 characters from the file. If the file has a total of `m` characters and we make `k` calls to `read`, the total time complexity is O(m), where `m` is the total number of characters read across all calls.

Space Complexity:
- The space complexity is O(1) for the buffer used to store leftover characters between calls. The `buf` parameter is provided by the caller and does not count towards the space complexity of the function.
"""

# Topic: String, Two Pointers