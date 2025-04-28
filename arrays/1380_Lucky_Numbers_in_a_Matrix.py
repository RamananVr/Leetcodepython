"""
LeetCode Problem #1380: Lucky Numbers in a Matrix

Problem Statement:
Given an `m x n` matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and the maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 50`
- `1 <= matrix[i][j] <= 10^5`
- All elements in the matrix are distinct.
"""

def luckyNumbers(matrix):
    """
    Finds all lucky numbers in the given matrix.

    Args:
    matrix (List[List[int]]): A 2D list of integers.

    Returns:
    List[int]: A list of lucky numbers.
    """
    # Step 1: Find the minimum element in each row
    min_in_rows = {min(row) for row in matrix}
    
    # Step 2: Find the maximum element in each column
    max_in_cols = {max(col) for col in zip(*matrix)}
    
    # Step 3: The lucky numbers are the intersection of the two sets
    return list(min_in_rows & max_in_cols)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(luckyNumbers(matrix1))  # Output: [15]

    # Test Case 2
    matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(luckyNumbers(matrix2))  # Output: [12]

    # Test Case 3
    matrix3 = [[7, 8], [1, 2]]
    print(luckyNumbers(matrix3))  # Output: [7]

    # Test Case 4
    matrix4 = [[5]]
    print(luckyNumbers(matrix4))  # Output: [5]

    # Test Case 5
    matrix5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(luckyNumbers(matrix5))  # Output: []

"""
Time Complexity Analysis:
- Finding the minimum in each row takes O(m * n), where `m` is the number of rows and `n` is the number of columns.
- Finding the maximum in each column takes O(m * n) (using `zip(*matrix)` to transpose the matrix).
- The intersection of two sets takes O(min(len(min_in_rows), len(max_in_cols))).
- Overall time complexity: O(m * n).

Space Complexity Analysis:
- The space used for `min_in_rows` and `max_in_cols` is O(m + n) in the worst case.
- Overall space complexity: O(m + n).

Topic: Arrays
"""