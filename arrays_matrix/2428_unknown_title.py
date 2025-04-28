"""
LeetCode Problem #2428: Maximum Sum of an Hourglass

Problem Statement:
You are given an `m x n` integer matrix `grid`.

We define an hourglass as a part of the matrix with the following form:
    a b c
      d
    e f g

The sum of an hourglass is the sum of the values in the hourglass.

Return the maximum sum of any hourglass in `grid`. If no hourglass can be formed, return 0.

An hourglass cannot be formed if the matrix has fewer than 3 rows or 3 columns.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `3 <= m, n <= 150`
- `-10^6 <= grid[i][j] <= 10^6`
"""

def maxSum(grid):
    """
    Function to calculate the maximum sum of an hourglass in the given grid.

    :param grid: List[List[int]] - 2D matrix of integers
    :return: int - Maximum sum of any hourglass in the grid
    """
    m, n = len(grid), len(grid[0])
    max_hourglass_sum = float('-inf')  # Initialize to negative infinity

    # Iterate through the grid to find all possible hourglasses
    for i in range(m - 2):  # Ensure we have enough rows for an hourglass
        for j in range(n - 2):  # Ensure we have enough columns for an hourglass
            # Calculate the sum of the current hourglass
            current_sum = (
                grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +  # Top row
                grid[i + 1][j + 1] +  # Middle element
                grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]  # Bottom row
            )
            # Update the maximum hourglass sum
            max_hourglass_sum = max(max_hourglass_sum, current_sum)

    return max_hourglass_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(maxSum(grid1))  # Expected Output: 35

    # Test Case 2
    grid2 = [
        [6, 2, 1, 3],
        [4, 2, 1, 5],
        [9, 2, 8, 7],
        [4, 1, 2, 9]
    ]
    print(maxSum(grid2))  # Expected Output: 30

    # Test Case 3
    grid3 = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1]
    ]
    print(maxSum(grid3))  # Expected Output: -7

    # Test Case 4
    grid4 = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 2, 4, 4],
        [0, 0, 0, 2, 0]
    ]
    print(maxSum(grid4))  # Expected Output: 19


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates over all possible top-left corners of hourglasses in the grid.
- There are (m - 2) * (n - 2) such top-left corners.
- For each hourglass, we compute the sum in O(1) time.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The function uses a constant amount of extra space (only variables for tracking the maximum sum).
- Therefore, the space complexity is O(1).

Topic: Arrays, Matrix
"""