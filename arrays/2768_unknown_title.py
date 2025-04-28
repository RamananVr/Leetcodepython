"""
LeetCode Problem #2768: Number of Black Blocks

Problem Statement:
You are given a 2D grid of size `m x n` consisting of cells with values 0 (white) or 1 (black). 
A block is defined as a 2x2 subgrid of the grid. A block is considered "black" if all four cells 
in the block are black (i.e., have a value of 1). Your task is to count the number of black blocks 
in the grid.

Write a function `countBlackBlocks(grid: List[List[int]]) -> int` that takes the grid as input and 
returns the number of black blocks in the grid.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 100`
- `grid[i][j]` is either 0 or 1.
"""

from typing import List

def countBlackBlocks(grid: List[List[int]]) -> int:
    """
    Counts the number of black 2x2 blocks in the given grid.

    Args:
    - grid (List[List[int]]): A 2D grid of integers (0 or 1).

    Returns:
    - int: The number of black 2x2 blocks.
    """
    m, n = len(grid), len(grid[0])
    black_blocks = 0

    # Iterate through all possible 2x2 subgrids
    for i in range(m - 1):
        for j in range(n - 1):
            # Check if the 2x2 block is completely black
            if grid[i][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1:
                black_blocks += 1

    return black_blocks

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print(countBlackBlocks(grid1))  # Output: 1

    # Test Case 2
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(countBlackBlocks(grid2))  # Output: 4

    # Test Case 3
    grid3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(countBlackBlocks(grid3))  # Output: 0

    # Test Case 4
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    print(countBlackBlocks(grid4))  # Output: 1

    # Test Case 5
    grid5 = [
        [1, 0],
        [0, 1]
    ]
    print(countBlackBlocks(grid5))  # Output: 0

"""
Time Complexity:
- The function iterates through all possible 2x2 subgrids in the grid.
- There are (m-1) * (n-1) such subgrids, where m and n are the dimensions of the grid.
- Checking each subgrid takes O(1) time.
- Therefore, the overall time complexity is O(m * n).

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""