"""
LeetCode Problem #1591: Strange Printer II

Problem Statement:
There is a strange printer with the following two special properties:
1. The printer can only print a sequence of the same color in each operation.
2. At each turn, the printer can print new colors over the existing colors.

You are given a 2D grid `targetGrid` where `targetGrid[row][col]` is the color in the cell `(row, col)`.

Return `true` if it is possible to print the grid using the printer, otherwise return `false`.

Constraints:
- `m == targetGrid.length`
- `n == targetGrid[i].length`
- `1 <= m, n <= 60`
- `1 <= targetGrid[row][col] <= 60`
"""

from collections import defaultdict, deque

def isPrintable(targetGrid):
    """
    Determines if the target grid can be printed using the strange printer.

    :param targetGrid: List[List[int]] - The target grid to be printed.
    :return: bool - True if the grid can be printed, False otherwise.
    """
    m, n = len(targetGrid), len(targetGrid[0])
    color_bounds = defaultdict(lambda: [float('inf'), float('-inf'), float('inf'), float('-inf')])

    # Step 1: Determine the bounding box for each color
    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            color_bounds[color][0] = min(color_bounds[color][0], i)  # top
            color_bounds[color][1] = max(color_bounds[color][1], i)  # bottom
            color_bounds[color][2] = min(color_bounds[color][2], j)  # left
            color_bounds[color][3] = max(color_bounds[color][3], j)  # right

    # Step 2: Build a graph of dependencies between colors
    graph = defaultdict(set)
    indegree = defaultdict(int)

    for color, (top, bottom, left, right) in color_bounds.items():
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if targetGrid[i][j] != color:
                    graph[color].add(targetGrid[i][j])

    # Step 3: Calculate indegrees for topological sorting
    for color in graph:
        for neighbor in graph[color]:
            indegree[neighbor] += 1

    # Step 4: Perform topological sort
    queue = deque([color for color in color_bounds if indegree[color] == 0])
    printed_colors = 0

    while queue:
        current = queue.popleft()
        printed_colors += 1
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If we printed all colors, return True; otherwise, return False
    return printed_colors == len(color_bounds)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    targetGrid1 = [
        [1, 1, 1, 1],
        [1, 2, 2, 1],
        [1, 2, 2, 1],
        [1, 1, 1, 1]
    ]
    print(isPrintable(targetGrid1))  # Expected Output: True

    # Test Case 2
    targetGrid2 = [
        [1, 1, 1],
        [3, 1, 3],
        [3, 3, 3]
    ]
    print(isPrintable(targetGrid2))  # Expected Output: False

    # Test Case 3
    targetGrid3 = [
        [1, 2, 2],
        [2, 2, 2],
        [2, 2, 1]
    ]
    print(isPrintable(targetGrid3))  # Expected Output: True


"""
Time Complexity Analysis:
- Determining the bounding box for each color: O(m * n), where m and n are the dimensions of the grid.
- Building the graph of dependencies: O(m * n), as we iterate over the bounding boxes.
- Topological sorting: O(V + E), where V is the number of colors and E is the number of dependencies.
Overall: O(m * n + V + E), which is efficient given the constraints.

Space Complexity Analysis:
- Space for color bounds: O(C), where C is the number of unique colors (at most 60).
- Space for the graph and indegree: O(C + E).
Overall: O(C + E), which is efficient given the constraints.

Topic: Graphs, Topological Sort
"""