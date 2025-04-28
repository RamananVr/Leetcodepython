"""
LeetCode Problem #1728: Cat and Mouse II

Problem Statement:
A game is played by a cat and a mouse named Cat and Mouse. The environment is represented by a grid of size m x n, where each element is a wall, floor, player (Cat, Mouse), or food.

- Players are represented by the characters 'C' (Cat), 'M' (Mouse).
- Floors are represented by the character '.'.
- Walls are represented by the character '#'.
- Food is represented by the character 'F'.

The players can move in four directions: up, down, left, and right. During each turn:
- The Mouse moves first, followed by the Cat.
- If the Mouse reaches the food, it wins.
- If the Cat catches the Mouse, the Cat wins.
- If both players are unable to move, the Cat wins.

The Cat cannot move to the Mouse's starting position, and the Mouse cannot move to the Cat's starting position. Additionally, players cannot move into walls.

Given a grid, and two integers catJump and mouseJump that represent the maximum number of cells the Cat and Mouse can jump in one move, return true if the Mouse can win the game if both players play optimally, otherwise return false.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 8
- grid[i][j] consists of characters 'C', 'M', 'F', '.', and '#'.
- There is exactly one 'C', one 'M', and one 'F' in grid.
- 1 <= catJump, mouseJump <= 8
"""

from collections import deque

def canMouseWin(grid, catJump, mouseJump):
    def neighbors(x, y, jump, rows, cols):
        """Generate all valid neighbors for a given position."""
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for step in range(1, jump + 1):
                nx, ny = x + dx * step, y + dy * step
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                    yield nx, ny
                else:
                    break

    rows, cols = len(grid), len(grid[0])
    mouse_start = cat_start = food = None

    # Parse the grid to find the starting positions of Mouse, Cat, and Food
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'M':
                mouse_start = (r, c)
            elif grid[r][c] == 'C':
                cat_start = (r, c)
            elif grid[r][c] == 'F':
                food = (r, c)

    # State: (mouse_x, mouse_y, cat_x, cat_y, turn)
    # turn = 0 -> Mouse's turn, turn = 1 -> Cat's turn
    queue = deque()
    dp = {}

    # Initialize the queue with terminal states
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(rows):
                for c2 in range(cols):
                    for turn in range(2):
                        if (r1, c1) == food:
                            dp[(r1, c1, r2, c2, turn)] = True  # Mouse wins
                        elif (r2, c2) == food or (r1, c1) == (r2, c2):
                            dp[(r1, c1, r2, c2, turn)] = False  # Cat wins
                        else:
                            dp[(r1, c1, r2, c2, turn)] = None

    # BFS to determine the outcome of all states
    while queue:
        mouse_x, mouse_y, cat_x, cat_y, turn = queue.popleft()
        if dp[(mouse_x, mouse_y, cat_x, cat_y, turn)] is not None:
            continue

        if turn == 0:  # Mouse's turn
            for nx, ny in neighbors(mouse_x, mouse_y, mouseJump, rows, cols):
                if dp[(nx, ny, cat_x, cat_y, 1)] == False:
                    dp[(mouse_x, mouse_y, cat_x, cat_y, turn)] = True
                    break
            else:
                dp[(mouse_x, mouse_y, cat_x, cat_y, turn)] = False
        else:  # Cat's turn
            for nx, ny in neighbors(cat_x, cat_y, catJump, rows, cols):
                if dp[(mouse_x, mouse_y, nx, ny, 0)] == True:
                    dp[(mouse_x, mouse_y, cat_x, cat_y, turn)] = False
                    break
            else:
                dp[(mouse_x, mouse_y, cat_x, cat_y, turn)] = True

    return dp[(mouse_start[0], mouse_start[1], cat_start[0], cat_start[1], 0)]


# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        "####F",
        "#C...",
        "M...."
    ]
    catJump1 = 1
    mouseJump1 = 2
    print(canMouseWin(grid1, catJump1, mouseJump1))  # Output: True

    grid2 = [
        "M.C...",
        "####F."
    ]
    catJump2 = 1
    mouseJump2 = 4
    print(canMouseWin(grid2, catJump2, mouseJump2))  # Output: True

    grid3 = [
        "C...#",
        "...#F",
        "M...."
    ]
    catJump3 = 2
    mouseJump3 = 5
    print(canMouseWin(grid3, catJump3, mouseJump3))  # Output: False


# Time Complexity Analysis:
# The grid has at most 8x8 cells, and there are at most 2 players with 2 turns.
# The total number of states is O((m * n)^2 * 2), where m and n are the grid dimensions.
# For each state, we explore up to O(max(catJump, mouseJump)) moves.
# Thus, the time complexity is O((m * n)^2 * max(catJump, mouseJump)).

# Space Complexity Analysis:
# The space complexity is O((m * n)^2 * 2) for the dp table.

# Topic: Graph, BFS, Game Theory