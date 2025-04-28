"""
LeetCode Problem #1139: Largest 1-Bordered Square

Problem Statement:
Given a 2D grid of 0s and 1s, return the size of the largest 1-bordered square in the grid. 
A 1-bordered square has all its borders consisting only of 1s. If there is no 1-bordered square, return 0.

Example:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Explanation: The largest 1-bordered square has a size of 3x3.

Constraints:
- 1 <= grid.length <= 100
- 1 <= grid[0].length <= 100
- grid[i][j] is 0 or 1.
"""

def largest1BorderedSquare(grid):
    """
    Finds the size of the largest 1-bordered square in the grid.

    :param grid: List[List[int]] - 2D grid of 0s and 1s
    :return: int - area of the largest 1-bordered square
    """
    rows, cols = len(grid), len(grid[0])
    
    # Precompute horizontal and vertical prefix sums
    hor = [[0] * cols for _ in range(rows)]
    ver = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                hor[i][j] = hor[i][j - 1] + 1 if j > 0 else 1
                ver[i][j] = ver[i - 1][j] + 1 if i > 0 else 1
    
    max_side = 0
    
    # Iterate over all possible bottom-right corners of squares
    for i in range(rows):
        for j in range(cols):
            # Check for the largest possible square with (i, j) as the bottom-right corner
            side = min(hor[i][j], ver[i][j])
            while side > max_side:
                if ver[i][j - side + 1] >= side and hor[i - side + 1][j] >= side:
                    max_side = side
                side -= 1
    
    return max_side * max_side

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(largest1BorderedSquare(grid1))  # Output: 9

    # Test Case 2
    grid2 = [[1, 1, 0, 0]]
    print(largest1BorderedSquare(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(largest1BorderedSquare(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[0, 0], [0, 0]]
    print(largest1BorderedSquare(grid4))  # Output: 0

    # Test Case 5
    grid5 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    print(largest1BorderedSquare(grid5))  # Output: 16

"""
Time Complexity:
- Precomputing the horizontal and vertical prefix sums takes O(rows * cols).
- Checking all possible squares takes O(rows * cols * min(rows, cols)) in the worst case.
- Overall time complexity: O(rows * cols * min(rows, cols)).

Space Complexity:
- The space used for the `hor` and `ver` arrays is O(rows * cols).
- Overall space complexity: O(rows * cols).

Topic: Dynamic Programming (DP), Prefix Sum
"""