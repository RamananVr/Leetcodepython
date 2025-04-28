"""
LeetCode Problem #1337: The K Weakest Rows in a Matrix

Problem Statement:
You are given an `m x n` binary matrix `mat` of `1`s (representing soldiers) and `0`s (representing civilians). 
The soldiers are always positioned in front of the civilians in each row, meaning all the `1`s will appear to 
the left of all the `0`s in each row.

A row `i` is weaker than a row `j` if one of the following is true:
  - The number of soldiers in row `i` is less than the number of soldiers in row `j`.
  - Both rows have the same number of soldiers, and `i < j`.

Return the indices of the `k` weakest rows in the matrix ordered from weakest to strongest.

Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,0,0]], 
k = 3
Output: [2, 0, 3]

Example 2:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0, 2]

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `2 <= n, m <= 100`
- `1 <= k <= m`
- `matrix[i][j]` is either 0 or 1.
"""

from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    # Calculate the number of soldiers in each row and pair it with the row index
    soldier_count = [(sum(row), i) for i, row in enumerate(mat)]
    # Sort by the number of soldiers, and by index in case of ties
    soldier_count.sort()
    # Extract the indices of the k weakest rows
    return [index for _, index in soldier_count[:k]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0]
    ]
    k1 = 3
    print(kWeakestRows(mat1, k1))  # Output: [2, 0, 3]

    # Test Case 2
    mat2 = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    k2 = 2
    print(kWeakestRows(mat2, k2))  # Output: [0, 2]

    # Test Case 3
    mat3 = [
        [1, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ]
    k3 = 2
    print(kWeakestRows(mat3, k3))  # Output: [3, 2]

"""
Time Complexity Analysis:
- Calculating the number of soldiers in each row takes O(m * n), where m is the number of rows and n is the number of columns.
- Sorting the rows based on the number of soldiers takes O(m * log(m)).
- Extracting the indices of the k weakest rows takes O(k).
- Overall time complexity: O(m * n + m * log(m)).

Space Complexity Analysis:
- The space required to store the soldier count and indices is O(m).
- Overall space complexity: O(m).

Topic: Arrays, Sorting
"""