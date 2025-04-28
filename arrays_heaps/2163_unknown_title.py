"""
LeetCode Problem #2163: Minimum Difference in Sums After Removal of Elements

Problem Statement:
You are given a 0-indexed integer array `nums` consisting of `3 * n` elements.

You are allowed to remove exactly `n` elements from either the beginning or the end of the array. 
The remaining `2 * n` elements will be split into two equal parts:
- The first part consists of the first `n` elements.
- The second part consists of the last `n` elements.

Let the sum of the first part be `sum1` and the sum of the second part be `sum2`.

The difference in sums is defined as `|sum1 - sum2|`.

Return the minimum difference possible between `sum1` and `sum2` after removing `n` elements.

Constraints:
- `nums.length == 3 * n`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
"""

# Solution
from heapq import heappush, heappop
from itertools import accumulate

def minimumDifference(nums):
    n = len(nums) // 3
    
    # Calculate prefix sums for the first n elements using a max heap
    left_heap = []
    left_sum = 0
    left_prefix = [0] * (2 * n + 1)
    for i in range(2 * n):
        heappush(left_heap, -nums[i])
        left_sum += nums[i]
        if len(left_heap) > n:
            left_sum += heappop(left_heap)
        left_prefix[i + 1] = left_sum
    
    # Calculate suffix sums for the last n elements using a min heap
    right_heap = []
    right_sum = 0
    right_suffix = [0] * (2 * n + 1)
    for i in range(2 * n - 1, n - 1, -1):
        heappush(right_heap, nums[i])
        right_sum += nums[i]
        if len(right_heap) > n:
            right_sum -= heappop(right_heap)
        right_suffix[i - n + 1] = right_sum
    
    # Find the minimum difference between prefix and suffix sums
    min_diff = float('inf')
    for i in range(n, 2 * n + 1):
        min_diff = min(min_diff, abs(left_prefix[i] - right_suffix[i]))
    
    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 2, 4, 5, 6, 7, 8, 9]
    print(minimumDifference(nums1))  # Expected Output: 1

    # Test Case 2
    nums2 = [1, 2, 3, 6, 5, 4, 9, 8, 7]
    print(minimumDifference(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(minimumDifference(nums3))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the prefix sums using a max heap takes O(n log n) for the first 2n elements.
- Constructing the suffix sums using a min heap takes O(n log n) for the last 2n elements.
- Comparing prefix and suffix sums takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The max heap and min heap each store up to n elements, so the space complexity for the heaps is O(n).
- The prefix and suffix arrays each store 2n elements, so the space complexity for these arrays is O(n).
- Overall space complexity: O(n).

Topic: Arrays, Heaps
"""