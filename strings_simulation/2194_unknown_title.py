"""
LeetCode Problem #2194: Cells in a Range on an Excel Sheet

Problem Statement:
You are given a string `s` that represents a range of cells in an Excel sheet, such as "A1:F1". 
The range of cells includes all the cells from the top-left cell to the bottom-right cell.

Return a list of all the cells in the range sorted lexicographically.

Example 1:
Input: s = "K1:L2"
Output: ["K1","K2","L1","L2"]
Explanation: The range of cells is from "K1" to "L2".

Example 2:
Input: s = "A1:F1"
Output: ["A1","B1","C1","D1","E1","F1"]
Explanation: The range of cells is from "A1" to "F1".

Constraints:
- `s` consists of two uppercase English letters and two digits, separated by a colon.
- The letters define the columns (from 'A' to 'Z').
- The digits define the rows (from '1' to '99').
"""

# Python Solution
def cellsInRange(s: str) -> list[str]:
    # Parse the input string to extract the start and end columns and rows
    start_col, start_row, end_col, end_row = s[0], s[1], s[3], s[4]
    
    # Generate the range of columns and rows
    columns = [chr(c) for c in range(ord(start_col), ord(end_col) + 1)]
    rows = [str(r) for r in range(int(start_row), int(end_row) + 1)]
    
    # Combine columns and rows to form the cell names
    result = [col + row for col in columns for row in rows]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "K1:L2"
    print(cellsInRange(s1))  # Output: ["K1", "K2", "L1", "L2"]

    # Test Case 2
    s2 = "A1:F1"
    print(cellsInRange(s2))  # Output: ["A1", "B1", "C1", "D1", "E1", "F1"]

    # Test Case 3
    s3 = "C3:E5"
    print(cellsInRange(s3))  # Output: ["C3", "C4", "C5", "D3", "D4", "D5", "E3", "E4", "E5"]

    # Test Case 4
    s4 = "Z1:Z3"
    print(cellsInRange(s4))  # Output: ["Z1", "Z2", "Z3"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating the range of columns takes O(end_col - start_col), which is at most 26 (for 'A' to 'Z').
- Generating the range of rows takes O(end_row - start_row), which is at most 99.
- Combining columns and rows takes O((end_col - start_col) * (end_row - start_row)).
Thus, the overall time complexity is O((end_col - start_col) * (end_row - start_row)).

Space Complexity:
- The space required for the result list is proportional to the number of cells in the range, 
  which is O((end_col - start_col) * (end_row - start_row)).
- Additional space is used for the intermediate lists of columns and rows, which is negligible compared to the result list.
Thus, the overall space complexity is O((end_col - start_col) * (end_row - start_row)).
"""

# Topic: Strings, Simulation