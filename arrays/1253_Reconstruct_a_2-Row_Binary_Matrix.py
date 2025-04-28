"""
LeetCode Problem #1253: Reconstruct a 2-Row Binary Matrix

Problem Statement:
Given the following details of a matrix with n rows and 2 columns:
1. The matrix is a binary matrix, which means each element in the matrix is either 0 or 1.
2. The sum of elements in the first row is given as `upper`.
3. The sum of elements in the second row is given as `lower`.
4. The sum of elements in each column is given as the array `colsum`.

Your task is to reconstruct and return the matrix. If there are multiple valid solutions, you may return any of them. If no valid solution exists, return an empty list.

Example 1:
Input: upper = 2, lower = 1, colsum = [1, 1, 1]
Output: [[1, 1, 0], [0, 0, 1]]

Example 2:
Input: upper = 2, lower = 3, colsum = [2, 2, 1, 1]
Output: []

Example 3:
Input: upper = 5, lower = 5, colsum = [2, 1, 2, 0, 1, 0, 1, 2]
Output: [[1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 1]]

Constraints:
- 1 <= colsum.length <= 10^5
- 0 <= upper, lower <= colsum.length
- 0 <= colsum[i] <= 2
"""

def reconstructMatrix(upper, lower, colsum):
    """
    Reconstructs a 2-row binary matrix based on the given constraints.

    :param upper: int, sum of elements in the first row
    :param lower: int, sum of elements in the second row
    :param colsum: List[int], sum of elements in each column
    :return: List[List[int]], reconstructed matrix or an empty list if no solution exists
    """
    n = len(colsum)
    matrix = [[0] * n for _ in range(2)]

    for i in range(n):
        if colsum[i] == 2:
            # Both rows must have 1
            if upper > 0 and lower > 0:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1
            else:
                return []  # Not enough upper or lower to satisfy colsum[i] == 2
        elif colsum[i] == 1:
            # Assign 1 to either upper or lower row
            if upper > lower and upper > 0:
                matrix[0][i] = 1
                upper -= 1
            elif lower > 0:
                matrix[1][i] = 1
                lower -= 1
            else:
                return []  # Not enough upper or lower to satisfy colsum[i] == 1

    # Check if upper and lower sums are satisfied
    if upper == 0 and lower == 0:
        return matrix
    return []  # If upper or lower is not satisfied, return an empty list


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    upper = 2
    lower = 1
    colsum = [1, 1, 1]
    print(reconstructMatrix(upper, lower, colsum))  # Expected Output: [[1, 1, 0], [0, 0, 1]]

    # Test Case 2
    upper = 2
    lower = 3
    colsum = [2, 2, 1, 1]
    print(reconstructMatrix(upper, lower, colsum))  # Expected Output: []

    # Test Case 3
    upper = 5
    lower = 5
    colsum = [2, 1, 2, 0, 1, 0, 1, 2]
    print(reconstructMatrix(upper, lower, colsum))  # Expected Output: [[1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 1]]


# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `colsum` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `colsum` array.

Space Complexity:
- The algorithm uses a matrix of size 2 x n to store the result.
- Therefore, the space complexity is O(n), where n is the length of the `colsum` array.
"""

# Topic: Arrays