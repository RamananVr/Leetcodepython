"""
LeetCode Question #2542: Maximum Subsequence Score

Problem Statement:
You are given two 0-indexed integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. 
You must choose a subsequence of indices from `nums1` of length `k`.

For chosen indices `i0, i1, ..., ik-1`, your score is defined as:
- The sum of the `k` elements in `nums1` corresponding to the chosen indices.
- Multiplied by the minimum of the `k` elements in `nums2` corresponding to the chosen indices.

Return the maximum possible score.

A subsequence of indices of an array is a set of indices chosen in increasing order (e.g., `[0, 1, 2]` or `[2, 4, 7]`).

Example:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
- Choose indices [1, 2, 3] (0-based). 
- Corresponding elements are nums1 = [3, 3, 2] and nums2 = [1, 3, 4].
- Minimum of nums2 is 1, and sum of nums1 is 3 + 3 + 2 = 8.
- Score = 8 * 1 = 12.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^5`
- `1 <= k <= n`
"""

from heapq import heappush, heappop
from typing import List

def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    # Pair nums1 and nums2 together and sort by nums2 in descending order
    pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
    
    # Min-heap to maintain the top k elements from nums1
    min_heap = []
    current_sum = 0
    max_score = 0
    
    for num1, num2 in pairs:
        # Add the current num1 to the heap and update the current sum
        heappush(min_heap, num1)
        current_sum += num1
        
        # If the heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            current_sum -= heappop(min_heap)
        
        # If the heap size is exactly k, calculate the score
        if len(min_heap) == k:
            max_score = max(max_score, current_sum * num2)
    
    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    print(maxScore(nums1, nums2, k))  # Output: 12

    # Test Case 2
    nums1 = [4, 2, 3, 1]
    nums2 = [7, 5, 10, 9]
    k = 2
    print(maxScore(nums1, nums2, k))  # Output: 56

    # Test Case 3
    nums1 = [5, 2, 1]
    nums2 = [3, 4, 2]
    k = 2
    print(maxScore(nums1, nums2, k))  # Output: 14

"""
Time Complexity:
- Sorting the pairs takes O(n log n).
- Iterating through the pairs and maintaining a heap of size k takes O(n log k).
- Overall time complexity: O(n log n).

Space Complexity:
- The heap can grow to a maximum size of k, so the space complexity is O(k).
- Additional space is used for the pairs array, which is O(n).
- Overall space complexity: O(n).

Topic: Greedy, Heap (Priority Queue)
"""