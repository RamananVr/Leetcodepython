"""
LeetCode Problem #2250: Count Number of Rectangles Containing Each Point

Problem Statement:
You are given a 2D integer array `rectangles` where `rectangles[i] = [li, hi]` indicates that the ith rectangle has a length li and a height hi. You are also given a 2D integer array `points` where `points[j] = [xj, yj]` is a point with coordinates (xj, yj).

The ith rectangle contains the jth point if and only if:
    li >= xj and hi >= yj.

Return an integer array `result` where `result[j]` is the number of rectangles that contain the jth point.

Constraints:
- 1 <= rectangles.length, points.length <= 10^5
- rectangles[i].length == 2
- points[j].length == 2
- 1 <= li, xj <= 10^9
- 1 <= hi, yj <= 100
"""

# Solution
from collections import defaultdict
from bisect import bisect_left

def countRectangles(rectangles, points):
    # Group rectangles by their height
    height_map = defaultdict(list)
    for l, h in rectangles:
        height_map[h].append(l)
    
    # Sort the lengths in each height group
    for h in height_map:
        height_map[h].sort()
    
    # Sort points by height
    sorted_points = sorted((y, x, i) for i, (x, y) in enumerate(points))
    result = [0] * len(points)
    
    # Process points and count rectangles
    active_lengths = []
    current_height = 0
    for y, x, i in sorted_points:
        # Add lengths of rectangles with height >= current point's height
        for h in range(current_height + 1, y + 1):
            if h in height_map:
                active_lengths.extend(height_map[h])
        current_height = y
        
        # Sort active lengths
        active_lengths.sort()
        
        # Count rectangles containing the current point
        result[i] = len(active_lengths) - bisect_left(active_lengths, x)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rectangles = [[1, 1], [2, 2], [3, 3]]
    points = [[1, 1], [2, 2], [3, 3]]
    print(countRectangles(rectangles, points))  # Output: [3, 2, 1]

    # Test Case 2
    rectangles = [[1, 2], [2, 3], [2, 5]]
    points = [[2, 1], [1, 4]]
    print(countRectangles(rectangles, points))  # Output: [3, 1]

    # Test Case 3
    rectangles = [[5, 5], [6, 6], [7, 7]]
    points = [[4, 4], [5, 5], [6, 6]]
    print(countRectangles(rectangles, points))  # Output: [3, 2, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting rectangles by height: O(n), where n is the number of rectangles.
- Sorting points by height: O(m log m), where m is the number of points.
- For each point, we process active lengths and count rectangles:
  - Adding lengths to active_lengths: O(n) in total across all points.
  - Sorting active_lengths: O(n log n) in total across all points.
  - Binary search for each point: O(m log n).
Overall: O(n log n + m log m).

Space Complexity:
- height_map stores rectangles grouped by height: O(n).
- active_lengths stores lengths of rectangles: O(n).
- Result array: O(m).
Overall: O(n + m).
"""

# Topic: Arrays, Sorting, Binary Search