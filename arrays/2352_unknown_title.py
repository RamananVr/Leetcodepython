"""
LeetCode Problem #2352: Equal Row and Column Pairs

Problem Statement:
Given a 0-indexed n x n integer matrix `grid`, return the number of pairs (r, c) such that row r and column c are equal.

A row and column pair is considered equal if:
- All elements of the row are equal to the corresponding elements of the column.

Example:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 pair (r, c) = (2, 1) where row 2 and column 1 are equal.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5
"""

def equalPairs(grid):
    """
    Function to count the number of equal row and column pairs in the given grid.

    :param grid: List[List[int]] - A 2D list representing the n x n matrix.
    :return: int - The number of equal row and column pairs.
    """
    from collections import Counter

    # Count the frequency of each row in the grid
    row_count = Counter(tuple(row) for row in grid)

    # Transpose the grid to get columns as rows
    n = len(grid)
    col_count = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))

    # Count the number of matching row-column pairs
    result = 0
    for row, freq in row_count.items():
        result += freq * col_count[row]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(equalPairs(grid1))  # Output: 1

    # Test Case 2
    grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print(equalPairs(grid2))  # Output: 3

    # Test Case 3
    grid3 = [[1, 2], [2, 1]]
    print(equalPairs(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[1, 1], [1, 1]]
    print(equalPairs(grid4))  # Output: 4

"""
Time Complexity Analysis:
- Constructing the row_count dictionary takes O(n^2) time, as we iterate over all rows of the grid.
- Constructing the col_count dictionary also takes O(n^2) time, as we iterate over all columns of the grid.
- The final loop to calculate the result iterates over the unique rows, which is at most O(n^2) in the worst case.
- Overall, the time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n^2) due to the storage of row_count and col_count dictionaries, which can store up to n^2 unique rows/columns in the worst case.
- The space used for the transposed columns is also O(n^2).
- Overall, the space complexity is O(n^2).

Topic: Arrays
"""