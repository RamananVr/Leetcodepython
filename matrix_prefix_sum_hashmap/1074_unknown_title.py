"""
LeetCode Problem #1074: Number of Submatrices That Sum to Target

Problem Statement:
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate
that is different: for example, if x1 != x1'.

Example:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 0-sum submatrices are:
- [[0]]
- [[0,1,0],[1,1,1],[0,1,0]] (the entire matrix)
- [[0,1,0],[1,1,1],[0,1,0]] (the entire matrix)
- [[0,1,0],[1,1,1],[0,1,0]] (the entire matrix)

Constraints:
1. The number of rows and columns of matrix will be in the range [1, 100].
2. -1000 <= matrix[i][j] <= 1000
3. -10^8 <= target <= 10^8
"""

# Python Solution
def numSubmatrixSumTarget(matrix, target):
    """
    Function to count the number of submatrices that sum to the given target.

    :param matrix: List[List[int]], the input matrix
    :param target: int, the target sum
    :return: int, the number of submatrices that sum to the target
    """
    from collections import defaultdict

    rows, cols = len(matrix), len(matrix[0])
    result = 0

    # Iterate over all pairs of rows
    for r1 in range(rows):
        # Initialize a list to store the cumulative sum for each column
        col_sum = [0] * cols
        for r2 in range(r1, rows):
            # Update the cumulative sum for each column
            for c in range(cols):
                col_sum[c] += matrix[r2][c]

            # Use a hashmap to count subarrays with the target sum
            prefix_sum_count = defaultdict(int)
            prefix_sum_count[0] = 1
            current_sum = 0

            for sum_val in col_sum:
                current_sum += sum_val
                result += prefix_sum_count[current_sum - target]
                prefix_sum_count[current_sum] += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target1 = 0
    print(numSubmatrixSumTarget(matrix1, target1))  # Output: 4

    # Test Case 2
    matrix2 = [[1, -1], [-1, 1]]
    target2 = 0
    print(numSubmatrixSumTarget(matrix2, target2))  # Output: 5

    # Test Case 3
    matrix3 = [[904]]
    target3 = 0
    print(numSubmatrixSumTarget(matrix3, target3))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over all pairs of rows, which is O(rows^2).
- For each pair of rows, we calculate the cumulative sum for each column (O(cols)).
- Then, we use a hashmap to count subarrays with the target sum, which is O(cols).
- Overall complexity: O(rows^2 * cols).

Space Complexity:
- We use a hashmap to store prefix sums, which requires O(cols) space.
- The cumulative sum array also requires O(cols) space.
- Overall space complexity: O(cols).

Topic: Matrix, Prefix Sum, Hashmap
"""