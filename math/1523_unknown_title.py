"""
LeetCode Problem #1523: Count Odd Numbers in an Interval Range

Problem Statement:
Given two non-negative integers `low` and `high`, return the count of odd numbers between `low` and `high` (inclusive).

Constraints:
- 0 <= low <= high <= 10^9

Example:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3, 5, 7].

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""

# Solution
def countOdds(low: int, high: int) -> int:
    """
    Count the number of odd numbers in the inclusive range [low, high].

    Args:
    low (int): The lower bound of the range.
    high (int): The upper bound of the range.

    Returns:
    int: The count of odd numbers in the range.
    """
    # Calculate the total numbers in the range
    total_numbers = high - low + 1
    
    # If both low and high are odd, the count of odd numbers is (total_numbers + 1) // 2
    # Otherwise, the count of odd numbers is total_numbers // 2
    return (total_numbers + (low % 2) + (high % 2)) // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 3
    high = 7
    print(countOdds(low, high))  # Output: 3

    # Test Case 2
    low = 8
    high = 10
    print(countOdds(low, high))  # Output: 1

    # Test Case 3
    low = 0
    high = 0
    print(countOdds(low, high))  # Output: 0

    # Test Case 4
    low = 1
    high = 1
    print(countOdds(low, high))  # Output: 1

    # Test Case 5
    low = 1
    high = 10
    print(countOdds(low, high))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution runs in O(1) time because it involves only a few arithmetic operations.

Space Complexity:
- The solution uses O(1) space as it does not require any additional data structures.

Topic: Math
"""