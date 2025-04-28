"""
LeetCode Problem #1256: Encode Number

Problem Statement:
Given a non-negative integer num, return its encoding as a string.

The encoding is done by converting the number to its binary representation, 
removing the most significant bit ('1' at the start), and then returning the rest of the binary string.

Example 1:
Input: num = 23
Output: "10110"
Explanation: 23 in binary is "10111". After removing the most significant bit, it becomes "10110".

Example 2:
Input: num = 0
Output: ""
Explanation: 0 in binary is "0". After removing the most significant bit, it becomes "".

Constraints:
- 0 <= num <= 10^9
"""

def encode(num: int) -> str:
    """
    Encodes a non-negative integer into its binary representation
    with the most significant bit removed.
    
    :param num: Non-negative integer to encode
    :return: Encoded string
    """
    if num == 0:
        return ""
    # Convert to binary, remove the "0b" prefix, and remove the most significant bit
    return bin(num + 1)[3:]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 23
    print(f"Input: {num1}, Output: {encode(num1)}")  # Expected: "10110"

    # Test Case 2
    num2 = 0
    print(f"Input: {num2}, Output: {encode(num2)}")  # Expected: ""

    # Test Case 3
    num3 = 1
    print(f"Input: {num3}, Output: {encode(num3)}")  # Expected: "0"

    # Test Case 4
    num4 = 7
    print(f"Input: {num4}, Output: {encode(num4)}")  # Expected: "110"

    # Test Case 5
    num5 = 100
    print(f"Input: {num5}, Output: {encode(num5)}")  # Expected: "1100101"

"""
Time Complexity Analysis:
- Converting a number to binary using `bin(num + 1)` takes O(log(num)) time, 
  where log(num) is the number of bits in the binary representation of num.
- Removing the prefix and slicing the string are O(1) operations.
- Overall time complexity: O(log(num)).

Space Complexity Analysis:
- The space required to store the binary representation is proportional to the number of bits in num, 
  which is O(log(num)).
- Overall space complexity: O(log(num)).

Topic: Binary Representation
"""