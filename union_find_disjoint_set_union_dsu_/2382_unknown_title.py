"""
LeetCode Problem #2382: Maximum Segment Sum After Removals

Problem Statement:
You are given two arrays `nums` and `remove` both of length `n`. For the `i-th` operation, you remove the element at index `remove[i]` from `nums`, making it unavailable for future operations. The array `nums` is initially a segment of length `n`.

After each removal, the array is split into several segments (contiguous subarrays). For each operation, find the maximum sum of these segments. If a segment is empty, its sum is considered to be 0.

Return an array `result` of length `n` where `result[i]` is the maximum segment sum after the `i-th` removal.

Constraints:
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= remove[i] < n`
- All elements of `remove` are unique.

Example:
Input: nums = [1,2,5,6,1], remove = [0,3,2,4,1]
Output: [14,7,2,2,0]

Explanation:
- Initially, nums = [1,2,5,6,1], max segment sum = 14.
- After removing index 0, nums = [_,2,5,6,1], max segment sum = 14.
- After removing index 3, nums = [_,2,5,_,1], max segment sum = 7.
- After removing index 2, nums = [_,2,_,_,1], max segment sum = 2.
- After removing index 4, nums = [_,2,_,_,_], max segment sum = 2.
- After removing index 1, nums = [_,_,_,_,_], max segment sum = 0.

Topic: Union-Find (Disjoint Set Union, DSU)
"""

from sortedcontainers import SortedList

def maximumSegmentSum(nums, remove):
    n = len(nums)
    result = [0] * n
    segment_sums = SortedList()
    total_sum = sum(nums)
    active_segments = {0: total_sum}  # {start_index: segment_sum}
    segment_sums.add(total_sum)

    for i in range(n):
        idx = remove[i]
        # Find the segment containing idx
        start = idx
        while start > 0 and start - 1 in active_segments:
            start -= 1
        end = idx
        while end + 1 < n and end + 1 in active_segments:
            end += 1