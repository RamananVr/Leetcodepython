"""
LeetCode Question #352: Data Stream as Disjoint Intervals

Problem Statement:
Given a data stream input of non-negative integers `a1, a2, ..., an`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:
- `SummaryRanges()` Initializes the object with an empty stream.
- `void addNum(int value)` Adds the integer `value` to the stream.
- `List[List[int]] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[starti, endi]`. The intervals should be sorted by the start value.

Constraints:
1. `0 <= value <= 10^4`
2. At most `3 * 10^4` calls will be made to `addNum` and `getIntervals`.

Example:
Input:
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]

Output:
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation:
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
"""

from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        # Use a SortedDict to store intervals with the start of the interval as the key
        self.intervals = SortedDict()

    def addNum(self, value: int) -> None:
        if value in self.intervals:
            return  # Value is already part of an interval

        # Find the intervals immediately before and after the value
        lower_key = self.intervals.bisect_left(value) - 1
        higher_key = self.intervals.bisect_right(value)

        lower_interval = self.intervals.peekitem(lower_key)[1] if lower_key >= 0 else None
        higher_interval = self.intervals.peekitem(higher_key)[1] if higher_key < len(self.intervals) else None

        # Check if the value can merge with the lower interval
        merge_with_lower = lower_interval and lower_interval[1] + 1 == value
        # Check if the value can merge with the higher interval
        merge_with_higher = higher_interval and higher_interval[0] - 1 == value

        if merge_with_lower and merge_with_higher:
            # Merge both intervals into one
            new_start = lower_interval[0]
            new_end = higher_interval[1]
            del self.intervals[lower_interval[0]]
            del self.intervals[higher_interval[0]]
            self.intervals[new_start] = [new_start, new_end]
        elif merge_with_lower:
            # Extend the lower interval
            self.intervals[lower_interval[0]][1] += 1
        elif merge_with_higher:
            # Extend the higher interval
            new_start = value
            new_end = higher_interval[1]
            del self.intervals[higher_interval[0]]
            self.intervals[new_start] = [new_start, new_end]
        else:
            # Create a new interval
            self.intervals[value] = [value, value]

    def getIntervals(self) -> list[list[int]]:
        return list(self.intervals.values())


# Example Test Cases
if __name__ == "__main__":
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    print(summaryRanges.getIntervals())  # Output: [[1, 1]]
    summaryRanges.addNum(3)
    print(summaryRanges.getIntervals())  # Output: [[1, 1], [3, 3]]
    summaryRanges.addNum(7)
    print(summaryRanges.getIntervals())  # Output: [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)
    print(summaryRanges.getIntervals())  # Output: [[1, 3], [7, 7]]
    summaryRanges.addNum(6)
    print(summaryRanges.getIntervals())  # Output: [[1, 3], [6, 7]]

"""
Time Complexity:
- `addNum`: O(log(n)) for insertion and deletion in the SortedDict.
- `getIntervals`: O(n) to retrieve all intervals.

Space Complexity:
- O(n) for storing the intervals in the SortedDict.

Topic: Data Structures (SortedDict, Intervals)
"""