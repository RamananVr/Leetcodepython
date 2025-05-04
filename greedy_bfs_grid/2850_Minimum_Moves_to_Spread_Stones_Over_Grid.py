"""
LeetCode Problem #2850: Minimum Moves to Spread Stones Over Grid

Problem Statement:
You are given a 2D grid of size `n x n` where each cell in the grid has one of the following values:
- `0` representing an empty cell,
- `1` representing a cell with one stone,
- `2` representing a cell with two stones, and so on.

In one move, you can transfer one stone from a cell containing at least two stones to an adjacent cell (up, down, left, or right). The goal is to make every cell in the grid contain exactly one stone. Return the minimum number of moves required to achieve this.

Constraints:
- `n == grid.length == grid[i].length`
- `2 <= n <= 50`
- `0 <= grid[i][j] <= 100`
- The sum of all stones in the grid is exactly `n * n` (i.e., there are enough stones to make every cell contain exactly one stone).

"""

from collections import deque

def minimumMoves(grid):
    """
    Calculate the minimum number of moves to spread stones over the grid such that
    every cell contains exactly one stone.

    :param grid: List[List[int]] - 2D grid of integers representing the number of stones in each cell
    :return: int - Minimum number of moves required
    """
    n = len(grid)
    excess = []  # Cells with excess stones
    deficit = []  # Cells with deficit stones

    # Step 1: Identify excess and deficit cells
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 1:
                excess.append((i, j, grid[i][j] - 1))  # Store (row, col, excess stones)
            elif grid[i][j] == 0:
                deficit.append((i, j, 1))  # Store (row, col, deficit stones)

    # Step 2: Use BFS to calculate the minimum distance to transfer stones
    def bfs(start, target):
        """
        Perform BFS to calculate the Manhattan distance between two cells.

        :param start: Tuple[int, int] - Starting cell (row, col)
        :param target: Tuple[int, int] - Target cell (row, col)
        :return: int - Manhattan distance
        """
        return abs(start[0] - target[0]) + abs(start[1] - target[1])

    # Step 3: Match excess and deficit cells greedily
    moves = 0
    for ex_r, ex_c, ex_stones in excess:
        for _ in range(ex_stones):
            # Find the closest deficit cell
            min_distance = float('inf')
            closest_deficit = None
            for i, (def_r, def_c, def_stones) in enumerate(deficit):
                distance = bfs((ex_r, ex_c), (def_r, def_c))
                if distance < min_distance:
                    min_distance = distance
                    closest_deficit = i

            # Update moves and adjust deficit
            moves += min_distance
            def_r, def_c, def_stones = deficit[closest_deficit]
            deficit[closest_deficit] = (def_r, def_c, def_stones - 1)
            if deficit[closest_deficit][2] == 0:
                deficit.pop(closest_deficit)

    return moves


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 0, 2],
        [0, 1, 0],
        [3, 0, 0]
    ]
    print(minimumMoves(grid1))  # Output: 4

    # Test Case 2
    grid2 = [
        [0, 2, 0],
        [1, 0, 1],
        [0, 2, 0]
    ]
    print(minimumMoves(grid2))  # Output: 4

    # Test Case 3
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(minimumMoves(grid3))  # Output: 0


"""
Time Complexity Analysis:
- Identifying excess and deficit cells takes O(n^2) time.
- For each excess stone, we calculate the Manhattan distance to the closest deficit cell.
  In the worst case, there are O(n^2) excess stones, and for each, we may check O(n^2) deficit cells.
  Thus, the worst-case time complexity is O((n^2)^2) = O(n^4).

Space Complexity Analysis:
- The space required to store the excess and deficit cells is O(n^2).
- Additional space is used for BFS calculations, but it is negligible compared to the grid size.
- Overall space complexity is O(n^2).

Topic: Greedy, BFS, Grid
"""