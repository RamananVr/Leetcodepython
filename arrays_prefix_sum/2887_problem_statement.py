"""
LeetCode Question #2887: Problem Statement

You are given a 2D grid of size m x n where each cell contains an integer. 
Your task is to find the maximum sum of a subgrid of size k x k.

A subgrid is defined as a contiguous block of cells in the grid. 
The sum of a subgrid is the sum of all the integers in that subgrid.

Write a function `maxSumSubgrid(grid: List[List[int]], k: int) -> int` 
that returns the maximum sum of any k x k subgrid in the given grid.

Constraints:
- 1 <= m, n <= 100
- 1 <= k <= min(m, n)
- -10^4 <= grid[i][j] <= 10^4
"""

from typing import List

def maxSumSubgrid(grid: List[List[int]], k: int) -> int:
    """
    Finds the maximum sum of any k x k subgrid in the given grid.

    :param grid: 2D list of integers representing the grid.
    :param k: Size of the subgrid (k x k).
    :return: Maximum sum of any k x k subgrid.
    """
    m, n = len(grid), len(grid[0])
    
    # Precompute the prefix sum for the grid
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i + 1][j + 1] = (
                grid[i][j]
                + prefix_sum[i][j + 1]
                + prefix_sum[i + 1][j]
                - prefix_sum[i][j]
            )
    
    max_sum = float('-inf')
    
    # Iterate over all possible k x k subgrids
    for i in range(k, m + 1):
        for j in range(k, n + 1):
            # Calculate the sum of the k x k subgrid using the prefix sum
            subgrid_sum = (
                prefix_sum[i][j]
                - prefix_sum[i - k][j]
                - prefix_sum[i][j - k]
                + prefix_sum[i - k][j - k]
            )
            max_sum = max(max_sum, subgrid_sum)
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k1 = 2
    print(maxSumSubgrid(grid1, k1))  # Expected Output: 28 (subgrid [[5, 6], [8, 9]])

    # Test Case 2
    grid2 = [
        [1, -1, 0],
        [-2, 3, 4],
        [5, 6, -7]
    ]
    k2 = 2
    print(maxSumSubgrid(grid2, k2))  # Expected Output: 14 (subgrid [[3, 4], [6, -7]])

    # Test Case 3
    grid3 = [
        [1, 2],
        [3, 4]
    ]
    k3 = 2
    print(maxSumSubgrid(grid3, k3))  # Expected Output: 10 (subgrid [[1, 2], [3, 4]])

    # Test Case 4
    grid4 = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    k4 = 2
    print(maxSumSubgrid(grid4, k4))  # Expected Output: -12 (subgrid [[-1, -2], [-4, -5]])

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing the prefix sum takes O(m * n), where m is the number of rows and n is the number of columns.
- Iterating over all possible k x k subgrids takes O((m - k + 1) * (n - k + 1)).
- Overall time complexity: O(m * n).

Space Complexity:
- The prefix sum array requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Arrays, Prefix Sum
"""