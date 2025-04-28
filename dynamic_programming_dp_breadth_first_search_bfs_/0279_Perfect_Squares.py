"""
LeetCode Problem #279: Perfect Squares

Problem Statement:
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
- 1 <= n <= 10^4
"""

from collections import deque
import math

def numSquares(n: int) -> int:
    """
    Returns the least number of perfect square numbers that sum to n.
    Uses Breadth-First Search (BFS) to find the solution.
    """
    # Generate all perfect squares less than or equal to n
    perfect_squares = []
    for i in range(1, int(math.sqrt(n)) + 1):
        perfect_squares.append(i * i)
    
    # BFS initialization
    queue = deque([n])
    level = 0  # Tracks the number of steps (or levels) in BFS

    while queue:
        level += 1
        for _ in range(len(queue)):
            remainder = queue.popleft()
            for square in perfect_squares:
                if remainder == square:
                    return level  # Found the solution
                if remainder < square:
                    break  # No need to check larger squares
                queue.append(remainder - square)
    
    return level  # This line is theoretically unreachable

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    print(f"Input: {n1}, Output: {numSquares(n1)}")  # Expected Output: 3

    # Test Case 2
    n2 = 13
    print(f"Input: {n2}, Output: {numSquares(n2)}")  # Expected Output: 2

    # Test Case 3
    n3 = 1
    print(f"Input: {n3}, Output: {numSquares(n3)}")  # Expected Output: 1

    # Test Case 4
    n4 = 17
    print(f"Input: {n4}, Output: {numSquares(n4)}")  # Expected Output: 2 (16 + 1)

    # Test Case 5
    n5 = 100
    print(f"Input: {n5}, Output: {numSquares(n5)}")  # Expected Output: 1 (100)

"""
Time Complexity:
- Let k = sqrt(n). The BFS explores all possible combinations of perfect squares.
- In the worst case, the BFS explores all numbers from n down to 0, and for each number, it iterates over k perfect squares.
- Thus, the time complexity is O(k * n), where k = sqrt(n).

Space Complexity:
- The space complexity is O(n) due to the queue used in BFS and the storage of visited nodes.

Topic: Dynamic Programming (DP), Breadth-First Search (BFS)
"""