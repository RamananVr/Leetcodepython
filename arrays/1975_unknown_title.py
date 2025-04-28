"""
LeetCode Problem #1975: Maximum Matrix Sum

Problem Statement:
You are given a 0-indexed 2D integer matrix `matrix` of size `m x n`. You can do the following operation any number of times:

- Pick any two adjacent elements in the matrix and multiply each of them by -1 (i.e., flip the sign of both elements).

Your goal is to maximize the sum of the matrix's elements after applying the above operation any number of times.

Return the maximum sum of the matrix's elements.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 250`
- `-10^5 <= matrix[i][j] <= 10^5`
"""

def maxMatrixSum(matrix):
    """
    Function to calculate the maximum sum of the matrix's elements after applying the operation.

    Args:
    matrix (List[List[int]]): 2D integer matrix.

    Returns:
    int: Maximum sum of the matrix's elements.
    """
    total_sum = 0
    min_abs_value = float('inf')
    negative_count = 0

    for row in matrix:
        for value in row:
            total_sum += abs(value)
            min_abs_value = min(min_abs_value, abs(value))
            if value < 0:
                negative_count += 1

    # If the number of negative values is odd, subtract twice the smallest absolute value
    if negative_count % 2 == 1:
        total_sum -= 2 * min_abs_value

    return total_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, -1], [-1, 1]]
    print(maxMatrixSum(matrix1))  # Expected Output: 4

    # Test Case 2
    matrix2 = [[1, 2, 3], [-1, -2, -3], [1, -1, 1]]
    print(maxMatrixSum(matrix2))  # Expected Output: 16

    # Test Case 3
    matrix3 = [[-1]]
    print(maxMatrixSum(matrix3))  # Expected Output: 1

    # Test Case 4
    matrix4 = [[-1, -2], [-3, -4]]
    print(maxMatrixSum(matrix4))  # Expected Output: 10


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through all elements of the matrix once.
- If the matrix has dimensions `m x n`, the total number of elements is `m * n`.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `total_sum`, `min_abs_value`, and `negative_count`.
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""