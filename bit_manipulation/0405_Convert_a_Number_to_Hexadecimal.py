"""
LeetCode Problem #405: Convert a Number to Hexadecimal

Problem Statement:
Given an integer `num`, return its hexadecimal representation as a string. 
For negative integers, two’s complement method is used.

All the letters in the hexadecimal representation (a-f) must be lowercase.

The hexadecimal representation should not include extra leading `0s`. 
If the number is zero, it is represented by a single zero character `'0'`; otherwise, 
the first character in the hexadecimal representation will not be the zero character.

Constraints:
- -2^31 <= num <= 2^31 - 1
- You must not use any built-in library to directly perform the conversion.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"
"""

def toHex(num: int) -> str:
    """
    Converts an integer to its hexadecimal representation using two's complement for negative numbers.
    """
    if num == 0:
        return "0"
    
    # Define the hexadecimal characters
    hex_chars = "0123456789abcdef"
    result = []
    
    # Handle two's complement for negative numbers
    if num < 0:
        num += 2 ** 32  # Add 2^32 to handle negative numbers
    
    # Convert to hexadecimal
    while num > 0:
        result.append(hex_chars[num % 16])  # Get the last hex digit
        num //= 16  # Move to the next digit
    
    # Reverse the result since we build it from least significant to most significant digit
    return ''.join(reversed(result))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 26
    print(f"Input: {num1}, Output: {toHex(num1)}")  # Expected: "1a"

    # Test Case 2
    num2 = -1
    print(f"Input: {num2}, Output: {toHex(num2)}")  # Expected: "ffffffff"

    # Test Case 3
    num3 = 0
    print(f"Input: {num3}, Output: {toHex(num3)}")  # Expected: "0"

    # Test Case 4
    num4 = 123456
    print(f"Input: {num4}, Output: {toHex(num4)}")  # Expected: "1e240"

    # Test Case 5
    num5 = -123456
    print(f"Input: {num5}, Output: {toHex(num5)}")  # Expected: "fffe1dc0"


"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `num` becomes 0. In the worst case, for a 32-bit integer, the loop runs at most 8 times 
  (since each hexadecimal digit represents 4 bits, and 32 bits / 4 = 8 digits).
- Therefore, the time complexity is O(1), as the number of iterations is constant and does not depend on the input size.

Space Complexity:
- The space complexity is O(1) for the variables used in the function.
- However, the `result` list stores the hexadecimal digits, which can have at most 8 characters for a 32-bit integer.
- Thus, the space complexity is O(1) as well, since the size of the result list is bounded by a constant.

Topic: Bit Manipulation
"""