"""
LeetCode Problem #2732: Find a Good Subset of the Matrix

Problem Statement:
You are given a binary matrix `grid` of size `m x n`. A binary matrix has only 0s and 1s as values.

A subset of rows in the matrix is good if there exists at least one column such that all the rows in the subset have a value of 0 in that column.

Return any good subset of rows from the matrix. If no good subset exists, return an empty list.

A subset of rows can be represented as a list of the indices of those rows in the matrix.

Example:
Input: grid = [[0,1,0],[0,0,1],[1,1,1]]
Output: [0,1]
Explanation: Choosing rows 0 and 1, column 2 has all 0s.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either 0 or 1.
"""

def findGoodSubset(grid):
    """
    Finds a good subset of rows in the binary matrix.

    Args:
    grid (List[List[int]]): A binary matrix of size m x n.

    Returns:
    List[int]: A list of indices representing a good subset of rows, or an empty list if no good subset exists.
    """
    m = len(grid)
    n = len(grid[0])

    # Iterate through all pairs of rows
    for i in range(m):
        for j in range(i, m):
            # Check if there exists a column where both rows have 0s
            if any(grid[i][k] == 0 and grid[j][k] == 0 for k in range(n)):
                return [i, j]

    # If no good subset is found, return an empty list
    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    print(findGoodSubset(grid1))  # Output: [0, 1]

    # Test Case 2
    grid2 = [[1, 1], [1, 1]]
    print(findGoodSubset(grid2))  # Output: []

    # Test Case 3
    grid3 = [[0, 0], [1, 0], [0, 1]]
    print(findGoodSubset(grid3))  # Output: [0, 2]

    # Test Case 4
    grid4 = [[0]]
    print(findGoodSubset(grid4))  # Output: [0, 0]

    # Test Case 5
    grid5 = [[1, 0], [0, 1]]
    print(findGoodSubset(grid5))  # Output: [0, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through all pairs of rows in the matrix, which takes O(m^2).
- For each pair of rows, it checks all columns, which takes O(n).
- Therefore, the overall time complexity is O(m^2 * n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Matrix
"""