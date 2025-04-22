"""
LeetCode Question #118: Pascal's Triangle

Problem Statement:
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example:
    Input: numRows = 5
    Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

Constraints:
    - 1 <= numRows <= 30
"""

def generate(numRows):
    """
    Generate the first numRows of Pascal's Triangle.

    :param numRows: int - Number of rows to generate
    :return: List[List[int]] - Pascal's Triangle up to numRows
    """
    if numRows <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, numRows):
        prev_row = triangle[-1]  # Get the previous row
        current_row = [1]  # Start the current row with 1
        for j in range(1, i):  # Compute the inner elements of the row
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)  # End the current row with 1
        triangle.append(current_row)  # Add the current row to the triangle

    return triangle

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numRows = 5
    print(f"Pascal's Triangle for numRows = {numRows}:")
    print(generate(numRows))  # Expected: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

    # Test Case 2
    numRows = 1
    print(f"Pascal's Triangle for numRows = {numRows}:")
    print(generate(numRows))  # Expected: [[1]]

    # Test Case 3
    numRows = 3
    print(f"Pascal's Triangle for numRows = {numRows}:")
    print(generate(numRows))  # Expected: [[1], [1,1], [1,2,1]]

"""
Time and Space Complexity Analysis:

Time Complexity:
    - The outer loop runs `numRows` times.
    - The inner loop runs up to `i` times for each row, where `i` is the row index.
    - The total number of operations is approximately 1 + 2 + 3 + ... + numRows = numRows * (numRows + 1) / 2.
    - Therefore, the time complexity is O(numRows^2).

Space Complexity:
    - The space required to store the triangle is proportional to the total number of elements in the triangle.
    - The total number of elements is 1 + 2 + 3 + ... + numRows = numRows * (numRows + 1) / 2.
    - Therefore, the space complexity is O(numRows^2).

Topic: Arrays
"""