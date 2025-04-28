"""
LeetCode Problem #1812: Determine Color of a Chessboard Square

Problem Statement:
You are given a string `coordinates` that represents the coordinates of a square on a chessboard. 
Below is a mapping of the chessboard:

- The chessboard is an 8x8 grid.
- Columns are labeled from 'a' to 'h' (left to right).
- Rows are labeled from '1' to '8' (bottom to top).

The input `coordinates` is a string of length 2, where:
- The first character represents the column ('a' to 'h').
- The second character represents the row ('1' to '8').

Return `True` if the square is white, and `False` if the square is black.

The chessboard alternates colors such that:
- Squares in the first column ('a') alternate between black and white starting with black.
- Squares in the second column ('b') alternate between black and white starting with white.
- This pattern continues for all columns.

Constraints:
- `coordinates.length == 2`
- `'a' <= coordinates[0] <= 'h'`
- `'1' <= coordinates[1] <= '8'`

Example:
Input: coordinates = "a1"
Output: False

Input: coordinates = "h3"
Output: True

Input: coordinates = "c7"
Output: False
"""

# Solution
def squareIsWhite(coordinates: str) -> bool:
    """
    Determines if a chessboard square is white or black based on its coordinates.

    Args:
    coordinates (str): A string representing the square's coordinates (e.g., "a1").

    Returns:
    bool: True if the square is white, False if the square is black.
    """
    column = ord(coordinates[0]) - ord('a')  # Convert column letter to a 0-based index
    row = int(coordinates[1]) - 1           # Convert row number to a 0-based index
    return (column + row) % 2 == 1          # White squares have an odd sum of indices

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    coordinates = "a1"
    print(squareIsWhite(coordinates))  # Output: False

    # Test Case 2
    coordinates = "h3"
    print(squareIsWhite(coordinates))  # Output: True

    # Test Case 3
    coordinates = "c7"
    print(squareIsWhite(coordinates))  # Output: False

    # Test Case 4
    coordinates = "d4"
    print(squareIsWhite(coordinates))  # Output: True

    # Test Case 5
    coordinates = "g8"
    print(squareIsWhite(coordinates))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves simple arithmetic operations and character manipulations, which are O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space for variables and does not depend on the input size.
- Therefore, the space complexity is O(1).

Topic: Strings
"""