"""
LeetCode Problem #2639: Find the Width of Columns of a Grid

Problem Statement:
You are given a 2D integer array `grid` where each row is a list of integers. A column's width is defined as the maximum number of characters needed to represent any integer in that column.

Return an integer array `widths` of size `n` where `widths[i]` is the width of the ith column.

Example:
Input: grid = [[1, 22, 333], [4444, 55, 6]]
Output: [4, 2, 3]
Explanation:
- The first column contains [1, 4444]. The maximum width is 4 because "4444" has 4 characters.
- The second column contains [22, 55]. The maximum width is 2 because "22" and "55" both have 2 characters.
- The third column contains [333, 6]. The maximum width is 3 because "333" has 3 characters.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-10^9 <= grid[i][j] <= 10^9`
"""

# Python Solution
def findColumnWidth(grid):
    """
    Function to calculate the width of each column in a 2D grid.

    Args:
    grid (List[List[int]]): A 2D list of integers.

    Returns:
    List[int]: A list of integers representing the width of each column.
    """
    # Transpose the grid to iterate over columns
    return [max(len(str(cell)) for cell in col) for col in zip(*grid)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 22, 333], [4444, 55, 6]]
    print(findColumnWidth(grid1))  # Output: [4, 2, 3]

    # Test Case 2
    grid2 = [[-1, -22, -333], [-4444, -55, -6]]
    print(findColumnWidth(grid2))  # Output: [5, 3, 4]

    # Test Case 3
    grid3 = [[0, 0, 0], [0, 0, 0]]
    print(findColumnWidth(grid3))  # Output: [1, 1, 1]

    # Test Case 4
    grid4 = [[123456789, 987654321], [123, 456]]
    print(findColumnWidth(grid4))  # Output: [9, 9]

    # Test Case 5
    grid5 = [[1]]
    print(findColumnWidth(grid5))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Transposing the grid using `zip(*grid)` takes O(m * n), where m is the number of rows and n is the number of columns.
- Calculating the maximum width for each column involves iterating over all elements in the column, which takes O(m) per column.
- Overall, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(n) for the result list, where n is the number of columns.
- The transposed grid does not require additional space as it uses iterators.
- Overall, the space complexity is O(n).
"""

# Topic: Arrays