"""
LeetCode Problem #85: Maximal Rectangle

Problem Statement:
Given a binary matrix `matrix`, return the maximum area of a rectangle formed only of 1's in the given matrix.

The input matrix is a 2D binary matrix filled with 0's and 1's.

Example:
Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 6
Explanation: The maximal rectangle is shown in the below diagram:
[
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
The rectangle of 1's with the largest area is 2x3, which has an area of 6.

Constraints:
- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is '0' or '1'.
"""

def maximalRectangle(matrix):
    """
    Function to find the maximal rectangle area in a binary matrix.
    :param matrix: List[List[str]] - 2D binary matrix
    :return: int - Maximum area of a rectangle formed by 1's
    """
    if not matrix or not matrix[0]:
        return 0

    # Convert the matrix to heights for each column
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for col in range(cols):
            # Update the height of the column
            heights[col] = heights[col] + 1 if row[col] == '1' else 0

        # Calculate the maximum area for the current row's histogram
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

def largestRectangleArea(heights):
    """
    Helper function to calculate the largest rectangle area in a histogram.
    :param heights: List[int] - Heights of the histogram
    :return: int - Maximum area of a rectangle in the histogram
    """
    stack = []
    max_area = 0
    heights.append(0)  # Add a sentinel value to flush the stack at the end

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()  # Remove the sentinel value
    return max_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print("Test Case 1 Output:", maximalRectangle(matrix1))  # Expected Output: 6

    # Test Case 2
    matrix2 = [
        ["0", "1"],
        ["1", "0"]
    ]
    print("Test Case 2 Output:", maximalRectangle(matrix2))  # Expected Output: 1

    # Test Case 3
    matrix3 = [
        ["1"]
    ]
    print("Test Case 3 Output:", maximalRectangle(matrix3))  # Expected Output: 1

    # Test Case 4
    matrix4 = [
        ["0"]
    ]
    print("Test Case 4 Output:", maximalRectangle(matrix4))  # Expected Output: 0

"""
Time Complexity:
- The outer loop iterates over each row of the matrix, so O(rows).
- For each row, we calculate the largest rectangle in a histogram, which takes O(cols) using a stack.
- Overall time complexity: O(rows * cols).

Space Complexity:
- We use an array `heights` of size `cols` to store the heights of the histogram, and a stack for the histogram calculation.
- Space complexity: O(cols).

Topic: Dynamic Programming, Stack, Matrix
"""