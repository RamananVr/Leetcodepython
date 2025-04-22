"""
LeetCode Question #633: Sum of Square Numbers

Problem Statement:
Given a non-negative integer `c`, decide whether there are two integers `a` and `b` such that:
    a^2 + b^2 = c

Return true if such integers exist, otherwise return false.

Example 1:
Input: c = 5
Output: true
Explanation: 1^2 + 2^2 = 5

Example 2:
Input: c = 3
Output: false

Example 3:
Input: c = 4
Output: true
Explanation: 0^2 + 2^2 = 4

Example 4:
Input: c = 2
Output: true
Explanation: 1^2 + 1^2 = 2

Example 5:
Input: c = 1
Output: true

Constraints:
- 0 <= c <= 2^31 - 1
"""

def judgeSquareSum(c: int) -> bool:
    """
    Determines if there exist two integers a and b such that a^2 + b^2 = c.

    :param c: Non-negative integer
    :return: True if such integers exist, otherwise False
    """
    # Use two-pointer technique
    left, right = 0, int(c**0.5)  # Start with 0 and the square root of c
    while left <= right:
        current_sum = left * left + right * right
        if current_sum == c:
            return True
        elif current_sum < c:
            left += 1
        else:
            right -= 1
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    c = 5
    print(judgeSquareSum(c))  # Output: True

    # Test Case 2
    c = 3
    print(judgeSquareSum(c))  # Output: False

    # Test Case 3
    c = 4
    print(judgeSquareSum(c))  # Output: True

    # Test Case 4
    c = 2
    print(judgeSquareSum(c))  # Output: True

    # Test Case 5
    c = 1
    print(judgeSquareSum(c))  # Output: True

    # Test Case 6
    c = 0
    print(judgeSquareSum(c))  # Output: True

    # Test Case 7
    c = 10
    print(judgeSquareSum(c))  # Output: True

    # Test Case 8
    c = 1000000
    print(judgeSquareSum(c))  # Output: True

"""
Time Complexity:
- The time complexity is O(sqrt(c)), where c is the input number. This is because the two-pointer approach iterates from 0 to sqrt(c).

Space Complexity:
- The space complexity is O(1) since we are only using a constant amount of extra space.

Topic: Two Pointers, Math
"""