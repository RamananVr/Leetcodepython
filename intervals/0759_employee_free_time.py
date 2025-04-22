"""
LeetCode Question #759: Employee Free Time

Problem Statement:
We are given a list `schedule` of employees, where each employee's schedule is represented as a list of non-overlapping intervals. Each interval is a pair of integers `[start, end]` representing the start and end time of the interval.

Return a list of intervals representing the common free time for all employees, sorted in increasing order. The common free time is the time that all employees are free, and it should be represented as a list of intervals `[start, end]`.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and their schedules are:
Employee 1: [1, 2], [5, 6]
Employee 2: [1, 3]
Employee 3: [4, 10]
The common free time is [3, 4].

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Constraints:
- `1 <= schedule.length, schedule[i].length <= 50`
- `0 <= schedule[i][j][0] < schedule[i][j][1] <= 10^8`

"""

# Python Solution
from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        # Flatten all intervals into a single list
        intervals = [interval for employee in schedule for interval in employee]
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # Merge overlapping intervals
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        
        # Find gaps between merged intervals
        free_time = []
        for i in range(1, len(merged)):
            free_time.append(Interval(merged[i-1].end, merged[i].start))
        
        return free_time

# Example Test Cases
if __name__ == "__main__":
    # Helper function to convert list of lists to list of Interval objects
    def create_schedule(schedule):
        return [[Interval(start, end) for start, end in employee] for employee in schedule]

    # Test Case 1
    schedule1 = create_schedule([[[1,2],[5,6]],[[1,3]],[[4,10]]])
    solution = Solution()
    print(solution.employeeFreeTime(schedule1))  # Output: [[3,4]]

    # Test Case 2
    schedule2 = create_schedule([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])
    print(solution.employeeFreeTime(schedule2))  # Output: [[5,6],[7,9]]

"""
Time and Space Complexity Analysis:

Time Complexity:
1. Flattening the schedule into a single list of intervals takes O(N), where N is the total number of intervals across all employees.
2. Sorting the intervals by start time takes O(N log N).
3. Merging intervals takes O(N).
4. Finding gaps between merged intervals takes O(M), where M is the number of merged intervals.

Overall, the time complexity is O(N log N).

Space Complexity:
1. The flattened list of intervals takes O(N) space.
2. The merged intervals list takes O(M) space.
3. The free time intervals list takes O(F) space, where F is the number of free time intervals.

Overall, the space complexity is O(N + M + F), which is dominated by O(N).

Topic: Intervals
"""