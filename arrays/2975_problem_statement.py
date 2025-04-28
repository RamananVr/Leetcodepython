"""
LeetCode Question #2975: Problem Statement

Given a 2D grid of size `m x n` where each cell contains an integer, your task is to find the maximum sum of any hourglass in the grid.

An hourglass is defined as a subset of values with the following pattern in the grid:

    a b c
      d
    e f g

The hourglass sum is the sum of the values in the hourglass. Return the maximum hourglass sum found in the grid.

Constraints:
- `m >= 3` and `n >= 3` (the grid will always have at least one hourglass).
- `-10^6 <= grid[i][j] <= 10^6`

Example:
Input: grid = [[1, 2, 3, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 2, 3, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 2, 3, 0, 0]]
Output: 7
Explanation: The hourglass with the maximum sum is:
    1 2 3
      2
    1 2 3
"""

# Python Solution
def maxHourglassSum(grid):
    """
    Function to calculate the maximum hourglass sum in a 2D grid.

    :param grid: List[List[int]] - 2D grid of integers
    :return: int - Maximum hourglass sum
    """
    m, n = len(grid), len(grid[0])
    max_sum = float('-inf')  # Initialize to negative infinity to handle negative values in the grid

    # Iterate through all possible hourglass centers
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            # Calculate the hourglass sum for the current center
            current_sum = (
                grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] +  # Top row
                grid[i][j] +                                                # Middle
                grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]    # Bottom row
            )
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 2, 3, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 2, 3, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 2, 3, 0, 0]
    ]
    print(maxHourglassSum(grid1))  # Output: 7

    # Test Case 2
    grid2 = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ]
    print(maxHourglassSum(grid2))  # Output: -6

    # Test Case 3
    grid3 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    print(maxHourglassSum(grid3))  # Output: 19

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates over all possible hourglass centers in the grid.
- For each center, it calculates the sum of 7 elements (constant time operation).
- If the grid has dimensions m x n, the number of hourglass centers is (m-2) x (n-2).
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `max_sum` and `current_sum`.
- Hence, the space complexity is O(1).
"""

# Topic: Arrays