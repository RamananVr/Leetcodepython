"""
LeetCode Problem #1219: Path with Maximum Gold

Problem Statement:
In a gold mine grid of size m x n, each cell in this grid has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the following rules:
1. Every time you are located in a cell, you will collect all the gold in that cell.
2. From your position, you can walk one step to the left, right, up, or down.
3. You can't visit the same cell more than once.
4. Never visit a cell with 0 gold.
5. You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0]]
Path to get the maximum gold, 7 -> 6 -> 5 -> 4 -> 3 -> 3.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 15
- 0 <= grid[i][j] <= 100
- There are at most 25 cells containing gold.
"""

def getMaximumGold(grid):
    """
    Function to calculate the maximum amount of gold that can be collected.
    :param grid: List[List[int]] - 2D grid representing the gold mine.
    :return: int - Maximum gold that can be collected.
    """
    def dfs(x, y, current_gold):
        nonlocal max_gold
        # Update the maximum gold collected so far
        max_gold = max(max_gold, current_gold)
        
        # Save the current cell's gold and mark it as visited
        original_gold = grid[x][y]
        grid[x][y] = 0
        
        # Explore all 4 possible directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                dfs(nx, ny, current_gold + grid[nx][ny])
        
        # Backtrack: Restore the cell's gold
        grid[x][y] = original_gold

    max_gold = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:  # Start DFS from cells with gold
                dfs(i, j, grid[i][j])
    
    return max_gold

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0,6,0],[5,8,7],[0,9,0]]
    print(getMaximumGold(grid1))  # Output: 24

    # Test Case 2
    grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0]]
    print(getMaximumGold(grid2))  # Output: 28

    # Test Case 3
    grid3 = [[0,0,0],[0,0,0],[0,0,0]]
    print(getMaximumGold(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[10]]
    print(getMaximumGold(grid4))  # Output: 10

"""
Time Complexity:
- The DFS function explores all possible paths starting from each cell with gold.
- In the worst case, we visit each cell with gold and explore all possible paths, leading to a time complexity of O(4^k), where k is the number of cells with gold (at most 25).

Space Complexity:
- The space complexity is O(k) due to the recursion stack, where k is the number of cells with gold.

Topic: Backtracking
"""