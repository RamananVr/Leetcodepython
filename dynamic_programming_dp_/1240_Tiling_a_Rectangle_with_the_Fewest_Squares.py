"""
LeetCode Problem #1240: Tiling a Rectangle with the Fewest Squares

Problem Statement:
Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.

Constraints:
- 1 <= n, m <= 13

Example:
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are required (1x1, 1x1, 2x2).

Input: n = 5, m = 8
Output: 5

Input: n = 11, m = 13
Output: 6
"""

def tilingRectangle(n: int, m: int) -> int:
    """
    Function to calculate the minimum number of squares required to tile a rectangle of size n x m.
    """
    # If the rectangle is already a square
    if n == m:
        return 1

    # Memoization dictionary to store results for subproblems
    memo = {}

    def dfs(h, w):
        # If the rectangle is already a square
        if h == w:
            return 1
        # If the result is already computed
        if (h, w) in memo:
            return memo[(h, w)]
        if (w, h) in memo:
            return memo[(w, h)]

        # Initialize the minimum number of squares to a large value
        min_squares = float('inf')

        # Try placing squares of size k x k
        for k in range(1, min(h, w) + 1):
            # Divide the rectangle into three parts after placing the square
            min_squares = min(
                min_squares,
                1 + dfs(h - k, w) + dfs(k, w - k)
            )

        # Store the result in the memoization dictionary
        memo[(h, w)] = min_squares
        return min_squares

    return dfs(n, m)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, m1 = 2, 3
    print(f"Minimum squares to tile {n1}x{m1} rectangle: {tilingRectangle(n1, m1)}")  # Output: 3

    # Test Case 2
    n2, m2 = 5, 8
    print(f"Minimum squares to tile {n2}x{m2} rectangle: {tilingRectangle(n2, m2)}")  # Output: 5

    # Test Case 3
    n3, m3 = 11, 13
    print(f"Minimum squares to tile {n3}x{m3} rectangle: {tilingRectangle(n3, m3)}")  # Output: 6

"""
Time Complexity Analysis:
- The function uses a depth-first search (DFS) approach with memoization.
- The number of unique states is bounded by the number of possible (h, w) pairs, which is O(n * m).
- For each state, we iterate over k from 1 to min(h, w), which is O(min(n, m)).
- Therefore, the overall time complexity is O(n * m * min(n, m)).

Space Complexity Analysis:
- The space complexity is determined by the memoization dictionary, which stores O(n * m) states.
- The recursion stack depth is at most O(max(n, m)).
- Therefore, the overall space complexity is O(n * m).

Topic: Dynamic Programming (DP)
"""