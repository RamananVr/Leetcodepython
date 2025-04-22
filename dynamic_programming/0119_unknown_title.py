"""
LeetCode Problem #119: Pascal's Triangle II

Problem Statement:
Given an integer `rowIndex`, return the `rowIndex`th (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example:
Input: rowIndex = 3
Output: [1, 3, 3, 1]

Explanation:
Row 0: [1]
Row 1: [1, 1]
Row 2: [1, 2, 1]
Row 3: [1, 3, 3, 1]

Constraints:
- 0 <= rowIndex <= 33

Follow up:
Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

def getRow(rowIndex: int) -> list[int]:
    """
    Returns the rowIndex-th row of Pascal's Triangle.
    Optimized to use O(rowIndex) space.
    """
    row = [1]  # Start with the first row
    for i in range(1, rowIndex + 1):
        # Compute the next row in reverse to avoid overwriting values
        row.append(1)  # Add a placeholder for the new row's last element
        for j in range(len(row) - 2, 0, -1):
            row[j] += row[j - 1]
    return row

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rowIndex = 3
    print(f"Input: rowIndex = {rowIndex}")
    print(f"Output: {getRow(rowIndex)}")  # Expected: [1, 3, 3, 1]

    # Test Case 2
    rowIndex = 0
    print(f"Input: rowIndex = {rowIndex}")
    print(f"Output: {getRow(rowIndex)}")  # Expected: [1]

    # Test Case 3
    rowIndex = 1
    print(f"Input: rowIndex = {rowIndex}")
    print(f"Output: {getRow(rowIndex)}")  # Expected: [1, 1]

    # Test Case 4
    rowIndex = 5
    print(f"Input: rowIndex = {rowIndex}")
    print(f"Output: {getRow(rowIndex)}")  # Expected: [1, 5, 10, 10, 5, 1]

"""
Time Complexity:
- The algorithm iterates through `rowIndex` rows, and for each row, it updates the elements in reverse order.
- The total number of updates is proportional to the sum of the first `rowIndex` integers, which is O(rowIndex^2).
- Therefore, the time complexity is O(rowIndex^2).

Space Complexity:
- The algorithm uses a single list `row` to store the current row of Pascal's Triangle.
- The size of this list is proportional to `rowIndex`.
- Therefore, the space complexity is O(rowIndex).

Topic: Dynamic Programming
"""