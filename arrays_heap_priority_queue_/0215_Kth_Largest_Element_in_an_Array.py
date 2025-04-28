"""
LeetCode Problem #215: Kth Largest Element in an Array

Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.
Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

You must solve it in `O(n)` time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
"""

# Solution
import heapq

def findKthLargest(nums, k):
    """
    Finds the kth largest element in the array using a min-heap.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The rank of the largest element to find.

    Returns:
    int: The kth largest element in the array.
    """
    # Use a min-heap of size k
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print("Test Case 1 Output:", findKthLargest(nums1, k1))  # Expected Output: 5

    # Test Case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print("Test Case 2 Output:", findKthLargest(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1]
    k3 = 1
    print("Test Case 3 Output:", findKthLargest(nums3, k3))  # Expected Output: 1

    # Test Case 4
    nums4 = [7, 10, 4, 3, 20, 15]
    k4 = 3
    print("Test Case 4 Output:", findKthLargest(nums4, k4))  # Expected Output: 10

    # Test Case 5
    nums5 = [5, 5, 5, 5, 5]
    k5 = 1
    print("Test Case 5 Output:", findKthLargest(nums5, k5))  # Expected Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the min-heap takes O(k) time for the first k elements.
- For the remaining (n - k) elements, each insertion and removal operation on the heap takes O(log k).
- Total time complexity: O(k) + O((n - k) * log k) = O(n log k), where n is the length of the array.

Space Complexity:
- The space complexity is O(k) for the min-heap, where k is the size of the heap.
"""

# Topic: Arrays, Heap (Priority Queue)