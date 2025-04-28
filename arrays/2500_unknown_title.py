"""
LeetCode Problem #2500: Delete Greatest Value in Each Row

Problem Statement:
You are given an m x n matrix `grid` consisting of positive integers.

Perform the following operation until `grid` becomes empty:
1. Delete the greatest value in each row. If multiple cells contain the greatest value, delete any one of them.
2. Add the greatest value from each row to a running sum.

Return the sum after performing the operation until the matrix becomes empty.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 1 <= grid[i][j] <= 100
"""

# Python Solution
def deleteGreatestValue(grid):
    """
    Deletes the greatest value in each row iteratively and computes the sum of the greatest values.

    :param grid: List[List[int]] - A 2D matrix of positive integers
    :return: int - The sum of the greatest values deleted from the matrix
    """
    # Sort each row in descending order
    for row in grid:
        row.sort(reverse=True)
    
    total_sum = 0
    # Iterate column by column (since rows are sorted)
    for col in range(len(grid[0])):
        max_value = max(row[col] for row in grid)
        total_sum += max_value
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 4], [3, 3, 1]]
    print(deleteGreatestValue(grid1))  # Expected Output: 8

    # Test Case 2
    grid2 = [[10, 20, 30], [5, 15, 25], [1, 2, 3]]
    print(deleteGreatestValue(grid2))  # Expected Output: 60

    # Test Case 3
    grid3 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    print(deleteGreatestValue(grid3))  # Expected Output: 18

    # Test Case 4
    grid4 = [[100]]
    print(deleteGreatestValue(grid4))  # Expected Output: 100

    # Test Case 5
    grid5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(deleteGreatestValue(grid5))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting each row takes O(n log n), where n is the number of columns in the row.
- There are m rows, so sorting all rows takes O(m * n log n).
- Finding the maximum value in each column takes O(m * n), as we iterate through m rows for n columns.
- Overall time complexity: O(m * n log n).

Space Complexity:
- Sorting is done in-place, so no additional space is used apart from the input grid.
- Space complexity: O(1).

Topic: Arrays
"""