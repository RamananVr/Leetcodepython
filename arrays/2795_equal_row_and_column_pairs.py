"""
LeetCode Question #2795: Equal Row and Column Pairs

Problem Statement:
Given a 0-indexed n x n integer matrix grid, return the number of pairs (r, c) such that row r and column c are equal.
A row and column pair is considered equal if they contain the same elements in the same order.

Example:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 pair (r, c) = (2, 1) where row 2 and column 1 are equal.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5
"""

# Python Solution
from collections import Counter

def equalPairs(grid):
    n = len(grid)
    row_counter = Counter(tuple(row) for row in grid)
    count = 0

    for col in range(n):
        column = tuple(grid[row][col] for row in range(n))
        count += row_counter[column]

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[3,2,1],[1,7,6],[2,7,7]]
    print(equalPairs(grid1))  # Output: 1

    # Test Case 2
    grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(grid2))  # Output: 3

    # Test Case 3
    grid3 = [[1,2,3],[4,5,6],[7,8,9]]
    print(equalPairs(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[1,1],[1,1]]
    print(equalPairs(grid4))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing row_counter takes O(n^2) time since we iterate over all rows in the grid.
- For each column, constructing the tuple takes O(n) time, and there are n columns, so this step takes O(n^2) time.
- Overall, the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n^2) due to the storage of row tuples in the Counter and column tuples during iteration.
"""

# Topic: Arrays