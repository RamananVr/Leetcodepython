"""
LeetCode Problem #339: Nested List Weight Sum

Problem Statement:
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. The "depth" of an integer is the number of lists that it is inside. For example, the integer 2 has a depth of 1 if it is directly inside the outermost list, and a depth of 2 if it is inside a list that is inside the outermost list.

Return the sum of all integers in the list weighted by their depth. Each integer is multiplied by its depth.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.

Constraints:
- The nested list structure is guaranteed to be well-formed and non-empty.
"""

from typing import List

# Definition for NestedInteger
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty nested list.
        Otherwise, initializes a single integer equal to value.
        """
        self.value = value
        self.is_integer = isinstance(value, int)
        self.nested_list = [] if not self.is_integer else None

    def isInteger(self) -> bool:
        """
        Return True if this NestedInteger holds a single integer, otherwise False.
        """
        return self.is_integer

    def getInteger(self) -> int:
        """
        Return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list.
        """
        return self.value if self.is_integer else None

    def getList(self) -> List['NestedInteger']:
        """
        Return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer.
        """
        return self.nested_list if not self.is_integer else None

def depthSum(nestedList: List[NestedInteger]) -> int:
    """
    Calculate the weighted sum of all integers in the nested list based on their depth.
    """
    def dfs(nested_list, depth):
        total = 0
        for ni in nested_list:
            if ni.isInteger():
                total += ni.getInteger() * depth
            else:
                total += dfs(ni.getList(), depth + 1)
        return total

    return dfs(nestedList, 1)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create NestedInteger objects
    def create_nested_list(data):
        if isinstance(data, int):
            return NestedInteger(data)
        nested_integer = NestedInteger()
        nested_integer.nested_list = [create_nested_list(item) for item in data]
        return nested_integer

    # Test Case 1
    nestedList1 = [create_nested_list([1, 1]), create_nested_list(2), create_nested_list([1, 1])]
    print(depthSum(nestedList1))  # Output: 10

    # Test Case 2
    nestedList2 = [create_nested_list(1), create_nested_list([4, [6]])]
    print(depthSum(nestedList2))  # Output: 27

    # Test Case 3
    nestedList3 = [create_nested_list([1, [2, [3]]])]
    print(depthSum(nestedList3))  # Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let n be the total number of integers and lists in the nested structure.
- The function traverses each element exactly once, so the time complexity is O(n).

Space Complexity:
- The space complexity is O(d), where d is the maximum depth of the nested list.
- This is due to the recursive call stack.

Topic: Depth-First Search (DFS), Recursion
"""