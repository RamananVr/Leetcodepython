"""
LeetCode Problem #573: Squirrel Simulation

Problem Statement:
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to minimize the distance the squirrel needs to collect all the nuts and put them under the tree.

The squirrel can only carry one nut at a time and must return to the tree after collecting each nut. The squirrel starts at a given position.

You are given the following:
- `height` and `width` of the grid.
- `tree` position as a list `[tree_x, tree_y]`.
- `squirrel` position as a list `[squirrel_x, squirrel_y]`.
- `nuts` positions as a list of lists, where each nut's position is `[nut_x, nut_y]`.

Return the minimum distance the squirrel needs to collect all the nuts and put them under the tree.

Constraints:
- 1 <= height, width <= 10000
- The number of nuts is between 1 and 1000.
- `tree`, `squirrel`, and `nuts` positions are valid and within the grid.

"""

# Python Solution
def minDistance(height, width, tree, squirrel, nuts):
    def distance(point1, point2):
        """Calculate Manhattan distance between two points."""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    # Total distance if the squirrel starts collecting nuts from the tree
    total_tree_distance = sum(2 * distance(tree, nut) for nut in nuts)

    # Find the first nut to minimize the extra distance
    min_extra_distance = float('inf')
    for nut in nuts:
        squirrel_to_nut = distance(squirrel, nut)
        nut_to_tree = distance(nut, tree)
        extra_distance = squirrel_to_nut - nut_to_tree
        min_extra_distance = min(min_extra_distance, extra_distance)

    return total_tree_distance + min_extra_distance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    height = 5
    width = 7
    tree = [2, 2]
    squirrel = [4, 4]
    nuts = [[3, 0], [2, 5], [1, 1]]
    print(minDistance(height, width, tree, squirrel, nuts))  # Expected Output: 18

    # Test Case 2
    height = 10
    width = 10
    tree = [5, 5]
    squirrel = [0, 0]
    nuts = [[1, 1], [9, 9], [6, 6]]
    print(minDistance(height, width, tree, squirrel, nuts))  # Expected Output: 40

    # Test Case 3
    height = 3
    width = 3
    tree = [1, 1]
    squirrel = [0, 0]
    nuts = [[0, 2], [2, 0]]
    print(minDistance(height, width, tree, squirrel, nuts))  # Expected Output: 8


# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the total tree distance takes O(n), where n is the number of nuts.
- Calculating the minimum extra distance involves iterating over all nuts, which is O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store distances and do not use any additional data structures.

"""

# Topic: Greedy Algorithm