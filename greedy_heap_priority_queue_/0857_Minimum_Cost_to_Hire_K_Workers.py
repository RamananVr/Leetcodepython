"""
LeetCode Problem #857: Minimum Cost to Hire K Workers

Problem Statement:
There are `n` workers. You are given two arrays `quality` and `wage` where:
- `quality[i]` is the amount of work the i-th worker can produce per hour.
- `wage[i]` is the minimum wage expectation of the i-th worker.

The cost of hiring one worker is `wage[i] / quality[i]` * `q`, where `q` is the total quality of the group of workers.

You want to hire exactly `k` workers to form a paid group such that every worker in the group is paid in proportion to their quality compared to the other workers in the group, and that every worker in the group meets their minimum wage expectation.

Return the minimum cost to hire exactly `k` workers.

Constraints:
- `1 <= k <= n <= 10^4`
- `1 <= quality[i], wage[i] <= 10^4`
- The input is guaranteed to have at least one valid answer.
"""

from heapq import heappush, heappop

def mincostToHireWorkers(quality, wage, k):
    """
    Calculate the minimum cost to hire exactly k workers.

    :param quality: List[int] - The quality of each worker.
    :param wage: List[int] - The minimum wage expectation of each worker.
    :param k: int - The number of workers to hire.
    :return: float - The minimum cost to hire k workers.
    """
    # Create a list of workers with their wage-to-quality ratio, quality, and wage
    workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
    
    # Minimize cost by maintaining a max-heap of quality
    heap = []
    total_quality = 0
    min_cost = float('inf')
    
    for ratio, q, w in workers:
        # Add the current worker's quality to the heap
        heappush(heap, -q)
        total_quality += q
        
        # If we have more than k workers, remove the one with the highest quality
        if len(heap) > k:
            total_quality += heappop(heap)
        
        # If we have exactly k workers, calculate the cost
        if len(heap) == k:
            min_cost = min(min_cost, total_quality * ratio)
    
    return min_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    k = 2
    print(mincostToHireWorkers(quality, wage, k))  # Expected Output: 105.0

    # Test Case 2
    quality = [3, 1, 10, 10, 1]
    wage = [4, 8, 2, 2, 7]
    k = 3
    print(mincostToHireWorkers(quality, wage, k))  # Expected Output: 30.66667

    # Test Case 3
    quality = [4, 8, 2]
    wage = [8, 16, 4]
    k = 2
    print(mincostToHireWorkers(quality, wage, k))  # Expected Output: 16.0

"""
Time Complexity:
- Sorting the workers by their wage-to-quality ratio takes O(n log n), where n is the number of workers.
- Iterating through the sorted workers and maintaining a max-heap of size k takes O(n log k).
- Overall time complexity: O(n log n).

Space Complexity:
- The max-heap can contain at most k elements, so the space complexity is O(k).

Topic: Greedy, Heap (Priority Queue)
"""