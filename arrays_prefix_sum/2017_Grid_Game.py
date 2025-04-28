"""
LeetCode Problem #2017: Grid Game

Problem Statement:
You are given a 2D array `grid` of size 2 x n representing a grid of points. You are tasked to play a game with this grid.

The rules of the game are as follows:
1. The first player starts at the top-left corner and moves to the bottom-right corner, collecting all the points in the top row and the bottom row that they pass through.
2. The second player starts at the bottom-left corner and moves to the top-right corner, collecting all the points in the bottom row and the top row that they pass through.
3. Both players cannot pass through the same cell.

The goal is to minimize the maximum points collected by the second player. Return the minimum possible value of the maximum points collected by the second player.

Constraints:
- `grid` is a 2 x n matrix.
- `1 <= n <= 10^5`
- `0 <= grid[i][j] <= 10^9`
"""

# Python Solution
def gridGame(grid):
    n = len(grid[0])
    
    # Prefix sums for the top and bottom rows
    top_prefix = [0] * n
    bottom_prefix = [0] * n
    
    # Calculate prefix sums for the top row
    top_prefix[0] = grid[0][0]
    for i in range(1, n):
        top_prefix[i] = top_prefix[i - 1] + grid[0][i]
    
    # Calculate prefix sums for the bottom row
    bottom_prefix[0] = grid[1][0]
    for i in range(1, n):
        bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
    
    # Initialize the minimum maximum points collected by the second player
    min_max_points = float('inf')
    
    # Iterate through each column to determine the split point
    for i in range(n):
        # Points collected by the second player if the first player stops at column i
        top_remaining = top_prefix[n - 1] - top_prefix[i] if i < n - 1 else 0
        bottom_remaining = bottom_prefix[i - 1] if i > 0 else 0
        
        # Maximum points collected by the second player
        max_points = max(top_remaining, bottom_remaining)
        
        # Update the minimum maximum points
        min_max_points = min(min_max_points, max_points)
    
    return min_max_points

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2, 5, 4], [1, 5, 1]]
    print(gridGame(grid1))  # Expected Output: 4

    # Test Case 2
    grid2 = [[3, 3, 1], [8, 5, 2]]
    print(gridGame(grid2))  # Expected Output: 4

    # Test Case 3
    grid3 = [[1, 3, 1, 15], [1, 3, 3, 1]]
    print(gridGame(grid3))  # Expected Output: 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating prefix sums for the top and bottom rows takes O(n).
- Iterating through each column to determine the split point takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use two arrays (`top_prefix` and `bottom_prefix`) of size n to store prefix sums.
- Overall space complexity: O(n).

Topic: Arrays, Prefix Sum
"""