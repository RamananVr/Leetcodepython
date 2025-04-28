"""
LeetCode Problem #2704: To Be or Not to Be

Problem Statement:
Write a function `isEven` that takes a single integer `num` as input and returns `True` if the number is even, and `False` otherwise.

An integer is even if it is divisible by 2 with no remainder. For example:
- 4 is even because 4 % 2 == 0.
- 7 is not even because 7 % 2 != 0.

Constraints:
- -10^9 <= num <= 10^9
- The function should run in constant time.

Example:
Input: num = 4
Output: True

Input: num = 7
Output: False
"""

# Solution
def isEven(num: int) -> bool:
    """
    Determines if a given integer is even.

    Args:
    num (int): The integer to check.

    Returns:
    bool: True if the integer is even, False otherwise.
    """
    return num % 2 == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Even number
    num1 = 4
    print(f"isEven({num1}) = {isEven(num1)}")  # Expected: True

    # Test Case 2: Odd number
    num2 = 7
    print(f"isEven({num2}) = {isEven(num2)}")  # Expected: False

    # Test Case 3: Zero (edge case)
    num3 = 0
    print(f"isEven({num3}) = {isEven(num3)}")  # Expected: True

    # Test Case 4: Negative even number
    num4 = -8
    print(f"isEven({num4}) = {isEven(num4)}")  # Expected: True

    # Test Case 5: Negative odd number
    num5 = -9
    print(f"isEven({num5}) = {isEven(num5)}")  # Expected: False

    # Test Case 6: Large even number
    num6 = 10**9
    print(f"isEven({num6}) = {isEven(num6)}")  # Expected: True

    # Test Case 7: Large odd number
    num7 = 10**9 - 1
    print(f"isEven({num7}) = {isEven(num7)}")  # Expected: False

# Time and Space Complexity Analysis
"""
Time Complexity:
The function runs in O(1) time because the modulo operation is a constant-time operation.

Space Complexity:
The function uses O(1) space as it does not allocate any additional memory that scales with the input size.
"""

# Topic: Math