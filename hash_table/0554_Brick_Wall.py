"""
LeetCode Problem #554: Brick Wall

Problem Statement:
There is a rectangular brick wall in front of you with `n` rows of bricks. The ith row has some number of bricks each of the same height (but they can be of different widths). The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You want to find out how to draw the line such that it crosses the least number of bricks.

You are given a list `wall` that contains `n` rows. Each row is a list of integers representing the widths of each brick in that row from left to right.

Return the minimum number of crossed bricks after drawing such a vertical line.

Constraints:
- `n == len(wall)`
- `1 <= n <= 10^4`
- `1 <= len(wall[i]) <= 10^4`
- `1 <= sum(wall[i]) <= 2 * 10^4`
- `1 <= wall[i][j] <= 2^31 - 1`
- The width of each row is the same.

Example:
Input: wall = [[1,2,2,1],
               [3,1,2],
               [1,3,2],
               [2,4],
               [3,1,2],
               [1,3,1,1]]
Output: 2

Explanation:
The best place to draw the line is after the second brick in the first row, which will cross only two bricks in total.
"""

from collections import defaultdict

def leastBricks(wall):
    """
    Finds the minimum number of bricks a vertical line crosses in the given wall.

    :param wall: List[List[int]] - A list of rows where each row is a list of brick widths.
    :return: int - The minimum number of bricks crossed.
    """
    edge_count = defaultdict(int)

    # Count the number of edges at each position
    for row in wall:
        position = 0
        # Exclude the last brick in each row to avoid counting the wall's edge
        for brick in row[:-1]:
            position += brick
            edge_count[position] += 1

    # If no edges are found, the line crosses all rows
    max_edges = max(edge_count.values(), default=0)
    return len(wall) - max_edges


# Example Test Cases
if __name__ == "__main__":
    wall1 = [[1, 2, 2, 1],
             [3, 1, 2],
             [1, 3, 2],
             [2, 4],
             [3, 1, 2],
             [1, 3, 1, 1]]
    print(leastBricks(wall1))  # Output: 2

    wall2 = [[1], [1], [1]]
    print(leastBricks(wall2))  # Output: 3

    wall3 = [[1, 1], [2], [1, 1]]
    print(leastBricks(wall3))  # Output: 0

    wall4 = [[1, 2, 3], [3, 3], [6]]
    print(leastBricks(wall4))  # Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the number of rows in the wall and `m` be the average number of bricks per row.
- Iterating through the wall takes O(n * m) time since we process each brick once.
- Updating the `edge_count` dictionary is O(1) per brick, so the total time complexity is O(n * m).

Space Complexity:
- The `edge_count` dictionary stores at most `sum(wall[i])` keys, which is the total width of the wall.
- In the worst case, the space complexity is O(W), where W is the total width of the wall.

Topic: Hash Table
"""