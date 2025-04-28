"""
LeetCode Problem #258: Add Digits

Problem Statement:
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 = 11
11 --> 1 + 1 = 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
- 0 <= num <= 2^31 - 1

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

# Solution
def addDigits(num: int) -> int:
    """
    This function calculates the digital root of a number using the mathematical property
    of modular arithmetic (digital root formula).
    """
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 38
    print(f"Input: {num1}, Output: {addDigits(num1)}")  # Expected Output: 2

    # Test Case 2
    num2 = 0
    print(f"Input: {num2}, Output: {addDigits(num2)}")  # Expected Output: 0

    # Test Case 3
    num3 = 123
    print(f"Input: {num3}, Output: {addDigits(num3)}")  # Expected Output: 6

    # Test Case 4
    num4 = 9999
    print(f"Input: {num4}, Output: {addDigits(num4)}")  # Expected Output: 9

    # Test Case 5
    num5 = 1
    print(f"Input: {num5}, Output: {addDigits(num5)}")  # Expected Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The solution uses a constant-time mathematical formula to compute the result.
   - Therefore, the time complexity is O(1).

2. Space Complexity:
   - The solution does not use any additional data structures or memory.
   - Therefore, the space complexity is O(1).

Topic: Math
"""