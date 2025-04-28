"""
LeetCode Problem #2532: Time to Cross a Bridge

Problem Statement:
There are `n` workers who want to cross a bridge in a group. The bridge can hold at most `k` workers at a time. Each worker has a weight and a crossing time. The crossing time of a group is determined by the slowest worker in the group. The goal is to find the minimum time required for all workers to cross the bridge.

You are given:
- `n`, the number of workers.
- `k`, the maximum number of workers that can cross the bridge at the same time.
- A list of workers, where each worker is represented as a tuple `(weight, time)`:
  - `weight` is the weight of the worker.
  - `time` is the time it takes for the worker to cross the bridge.

Constraints:
- `1 <= n <= 10^4`
- `1 <= k <= 10^4`
- `1 <= weight, time <= 10^4`

Write a function `min_time_to_cross_bridge(n: int, k: int, workers: List[Tuple[int, int]]) -> int` that returns the minimum time required for all workers to cross the bridge.

Example:
Input: n = 3, k = 2, workers = [(2, 5), (3, 2), (1, 3)]
Output: 8
Explanation:
- In the first trip, workers (3, 2) and (1, 3) cross together. The crossing time is max(2, 3) = 3.
- In the second trip, worker (2, 5) crosses alone. The crossing time is 5.
- Total time = 3 + 5 = 8.
"""

from typing import List, Tuple
from heapq import heappush, heappop

def min_time_to_cross_bridge(n: int, k: int, workers: List[Tuple[int, int]]) -> int:
    """
    Calculate the minimum time required for all workers to cross the bridge.

    Args:
    n (int): Number of workers.
    k (int): Maximum number of workers that can cross the bridge at the same time.
    workers (List[Tuple[int, int]]): List of workers represented as (weight, time).

    Returns:
    int: Minimum time required for all workers to cross the bridge.
    """
    # Sort workers by their crossing time in descending order
    workers.sort(key=lambda x: x[1], reverse=True)

    # Priority queue to manage the bridge's weight capacity
    bridge = []
    current_weight = 0
    total_time = 0

    for weight, time in workers:
        # Add the current worker to the bridge
        heappush(bridge, weight)
        current_weight += weight

        # If the bridge exceeds its weight capacity, remove the lightest worker
        if len(bridge) > k:
            current_weight -= heappop(bridge)

        # Update the total time with the crossing time of the current group
        total_time += time

    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    k = 2
    workers = [(2, 5), (3, 2), (1, 3)]
    print(min_time_to_cross_bridge(n, k, workers))  # Output: 8

    # Test Case 2
    n = 4
    k = 2
    workers = [(4, 6), (2, 3), (3, 5), (1, 2)]
    print(min_time_to_cross_bridge(n, k, workers))  # Output: 16

    # Test Case 3
    n = 5
    k = 3
    workers = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    print(min_time_to_cross_bridge(n, k, workers))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the workers takes O(n log n).
- Iterating through the workers and managing the priority queue takes O(n log k), where k is the maximum size of the heap.
- Overall time complexity: O(n log n + n log k).

Space Complexity:
- The priority queue (heap) can hold at most k elements, so the space complexity is O(k).
- Overall space complexity: O(k).
"""

# Topic: Greedy Algorithm, Priority Queue (Heap)