"""
LeetCode Problem #2822: Maximum Segment Sum After Removals

Problem Statement:
You are given two integer arrays `nums` and `removeQueries`, both of length `n`. The array `nums` represents an array of integers, and the array `removeQueries` represents the order in which elements are removed from `nums`.

After removing an element, the array is split into segments (contiguous subarrays). The sum of each segment is the sum of its elements. The maximum segment sum is the largest sum among all segments.

Initially, the array is empty. You need to return an array `result` of length `n` where `result[i]` is the maximum segment sum after the first `i + 1` elements are removed in the order specified by `removeQueries`.

Constraints:
- `n == nums.length == removeQueries.length`
- `1 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= removeQueries[i] < n`
- All the values of `removeQueries` are unique.

Example:
Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
Output: [14,7,2,2,0]

Explanation:
- After removing 0: nums = [2,5,6,1], max segment sum = 14
- After removing 3: nums = [2,5,1], max segment sum = 7
- After removing 2: nums = [2,1], max segment sum = 2
- After removing 4: nums = [2], max segment sum = 2
- After removing 1: nums = [], max segment sum = 0
"""

from sortedcontainers import SortedDict

def maximumSegmentSum(nums, removeQueries):
    n = len(nums)
    result = [0] * n
    active_segments = SortedDict()
    active_segments[0] = sum(nums)
    max_segment_sum = active_segments[0]

    for i, remove_index in enumerate(removeQueries):
        # Update result
        result[i] = max_segment_sum
        # Remove the segment
        del active_segments[remove_index]
        # Update max_segment_sum
        max_segment_sum=max(max_segment_sum