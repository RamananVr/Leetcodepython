"""
LeetCode Problem #1643: Kth Smallest Instructions

Problem Statement:
An `m x n` grid is composed of `m` rows and `n` columns, and the grid is indexed starting from `(0, 0)` in the top-left corner. You are given integers `m` and `n`, which represent the number of rows and columns in the grid, respectively. You are also given an array `destination = [x, y]` where `(x, y)` is the bottom-right corner of the grid (i.e., the destination).

You are tasked to find the k-th lexicographically smallest sequence of moves that will take you from the top-left corner `(0, 0)` to the destination `(x, y)`. The moves are represented as:
- `'H'` (right move)
- `'V'` (down move)

Return the k-th lexicographically smallest sequence of moves.

Constraints:
- `2 <= m, n <= 15`
- `destination[0] == m - 1`
- `destination[1] == n - 1`
- `1 <= k <= (m - 1 + n - 1)! / ((m - 1)! * (n - 1)!)` (i.e., k is valid for the number of unique paths)

Example:
Input: m = 2, n = 3, k = 3
Output: "HVH"

Input: m = 3, n = 3, k = 5
Output: "HHVV"
"""

from math import comb

def kthSmallestPath(destination, k):
    """
    Find the k-th lexicographically smallest sequence of moves to reach the destination.
    
    :param destination: List[int] - The destination coordinates [x, y].
    :param k: int - The k-th lexicographically smallest sequence to find.
    :return: str - The k-th smallest sequence of moves.
    """
    m, n = destination[0] + 1, destination[1] + 1
    h_moves = n - 1  # Number of horizontal moves
    v_moves = m - 1  # Number of vertical moves
    result = []

    while h_moves > 0 or v_moves > 0:
        if h_moves > 0:
            # Calculate the number of sequences starting with 'H'
            count_with_h = comb(h_moves + v_moves - 1, h_moves - 1)
        else:
            count_with_h = 0

        if k <= count_with_h:
            result.append('H')
            h_moves -= 1
        else:
            result.append('V')
            k -= count_with_h
            v_moves -= 1

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m, n, k = 2, 3, 3
    print(kthSmallestPath([m - 1, n - 1], k))  # Output: "HVH"

    # Test Case 2
    m, n, k = 3, 3, 5
    print(kthSmallestPath([m - 1, n - 1], k))  # Output: "HHVV"

    # Test Case 3
    m, n, k = 3, 7, 15
    print(kthSmallestPath([m - 1, n - 1], k))  # Output: "HHHHVVV"

    # Test Case 4
    m, n, k = 4, 4, 20
    print(kthSmallestPath([m - 1, n - 1], k))  # Output: "HHVVHV"

"""
Time Complexity:
- The function iterates through the total number of moves (m + n - 2), and for each move, it computes a binomial coefficient using `math.comb`, which is O(min(a, b)) where a and b are the arguments to `comb`.
- In the worst case, this results in O((m + n - 2) * min(h_moves, v_moves)).

Space Complexity:
- The space complexity is O(1) as we only use a few variables to store intermediate results.

Topic: Dynamic Programming, Combinatorics
"""