"""
LeetCode Problem #2015: Average Height of Buildings in Each Segment

Problem Statement:
You are given a 2D integer array `buildings` where `buildings[i] = [start_i, end_i, height_i]`:
- `start_i` is the starting point of the i-th building.
- `end_i` is the ending point of the i-th building (exclusive).
- `height_i` is the height of the i-th building.

The buildings overlap if their ranges intersect. For each segment of the x-axis covered by at least one building, calculate the average height of the buildings covering that segment.

Return a 2D array `result` where `result[j] = [start_j, end_j, averageHeight_j]`:
- `start_j` is the starting point of the j-th segment.
- `end_j` is the ending point of the j-th segment.
- `averageHeight_j` is the average height of the buildings covering that segment.

The result should be sorted by `start_j` in ascending order, and within each segment, the average height should be rounded down to the nearest integer.

Constraints:
- 1 <= buildings.length <= 10^5
- 1 <= start_i < end_i <= 10^9
- 1 <= height_i <= 10^4

Example:
Input: buildings = [[1, 5, 2], [2, 7, 3]]
Output: [[1, 2, 2], [2, 5, 2], [5, 7, 3]]

Explanation:
- From 1 to 2, only the first building is present with height 2.
- From 2 to 5, both buildings overlap, and their average height is (2 + 3) // 2 = 2.
- From 5 to 7, only the second building is present with height 3.
"""

from collections import defaultdict
import heapq

def averageHeightOfBuildings(buildings):
    """
    Calculate the average height of buildings in each segment of the x-axis.

    :param buildings: List[List[int]] - List of buildings represented as [start, end, height].
    :return: List[List[int]] - List of segments with their average heights.
    """
    events = []
    
    # Create events for start and end of buildings
    for start, end, height in buildings:
        events.append((start, height))  # Start of a building
        events.append((end, -height))  # End of a building
    
    # Sort events by x-coordinate, and process starts before ends if they are at the same x
    events.sort()
    
    result = []
    prev_x = None
    active_heights = 0
    active_count = 0
    
    for x, height_change in events:
        if prev_x is not None and active_count > 0:
            # Add the segment to the result
            avg_height = active_heights // active_count
            result.append([prev_x, x, avg_height])
        
        # Update active heights and count
        if height_change > 0:
            active_heights += height_change
            active_count += 1
        else:
            active_heights += height_change  # Subtract height
            active_count -= 1
        
        prev_x = x
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buildings = [[1, 5, 2], [2, 7, 3]]
    print(averageHeightOfBuildings(buildings))  # Expected: [[1, 2, 2], [2, 5, 2], [5, 7, 3]]

    # Test Case 2
    buildings = [[1, 3, 4], [2, 5, 2], [4, 6, 3]]
    print(averageHeightOfBuildings(buildings))  # Expected: [[1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 5, 2], [5, 6, 3]]

    # Test Case 3
    buildings = [[1, 10, 5], [2, 6, 3], [7, 9, 4]]
    print(averageHeightOfBuildings(buildings))  # Expected: [[1, 2, 5], [2, 6, 4], [6, 7, 5], [7, 9, 4], [9, 10, 5]]

# Time Complexity Analysis:
# - Sorting the events takes O(n log n), where n is the number of buildings.
# - Processing the events takes O(n), as we iterate through the sorted list.
# Overall time complexity: O(n log n).

# Space Complexity Analysis:
# - The space required for the events list is O(n).
# - Additional space for the result list is O(k), where k is the number of segments (k <= 2n).
# Overall space complexity: O(n).

# Topic: Arrays, Sorting, Sweep Line