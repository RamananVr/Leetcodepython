"""
LeetCode Problem #2397: Maximum Rows Covered by Columns

Problem Statement:
You are given a 0-indexed m x n binary matrix `mat` and an integer `cols`, which denotes the number of columns you must choose.

A row is covered by a set of columns if all the 1's in the row are also covered by the chosen columns.

Return the maximum number of rows that can be covered by choosing `cols` columns.

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 12`
- `0 <= mat[i][j] <= 1`
- `1 <= cols <= n`
"""

from itertools import combinations

def maximumRows(mat, cols):
    """
    Function to calculate the maximum number of rows covered by choosing `cols` columns.

    :param mat: List[List[int]] - The binary matrix
    :param cols: int - The number of columns to choose
    :return: int - The maximum number of rows covered
    """
    m, n = len(mat), len(mat[0])
    max_covered = 0

    # Generate all possible combinations of `cols` columns
    for col_indices in combinations(range(n), cols):
        covered_rows = 0
        for row in mat:
            # Check if all 1's in the row are covered by the selected columns
            if all(row[j] == 0 or j in col_indices for j in range(n)):
                covered_rows += 1
        max_covered = max(max_covered, covered_rows)

    return max_covered

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    cols1 = 2
    print(maximumRows(mat1, cols1))  # Expected Output: 2

    # Test Case 2
    mat2 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]
    cols2 = 2
    print(maximumRows(mat2, cols2))  # Expected Output: 2

    # Test Case 3
    mat3 = [
        [1, 1, 1],
        [1, 0, 1],
        [0, 0, 0]
    ]
    cols3 = 3
    print(maximumRows(mat3, cols3))  # Expected Output: 3

"""
Time Complexity Analysis:
- The number of combinations of `cols` columns from `n` columns is C(n, cols) = n! / (cols! * (n - cols)!).
- For each combination, we iterate through all `m` rows and check if the row is covered, which takes O(m * n) in the worst case.
- Therefore, the overall time complexity is O(C(n, cols) * m * n), which simplifies to O((n choose cols) * m * n).

Space Complexity Analysis:
- The space complexity is dominated by the storage of combinations, which is O(C(n, cols)).
- Thus, the space complexity is O((n choose cols)).

Topic: Combinatorics, Matrix, Brute Force
"""