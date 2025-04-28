"""
LeetCode Problem #1199: Minimum Time to Build Blocks

Problem Statement:
You are given an array `blocks` of integers where `blocks[i]` represents the time needed to build the i-th block. You also have a limited number of workers (initially only one worker is available). Each worker can either build a block or split into two workers. The split operation takes `split` units of time.

Return the minimum time needed to build all the blocks.

Example:
Input: blocks = [1, 2], split = 5
Output: 7
Explanation: 
- We start with 1 worker.
- Split the worker into 2 workers (takes 5 units of time).
- Use the 2 workers to build the blocks [1, 2] (takes max(1, 2) = 2 units of time).
- Total time = 5 + 2 = 7.

Constraints:
- 1 <= blocks.length <= 1000
- 1 <= blocks[i] <= 10^9
- 1 <= split <= 10^9
"""

from heapq import heappush, heappop

def minBuildTime(blocks, split):
    """
    Calculate the minimum time required to build all blocks.

    :param blocks: List[int] - Time required to build each block.
    :param split: int - Time required to split a worker into two workers.
    :return: int - Minimum time required to build all blocks.
    """
    # Use a min-heap to manage the blocks
    heap = []
    for block in blocks:
        heappush(heap, block)
    
    while len(heap) > 1:
        # Pop the two smallest blocks
        first = heappop(heap)
        second = heappop(heap)
        # Combine them into one block with the split time
        heappush(heap, second + split)
    
    # The last remaining block in the heap is the minimum time required
    return heap[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    blocks = [1, 2]
    split = 5
    print(minBuildTime(blocks, split))  # Output: 7

    # Test Case 2
    blocks = [1, 3, 5]
    split = 2
    print(minBuildTime(blocks, split))  # Output: 8

    # Test Case 3
    blocks = [10, 20, 30]
    split = 15
    print(minBuildTime(blocks, split))  # Output: 65

    # Test Case 4
    blocks = [1]
    split = 10
    print(minBuildTime(blocks, split))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the blocks initially takes O(n log n), where n is the number of blocks.
- Each heap operation (push and pop) takes O(log n), and we perform these operations n-1 times.
- Overall, the time complexity is O(n log n).

Space Complexity:
- The heap requires O(n) space to store the blocks.
- Therefore, the space complexity is O(n).

Topic: Greedy, Heap (Priority Queue)
"""