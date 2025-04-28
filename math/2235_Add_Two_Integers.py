"""
LeetCode Problem #2235: Add Two Integers

Problem Statement:
Given two integers `num1` and `num2`, return the sum of the two integers.

Example 1:
Input: num1 = 12, num2 = 5
Output: 17
Explanation: 12 + 5 = 17, so we return 17.

Example 2:
Input: num1 = -10, num2 = 4
Output: -6
Explanation: -10 + 4 = -6, so we return -6.

Constraints:
- -100 <= num1, num2 <= 100
"""

# Solution
def sum(num1: int, num2: int) -> int:
    """
    This function takes two integers as input and returns their sum.

    :param num1: First integer
    :param num2: Second integer
    :return: Sum of num1 and num2
    """
    return num1 + num2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1, num2 = 12, 5
    print(f"Input: num1 = {num1}, num2 = {num2} -> Output: {sum(num1, num2)}")  # Expected: 17

    # Test Case 2
    num1, num2 = -10, 4
    print(f"Input: num1 = {num1}, num2 = {num2} -> Output: {sum(num1, num2)}")  # Expected: -6

    # Test Case 3
    num1, num2 = 0, 0
    print(f"Input: num1 = {num1}, num2 = {num2} -> Output: {sum(num1, num2)}")  # Expected: 0

    # Test Case 4
    num1, num2 = -100, 100
    print(f"Input: num1 = {num1}, num2 = {num2} -> Output: {sum(num1, num2)}")  # Expected: 0

    # Test Case 5
    num1, num2 = 50, 50
    print(f"Input: num1 = {num1}, num2 = {num2} -> Output: {sum(num1, num2)}")  # Expected: 100

# Time and Space Complexity Analysis
"""
Time Complexity:
The function performs a single addition operation, which is O(1). 
Thus, the time complexity is O(1).

Space Complexity:
The function uses a constant amount of space to store the input and output. 
Thus, the space complexity is O(1).
"""

# Topic: Math