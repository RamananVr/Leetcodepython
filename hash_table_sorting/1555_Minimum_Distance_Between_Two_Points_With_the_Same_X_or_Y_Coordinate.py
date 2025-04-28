"""
LeetCode Problem #1555: Minimum Distance Between Two Points With the Same X or Y Coordinate

Problem Statement:
Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, 
return the minimum Manhattan distance between any two points with the same x-coordinate 
or the same y-coordinate. If no two points share the same x or y coordinate, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is defined as:
    |x1 - x2| + |y1 - y2|.

Constraints:
1. 2 <= points.length <= 10^4
2. points[i].length == 2
3. 0 <= xi, yi <= 10^9

Example:
Input: points = [[1,2],[1,3],[3,4],[2,3],[4,4]]
Output: 1
Explanation: The points (1,2) and (1,3) share the same x-coordinate. Their Manhattan distance is |2-3| = 1, which is the minimum.

Input: points = [[3,4],[1,2],[4,4],[2,3]]
Output: -1
Explanation: No two points share the same x or y coordinate.

Follow-up: Can you solve the problem in O(n log n) time complexity?
"""

from collections import defaultdict

def min_manhattan_distance(points):
    """
    Finds the minimum Manhattan distance between any two points with the same x-coordinate
    or the same y-coordinate.

    :param points: List[List[int]] - List of points on the X-Y plane
    :return: int - Minimum Manhattan distance or -1 if no two points share the same x or y coordinate
    """
    # Dictionaries to store points grouped by x and y coordinates
    x_map = defaultdict(list)
    y_map = defaultdict(list)

    # Group points by their x and y coordinates
    for x, y in points:
        x_map[x].append(y)
        y_map[y].append(x)

    # Function to calculate the minimum distance for a given map
    def calculate_min_distance(coord_map):
        min_distance = float('inf')
        for key in coord_map:
            # Sort the points along the same coordinate
            coord_map[key].sort()
            # Calculate the minimum distance between consecutive points
            for i in range(1, len(coord_map[key])):
                min_distance = min(min_distance, coord_map[key][i] - coord_map[key][i - 1])
        return min_distance

    # Calculate the minimum distance for x and y coordinates
    min_x_distance = calculate_min_distance(x_map)
    min_y_distance = calculate_min_distance(y_map)

    # Get the overall minimum distance
    result = min(min_x_distance, min_y_distance)

    # If no valid distance was found, return -1
    return result if result != float('inf') else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 2], [1, 3], [3, 4], [2, 3], [4, 4]]
    print(min_manhattan_distance(points1))  # Output: 1

    # Test Case 2
    points2 = [[3, 4], [1, 2], [4, 4], [2, 3]]
    print(min_manhattan_distance(points2))  # Output: -1

    # Test Case 3
    points3 = [[1, 1], [1, 5], [1, 10], [2, 2], [2, 8]]
    print(min_manhattan_distance(points3))  # Output: 3

    # Test Case 4
    points4 = [[1, 1], [2, 2], [3, 3]]
    print(min_manhattan_distance(points4))  # Output: -1


"""
Time Complexity Analysis:
- Grouping points by x and y coordinates takes O(n), where n is the number of points.
- Sorting the points for each x or y coordinate takes O(k log k) for each group, where k is the size of the group.
  In the worst case, this is O(n log n) if all points share the same x or y coordinate.
- Calculating the minimum distance for each group is O(k) for each group, which is O(n) in total.
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The space required for the x_map and y_map dictionaries is O(n) in the worst case.
- Overall space complexity: O(n).

Topic: Hash Table, Sorting
"""