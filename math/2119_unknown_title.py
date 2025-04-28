"""
LeetCode Problem #2119: A Number After a Double Reversal

Problem Statement:
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. 
Return true if reversed2 equals num. Otherwise, return false.

A number num is said to be a "double-reversal number" if reversing it twice results in the original number.

Example:
- Input: num = 526
- Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Constraints:
- 0 <= num <= 10^6
"""

def isSameAfterReversals(num: int) -> bool:
    """
    Determines if a number is the same after a double reversal.

    Args:
    num (int): The input number.

    Returns:
    bool: True if the number is the same after a double reversal, False otherwise.
    """
    # A number is the same after a double reversal if:
    # 1. It is 0 (special case).
    # 2. It does not end with a trailing zero (i.e., num % 10 != 0).
    return num == 0 or num % 10 != 0


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Number with no trailing zero
    num1 = 526
    print(isSameAfterReversals(num1))  # Output: True

    # Test Case 2: Number with trailing zero
    num2 = 120
    print(isSameAfterReversals(num2))  # Output: False

    # Test Case 3: Number is 0
    num3 = 0
    print(isSameAfterReversals(num3))  # Output: True

    # Test Case 4: Single-digit number
    num4 = 7
    print(isSameAfterReversals(num4))  # Output: True

    # Test Case 5: Large number with trailing zero
    num5 = 1000000
    print(isSameAfterReversals(num5))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a simple modulo operation and comparison, both of which are O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space, as no additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Math
"""