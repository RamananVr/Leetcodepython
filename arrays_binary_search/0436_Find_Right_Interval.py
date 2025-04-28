"""
LeetCode Problem #436: Find Right Interval

Problem Statement:
You are given an array of intervals, where intervals[i] = [start_i, end_i] represents the start and end of the ith interval. 
For each interval i, check if there exists an interval j whose start is greater than or equal to the end of interval i, 
and j is the minimum interval satisfying this condition. Return an array of indices answer, where answer[i] is the index 
of the interval j chosen. If no such interval exists, set answer[i] = -1.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it is impossible to find another interval.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: For interval [3,4], there is no interval that starts after 4, so answer[0] = -1.
For interval [2,3], the interval [3,4] starts after 3, so answer[1] = 0.
For interval [1,2], the interval [2,3] starts after 2, so answer[2] = 1.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: For interval [1,4], there is no interval that starts after 4, so answer[0] = -1.
For interval [2,3], the interval [3,4] starts after 3, so answer[1] = 2.
For interval [3,4], there is no interval that starts after 4, so answer[2] = -1.

Constraints:
- 1 <= intervals.length <= 2 * 10^4
- intervals[i].length == 2
- -10^6 <= start_i <= end_i <= 10^6
- The start point of each interval is unique.
"""

# Python Solution
from bisect import bisect_left

def findRightInterval(intervals):
    # Create a list of tuples (start, index) and sort it by start
    sorted_intervals = sorted((start, i) for i, (start, end) in enumerate(intervals))
    starts = [start for start, _ in sorted_intervals]
    result = []
    
    for _, end in intervals:
        # Use binary search to find the smallest start >= end
        idx = bisect_left(starts, end)
        if idx < len(starts):
            result.append(sorted_intervals[idx][1])
        else:
            result.append(-1)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1,2]]
    print(findRightInterval(intervals1))  # Output: [-1]

    # Test Case 2
    intervals2 = [[3,4],[2,3],[1,2]]
    print(findRightInterval(intervals2))  # Output: [-1,0,1]

    # Test Case 3
    intervals3 = [[1,4],[2,3],[3,4]]
    print(findRightInterval(intervals3))  # Output: [-1,2,-1]

    # Additional Test Case
    intervals4 = [[1,2],[2,3],[3,4],[4,5]]
    print(findRightInterval(intervals4))  # Output: [1,2,3,-1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the intervals by their start times takes O(n log n), where n is the number of intervals.
- For each interval, we perform a binary search on the sorted starts, which takes O(log n).
- Overall, the time complexity is O(n log n).

Space Complexity:
- The sorted_intervals list and starts list both take O(n) space.
- The result list also takes O(n) space.
- Therefore, the space complexity is O(n).

Topic: Arrays, Binary Search
"""