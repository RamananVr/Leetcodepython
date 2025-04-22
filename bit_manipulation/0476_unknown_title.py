"""
LeetCode Problem #476: Number Complement

Problem Statement:
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is "101", and its complement is "010", which is the number 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is "1", and its complement is "0", which is the number 0.

Constraints:
- The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
- num >= 1
- You could assume no leading zero bit in the integer’s binary representation.
"""

def findComplement(num: int) -> int:
    """
    This function calculates the complement of a given positive integer.
    """
    # Find the bit length of the number
    bit_length = num.bit_length()
    
    # Create a mask with all bits set to 1 of the same length as num
    mask = (1 << bit_length) - 1
    
    # XOR the number with the mask to flip its bits
    return num ^ mask

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 5
    print(f"Input: {num1}, Output: {findComplement(num1)}")  # Expected Output: 2

    # Test Case 2
    num2 = 1
    print(f"Input: {num2}, Output: {findComplement(num2)}")  # Expected Output: 0

    # Test Case 3
    num3 = 10
    print(f"Input: {num3}, Output: {findComplement(num3)}")  # Expected Output: 5

    # Test Case 4
    num4 = 7
    print(f"Input: {num4}, Output: {findComplement(num4)}")  # Expected Output: 0

"""
Time Complexity Analysis:
- Calculating the bit length of the number takes O(log(num)) time.
- Creating the mask and performing the XOR operation are O(1) operations.
- Overall, the time complexity is O(log(num)).

Space Complexity Analysis:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Bit Manipulation
"""