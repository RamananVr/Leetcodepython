"""
LeetCode Problem #218: The Skyline Problem

Problem Statement:
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

Each building is represented by a triplet [left, right, height], where:
- left: the x-coordinate of the left edge of the building.
- right: the x-coordinate of the right edge of the building.
- height: the height of the building.

The output is a list of "key points" (x, y) that uniquely define a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the skyline ends, is always at height 0.

The output should be sorted by the x-coordinate. If two key points have the same x-coordinate, the one with the larger y-coordinate should appear first.

Input:
- A list of buildings, where each building is represented as [left, right, height].

Output:
- A list of key points, where each key point is represented as [x, y].

Constraints:
1. 1 <= buildings.length <= 10^4
2. 0 <= left < right <= 2^31 - 1
3. 1 <= height <= 2^31 - 1
4. The buildings are perfect rectangles aligned to the x and y axes.

Example:
Input: buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
Output: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
"""

from heapq import heappush, heappop
from collections import defaultdict

def getSkyline(buildings):
    """
    Solves the Skyline Problem using a sweep line algorithm with a max heap.

    :param buildings: List[List[int]] - List of buildings represented as [left, right, height]
    :return: List[List[int]] - List of key points representing the skyline
    """
    # Step 1: Create a list of events (start and end of buildings)
    events = []
    for left, right, height in buildings:
        events.append((left, -height, right))  # Start of a building
        events.append((right, 0, 0))          # End of a building
    events.sort()  # Sort events by x-coordinate, then by height

    # Step 2: Use a max heap to track active buildings
    result = []
    max_heap = [(0, float('inf'))]  # (negative height, end position)
    prev_max_height = 0

    for x, neg_height, end in events:
        # Remove buildings from the heap that have ended
        while max_heap[0][1] <= x:
            heappop(max_heap)

        # Add new buildings to the heap
        if neg_height != 0:
            heappush(max_heap, (neg_height, end))

        # Get the current max height
        current_max_height = -max_heap[0][0]

        # If the max height changes, add a key point
        if current_max_height != prev_max_height:
            result.append([x, current_max_height])
            prev_max_height = current_max_height

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(getSkyline(buildings))  # Expected: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

    # Test Case 2
    buildings = [[0, 2, 3], [2, 5, 3]]
    print(getSkyline(buildings))  # Expected: [[0, 3], [5, 0]]

    # Test Case 3
    buildings = [[1, 3, 4], [2, 4, 6], [8, 11, 5]]
    print(getSkyline(buildings))  # Expected: [[1, 4], [2, 6], [4, 0], [8, 5], [11, 0]]

# Time Complexity Analysis:
# - Sorting the events takes O(n log n), where n is the number of buildings.
# - Each building is added to and removed from the heap at most once, and heap operations take O(log n).
# - Overall, the time complexity is O(n log n).

# Space Complexity Analysis:
# - The heap can contain at most n elements, so the space complexity is O(n).

# Topic: Sweep Line Algorithm, Heap (Priority Queue)