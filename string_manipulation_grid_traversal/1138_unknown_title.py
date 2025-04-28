"""
LeetCode Problem #1138: Alphabet Board Path

Problem Statement:
On an alphabet board, we have the letters 'a' to 'z' written in rows and columns like this:

    a b c d e
    f g h i j
    k l m n o
    p q r s t
    u v w x y
    z

Given a string `target`, return the sequence of moves to spell the string `target` on the board. 
You can start at the position of letter 'a'. Each move takes the form:

- 'U' (up), 'D' (down), 'L' (left), 'R' (right), or '!' (select the current letter).

The board is represented as a grid with coordinates (row, col), where row is the index of the row (0-indexed) and col is the index of the column (0-indexed). The letter 'z' is at position (5, 0).

You may assume that the input string `target` consists of only lowercase English letters.

Example:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Constraints:
- 1 <= target.length <= 100
- `target` consists only of lowercase English letters.
"""

# Python Solution
def alphabetBoardPath(target: str) -> str:
    def get_position(char):
        """Helper function to get the (row, col) position of a character on the board."""
        index = ord(char) - ord('a')
        return divmod(index, 5)  # row = index // 5, col = index % 5

    result = []
    current_row, current_col = 0, 0  # Start at 'a' (0, 0)

    for char in target:
        target_row, target_col = get_position(char)

        # Special handling for 'z' since it's at (5, 0) and requires careful movement
        if char == 'z':
            # Move horizontally first, then vertically
            if current_col > target_col:
                result.append('L' * (current_col - target_col))
            if current_row < target_row:
                result.append('D' * (target_row - current_row))
        else:
            # Move vertically first, then horizontally
            if current_row > target_row:
                result.append('U' * (current_row - target_row))
            if current_row < target_row:
                result.append('D' * (target_row - current_row))
            if current_col > target_col:
                result.append('L' * (current_col - target_col))
            if current_col < target_col:
                result.append('R' * (target_col - current_col))

        # Add '!' to select the current letter
        result.append('!')
        current_row, current_col = target_row, target_col

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = "leet"
    print(alphabetBoardPath(target))  # Output: "DDR!UURRR!!DDD!"

    # Test Case 2
    target = "code"
    print(alphabetBoardPath(target))  # Output: "RR!DDRR!UUL!R!"

    # Test Case 3
    target = "z"
    print(alphabetBoardPath(target))  # Output: "DDDDD!"

    # Test Case 4
    target = "abc"
    print(alphabetBoardPath(target))  # Output: "!R!R!"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each character in the `target` string, and for each character, it calculates the position and appends the moves to the result.
- Calculating the position and appending moves are O(1) operations.
- Therefore, the time complexity is O(n), where n is the length of the `target` string.

Space Complexity:
- The space complexity is O(n) for the result string, which stores the sequence of moves.
- No additional data structures are used, so the space complexity is O(n).
"""

# Topic: String Manipulation, Grid Traversal