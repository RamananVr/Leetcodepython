"""
LeetCode Problem #2252: "Count Number of Rectangles Containing Each Point"

Problem Statement:
You are given a 2D array `rectangles` where `rectangles[i] = [li, hi]` indicates that the ith rectangle has a length of `li` and a height of `hi`. You are also given a 2D array `points` where `points[j] = [xj, yj]` is a point with coordinates `(xj, yj)`.

The ith rectangle covers a point `(x, y)` if `0 <= x <= li` and `0 <= y <= hi`. A point is considered "contained" in a rectangle if it lies within the rectangle's boundaries (inclusive).

For each point in `points`, return an array `result` of length `points.length` where `result[j]` is the number of rectangles that contain the jth point.

Example:
Input: rectangles = [[1, 2], [2, 3], [2, 5]], points = [[2, 1], [1, 4]]
Output: [2, 1]

Constraints:
- 1 <= rectangles.length, points.length <= 5 * 10^4
- rectangles[i].length == 2
- 1 <= li, hi <= 10^9
- points[j].length == 2
- 1 <= xj, yj <= 10^9
- All the rectangles are distinct.
- All the points are distinct.
"""

from collections import defaultdict
import bisect

def countRectangles(rectangles, points):
    """
    Function to count the number of rectangles containing each point.

    Args:
    rectangles (List[List[int]]): List of rectangles where each rectangle is represented as [li, hi].
    points (List[List[int]]): List of points where each point is represented as [xj, yj].

    Returns:
    List[int]: A list where the jth element is the number of rectangles containing the jth point.
    """
    # Group rectangles by height
    height_map = defaultdict(list)
    for l, h in rectangles:
        height_map[h].append(l)

    # Sort the lengths for each height
    for h in height_map:
        height_map[h].sort()

    # Sort points by y-coordinate
    sorted_points = sorted((y, x, i) for i, (x, y) in enumerate(points))
    sorted_heights = sorted(height_map.keys())

    result = [0] * len(points)
    active_lengths = []

    # Process points in increasing order of y-coordinate
    j = 0
    for y, x, idx in sorted_points:
        # Add all rectangles with height >= y to active_lengths
        while j < len(sorted_heights) and sorted_heights[j] >= y:
            active_lengths.extend(height_map[sorted_heights[j]])
            j += 1
        active_lengths.sort()

        # Count rectangles containing the point
        result[idx] = len(active_lengths) - bisect.bisect_left(active_lengths, x)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rectangles = [[1, 2], [2, 3], [2, 5]]
    points = [[2, 1], [1, 4]]
    print(countRectangles(rectangles, points))  # Output: [2, 1]

    # Test Case 2
    rectangles = [[1, 1], [2, 2], [3, 3]]
    points = [[1, 1], [2, 2], [3, 3], [4, 4]]
    print(countRectangles(rectangles, points))  # Output: [3, 2, 1, 0]

    # Test Case 3
    rectangles = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(countRectangles(rectangles, points))  # Output: [5, 4, 3, 2, 1]

"""
Time Complexity:
- Sorting the rectangles by height: O(R), where R is the number of rectangles.
- Sorting the points by y-coordinate: O(P log P), where P is the number of points.
- For each point, we perform a binary search on the active lengths: O(P log R).
- Overall: O(R log R + P log P + P log R).

Space Complexity:
- The height_map dictionary stores all rectangle lengths grouped by height: O(R).
- The active_lengths list stores the lengths of rectangles with height >= y: O(R).
- Overall: O(R + P).

Topic: Sorting, Binary Search, Arrays
"""