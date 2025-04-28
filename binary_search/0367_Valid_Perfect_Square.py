"""
LeetCode Problem #367: Valid Perfect Square

Problem Statement:
Given a positive integer num, write a function that returns true if num is a perfect square, otherwise return false.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: 4 * 4 = 16

Example 2:
Input: num = 14
Output: false

Constraints:
- 1 <= num <= 2^31 - 1
"""

def isPerfectSquare(num: int) -> bool:
    """
    Determines if a given number is a perfect square using binary search.

    :param num: A positive integer
    :return: True if num is a perfect square, False otherwise
    """
    if num < 1:
        return False

    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: num = 16 (perfect square)
    print(isPerfectSquare(16))  # Expected output: True

    # Test Case 2: num = 14 (not a perfect square)
    print(isPerfectSquare(14))  # Expected output: False

    # Test Case 3: num = 1 (perfect square)
    print(isPerfectSquare(1))  # Expected output: True

    # Test Case 4: num = 25 (perfect square)
    print(isPerfectSquare(25))  # Expected output: True

    # Test Case 5: num = 2 (not a perfect square)
    print(isPerfectSquare(2))  # Expected output: False

    # Test Case 6: num = 808201 (perfect square)
    print(isPerfectSquare(808201))  # Expected output: True

"""
Time Complexity:
- The binary search algorithm runs in O(log(num)) time, where num is the input number.
- At each step, the search space is halved, leading to logarithmic complexity.

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""