"""
LeetCode Problem #57: Insert Interval

Problem Statement:
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^5
- intervals is sorted by `start_i` in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5
"""

def insert(intervals, newInterval):
    """
    Inserts a new interval into a list of sorted, non-overlapping intervals and merges if necessary.

    :param intervals: List[List[int]] - List of sorted, non-overlapping intervals
    :param newInterval: List[int] - The new interval to insert
    :return: List[List[int]] - The updated list of intervals
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add all intervals that come after the new interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    print(insert(intervals1, newInterval1))  # Output: [[1, 5], [6, 9]]

    # Test Case 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    print(insert(intervals2, newInterval2))  # Output: [[1, 2], [3, 10], [12, 16]]

    # Test Case 3
    intervals3 = []
    newInterval3 = [5, 7]
    print(insert(intervals3, newInterval3))  # Output: [[5, 7]]

    # Test Case 4
    intervals4 = [[1, 5]]
    newInterval4 = [2, 3]
    print(insert(intervals4, newInterval4))  # Output: [[1, 5]]

    # Test Case 5
    intervals5 = [[1, 5]]
    newInterval5 = [6, 8]
    print(insert(intervals5, newInterval5))  # Output: [[1, 5], [6, 8]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the list of intervals once, performing constant-time operations for each interval.
- Therefore, the time complexity is O(n), where n is the number of intervals.

Space Complexity:
- The algorithm uses a result list to store the merged intervals. In the worst case, the result list contains all the original intervals plus the new interval.
- Therefore, the space complexity is O(n), where n is the number of intervals.

Topic: Arrays
"""