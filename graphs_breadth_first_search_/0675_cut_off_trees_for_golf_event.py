"""
LeetCode Question #675: Cut Off Trees for Golf Event

Problem Statement:
You are asked to cut off trees in a forest for a golf event. The forest is represented as a 2D grid, where:
- `forest[i][j]` is the height of the tree at position `(i, j)`.
- A value of `0` represents an obstacle that you cannot pass through.
- A value of `1` represents ground that you can walk on.

You can move up, down, left, or right, and you must cut off the trees in order of their height (ascending order). After cutting a tree, the cell becomes `1` (ground).

Return the minimum steps required to cut off all the trees in the forest. If it is impossible to cut off all the trees, return `-1`.

Constraints:
- `1 <= forest.length <= 50`
- `1 <= forest[i].length <= 50`
- `0 <= forest[i][j] <= 10^9`

"""

from collections import deque

def cutOffTree(forest):
    """
    Function to calculate the minimum steps required to cut off all trees in the forest.
    :param forest: List[List[int]] - 2D grid representing the forest.
    :return: int - Minimum steps required to cut off all trees, or -1 if impossible.
    """
    def bfs(start, target):
        """
        Perform BFS to find the shortest path from start to target.
        :param start: Tuple[int, int] - Starting position (x, y).
        :param target: Tuple[int, int] - Target position (x, y).
        :return: int - Minimum steps to reach target, or -1 if unreachable.
        """
        rows, cols = len(forest), len(forest[0])
        visited = set()
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
        visited.add(start)
        
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == target:
                return steps
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and forest[nx][ny] > 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        
        return -1

    # Extract all trees with their heights and positions
    trees = sorted((height, x, y) for x, row in enumerate(forest) for y, height in enumerate(row) if height > 1)
    
    # Start from (0, 0)
    start = (0, 0)
    total_steps = 0
    
    for _, x, y in trees:
        steps = bfs(start, (x, y))
        if steps == -1:
            return -1
        total_steps += steps
        start = (x, y)  # Move to the current tree's position
    
    return total_steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    forest1 = [
        [1, 2, 3],
        [0, 0, 4],
        [7, 6, 5]
    ]
    print(cutOffTree(forest1))  # Expected Output: 6

    # Test Case 2
    forest2 = [
        [1, 2, 3],
        [0, 0, 0],
        [7, 6, 5]
    ]
    print(cutOffTree(forest2))  # Expected Output: -1

    # Test Case 3
    forest3 = [
        [1, 2, 3],
        [0, 0, 4],
        [7, 0, 5]
    ]
    print(cutOffTree(forest3))  # Expected Output: 8

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting the trees: O(m * n * log(m * n)), where m is the number of rows and n is the number of columns.
   - BFS for each tree: O(m * n) in the worst case.
   - Total: O(m * n * log(m * n) + k * m * n), where k is the number of trees.
   - In the worst case, k = m * n, so the complexity is O(m * n * log(m * n)).

2. Space Complexity:
   - BFS uses a queue and a visited set, both of which can store up to O(m * n) elements.
   - Total: O(m * n).

Topic: Graphs (Breadth-First Search)
"""