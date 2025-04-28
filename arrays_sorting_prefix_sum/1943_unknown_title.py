"""
LeetCode Problem #1943: Describe the Painting

Problem Statement:
There is a long and narrow painting that can be represented as a number line. The painting starts at point 0 and ends at point 10^9. You are given a 2D integer array `segments`, where `segments[i] = [start_i, end_i, color_i]` describes the painting of a segment of the number line from `start_i` to `end_i` with the color `color_i`.

The colors in the segments can overlap. When two segments overlap, the resulting color of the overlapping part is the sum of the colors of the overlapping segments. For example, if a segment of color 4 overlaps with a segment of color 7, then the resulting color of the overlapping part is 4 + 7 = 11.

Return a 2D array `result` of the form `[start, end, color]` describing the resulting painting. The `result` should be sorted by `start` in ascending order, and if two or more segments have the same `start`, they should be sorted by `end` in ascending order. Also, the segments in the `result` should not overlap (i.e., the end of one segment should be equal to the start of the next segment).

Constraints:
- `1 <= segments.length <= 10^5`
- `0 <= start_i < end_i <= 10^9`
- `1 <= color_i <= 10^4`
"""

from collections import defaultdict
from itertools import accumulate

def splitPainting(segments):
    """
    Function to compute the resulting painting after merging overlapping segments.
    
    Args:
    segments (List[List[int]]): List of segments where each segment is represented as [start, end, color].
    
    Returns:
    List[List[int]]: Resulting painting as a list of non-overlapping segments.
    """
    changes = defaultdict(int)
    
    # Record the changes in color at each point
    for start, end, color in segments:
        changes[start] += color
        changes[end] -= color
    
    # Sort the points and calculate the accumulated color
    sorted_points = sorted(changes.keys())
    accumulated_color = list(accumulate(changes[point] for point in sorted_points))
    
    # Build the result
    result = []
    for i in range(len(sorted_points) - 1):
        if accumulated_color[i] > 0:  # Only include segments with non-zero color
            result.append([sorted_points[i], sorted_points[i + 1], accumulated_color[i]])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    segments1 = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]
    print(splitPainting(segments1))
    # Expected Output: [[1, 4, 14], [4, 7, 16]]

    # Test Case 2
    segments2 = [[1, 4, 5], [4, 7, 7]]
    print(splitPainting(segments2))
    # Expected Output: [[1, 4, 5], [4, 7, 7]]

    # Test Case 3
    segments3 = [[1, 10, 1], [2, 5, 2], [6, 9, 3]]
    print(splitPainting(segments3))
    # Expected Output: [[1, 2, 1], [2, 5, 3], [5, 6, 1], [6, 9, 4], [9, 10, 1]]

"""
Time Complexity Analysis:
- Sorting the points: O(N log N), where N is the number of unique points in the `changes` dictionary.
- Accumulating the color changes: O(N), where N is the number of unique points.
- Constructing the result: O(N), where N is the number of unique points.
Overall: O(N log N), where N is the number of unique points.

Space Complexity Analysis:
- The `changes` dictionary stores at most 2 * len(segments) keys, so O(N) space.
- The `accumulated_color` list and `sorted_points` list also take O(N) space.
Overall: O(N), where N is the number of unique points.

Topic: Arrays, Sorting, Prefix Sum
"""