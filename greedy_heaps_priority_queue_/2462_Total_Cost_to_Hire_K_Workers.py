"""
LeetCode Problem #2462: Total Cost to Hire K Workers

Problem Statement:
You are given a 0-indexed integer array `costs` where `costs[i]` is the cost of hiring the ith worker. 
You are also given two integers `k` and `candidates`. 

We want to hire exactly `k` workers according to the following rules:
1. You will run `k` sessions and hire one worker in each session.
2. In each hiring session, choose the worker with the lowest cost from either the first `candidates` workers or the last `candidates` workers. 
   - Break ties by choosing the worker with the smallest index.
   - If there are fewer than `candidates` workers remaining in the array, choose the worker with the lowest cost among them.
3. Remove the chosen worker from the array.

Return the total cost to hire exactly `k` workers.

Constraints:
- 1 <= costs.length <= 10^5
- 1 <= costs[i] <= 10^5
- 1 <= k, candidates <= costs.length
"""

from heapq import heappush, heappop

def totalCost(costs, k, candidates):
    """
    Calculate the total cost to hire k workers based on the given rules.

    :param costs: List[int] - The cost of hiring each worker.
    :param k: int - The number of workers to hire.
    :param candidates: int - The number of candidates to consider from the start and end.
    :return: int - The total cost to hire k workers.
    """
    n = len(costs)
    left_heap, right_heap = [], []
    left, right = 0, n - 1
    total_cost = 0

    # Initialize the heaps with the first and last `candidates` workers
    for _ in range(candidates):
        if left <= right:
            heappush(left_heap, (costs[left], left))
            left += 1
        if left <= right:
            heappush(right_heap, (costs[right], right))
            right -= 1

    # Hire k workers
    for _ in range(k):
        # Choose the worker with the lowest cost
        if right_heap and (not left_heap or left_heap[0][0] > right_heap[0][0]):
            cost, idx = heappop(right_heap)
            total_cost += cost
            # Add a new candidate from the right side if possible
            if left <= right:
                heappush(right_heap, (costs[right], right))
                right -= 1
        else:
            cost, idx = heappop(left_heap)
            total_cost += cost
            # Add a new candidate from the left side if possible
            if left <= right:
                heappush(left_heap, (costs[left], left))
                left += 1

    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    print(totalCost(costs, k, candidates))  # Output: 11

    # Test Case 2
    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3
    print(totalCost(costs, k, candidates))  # Output: 4

    # Test Case 3
    costs = [5, 3, 8, 2, 6]
    k = 2
    candidates = 2
    print(totalCost(costs, k, candidates))  # Output: 5

"""
Time Complexity:
- Initializing the heaps takes O(candidates * log(candidates)) since we push up to `candidates` elements into each heap.
- For each of the `k` hiring sessions, we perform a heap operation (push and pop), which takes O(log(candidates)).
- In total, the time complexity is O(candidates * log(candidates) + k * log(candidates)).

Space Complexity:
- The space complexity is O(candidates) for the two heaps.

Topic: Greedy, Heaps (Priority Queue)
"""