"""
LeetCode Question #2333: Minimum Sum of Squared Difference

Problem Statement:
You are given two positive integer arrays `nums1` and `nums2`, both of length `n`. The squared difference of the two arrays is defined as:

    squared_difference = sum((nums1[i] - nums2[i])^2 for i in range(n))

You are also given two integers `k1` and `k2`. You can perform the following operation at most `k1 + k2` times:

    - Increment or decrement any element of `nums1` or `nums2` by 1.

Your goal is to minimize the squared difference after performing the operations.

Return the minimum possible squared difference.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^5`
- `0 <= k1, k2 <= 10^9`
"""

from heapq import heapify, heappop, heappush
from typing import List

def minSumSquareDiff(nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
    """
    Minimize the squared difference between nums1 and nums2 by performing at most k1 + k2 operations.
    """
    n = len(nums1)
    k = k1 + k2

    # Calculate the absolute differences between nums1 and nums2
    diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]

    # Use a max-heap to prioritize the largest differences
    max_heap = [-diff for diff in diffs if diff > 0]
    heapify(max_heap)

    # Reduce the largest differences using the available operations
    while k > 0 and max_heap:
        largest = -heappop(max_heap)
        if largest == 0:
            break

        # Determine how many operations to apply to the largest difference
        next_largest = -max_heap[0] if max_heap else 0
        reduce_by = min(k, largest - next_largest, 1)
        k -= reduce_by
        largest -= reduce_by

        # Push the updated difference back into the heap
        heappush(max_heap, -largest)

    # Calculate the minimized squared difference
    return sum(x * x for x in [-val for val in max_heap])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k1 = 1
    k2 = 2
    print(minSumSquareDiff(nums1, nums2, k1, k2))  # Expected Output: 27

    # Test Case 2
    nums1 = [10, 20, 30]
    nums2 = [10, 20, 30]
    k1 = 0
    k2 = 0
    print(minSumSquareDiff(nums1, nums2, k1, k2))  # Expected Output: 0

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [7, 8, 9]
    k1 = 10
    k2 = 10
    print(minSumSquareDiff(nums1, nums2, k1, k2))  # Expected Output: 0

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k1 = 5
    k2 = 5
    print(minSumSquareDiff(nums1, nums2, k1, k2))  # Expected Output: 0

"""
Time Complexity:
- Calculating the absolute differences: O(n)
- Building the max-heap: O(n)
- Reducing the largest differences: O(k log n), where k is the total number of operations.
- Calculating the final squared difference: O(n)
Overall: O(n + k log n)

Space Complexity:
- Storing the differences in a heap: O(n)
Overall: O(n)

Topic: Heap (Priority Queue)
"""