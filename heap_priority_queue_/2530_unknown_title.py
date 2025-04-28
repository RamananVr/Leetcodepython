"""
LeetCode Problem #2530: Maximal Score After Applying K Operations

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`. You have a chance to perform the following operation exactly `k` times:

1. Choose an index `i` such that `nums[i]` is the largest value in `nums`.
2. Replace `nums[i]` with `ceil(nums[i] / 3)`.

Return the maximum possible sum of the array after applying the operation `k` times.

Note:
- `ceil(x)` is the smallest integer greater than or equal to `x`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= min(10^5, nums.length)`
"""

import heapq
import math

def maxKelements(nums, k):
    """
    Calculate the maximum possible sum of the array after applying the operation k times.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The number of operations to perform.

    Returns:
    int: The maximum possible sum of the array after k operations.
    """
    # Use a max-heap to efficiently get the largest element
    # Python's heapq is a min-heap, so we use negative values to simulate a max-heap
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    total_sum = 0

    for _ in range(k):
        # Extract the largest element (convert back to positive)
        largest = -heapq.heappop(max_heap)
        total_sum += largest

        # Apply the operation and push the updated value back into the heap
        updated_value = math.ceil(largest / 3)
        heapq.heappush(max_heap, -updated_value)

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 20, 7]
    k1 = 4
    print(maxKelements(nums1, k1))  # Expected Output: 47

    # Test Case 2
    nums2 = [1, 10, 3, 3, 3]
    k2 = 3
    print(maxKelements(nums2, k2))  # Expected Output: 17

    # Test Case 3
    nums3 = [5]
    k3 = 1
    print(maxKelements(nums3, k3))  # Expected Output: 5

    # Test Case 4
    nums4 = [100, 200, 300]
    k4 = 5
    print(maxKelements(nums4, k4))  # Expected Output: 833

"""
Time Complexity Analysis:
- Building the heap takes O(n), where n is the length of the input array `nums`.
- Each of the `k` operations involves extracting the maximum element and inserting a new element into the heap.
  - Extracting the maximum and inserting into the heap each take O(log n).
- Therefore, the total time complexity is O(n + k log n).

Space Complexity Analysis:
- The heap requires O(n) space to store the elements of the array.
- Thus, the space complexity is O(n).

Topic: Heap (Priority Queue)
"""