"""
LeetCode Problem #764: Largest Plus Sign

Problem Statement:
You are given an integer n. You have an n x n binary grid with all cells initially set to 1. 
You are also given an array mines, where mines[i] = [xi, yi] represents that the cell (xi, yi) 
is set to 0. Return the order of the largest axis-aligned plus sign of 1's contained in the grid. 
If there is no plus sign of 1's, return 0.

An axis-aligned plus sign of 1's of order k has some center cell (r, c) with value 1, and 
1's of order k in the four cardinal directions: up, down, left, and right. You can assume 
that the plus sign is centered within the grid and its arms extend until they reach the 
boundary of the grid or a cell with value 0. 

Example 1:
Input: n = 5, mines = [[4, 2]]
Output: 2
Explanation: The largest plus sign has order 2. One of the order 2 plus signs is centered at grid[2][2].

Example 2:
Input: n = 1, mines = [[0, 0]]
Output: 0
Explanation: There is no plus sign, so return 0.

Constraints:
- 1 <= n <= 500
- 0 <= mines.length <= 5000
- 0 <= xi, yi < n
"""

# Python Solution
def orderOfLargestPlusSign(n: int, mines: list[list[int]]) -> int:
    # Initialize the grid with all 1s
    grid = [[1] * n for _ in range(n)]
    
    # Set cells in mines to 0
    for x, y in mines:
        grid[x][y] = 0
    
    # Create DP arrays for each direction
    left = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    up = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)]
    
    # Fill DP arrays
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1 if j > 0 else 1
                up[i][j] = up[i - 1][j] + 1 if i > 0 else 1
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = right[i][j + 1] + 1 if j < n - 1 else 1
                down[i][j] = down[i + 1][j] + 1 if i < n - 1 else 1
    
    # Calculate the largest plus sign
    max_order = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                max_order = max(max_order, order)
    
    return max_order

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    mines1 = [[4, 2]]
    print(orderOfLargestPlusSign(n1, mines1))  # Output: 2

    # Test Case 2
    n2 = 1
    mines2 = [[0, 0]]
    print(orderOfLargestPlusSign(n2, mines2))  # Output: 0

    # Test Case 3
    n3 = 3
    mines3 = [[0, 0], [0, 1], [1, 0]]
    print(orderOfLargestPlusSign(n3, mines3))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Initializing the grid: O(n^2)
- Setting mines to 0: O(len(mines))
- Filling DP arrays: O(n^2)
- Calculating the largest plus sign: O(n^2)
Overall: O(n^2)

Space Complexity:
- Grid: O(n^2)
- DP arrays (left, right, up, down): O(n^2)
Overall: O(n^2)
"""

# Topic: Dynamic Programming