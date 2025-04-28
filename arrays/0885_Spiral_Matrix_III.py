"""
LeetCode Problem #885: Spiral Matrix III

Problem Statement:
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue the walk outside the grid (but the position is not added to the result). Eventually, we return to a position inside the grid.

Return a list of coordinates representing the positions of the cells in the order you visit them.

Constraints:
- 1 <= rows, cols <= 100
- 0 <= rStart < rows
- 0 <= cStart < cols
"""

def spiralMatrixIII(rows, cols, rStart, cStart):
    """
    Generate the coordinates of the cells in a spiral order starting from (rStart, cStart).
    
    :param rows: int - Number of rows in the grid
    :param cols: int - Number of columns in the grid
    :param rStart: int - Starting row index
    :param cStart: int - Starting column index
    :return: List[List[int]] - List of coordinates in spiral order
    """
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    steps = 1  # Number of steps to take in the current direction
    x, y = rStart, cStart  # Current position
    direction_index = 0  # Start with moving right

    while len(result) < rows * cols:
        for _ in range(2):  # Each step size is repeated twice (e.g., right and down, then left and up)
            for _ in range(steps):
                # Check if the current position is within bounds
                if 0 <= x < rows and 0 <= y < cols:
                    result.append([x, y])
                # Move in the current direction
                dx, dy = directions[direction_index]
                x, y = x + dx, y + dy
            # Change direction (right -> down -> left -> up)
            direction_index = (direction_index + 1) % 4
        # Increase the step size after completing two directions
        steps += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rows, cols, rStart, cStart = 1, 4, 0, 0
    print(spiralMatrixIII(rows, cols, rStart, cStart))
    # Expected Output: [[0, 0], [0, 1], [0, 2], [0, 3]]

    # Test Case 2
    rows, cols, rStart, cStart = 5, 6, 1, 4
    print(spiralMatrixIII(rows, cols, rStart, cStart))
    # Expected Output: [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], ...]

    # Test Case 3
    rows, cols, rStart, cStart = 3, 3, 0, 0
    print(spiralMatrixIII(rows, cols, rStart, cStart))
    # Expected Output: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1]]

"""
Time Complexity:
- The algorithm visits every cell in the grid exactly once.
- Therefore, the time complexity is O(rows * cols).

Space Complexity:
- The space complexity is O(rows * cols) to store the result list.

Topic: Arrays
"""