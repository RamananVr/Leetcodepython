"""
LeetCode Question #56: Merge Intervals

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4
"""

def merge(intervals):
    """
    Merges overlapping intervals.

    :param intervals: List[List[int]] - A list of intervals where each interval is represented as [start, end].
    :return: List[List[int]] - A list of merged non-overlapping intervals.
    """
    # Step 1: Sort intervals by their start times
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the result list
    merged = []
    
    # Step 3: Iterate through the intervals
    for interval in intervals:
        # If the result list is empty or the current interval does not overlap with the last interval in the result list
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge the current interval with the last interval in the result list
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals1))  # Output: [[1,6],[8,10],[15,18]]

    # Test Case 2
    intervals2 = [[1,4],[4,5]]
    print(merge(intervals2))  # Output: [[1,5]]

    # Test Case 3
    intervals3 = [[1,4],[2,3]]
    print(merge(intervals3))  # Output: [[1,4]]

    # Test Case 4
    intervals4 = [[1,4],[5,6]]
    print(merge(intervals4))  # Output: [[1,4],[5,6]]

    # Test Case 5
    intervals5 = [[1,10],[2,3],[4,5],[6,7],[8,9]]
    print(merge(intervals5))  # Output: [[1,10]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- Iterating through the intervals takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space complexity is O(n) for the result list `merged`.
- Sorting the intervals in-place does not require additional space.
- Overall space complexity: O(n).

Topic: Arrays
"""