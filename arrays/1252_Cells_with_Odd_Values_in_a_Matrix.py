"""
LeetCode Problem #1252: Cells with Odd Values in a Matrix

Problem Statement:
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-based index (ri, ci).

For each pair of (ri, ci) in indices, you must increment all the cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Constraints:
- 1 <= m, n <= 50
- 1 <= indices.length <= 100
- 0 <= ri < m
- 0 <= ci < n
"""

# Python Solution
def oddCells(m: int, n: int, indices: list[list[int]]) -> int:
    # Initialize row and column increment counters
    row_increments = [0] * m
    col_increments = [0] * n

    # Apply increments based on indices
    for r, c in indices:
        row_increments[r] += 1
        col_increments[c] += 1

    # Count cells with odd values
    odd_count = 0
    for i in range(m):
        for j in range(n):
            # Calculate the value of the cell
            cell_value = row_increments[i] + col_increments[j]
            if cell_value % 2 == 1:
                odd_count += 1

    return odd_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m1, n1, indices1 = 2, 3, [[0, 1], [1, 1]]
    print(oddCells(m1, n1, indices1))  # Expected Output: 6

    # Test Case 2
    m2, n2, indices2 = 2, 2, [[1, 1], [0, 0]]
    print(oddCells(m2, n2, indices2))  # Expected Output: 0

    # Test Case 3
    m3, n3, indices3 = 3, 3, [[0, 0], [1, 1], [2, 2]]
    print(oddCells(m3, n3, indices3))  # Expected Output: 3

# Time and Space Complexity Analysis
# Time Complexity:
# - Calculating row and column increments takes O(len(indices)).
# - Counting odd cells involves iterating over the entire matrix, which takes O(m * n).
# - Overall time complexity: O(len(indices) + m * n).

# Space Complexity:
# - We use two auxiliary arrays, row_increments and col_increments, of sizes m and n respectively.
# - Space complexity: O(m + n).

# Topic: Arrays