"""
LeetCode Question #631: Design Excel Sum Formula

Problem Statement:
Design a class to represent a simplified Excel spreadsheet. The spreadsheet has the following features:
1. You can set the value of a cell.
2. You can get the value of a cell.
3. You can set a cell to be the sum of other cells (possibly including itself).

Implement the `Excel` class:
- `Excel(int height, char width)` Initializes the object with the height and width of the spreadsheet. The spreadsheet is a grid of size `height x width` where the top-left cell is `(1, 'A')` and the bottom-right cell is `(height, width)`. The column letter `width` is converted to an integer where 'A' = 1, 'B' = 2, ..., 'Z' = 26.
- `set(int row, char column, int value)` Sets the value of the cell `(row, column)` to `value`.
- `get(int row, char column)` Returns the value of the cell `(row, column)`.
- `sum(int row, char column, List[str] numbers)` Sets the cell `(row, column)` to be the sum of the specified cells. The `numbers` list contains strings in the format `"A1"` or `"A1:B2"`. Each string represents either a single cell or a rectangular range of cells. The value of the cell `(row, column)` should be updated to the sum of the values of the specified cells.

Constraints:
- `1 <= height <= 26`
- `'A' <= width <= 'Z'`
- `1 <= row <= height`
- `'A' <= column <= width`
- `-100 <= value <= 100`
- At most 1000 calls will be made to `set`, `get`, and `sum`.

"""

class Excel:
    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1
        self.grid = [[0] * self.width for _ in range(height)]
        self.formulas = {}

    def set(self, row: int, column: str, value: int) -> None:
        col = ord(column) - ord('A')
        self.grid[row - 1][col] = value
        if (row, column) in self.formulas:
            del self.formulas[(row, column)]

    def get(self, row: int, column: str) -> int:
        col = ord(column) - ord('A')
        if (row, column) in self.formulas:
            return self._calculate_sum(row, column)
        return self.grid[row - 1][col]

    def sum(self, row: int, column: str, numbers: list) -> int:
        self.formulas[(row, column)] = numbers
        return self._calculate_sum(row, column)

    def _calculate_sum(self, row: int, column: str) -> int:
        numbers = self.formulas[(row, column)]
        total = 0
        for num in numbers:
            if ':' in num:
                start, end = num.split(':')
                start_row, start_col = int(start[1:]), ord(start[0]) - ord('A')
                end_row, end_col = int(end[1:]), ord(end[0]) - ord('A')
                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        total += self.get(r, chr(c + ord('A')))
            else:
                r, c = int(num[1:]), ord(num[0]) - ord('A')
                total += self.get(r, chr(c + ord('A')))
        self.grid[row - 1][ord(column) - ord('A')] = total
        return total


# Example Test Cases
if __name__ == "__main__":
    excel = Excel(3, 'C')
    excel.set(1, 'A', 5)
    print(excel.get(1, 'A'))  # Output: 5
    print(excel.sum(1, 'B', ["A1"]))  # Output: 5
    excel.set(2, 'A', 3)
    print(excel.sum(1, 'B', ["A1", "A2"]))  # Output: 8
    excel.set(1, 'A', 2)
    print(excel.get(1, 'B'))  # Output: 5 (sum formula still applies)

"""
Time and Space Complexity Analysis:
- `set`: O(1) time and space complexity.
- `get`: O(1) time and space complexity for direct access; O(k) for sum formula where k is the number of cells in the formula.
- `sum`: O(k) time complexity where k is the number of cells in the formula; O(1) space complexity.
- Overall space complexity: O(h * w + f) where h is the height, w is the width, and f is the number of formulas.

Topic: Design, HashMap, Simulation
"""