"""
LeetCode Problem #1642: Furthest Building You Can Reach

Problem Statement:
You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders. While moving from building `i` to building `i+1` (0-indexed),
- If the current building's height is greater than or equal to the next building's height, you can move without using any resources.
- If the current building's height is less than the next building's height, you can either:
  - Use `bricks` equal to the difference between the heights, or
  - Use one ladder.

Return the furthest building index (0-indexed) you can reach if you use the given bricks and ladders optimally.

Constraints:
- `1 <= heights.length <= 10^5`
- `1 <= heights[i] <= 10^6`
- `0 <= bricks <= 10^9`
- `0 <= ladders <= heights.length`

"""

from heapq import heappush, heappop

def furthestBuilding(heights, bricks, ladders):
    """
    Determines the furthest building index you can reach using the given bricks and ladders optimally.

    :param heights: List[int] - Heights of the buildings
    :param bricks: int - Number of bricks available
    :param ladders: int - Number of ladders available
    :return: int - The furthest building index you can reach
    """
    min_heap = []  # Min-heap to track the largest height differences where ladders are used

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        
        # If the next building is taller, we need to handle the height difference
        if diff > 0:
            heappush(min_heap, diff)  # Push the height difference into the heap

            # If the heap size exceeds the number of ladders, we must use bricks for the smallest difference
            if len(min_heap) > ladders:
                bricks -= heappop(min_heap)

            # If we run out of bricks, we cannot proceed further
            if bricks < 0:
                return i

    # If we can traverse all buildings, return the last index
    return len(heights) - 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    print(furthestBuilding(heights, bricks, ladders))  # Output: 4

    # Test Case 2
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    print(furthestBuilding(heights, bricks, ladders))  # Output: 7

    # Test Case 3
    heights = [14, 3, 19, 3]
    bricks = 17
    ladders = 0
    print(furthestBuilding(heights, bricks, ladders))  # Output: 3

    # Test Case 4
    heights = [1, 2, 3, 4, 5]
    bricks = 0
    ladders = 1
    print(furthestBuilding(heights, bricks, ladders))  # Output: 4


"""
Time Complexity Analysis:
- Let `n` be the length of the `heights` array.
- For each building, we calculate the height difference and potentially push it into a min-heap.
- The heap operations (push and pop) take O(log k) time, where `k` is the size of the heap.
- In the worst case, the heap size is bounded by the number of ladders, so the time complexity is O(n log k), where k <= n.

Space Complexity Analysis:
- The space complexity is O(k), where `k` is the number of ladders, as the heap stores at most `k` elements.

Topic: Greedy, Heap (Priority Queue)
"""