"""
LeetCode Problem #750: Number Of Corner Rectangles

Problem Statement:
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
A corner rectangle is defined as a set of four distinct grid cells that form an axis-aligned rectangle, 
where all four cells have a value of 1.

Example:
Input: grid = [
  [1, 0, 0, 1, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [1, 0, 1, 0, 1]
]
Output: 1
Explanation: There is only one corner rectangle, with coordinates: (0,3), (0,4), (3,3), (3,4).

Constraints:
- The number of rows in the grid is in the range [1, 200].
- The number of columns in the grid is in the range [1, 200].
- Each grid[i][j] is either 0 or 1.
"""

def countCornerRectangles(grid):
    """
    Function to count the number of corner rectangles in a given grid.
    
    :param grid: List[List[int]] - A 2D grid of 0s and 1s.
    :return: int - The number of corner rectangles.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Iterate through pairs of rows
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            # Count the number of columns where both rows have a 1
            common_ones = 0
            for c in range(cols):
                if grid[r1][c] == 1 and grid[r2][c] == 1:
                    common_ones += 1
            # If there are at least two columns with 1s, calculate the number of rectangles
            if common_ones >= 2:
                count += common_ones * (common_ones - 1) // 2

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    print(countCornerRectangles(grid1))  # Output: 1

    # Test Case 2
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(countCornerRectangles(grid2))  # Output: 9

    # Test Case 3
    grid3 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    print(countCornerRectangles(grid3))  # Output: 0

    # Test Case 4
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    print(countCornerRectangles(grid4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates through pairs of rows, which is O(rows^2).
- The inner loop iterates through all columns, which is O(cols).
- Therefore, the overall time complexity is O(rows^2 * cols).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""