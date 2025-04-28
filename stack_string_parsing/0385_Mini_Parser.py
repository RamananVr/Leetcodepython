"""
LeetCode Problem #385: Mini Parser

Problem Statement:
Given a string s representing a nested list of integers, implement a parser to deserialize it into a NestedInteger.

Each element is either an integer, a list, or a list of lists. A NestedInteger is a class with the following interface:
- `isInteger()`: Returns true if this NestedInteger holds a single integer, rather than a nested list.
- `getInteger()`: Returns the single integer that this NestedInteger holds, if it holds a single integer. Returns None if this NestedInteger holds a nested list.
- `setInteger(value)`: Sets this NestedInteger to hold a single integer equal to value.
- `add(elem)`: Adds a NestedInteger element to this NestedInteger.
- `getList()`: Returns the nested list that this NestedInteger holds, if it holds a nested list. Returns None if this NestedInteger holds a single integer.

You are given a string s that represents a nested list of integers. Implement the function:
    def deserialize(s: str) -> NestedInteger

The input string is guaranteed to be valid and follows these rules:
1. Strings are non-empty and contain only digits, square brackets "[]", negative signs '-', and commas ','.
2. The string represents a valid nested list according to the problem description.

Example 1:
Input: s = "324"
Output: A NestedInteger object containing the integer 324.

Example 2:
Input: s = "[123,[456,[789]]]"
Output: A NestedInteger object containing a nested list with the structure [123,[456,[789]]].
"""

# Python Solution
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise, initializes a single integer equal to value.
        """
        if value is None:
            self._list = []
            self._integer = None
        else:
            self._list = None
            self._integer = value

    def isInteger(self):
        """
        Returns True if this NestedInteger holds a single integer, otherwise False.
        """
        return self._integer is not None

    def getInteger(self):
        """
        Returns the single integer that this NestedInteger holds, or None if it holds a nested list.
        """
        return self._integer

    def setInteger(self, value):
        """
        Sets this NestedInteger to hold a single integer.
        """
        self._integer = value
        self._list = None

    def add(self, elem):
        """
        Adds a NestedInteger element to this NestedInteger.
        """
        if self._list is None:
            self._list = []
        self._list.append(elem)

    def getList(self):
        """
        Returns the nested list that this NestedInteger holds, or None if it holds a single integer.
        """
        return self._list

def deserialize(s: str) -> NestedInteger:
    if s[0] != '[':  # If the string does not start with '[', it's a single integer.
        return NestedInteger(int(s))
    
    stack = []
    current = None
    num = ""
    
    for char in s:
        if char == '[':
            if current is not None:
                stack.append(current)
            current = NestedInteger()
        elif char == ']':
            if num:
                current.add(NestedInteger(int(num)))
                num = ""
            if stack:
                parent = stack.pop()
                parent.add(current)
                current = parent
        elif char == ',':
            if num:
                current.add(NestedInteger(int(num)))
                num = ""
        else:  # It's a number or part of a number (including '-').
            num += char
    
    return current

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Single integer
    s1 = "324"
    result1 = deserialize(s1)
    print(result1.getInteger())  # Output: 324

    # Test Case 2: Nested list
    s2 = "[123,[456,[789]]]"
    result2 = deserialize(s2)
    print(result2.getList())  # Output: NestedInteger structure representing [123, [456, [789]]]

    # Test Case 3: Empty list
    s3 = "[]"
    result3 = deserialize(s3)
    print(result3.getList())  # Output: []

    # Test Case 4: List with multiple integers
    s4 = "[1,2,3]"
    result4 = deserialize(s4)
    print(result4.getList())  # Output: NestedInteger structure representing [1, 2, 3]

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the length of the input string `s`. We process each character in the string once.
# Space Complexity: O(n), for the stack used to store NestedInteger objects during parsing.

# Topic: Stack, String Parsing