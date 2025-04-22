"""
LeetCode Problem #59: Spiral Matrix II

Problem Statement:
Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.

Example 1:
Input: n = 3
Output: 
[
 [1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]
]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
- 1 <= n <= 20
"""

def generateMatrix(n):
    """
    Generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

    :param n: int
    :return: List[List[int]]
    """
    # Initialize an empty n x n matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries of the spiral
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  # Start filling the matrix with 1
    
    while top <= bottom and left <= right:
        # Fill the top row
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        # Fill the right column
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        # Fill the bottom row (if still within bounds)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        # Fill the left column (if still within bounds)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    return matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print("Input:", n)
    print("Output:", generateMatrix(n))
    # Expected Output:
    # [
    #  [1, 2, 3],
    #  [8, 9, 4],
    #  [7, 6, 5]
    # ]

    # Test Case 2
    n = 1
    print("Input:", n)
    print("Output:", generateMatrix(n))
    # Expected Output: [[1]]

    # Test Case 3
    n = 4
    print("Input:", n)
    print("Output:", generateMatrix(n))
    # Expected Output:
    # [
    #  [1, 2, 3, 4],
    #  [12, 13, 14, 5],
    #  [11, 16, 15, 6],
    #  [10, 9, 8, 7]
    # ]

"""
Time Complexity Analysis:
- The algorithm iterates over all elements of the matrix exactly once.
- Filling the matrix takes O(n^2) time, where n is the size of the matrix.

Space Complexity Analysis:
- The algorithm uses O(n^2) space to store the matrix.
- No additional space is used apart from the matrix itself, so the space complexity is O(n^2).

Topic: Arrays
"""