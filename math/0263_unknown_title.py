"""
LeetCode Problem #263: Ugly Number

Problem Statement:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer `n`, return `true` if `n` is an ugly number, otherwise return `false`.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 is considered an ugly number.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not an ugly number since it includes the prime factor 7.

Constraints:
- -2^31 <= n <= 2^31 - 1
"""

def isUgly(n: int) -> bool:
    """
    Determines if a number is an ugly number.

    :param n: Integer to check
    :return: True if n is an ugly number, False otherwise
    """
    if n <= 0:
        return False
    
    # Divide n by 2, 3, and 5 as long as it is divisible
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    
    # If n becomes 1, it is an ugly number
    return n == 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 6
    print(isUgly(6))  # Expected Output: True

    # Test Case 2: n = 1
    print(isUgly(1))  # Expected Output: True

    # Test Case 3: n = 14
    print(isUgly(14))  # Expected Output: False

    # Test Case 4: n = 0
    print(isUgly(0))  # Expected Output: False

    # Test Case 5: n = -6
    print(isUgly(-6))  # Expected Output: False

    # Test Case 6: n = 30
    print(isUgly(30))  # Expected Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iteratively divides `n` by 2, 3, and 5 until it is no longer divisible.
- In the worst case, the number is repeatedly divided by the smallest factor (2), which takes O(log(n)) divisions.
- Since there are only three factors (2, 3, and 5), the overall time complexity is O(log(n)).

Space Complexity:
- The function uses a constant amount of space (no additional data structures are used).
- Space complexity is O(1).

Topic: Math
"""