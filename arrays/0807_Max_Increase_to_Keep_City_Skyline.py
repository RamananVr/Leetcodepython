"""
LeetCode Problem #807: Max Increase to Keep City Skyline

Problem Statement:
In a 2D grid of integers, each value represents the height of a building located at that point (i.e., grid[i][j] is the height of the building at position (i, j)).

We want to increase the height of buildings, but we cannot change the city's skyline when viewed from the top, bottom, left, or right. A city's skyline is the outer contour of the grid when viewed from these four directions.

Write a function to calculate the maximum total sum that the height of the buildings can be increased while keeping the skyline unchanged.

Constraints:
- n == grid.length
- n == grid[i].length
- 2 <= n <= 50
- 0 <= grid[i][j] <= 100

Example:
Input: grid = [[3, 0, 8, 4],
               [2, 4, 5, 7],
               [9, 2, 6, 3],
               [0, 3, 1, 0]]
Output: 35
Explanation:
The grid after increasing the height of buildings while keeping the skyline unchanged is:
gridNew = [[8, 4, 8, 7],
           [7, 4, 7, 7],
           [9, 4, 8, 7],
           [3, 3, 3, 3]]
The total sum of the increases is 35.

"""

def maxIncreaseKeepingSkyline(grid):
    """
    Calculate the maximum total sum that the height of the buildings can be increased
    while keeping the skyline unchanged.

    :param grid: List[List[int]] - 2D grid of building heights
    :return: int - Maximum total sum of height increases
    """
    # Determine the maximum heights for each row and column
    max_row = [max(row) for row in grid]
    max_col = [max(col) for col in zip(*grid)]

    # Calculate the maximum increase for each building
    total_increase = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # The new height is limited by the minimum of the row and column skylines
            max_height = min(max_row[i], max_col[j])
            total_increase += max_height - grid[i][j]

    return total_increase


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[3, 0, 8, 4],
             [2, 4, 5, 7],
             [9, 2, 6, 3],
             [0, 3, 1, 0]]
    print(maxIncreaseKeepingSkyline(grid1))  # Output: 35

    # Test Case 2
    grid2 = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(maxIncreaseKeepingSkyline(grid2))  # Output: 0 (No increase possible)

    # Test Case 3
    grid3 = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    print(maxIncreaseKeepingSkyline(grid3))  # Output: 0 (No increase possible)

    # Test Case 4
    grid4 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    print(maxIncreaseKeepingSkyline(grid4))  # Output: 0 (No increase possible)


"""
Time Complexity Analysis:
- Calculating `max_row` takes O(n^2) time, where n is the number of rows/columns in the grid.
- Calculating `max_col` also takes O(n^2) time.
- The nested loop to calculate the total increase also takes O(n^2) time.
- Overall, the time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n) for storing `max_row` and `max_col`.

Topic: Arrays
"""