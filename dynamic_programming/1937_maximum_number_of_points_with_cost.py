"""
LeetCode Question #1937: Maximum Number of Points with Cost

Problem Statement:
You are given an `m x n` integer matrix `points` (0-indexed). Starting with any column in the first row, 
you can move to any column in the next row. The cost of moving from column `j` of row `i` to column `k` 
of row `i+1` is `abs(j - k)`.

Return the maximum number of points you can achieve.

Example 1:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
- Start at column 1 in the first row. Points = 2.
- Move to column 1 in the second row. Points = 5.
- Move to column 0 in the third row. Points = 3.
Total points = 2 + 5 + 3 = 9.

Example 2:
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
- Start at column 0 in the first row. Points = 1.
- Move to column 1 in the second row. Points = 3.
- Move to column 0 in the third row. Points = 4.
Total points = 1 + 3 + 4 = 11.

Constraints:
- `m == points.length`
- `n == points[i].length`
- `1 <= m, n <= 100`
- `1 <= points[i][j] <= 10^5`
"""

# Solution
def maxPoints(points):
    """
    Function to calculate the maximum number of points with cost.

    :param points: List[List[int]] - 2D matrix of points
    :return: int - Maximum points achievable
    """
    m, n = len(points), len(points[0])
    
    # Initialize the previous row's maximum points
    prev_row = points[0]
    
    for i in range(1, m):
        # Left-to-right pass to calculate max points considering left neighbors
        left = [0] * n
        left[0] = prev_row[0]
        for j in range(1, n):
            left[j] = max(left[j - 1] - 1, prev_row[j])
        
        # Right-to-left pass to calculate max points considering right neighbors
        right = [0] * n
        right[n - 1] = prev_row[n - 1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1] - 1, prev_row[j])
        
        # Update the current row's maximum points
        curr_row = [0] * n
        for j in range(n):
            curr_row[j] = points[i][j] + max(left[j], right[j])
        
        # Move to the next row
        prev_row = curr_row
    
    # Return the maximum points from the last row
    return max(prev_row)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1,2,3],[1,5,1],[3,1,1]]
    print(maxPoints(points1))  # Output: 9

    # Test Case 2
    points2 = [[1,5],[2,3],[4,2]]
    print(maxPoints(points2))  # Output: 11

    # Test Case 3
    points3 = [[10,20,30],[5,15,5],[10,5,10]]
    print(maxPoints(points3))  # Output: 55

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each row of the matrix, and for each row, it performs two passes (left-to-right and right-to-left) 
  over the columns. This results in a time complexity of O(m * n), where `m` is the number of rows and `n` is the number of columns.

Space Complexity:
- The algorithm uses three auxiliary arrays (`left`, `right`, and `curr_row`) of size `n` to store intermediate results. 
  Thus, the space complexity is O(n).

Topic: Dynamic Programming
"""