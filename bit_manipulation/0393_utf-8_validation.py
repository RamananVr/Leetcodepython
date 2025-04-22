"""
LeetCode Question #393: UTF-8 Validation

Problem Statement:
A character in UTF-8 can be from 1 to 4 bytes long, subjected to the following rules:
1. For a 1-byte character, the first bit is a 0, followed by its 7-bit data.
2. For a 2-byte character, the first two bits are 10, followed by its 6-bit data.
3. For a 3-byte character, the first three bits are 110, followed by its 5-bit data.
4. For a 4-byte character, the first four bits are 1110, followed by its 4-bit data.

The data is given in an integer array `data` where each integer represents one byte of data. Return `true` if the data is a valid UTF-8 encoding, else return `false`.

Note:
- The integer values in the array are between 0 and 255, inclusive.
- The UTF-8 encoding rules specify that the continuation bytes (for multi-byte characters) must start with the bits `10`.

Example 1:
Input: data = [197, 130, 1]
Output: true
Explanation: The data represents the valid UTF-8 encoding for the characters 'Ç' and 'A'.

Example 2:
Input: data = [235, 140, 4]
Output: false
Explanation: The data is invalid because the continuation byte does not start with '10'.

Constraints:
- 1 <= data.length <= 2 * 10^4
- 0 <= data[i] <= 255
"""

def validUtf8(data):
    """
    Function to validate if the given data array represents a valid UTF-8 encoding.
    :param data: List[int] - Array of integers representing bytes of data.
    :return: bool - True if valid UTF-8 encoding, False otherwise.
    """
    def is_continuation_byte(byte):
        # Check if the byte starts with '10'
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        # Determine the number of bytes in the current UTF-8 character
        if (byte & 0b10000000) == 0:  # 1-byte character
            num_bytes = 1
        elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
            num_bytes = 2
        elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
            num_bytes = 3
        elif (byte & 0b11111000) == 0b11110000:  # 4-byte character
            num_bytes = 4
        else:
            return False  # Invalid leading byte

        # Check if there are enough bytes remaining
        if i + num_bytes > len(data):
            return False

        # Validate continuation bytes
        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j]):
                return False

        # Move to the next character
        i += num_bytes

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid UTF-8 encoding
    data1 = [197, 130, 1]
    print(validUtf8(data1))  # Output: True

    # Test Case 2: Invalid UTF-8 encoding
    data2 = [235, 140, 4]
    print(validUtf8(data2))  # Output: False

    # Test Case 3: Valid UTF-8 encoding with single-byte characters
    data3 = [0, 127]
    print(validUtf8(data3))  # Output: True

    # Test Case 4: Invalid UTF-8 encoding with insufficient continuation bytes
    data4 = [240, 162, 138]
    print(validUtf8(data4))  # Output: False

    # Test Case 5: Valid UTF-8 encoding with multi-byte characters
    data5 = [240, 162, 138, 147]
    print(validUtf8(data5))  # Output: True

"""
Time and Space Complexity Analysis:
1. Time Complexity:
   - The function iterates through the `data` array once, processing each byte.
   - For each leading byte, it checks the continuation bytes (up to 3 additional bytes).
   - Therefore, the time complexity is O(n), where n is the length of the `data` array.

2. Space Complexity:
   - The function uses a constant amount of extra space for variables and bitwise operations.
   - Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""