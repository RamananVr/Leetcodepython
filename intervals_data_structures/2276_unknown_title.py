"""
LeetCode Problem #2276: Count Integers in Intervals

Problem Statement:
A data structure is required to efficiently manage a set of intervals and count the number of integers contained within these intervals. Implement the `CountIntervals` class:

1. `CountIntervals()` Initializes the object with an empty set of intervals.
2. `add(left: int, right: int) -> None` Adds the interval `[left, right]` to the set of intervals. If any integers are already covered by existing intervals, they should not be double-counted.
3. `count() -> int` Returns the total number of integers that are covered by the intervals in the set.

Constraints:
- `1 <= left <= right <= 10^9`
- At most `10^5` calls will be made to `add` and `count`.

Example:
    obj = CountIntervals()
    obj.add(2, 3)
    obj.add(7, 10)
    print(obj.count())  # Output: 6
    obj.add(5, 8)
    print(obj.count())  # Output: 8
"""

from sortedcontainers import SortedDict

class CountIntervals:
    def __init__(self):
        # Use a sorted dictionary to store intervals
        self.intervals = SortedDict()
        self.total_count = 0

    def add(self, left: int, right: int) -> None:
        # Find the intervals that overlap with [left, right]
        start = self.intervals.bisect_left(left)
        end = self.intervals.bisect_right(right)
        
        # Merge overlapping intervals and update total_count
        keys_to_remove = []
        for key in list(self.intervals.islice(start, end)):
            l, r = key, self.intervals[key]
            if r < left or l > right:
                continue
            left = min(left, l)
            right = max(right, r)
            self.total_count -= (r - l + 1)
            keys_to_remove.append(l)
        
        # Remove merged intervals
        for key in keys_to_remove:
            del self.intervals[key]
        
        # Add the new merged interval
        self.intervals[left] = right
        self.total_count += (right - left + 1)

    def count(self) -> int:
        return self.total_count


# Example Test Cases
if __name__ == "__main__":
    obj = CountIntervals()
    obj.add(2, 3)
    obj.add(7, 10)
    print(obj.count())  # Output: 6
    obj.add(5, 8)
    print(obj.count())  # Output: 8

"""
Time and Space Complexity Analysis:

1. `add(left, right)`:
   - Time Complexity: O(k + log(n)), where `k` is the number of overlapping intervals and `n` is the number of intervals stored. The `bisect_left` and `bisect_right` operations take O(log(n)), and merging overlapping intervals takes O(k).
   - Space Complexity: O(n), where `n` is the number of intervals stored in the SortedDict.

2. `count()`:
   - Time Complexity: O(1), as it simply returns the precomputed `total_count`.
   - Space Complexity: O(1), as no additional space is used.

Topic: Intervals, Data Structures
"""