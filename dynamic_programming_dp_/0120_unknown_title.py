"""
LeetCode Problem #120: Triangle

Problem Statement:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i-1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

Follow-up:
Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""

# Solution
def minimumTotal(triangle):
    """
    Function to calculate the minimum path sum in a triangle.

    :param triangle: List[List[int]] - A list of lists representing the triangle.
    :return: int - The minimum path sum from top to bottom.
    """
    # Start from the second-to-last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current cell with the minimum path sum
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element contains the minimum path sum
    return triangle[0][0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minimumTotal(triangle1))  # Output: 11

    # Test Case 2
    triangle2 = [[-10]]
    print(minimumTotal(triangle2))  # Output: -10

    # Test Case 3
    triangle3 = [[1],[2,3],[3,6,7],[4,5,6,7]]
    print(minimumTotal(triangle3))  # Output: 10

    # Test Case 4
    triangle4 = [[1],[2,3],[4,5,6],[7,8,9,10]]
    print(minimumTotal(triangle4))  # Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each row of the triangle from bottom to top.
- For each row, it processes all elements in that row.
- The total number of elements in the triangle is approximately n(n+1)/2, where n is the number of rows.
- Therefore, the time complexity is O(n^2), where n is the number of rows.

Space Complexity:
- The algorithm modifies the input triangle in place, so no additional space is used.
- The space complexity is O(1) if we disregard the input triangle, or O(n^2) if we count the input triangle.

Topic: Dynamic Programming (DP)
"""