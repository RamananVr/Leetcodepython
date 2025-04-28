"""
LeetCode Problem #2413: Smallest Even Multiple

Problem Statement:
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 5
Output: 10
Explanation: The smallest positive integer that is a multiple of both 2 and 5 is 10.

Input: n = 6
Output: 6
Explanation: The smallest positive integer that is a multiple of both 2 and 6 is 6.
"""

# Solution
def smallestEvenMultiple(n: int) -> int:
    """
    Returns the smallest positive integer that is a multiple of both 2 and n.

    :param n: Positive integer (1 <= n <= 1000)
    :return: Smallest positive integer that is a multiple of both 2 and n
    """
    # If n is even, the smallest even multiple is n itself.
    # If n is odd, the smallest even multiple is 2 * n.
    return n if n % 2 == 0 else 2 * n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    print(f"Input: n = {n1}, Output: {smallestEvenMultiple(n1)}")  # Expected Output: 10

    # Test Case 2
    n2 = 6
    print(f"Input: n = {n2}, Output: {smallestEvenMultiple(n2)}")  # Expected Output: 6

    # Test Case 3
    n3 = 1
    print(f"Input: n = {n3}, Output: {smallestEvenMultiple(n3)}")  # Expected Output: 2

    # Test Case 4
    n4 = 1000
    print(f"Input: n = {n4}, Output: {smallestEvenMultiple(n4)}")  # Expected Output: 1000

    # Test Case 5
    n5 = 7
    print(f"Input: n = {n5}, Output: {smallestEvenMultiple(n5)}")  # Expected Output: 14

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution involves a single modulo operation and a conditional check, both of which are O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution does not use any additional data structures or memory.
- Therefore, the space complexity is O(1).
"""

# Topic: Math