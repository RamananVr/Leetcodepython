"""
LeetCode Problem #1030: Matrix Cells in Distance Order

Problem Statement:
You are given four integers `rows`, `cols`, `rCenter`, and `cCenter` representing the dimensions of a matrix with `rows` rows and `cols` columns, and the position of a cell in that matrix (rCenter, cCenter).

Return a 2D array of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from smallest to largest. Here, the distance between two cells (r1, c1) and (r2, c2) is defined as `|r1 - r2| + |c1 - c2|` (Manhattan distance).

You may return the answer in any order that satisfies this condition.

Constraints:
- 1 <= rows, cols <= 100
- 0 <= rCenter < rows
- 0 <= cCenter < cols
"""

# Solution
from typing import List

def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    # Generate all cells in the matrix
    cells = [[r, c] for r in range(rows) for c in range(cols)]
    
    # Sort cells by their Manhattan distance from (rCenter, cCenter)
    cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
    
    return cells

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rows, cols, rCenter, cCenter = 1, 2, 0, 0
    print(allCellsDistOrder(rows, cols, rCenter, cCenter))
    # Expected Output: [[0, 0], [0, 1]]

    # Test Case 2
    rows, cols, rCenter, cCenter = 2, 2, 0, 1
    print(allCellsDistOrder(rows, cols, rCenter, cCenter))
    # Expected Output: [[0, 1], [0, 0], [1, 1], [1, 0]]

    # Test Case 3
    rows, cols, rCenter, cCenter = 3, 3, 2, 2
    print(allCellsDistOrder(rows, cols, rCenter, cCenter))
    # Expected Output: [[2, 2], [2, 1], [1, 2], [2, 0], [1, 1], [0, 2], [1, 0], [0, 1], [0, 0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating all cells takes O(rows * cols).
- Sorting the cells by Manhattan distance takes O((rows * cols) * log(rows * cols)).
- Overall time complexity: O(rows * cols * log(rows * cols)).

Space Complexity:
- The `cells` list stores all cells in the matrix, which requires O(rows * cols) space.
- Overall space complexity: O(rows * cols).
"""

# Topic: Sorting