"""
LeetCode Question #1036: Escape a Large Maze

Problem Statement:
In a 1 million by 1 million grid, you start at the source (0, 0) and want to reach the target (tx, ty). 
There are some blocked cells given as a list of coordinates, where blocked[i] = [xi, yi] indicates that 
cell (xi, yi) is blocked.

You are allowed to move up, down, left, or right, and you cannot move into a blocked cell. Return true 
if and only if it is possible to reach the target from the source without getting stuck in a blocked 
area.

Constraints:
- 0 <= blocked.length <= 200
- blocked[i].length == 2
- 0 <= xi, yi < 10^6
- source.length == 2
- target.length == 2
- 0 <= sx, sy, tx, ty < 10^6
"""

from collections import deque

def isEscapePossible(blocked, source, target):
    """
    Determines if it is possible to escape from the source to the target in a large grid with blocked cells.

    :param blocked: List[List[int]] - List of blocked cells
    :param source: List[int] - Starting cell [sx, sy]
    :param target: List[int] - Target cell [tx, ty]
    :return: bool - True if escape is possible, False otherwise
    """
    # Define the maximum number of cells we can explore before concluding escape is possible
    MAX_EXPLORE = len(blocked) * (len(blocked) - 1) // 2

    # Convert blocked cells to a set for O(1) lookup
    blocked_set = set(map(tuple, blocked))

    def bfs(start, end):
        """
        Perform BFS to check if we can reach the end from the start or explore enough cells to conclude escape is possible.
        """
        queue = deque([start])
        visited = set()
        visited.add(tuple(start))

        while queue:
            x, y = queue.popleft()

            # If we reach the target, return True
            if [x, y] == end:
                return True

            # If we explore more than MAX_EXPLORE cells, conclude escape is possible
            if len(visited) > MAX_EXPLORE:
                return True

            # Explore neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in visited and (nx, ny) not in blocked_set:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        # If we exhaust all possibilities without reaching the target, return False
        return False

    # Perform BFS from source and target
    return bfs(source, target) and bfs(target, source)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Escape is possible
    blocked = [[0, 1], [1, 0]]
    source = [0, 0]
    target = [0, 2]
    print(isEscapePossible(blocked, source, target))  # Output: True

    # Test Case 2: Escape is not possible
    blocked = [[0, 1], [1, 0], [1, 1]]
    source = [0, 0]
    target = [0, 2]
    print(isEscapePossible(blocked, source, target))  # Output: False

    # Test Case 3: No blocked cells, escape is trivially possible
    blocked = []
    source = [0, 0]
    target = [999999, 999999]
    print(isEscapePossible(blocked, source, target))  # Output: True


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The BFS explores up to MAX_EXPLORE cells, where MAX_EXPLORE = len(blocked) * (len(blocked) - 1) // 2.
   - In the worst case, BFS runs twice (once from source and once from target).
   - Therefore, the time complexity is O(MAX_EXPLORE) = O(len(blocked)^2).

2. Space Complexity:
   - The space complexity is dominated by the visited set and the queue used in BFS.
   - Both can grow up to MAX_EXPLORE cells.
   - Therefore, the space complexity is O(MAX_EXPLORE) = O(len(blocked)^2).

Topic: Graph Traversal (BFS)
"""