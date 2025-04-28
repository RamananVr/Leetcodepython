"""
LeetCode Problem #2230: The Number of Consecutive Integers in a Range

Problem Statement:
You are given two integers `low` and `high` representing a range of integers [low, high] (inclusive).
Return the number of consecutive integers in this range.

Example:
Input: low = 3, high = 7
Output: 5
Explanation: The integers in the range [3, 7] are {3, 4, 5, 6, 7}, and there are 5 integers.

Constraints:
- -10^9 <= low <= high <= 10^9
"""

# Solution
def count_consecutive_integers(low: int, high: int) -> int:
    """
    Calculate the number of consecutive integers in the range [low, high].

    Args:
    low (int): The lower bound of the range.
    high (int): The upper bound of the range.

    Returns:
    int: The number of integers in the range [low, high].
    """
    return high - low + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 3
    high = 7
    print(count_consecutive_integers(low, high))  # Output: 5

    # Test Case 2
    low = -5
    high = 5
    print(count_consecutive_integers(low, high))  # Output: 11

    # Test Case 3
    low = 0
    high = 0
    print(count_consecutive_integers(low, high))  # Output: 1

    # Test Case 4
    low = -10
    high = -1
    print(count_consecutive_integers(low, high))  # Output: 10

    # Test Case 5
    low = 100
    high = 1000
    print(count_consecutive_integers(low, high))  # Output: 901

"""
Time and Space Complexity Analysis:

Time Complexity:
The solution runs in O(1) time because it involves a single arithmetic operation (subtraction and addition).

Space Complexity:
The solution uses O(1) space as it does not require any additional data structures or memory allocation.

Topic: Math
"""