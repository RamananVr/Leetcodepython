"""
LeetCode Question #1476: Subrectangle Queries

Problem Statement:
Implement the class `SubrectangleQueries` which receives a `rectangle` (a 2D array of integers) as a parameter. 
The class should support the following two methods:

1. `updateSubrectangle(row1: int, col1: int, row2: int, col2: int, newValue: int) -> None`:
   Updates all values with `newValue` in the subrectangle whose upper left coordinate is `(row1, col1)` 
   and bottom right coordinate is `(row2, col2)`.

2. `getValue(row: int, col: int) -> int`:
   Returns the current value of the coordinate `(row, col)`.

Constraints:
- There will be at most `500` operations considering both methods.
- `1 <= rows, cols <= 100`
- `0 <= row1 <= row2 < rows`
- `0 <= col1 <= col2 < cols`
- `1 <= rectangle[i][j] <= 10^9`
- `0 <= row < rows`
- `0 <= col < cols`

Example:
Input:
    rectangle = [
        [1, 2, 1],
        [4, 3, 4],
        [3, 2, 1],
        [1, 1, 1]
    ]
    subrectangleQueries = SubrectangleQueries(rectangle)
    subrectangleQueries.getValue(0, 2) # return 1
    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
    subrectangleQueries.getValue(0, 2) # return 5
    subrectangleQueries.getValue(3, 1) # return 5
    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
    subrectangleQueries.getValue(3, 1) # return 10
    subrectangleQueries.getValue(0, 2) # return 5
"""

class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        """
        Initialize the SubrectangleQueries object with the given rectangle.
        """
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        """
        Update all values in the subrectangle defined by (row1, col1) to (row2, col2) to newValue.
        """
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        """
        Return the value of the cell at (row, col).
        """
        return self.rectangle[row][col]


# Example Test Cases
if __name__ == "__main__":
    # Initialize the rectangle
    rectangle = [
        [1, 2, 1],
        [4, 3, 4],
        [3, 2, 1],
        [1, 1, 1]
    ]
    subrectangleQueries = SubrectangleQueries(rectangle)

    # Test getValue
    assert subrectangleQueries.getValue(0, 2) == 1  # Expected: 1

    # Test updateSubrectangle
    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
    assert subrectangleQueries.getValue(0, 2) == 5  # Expected: 5
    assert subrectangleQueries.getValue(3, 1) == 5  # Expected: 5

    # Test another updateSubrectangle
    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
    assert subrectangleQueries.getValue(3, 1) == 10  # Expected: 10
    assert subrectangleQueries.getValue(0, 2) == 5  # Expected: 5

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `updateSubrectangle`:
   - Time Complexity: O((row2 - row1 + 1) * (col2 - col1 + 1)) 
     This is because we iterate over all cells in the specified subrectangle.
   - Space Complexity: O(1) 
     No additional space is used apart from the input rectangle.

2. `getValue`:
   - Time Complexity: O(1) 
     Accessing a specific cell in a 2D array is a constant-time operation.
   - Space Complexity: O(1) 
     No additional space is used.

Overall:
- Time Complexity: Depends on the number of operations and the size of the subrectangle being updated.
- Space Complexity: O(1) (excluding the input rectangle).

Topic: Arrays
"""