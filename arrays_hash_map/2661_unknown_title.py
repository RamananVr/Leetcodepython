"""
LeetCode Problem #2661: First Completely Painted Row or Column

Problem Statement:
You are given an integer `n` representing the number of rows and columns in a square matrix, and a 2D integer array `mat` of size `n x n` where `mat[i][j]` represents the color of the cell `(i, j)` in the matrix. You are also given an integer array `arr` where `arr[k]` represents the color that is painted at step `k`.

Initially, all cells in the matrix are unpainted. At step `k`, every cell in the matrix with color `arr[k]` is painted. Return the step at which either a row or a column is completely painted for the first time. If no row or column is completely painted, return -1.

Constraints:
- `1 <= n <= 100`
- `1 <= mat[i][j], arr[k] <= 10^4`
- `1 <= arr.length <= 10^4`

"""

# Solution
def first_completely_painted(mat, arr):
    from collections import defaultdict

    n = len(mat)
    row_count = [0] * n
    col_count = [0] * n
    color_to_cells = defaultdict(list)

    # Map colors to their corresponding cells
    for i in range(n):
        for j in range(n):
            color_to_cells[mat[i][j]].append((i, j))

    # Process the painting steps
    for step, color in enumerate(arr):
        if color in color_to_cells:
            for i, j in color_to_cells[color]:
                row_count[i] += 1
                col_count[j] += 1
                if row_count[i] == n or col_count[j] == n:
                    return step

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    arr1 = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    print(first_completely_painted(mat1, arr1))  # Output: 6

    # Test Case 2
    mat2 = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]
    arr2 = [1, 2, 3]
    print(first_completely_painted(mat2, arr2))  # Output: 0

    # Test Case 3
    mat3 = [
        [1, 2],
        [3, 4]
    ]
    arr3 = [1, 3, 2, 4]
    print(first_completely_painted(mat3, arr3))  # Output: 2

    # Test Case 4
    mat4 = [
        [1, 2],
        [3, 4]
    ]
    arr4 = [5, 6, 7]
    print(first_completely_painted(mat4, arr4))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Mapping colors to cells takes O(n^2), where n is the size of the matrix.
- Processing the painting steps takes O(arr.length * average_cells_per_color). In the worst case, each color could correspond to all n^2 cells, making this O(arr.length * n^2).
- Overall, the time complexity is O(n^2 + arr.length * n^2).

Space Complexity:
- The `color_to_cells` dictionary stores mappings of colors to their corresponding cells, which can take up to O(n^2) space.
- The `row_count` and `col_count` arrays each take O(n) space.
- Overall, the space complexity is O(n^2).
"""

# Topic: Arrays, Hash Map