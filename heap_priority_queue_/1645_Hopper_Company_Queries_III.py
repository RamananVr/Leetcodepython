"""
LeetCode Problem #1645: "Hopper Company Queries III"

Problem Statement:
You are given two arrays `nums1` and `nums2` of size `n` and an integer `k`. 
The arrays are sorted in ascending order. You need to find the k-th smallest 
sum of pairs (nums1[i] + nums2[j]) where 0 <= i, j < n.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[j] <= 10^9
- 1 <= k <= min(2000, nums1.length * nums2.length)

Example:
Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
Output: 7
Explanation: The sums of pairs are [3, 5, 7, 9, 11, 13, 15, 17]. The 3rd smallest sum is 7.
"""

import heapq

def kthSmallestPairSum(nums1, nums2, k):
    """
    Finds the k-th smallest sum of pairs (nums1[i] + nums2[j]) where 0 <= i, j < n.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.
    k (int): The k-th smallest sum to find.

    Returns:
    int: The k-th smallest sum.
    """
    # Min-heap to store pairs and their sums
    min_heap = []
    n1, n2 = len(nums1), len(nums2)

    # Initialize the heap with the smallest sums from nums1 and nums2
    for i in range(min(k, n1)):  # Only need the first k elements from nums1
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    # Extract the k-th smallest sum
    for _ in range(k):
        current_sum, i, j = heapq.heappop(min_heap)
        if j + 1 < n2:  # If there's a next element in nums2
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return current_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(kthSmallestPairSum(nums1, nums2, k))  # Output: 7

    # Test Case 2
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(kthSmallestPairSum(nums1, nums2, k))  # Output: 2

    # Test Case 3
    nums1 = [1, 2]
    nums2 = [3, 4]
    k = 4
    print(kthSmallestPairSum(nums1, nums2, k))  # Output: 6

    # Test Case 4
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    k = 5
    print(kthSmallestPairSum(nums1, nums2, k))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The heap operations (push and pop) take O(log(min(k, n1))).
- We perform k heap operations, so the total time complexity is O(k * log(min(k, n1))).

Space Complexity:
- The heap stores at most min(k, n1) elements, so the space complexity is O(min(k, n1)).

Topic: Heap (Priority Queue)
"""