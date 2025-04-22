"""
LeetCode Question #69: Sqrt(x)

Problem Statement:
Given a non-negative integer `x`, compute and return the square root of `x`.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note:
- You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
- 0 <= x <= 2^31 - 1
"""

def mySqrt(x: int) -> int:
    """
    Computes the square root of a non-negative integer x, truncating the decimal part.
    
    :param x: Non-negative integer
    :return: Integer part of the square root of x
    """
    if x < 2:
        return x  # Base cases: sqrt(0) = 0, sqrt(1) = 1
    
    # Binary search to find the square root
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # When the loop ends, `right` will be the largest integer whose square is <= x
    return right

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Perfect square
    x1 = 4
    print(f"Input: {x1}, Output: {mySqrt(x1)}")  # Expected Output: 2

    # Test Case 2: Non-perfect square
    x2 = 8
    print(f"Input: {x2}, Output: {mySqrt(x2)}")  # Expected Output: 2

    # Test Case 3: Edge case (smallest input)
    x3 = 0
    print(f"Input: {x3}, Output: {mySqrt(x3)}")  # Expected Output: 0

    # Test Case 4: Edge case (largest input)
    x4 = 2**31 - 1
    print(f"Input: {x4}, Output: {mySqrt(x4)}")  # Expected Output: 46340

    # Test Case 5: Another perfect square
    x5 = 16
    print(f"Input: {x5}, Output: {mySqrt(x5)}")  # Expected Output: 4

"""
Time Complexity:
- The binary search runs in O(log(x)) time because the search space is halved at each step.

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""