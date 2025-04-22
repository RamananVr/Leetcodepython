"""
LeetCode Question #364: Nested List Weight Sum II

Problem Statement:
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. The depth of an integer is the number of lists that it is inside of. For example, the integer 2 has a depth of 2 if it is inside a list that is inside another list.

Return the sum of each integer in `nestedList` multiplied by its depth. However, the weight of an integer is defined as the maximum depth of the list minus the depth of the integer, plus 1. In other words, the weight of an integer is inversely proportional to its depth.

Example:
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: The maximum depth is 2. At depth 1, we have integers [2], so the weight is 2. At depth 2, we have integers [1,1,1,1], so the weight is 1.
Weighted sum = (2 * 2) + (1 * 1) + (1 * 1) + (1 * 1) + (1 * 1) = 8.

Constraints:
- The depth of the nested list does not exceed 50.
- The total number of integers in the nested list is in the range [1, 1000].
"""

from typing import List

class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation.
    """
    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getInteger(self) -> int:
        """Return the single integer that this NestedInteger holds, if it holds a single integer. Return None if it holds a nested list."""
        pass

    def getList(self) -> List['NestedInteger']:
        """Return the nested list that this NestedInteger holds, if it holds a nested list. Return None if it holds a single integer."""
        pass

def depthSumInverse(nestedList: List[NestedInteger]) -> int:
    """
    Calculate the weighted sum of integers in the nested list where the weight is inversely proportional to the depth.
    """
    def get_max_depth(nested_list, depth):
        max_depth = depth
        for ni in nested_list:
            if not ni.isInteger():
                max_depth = max(max_depth, get_max_depth(ni.getList(), depth + 1))
        return max_depth

    def get_weighted_sum(nested_list, depth, max_depth):
        total = 0
        for ni in nested_list:
            if ni.isInteger():
                total += ni.getInteger() * (max_depth - depth + 1)
            else:
                total += get_weighted_sum(ni.getList(), depth + 1, max_depth)
        return total

    max_depth = get_max_depth(nestedList, 1)
    return get_weighted_sum(nestedList, 1, max_depth)

# Example Test Cases
class NestedIntegerImpl(NestedInteger):
    """
    A concrete implementation of NestedInteger for testing purposes.
    """
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer

    def getList(self) -> List[NestedInteger]:
        return self._list

# Test Case 1
nestedList1 = [
    NestedIntegerImpl([NestedIntegerImpl(1), NestedIntegerImpl(1)]),
    NestedIntegerImpl(2),
    NestedIntegerImpl([NestedIntegerImpl(1), NestedIntegerImpl(1)])
]
print(depthSumInverse(nestedList1))  # Output: 8

# Test Case 2
nestedList2 = [
    NestedIntegerImpl(1),
    NestedIntegerImpl([NestedIntegerImpl(4), NestedIntegerImpl([NestedIntegerImpl(6)])])
]
print(depthSumInverse(nestedList2))  # Output: 17

# Test Case 3
nestedList3 = [
    NestedIntegerImpl([NestedIntegerImpl([NestedIntegerImpl(1)])])
]
print(depthSumInverse(nestedList3))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `get_max_depth` function traverses the entire nested list structure once, which takes O(n), where n is the total number of integers and lists in the nested structure.
- The `get_weighted_sum` function also traverses the entire nested list structure once, which takes O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion depth, which is proportional to the maximum depth of the nested list. In the worst case, the space complexity is O(d), where d is the maximum depth of the nested list.
"""

# Topic: Depth-First Search (DFS), Recursion