"""
LeetCode Question #2655: Find Maximal Uncovered Ranges

Problem Statement:
You are given an integer n which is the length of a 0-indexed array, and a 0-indexed 2D array ranges, where ranges[i] = [start_i, end_i] indicates that all integers from start_i to end_i (both inclusive) are covered.

You are also given an integer left and an integer right. You need to find the maximal uncovered ranges in the segment [left, right].

Return a 2D array answer where answer[j] = [start_j, end_j] represents that all integers from start_j to end_j (both inclusive) are uncovered. The ranges in answer should be sorted in ascending order.

Examples:
Example 1:
Input: n = 10, ranges = [[1,3],[6,8]], left = 0, right = 9
Output: [[0,0],[4,5],[9,9]]
Explanation: The ranges that are covered are [1,3] and [6,8]. The uncovered ranges in [0,9] are [0,0], [4,5], and [9,9].

Example 2:
Input: n = 3, ranges = [[0,2]], left = 0, right = 2
Output: []
Explanation: The range [0,2] is covered, so there are no uncovered ranges in [0,2].

Example 3:
Input: n = 7, ranges = [[2,4]], left = 1, right = 6
Output: [[1,1],[5,6]]
Explanation: The range [2,4] is covered. The uncovered ranges in [1,6] are [1,1] and [5,6].

Constraints:
- 1 <= n <= 50
- 0 <= left <= right < n
- 0 <= start_i <= end_i < n
- 1 <= ranges.length <= 50
"""

from typing import List

def findMaximalUncoveredRanges(n: int, ranges: List[List[int]], left: int, right: int) -> List[List[int]]:
    """
    Find maximal uncovered ranges in the segment [left, right].
    
    Approach:
    1. Filter and merge overlapping ranges within [left, right]
    2. Find gaps between merged ranges
    """
    # Filter ranges that intersect with [left, right]
    filtered_ranges = []
    for start, end in ranges:
        # Clip the range to [left, right]
        clipped_start = max(start, left)
        clipped_end = min(end, right)
        
        # Only include if valid range
        if clipped_start <= clipped_end:
            filtered_ranges.append([clipped_start, clipped_end])
    
    if not filtered_ranges:
        return [[left, right]]
    
    # Sort ranges by start position
    filtered_ranges.sort()
    
    # Merge overlapping ranges
    merged_ranges = [filtered_ranges[0]]
    
    for current_start, current_end in filtered_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        
        # If current range overlaps or is adjacent to last range, merge them
        if current_start <= last_end + 1:
            merged_ranges[-1][1] = max(last_end, current_end)
        else:
            merged_ranges.append([current_start, current_end])
    
    # Find uncovered ranges
    uncovered_ranges = []
    
    # Check if there's a gap before the first range
    first_start = merged_ranges[0][0]
    if left < first_start:
        uncovered_ranges.append([left, first_start - 1])
    
    # Check gaps between consecutive ranges
    for i in range(len(merged_ranges) - 1):
        current_end = merged_ranges[i][1]
        next_start = merged_ranges[i + 1][0]
        
        if current_end + 1 < next_start:
            uncovered_ranges.append([current_end + 1, next_start - 1])
    
    # Check if there's a gap after the last range
    last_end = merged_ranges[-1][1]
    if last_end < right:
        uncovered_ranges.append([last_end + 1, right])
    
    return uncovered_ranges

def findMaximalUncoveredRangesSimple(n: int, ranges: List[List[int]], left: int, right: int) -> List[List[int]]:
    """
    Simple approach using boolean array to mark covered positions.
    """
    # Mark covered positions
    covered = [False] * (right - left + 1)
    
    for start, end in ranges:
        # Clip range to [left, right]
        clipped_start = max(start, left)
        clipped_end = min(end, right)
        
        # Mark positions as covered
        for i in range(clipped_start, clipped_end + 1):
            if left <= i <= right:
                covered[i - left] = True
    
    # Find uncovered ranges
    uncovered_ranges = []
    i = 0
    length = right - left + 1
    
    while i < length:
        if not covered[i]:
            start = i + left
            # Find end of current uncovered range
            while i < length and not covered[i]:
                i += 1
            end = i - 1 + left
            uncovered_ranges.append([start, end])
        else:
            i += 1
    
    return uncovered_ranges

def findMaximalUncoveredRangesOptimized(n: int, ranges: List[List[int]], left: int, right: int) -> List[List[int]]:
    """
    Optimized approach with careful range handling.
    """
    if not ranges:
        return [[left, right]]
    
    # Create events for range boundaries
    events = []
    for start, end in ranges:
        if end >= left and start <= right:
            events.append((max(start, left), 1))  # start of range
            events.append((min(end, right) + 1, -1))  # end of range + 1
    
    if not events:
        return [[left, right]]
    
    # Sort events
    events.sort()
    
    # Process events to find covered intervals
    covered_intervals = []
    active_count = 0
    start_covered = None
    
    for pos, delta in events:
        if active_count == 0 and delta == 1:
            start_covered = pos
        active_count += delta
        if active_count == 0 and start_covered is not None:
            covered_intervals.append([start_covered, pos - 1])
    
    # Find uncovered ranges
    if not covered_intervals:
        return [[left, right]]
    
    uncovered = []
    
    # Before first covered interval
    if covered_intervals[0][0] > left:
        uncovered.append([left, covered_intervals[0][0] - 1])
    
    # Between covered intervals
    for i in range(len(covered_intervals) - 1):
        gap_start = covered_intervals[i][1] + 1
        gap_end = covered_intervals[i + 1][0] - 1
        if gap_start <= gap_end:
            uncovered.append([gap_start, gap_end])
    
    # After last covered interval
    if covered_intervals[-1][1] < right:
        uncovered.append([covered_intervals[-1][1] + 1, right])
    
    return uncovered

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (10, [[1, 3], [6, 8]], 0, 9, [[0, 0], [4, 5], [9, 9]]),
        (3, [[0, 2]], 0, 2, []),
        (7, [[2, 4]], 1, 6, [[1, 1], [5, 6]]),
        (5, [], 0, 4, [[0, 4]]),
        (10, [[0, 9]], 0, 9, []),
        (10, [[2, 3], [5, 6]], 0, 9, [[0, 1], [4, 4], [7, 9]]),
        (5, [[1, 1], [3, 3]], 0, 4, [[0, 0], [2, 2], [4, 4]])
    ]
    
    print("Testing main approach:")
    for n, ranges, left, right, expected in test_cases:
        result = findMaximalUncoveredRanges(n, ranges, left, right)
        print(f"findMaximalUncoveredRanges({n}, {ranges}, {left}, {right}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}\n")
    
    print("Testing simple approach:")
    for n, ranges, left, right, expected in test_cases:
        result = findMaximalUncoveredRangesSimple(n, ranges, left, right)
        print(f"findMaximalUncoveredRangesSimple({n}, {ranges}, {left}, {right}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}\n")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(R log R) where R is the number of ranges
- O(R log R) for sorting ranges
- O(R) for merging overlapping ranges
- O(R) for finding uncovered gaps
Space Complexity: O(R) - for storing filtered and merged ranges

Simple Approach:
Time Complexity: O(R * (right - left + 1) + (right - left + 1))
- O(R * (right - left + 1)) for marking covered positions
- O(right - left + 1) for finding uncovered ranges
Space Complexity: O(right - left + 1) - boolean array for covered positions

Optimized Approach:
Time Complexity: O(R log R) - for sorting events and processing
Space Complexity: O(R) - for storing events and covered intervals

Topic: Arrays, Intervals, Sorting, Merge Intervals
"""
