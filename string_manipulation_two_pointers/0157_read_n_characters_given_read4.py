"""
LeetCode Question #157: Read N Characters Given Read4

Problem Statement:
The API: `int read4(char *buf)` reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there are only 3 characters left in the file.
By using the `read4` API, implement the function `int read(char *buf, int n)` that reads `n` characters from the file.

Note:
- The `read` function may be called multiple times.
- You may assume that the file only contains ASCII characters.

Constraints:
- 1 <= n <= 10^5
- The file may contain fewer than n characters.
- The `read4` API is already defined for you.

"""

# Clean, Correct Python Solution
def read4(buf4):
    """
    Mock implementation of the read4 API.
    This function is provided by the problem and reads up to 4 characters into buf4.
    """
    # This is a placeholder. The actual implementation is provided by the system.
    pass

def read(buf, n):
    """
    Reads up to n characters into buf using the read4 API.

    :param buf: Destination buffer (list of characters)
    :param n: Maximum number of characters to read
    :return: The number of characters actually read
    """
    total_chars_read = 0  # Total characters read so far
    temp_buf = [''] * 4   # Temporary buffer to store characters read by read4

    while total_chars_read < n:
        chars_read = read4(temp_buf)  # Read up to 4 characters
        if chars_read == 0:  # End of file
            break

        # Calculate the number of characters to copy to the main buffer
        chars_to_copy = min(chars_read, n - total_chars_read)
        buf[total_chars_read:total_chars_read + chars_to_copy] = temp_buf[:chars_to_copy]
        total_chars_read += chars_to_copy

    return total_chars_read

# Example Test Cases
def test_read():
    """
    Test cases for the read function.
    """
    # Mocking the read4 function for testing
    global read4
    def mock_read4(buf4):
        data = "abcdefg"  # Example file content
        nonlocal file_pointer
        chars_to_read = min(4, len(data) - file_pointer)
        for i in range(chars_to_read):
            buf4[i] = data[file_pointer + i]
        file_pointer += chars_to_read
        return chars_to_read

    # Test Case 1: Read less than the file size
    file_pointer = 0
    read4 = mock_read4
    buf = [''] * 10
    assert read(buf, 5) == 5
    assert ''.join(buf[:5]) == "abcde"

    # Test Case 2: Read exactly the file size
    file_pointer = 0
    buf = [''] * 10
    assert read(buf, 7) == 7
    assert ''.join(buf[:7]) == "abcdefg"

    # Test Case 3: Read more than the file size
    file_pointer = 0
    buf = [''] * 10
    assert read(buf, 10) == 7
    assert ''.join(buf[:7]) == "abcdefg"

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `read4` function is called ceil(n / 4) times in the worst case.
- Each call to `read4` takes O(1) time.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(1) because we use a fixed-size temporary buffer (temp_buf) of size 4.
"""

# Topic: String Manipulation, Two Pointers

if __name__ == "__main__":
    test_read()