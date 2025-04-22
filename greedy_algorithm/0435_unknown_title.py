"""
LeetCode Problem #435: Non-overlapping Intervals

Problem Statement:
Given an array of intervals `intervals` where intervals[i] = [start_i, end_i], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Constraints:
1. 1 <= intervals.length <= 10^5
2. intervals[i].length == 2
3. -5 * 10^4 <= start_i < end_i <= 5 * 10^4

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any intervals since they are already non-overlapping.
"""

def erase_overlap_intervals(intervals):
    """
    Function to find the minimum number of intervals to remove to make the rest non-overlapping.

    :param intervals: List[List[int]] - List of intervals where each interval is [start, end]
    :return: int - Minimum number of intervals to remove
    """
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    # Initialize variables
    non_overlapping_count = 0
    prev_end = float('-inf')
    
    # Iterate through the intervals
    for start, end in intervals:
        if start >= prev_end:
            # If the current interval does not overlap with the previous one, include it
            non_overlapping_count += 1
            prev_end = end
        # Otherwise, skip the current interval (remove it)
    
    # Total intervals - non-overlapping intervals = intervals to remove
    return len(intervals) - non_overlapping_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(erase_overlap_intervals(intervals1))  # Output: 1

    # Test Case 2
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    print(erase_overlap_intervals(intervals2))  # Output: 2

    # Test Case 3
    intervals3 = [[1, 2], [2, 3]]
    print(erase_overlap_intervals(intervals3))  # Output: 0

    # Test Case 4
    intervals4 = [[1, 5], [2, 3], [3, 4], [4, 6]]
    print(erase_overlap_intervals(intervals4))  # Output: 1

    # Test Case 5
    intervals5 = [[1, 100], [2, 3], [3, 4], [4, 5]]
    print(erase_overlap_intervals(intervals5))  # Output: 1

"""
Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- Iterating through the intervals takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation uses O(1) additional space if done in-place, or O(n) if not.
- The algorithm itself uses O(1) additional space for variables.
- Overall space complexity: O(1).

Topic: Greedy Algorithm
"""