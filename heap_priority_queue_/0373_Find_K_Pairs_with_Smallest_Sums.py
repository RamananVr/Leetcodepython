"""
LeetCode Problem #373: Find K Pairs with Smallest Sums

Problem Statement:
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^4
- -10^9 <= nums1[i], nums2[i] <= 10^9
- nums1 and nums2 are sorted in ascending order.
- 1 <= k <= 10^4

Example:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],...

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[1,3],[2,1],[2,2],...

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned since k is larger than the total number of pairs.
"""

from heapq import heappush, heappop

def kSmallestPairs(nums1, nums2, k):
    """
    Finds the k pairs with the smallest sums from two sorted arrays.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.
    k (int): Number of pairs to return.

    Returns:
    List[List[int]]: List of k pairs with the smallest sums.
    """
    if not nums1 or not nums2 or k == 0:
        return []

    # Min-heap to store the pairs along with their sums
    min_heap = []
    result = []

    # Initialize the heap with the first element of nums1 paired with every element of nums2
    for i in range(min(k, len(nums1))):  # Only need the first k elements from nums1
        heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)

    # Extract the k smallest pairs
    while k > 0 and min_heap:
        current_sum, i, j = heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        k -= 1

        # If there is a next element in nums2, push the next pair into the heap
        if j + 1 < len(nums2):
            heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(kSmallestPairs(nums1, nums2, k))  # Output: [[1, 2], [1, 4], [1, 6]]

    # Test Case 2
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(kSmallestPairs(nums1, nums2, k))  # Output: [[1, 1], [1, 1]]

    # Test Case 3
    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    print(kSmallestPairs(nums1, nums2, k))  # Output: [[1, 3], [2, 3]]

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 5
    print(kSmallestPairs(nums1, nums2, k))  # Output: [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5]]

"""
Time Complexity:
- Building the initial heap takes O(min(k, len(nums1))) since we push at most k elements into the heap.
- Each heappop and heappush operation takes O(log(min(k, len(nums1)))).
- In the worst case, we perform k heappop and heappush operations.
- Therefore, the overall time complexity is O(k * log(min(k, len(nums1)))).

Space Complexity:
- The heap stores at most min(k, len(nums1)) elements at any time, so the space complexity is O(min(k, len(nums1))).

Topic: Heap (Priority Queue)
"""