"""
LeetCode Problem #715: Range Module

Problem Statement:
A Range Module is a module that tracks ranges of numbers. Your task is to implement the RangeModule class, which supports the following methods:

1. addRange(left: int, right: int) -> None:
   Adds the range [left, right) to the module. If the range already exists, it does nothing. If part of the range overlaps with existing ranges, it merges them.

2. queryRange(left: int, right: int) -> bool:
   Returns true if the range [left, right) is completely covered by the module, otherwise returns false.

3. removeRange(left: int, right: int) -> None:
   Removes the range [left, right) from the module. If part of the range overlaps with existing ranges, it removes only the overlapping portion.

Constraints:
- 1 <= left < right <= 10^9
- At most 10^4 calls will be made to addRange, queryRange, and removeRange.

"""

# Solution
from sortedcontainers import SortedDict

class RangeModule:
    def __init__(self):
        self.ranges = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        # Find the starting point for merging
        start = self.ranges.bisect_left(left)
        if start > 0 and self.ranges.peekitem(start - 1)[1] >= left:
            start -= 1

        # Merge overlapping ranges
        new_left, new_right = left, right
        while start < len(self.ranges) and self.ranges.peekitem(start)[0] <= right:
            new_left = min(new_left, self.ranges.peekitem(start)[0])
            new_right = max(new_right, self.ranges.peekitem(start)[1])
            self.ranges.popitem(start)

        self.ranges[new_left] = new_right

    def queryRange(self, left: int, right: int) -> bool:
        # Find the range that might contain [left, right)
        start = self.ranges.bisect_right(left)
        if start == 0:
            return False
        start -= 1
        return self.ranges.peekitem(start)[0] <= left and self.ranges.peekitem(start)[1] >= right

    def removeRange(self, left: int, right: int) -> None:
        # Find the starting point for splitting/removing
        start = self.ranges.bisect_left(left)
        if start > 0 and self.ranges.peekitem(start - 1)[1] > left:
            start -= 1

        # Remove or split overlapping ranges
        to_add = []
        while start < len(self.ranges) and self.ranges.peekitem(start)[0] < right:
            cur_left, cur_right = self.ranges.popitem(start)
            if cur_left < left:
                to_add.append((cur_left, left))
            if cur_right > right:
                to_add.append((right, cur_right))

        for l, r in to_add:
            self.ranges[l] = r


# Example Test Cases
if __name__ == "__main__":
    rm = RangeModule()
    
    # Test Case 1: Add and Query
    rm.addRange(10, 20)
    assert rm.queryRange(10, 15) == True  # Fully covered
    assert rm.queryRange(15, 25) == False  # Partially covered
    
    # Test Case 2: Remove and Query
    rm.removeRange(14, 16)
    assert rm.queryRange(10, 14) == True  # Fully covered
    assert rm.queryRange(14, 16) == False  # Removed
    assert rm.queryRange(16, 20) == True  # Fully covered
    
    # Test Case 3: Add overlapping ranges
    rm.addRange(18, 25)
    assert rm.queryRange(18, 25) == True  # Fully covered
    assert rm.queryRange(10, 25) == False  # Not fully covered
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. addRange(left, right):
   - Time Complexity: O(n), where n is the number of ranges in the module. This is due to merging overlapping ranges.
   - Space Complexity: O(n), as we store the ranges in a SortedDict.

2. queryRange(left, right):
   - Time Complexity: O(log n), where n is the number of ranges in the module. This is due to the binary search in SortedDict.
   - Space Complexity: O(1), as no additional space is used.

3. removeRange(left, right):
   - Time Complexity: O(n), where n is the number of ranges in the module. This is due to splitting/removing overlapping ranges.
   - Space Complexity: O(n), as we store the ranges in a SortedDict.

Topic: Intervals
"""