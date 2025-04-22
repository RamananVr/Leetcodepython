"""
LeetCode Question #341: Flatten Nested List Iterator

Problem Statement:
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:
- `NestedIterator(List[NestedInteger] nestedList)` Initializes the iterator with the nested list `nestedList`.
- `int next()` Returns the next integer in the nested list.
- `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:
```
nestedList = [NestedInteger([1,1]), NestedInteger(2), NestedInteger([1,1])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
```
`v` should be `[1,1,2,1,1]`.

Constraints:
- The input list's length is in the range `[1, 500]`.
- The values of the integers in the nested list are in the range `[-10^6, 10^6]`.

Note: The `NestedInteger` class is provided for you. You cannot make any assumptions about its implementation.
"""

from typing import List

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list.
        """
        pass

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer.
        """
        pass

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        Initialize the iterator with the nested list.
        """
        self.stack = []
        self._flatten(nestedList)

    def _flatten(self, nestedList: List[NestedInteger]):
        """
        Helper function to flatten the nested list into a stack.
        """
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self) -> int:
        """
        Return the next integer in the nested list.
        """
        if self.hasNext():
            return self.stack.pop().getInteger()
        return None

    def hasNext(self) -> bool:
        """
        Return True if there are still integers to be iterated over.
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._flatten(top.getList())
        return False

# Example Test Cases
if __name__ == "__main__":
    # Mock NestedInteger class for testing
    class MockNestedInteger(NestedInteger):
        def __init__(self, value):
            if isinstance(value, int):
                self.value = value
                self.is_int = True
            else:
                self.value = value
                self.is_int = False

        def isInteger(self) -> bool:
            return self.is_int

        def getInteger(self) -> int:
            if self.is_int:
                return self.value
            return None

        def getList(self) -> List['NestedInteger']:
            if not self.is_int:
                return self.value
            return None

    # Test case 1
    nestedList = [
        MockNestedInteger([MockNestedInteger(1), MockNestedInteger(1)]),
        MockNestedInteger(2),
        MockNestedInteger([MockNestedInteger(1), MockNestedInteger(1)])
    ]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)  # Output: [1, 1, 2, 1, 1]

    # Test case 2
    nestedList = [
        MockNestedInteger(1),
        MockNestedInteger([MockNestedInteger(4), MockNestedInteger([MockNestedInteger(6)])])
    ]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)  # Output: [1, 4, 6]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `hasNext` and `next` methods together process each element of the nested list exactly once.
   - Flattening a nested list is proportional to the total number of integers in the nested structure, denoted as `n`.
   - Therefore, the overall time complexity is O(n).

2. Space Complexity:
   - The space complexity is determined by the stack used to store the elements of the nested list.
   - In the worst case, the stack can grow to hold all elements of the nested list, which is O(n).

Topic: Stack
"""