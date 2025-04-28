"""
LeetCode Problem #2965: "Maximum Number of Odd Integers"

Problem Statement:
You are given an integer `n`. You need to find the maximum number of odd integers that sum up to `n`.
An odd integer is any integer that is not divisible by 2. For example, 1, 3, 5, etc., are odd integers.

Return the maximum number of odd integers that can sum up to `n`.

Constraints:
- 1 <= n <= 10^9
"""

def maximumOddCount(n: int) -> int:
    """
    Function to calculate the maximum number of odd integers that sum up to n.

    Args:
    n (int): The target sum.

    Returns:
    int: The maximum number of odd integers that can sum up to n.
    """
    # The maximum number of odd integers that can sum up to n is the largest k such that
    # the sum of the first k odd integers (1, 3, 5, ..., 2k-1) is less than or equal to n.
    # The sum of the first k odd integers is k^2.
    # We need to find the largest k such that k^2 <= n.
    
    # Use binary search to find the largest k such that k^2 <= n.
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(maximumOddCount(n))  # Expected Output: 3 (1 + 3 + 5 = 9)

    # Test Case 2
    n = 15
    print(maximumOddCount(n))  # Expected Output: 3 (1 + 3 + 5 = 9)

    # Test Case 3
    n = 1
    print(maximumOddCount(n))  # Expected Output: 1 (1 = 1)

    # Test Case 4
    n = 25
    print(maximumOddCount(n))  # Expected Output: 5 (1 + 3 + 5 + 7 + 9 = 25)

    # Test Case 5
    n = 1000000
    print(maximumOddCount(n))  # Expected Output: 1000 (1 + 3 + 5 + ... + 1999 = 1000000)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(n)) time, as we are halving the search space in each iteration.

Space Complexity:
- The space complexity is O(1), as we are using a constant amount of space.

Topic: Math, Binary Search
"""