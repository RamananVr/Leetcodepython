"""
LeetCode Problem #2649: Nested Array Generator

Problem Statement:
Given a nested array of integers, implement a generator function that flattens the array. 
The generator should yield each integer in the array in a depth-first order.

Example:
Input: nestedList = [[1, 2], [3, [4, 5]]]
Output: [1, 2, 3, 4, 5]

Constraints:
- The input array can be arbitrarily nested.
- The elements of the array are either integers or other arrays.
- The generator should yield integers one by one in depth-first order.
"""

# Solution
def* nested_array_generator(nestedList):
    """
    A generator function to flatten a nested array of integers.

    Args:
    nestedList (list): A nested list of integers.

    Yields:
    int: The next integer in depth-first order.
    """
    for element in nestedList:
        if isinstance(element, list):
            yield from nested_array_generator(element)
        else:
            yield element

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nestedList1 = [[1, 2], [3, [4, 5]]]
    print(list(nested_array_generator(nestedList1)))  # Output: [1, 2, 3, 4, 5]

    # Test Case 2
    nestedList2 = [1, [2, [3, [4, 5]]]]
    print(list(nested_array_generator(nestedList2)))  # Output: [1, 2, 3, 4, 5]

    # Test Case 3
    nestedList3 = [1, 2, 3]
    print(list(nested_array_generator(nestedList3)))  # Output: [1, 2, 3]

    # Test Case 4
    nestedList4 = []
    print(list(nested_array_generator(nestedList4)))  # Output: []

    # Test Case 5
    nestedList5 = [[[[1]]], 2, [[3, 4]], 5]
    print(list(nested_array_generator(nestedList5)))  # Output: [1, 2, 3, 4, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the total number of integers in the nested list.
- The generator visits each integer exactly once, so the time complexity is O(n).

Space Complexity:
- The space complexity depends on the maximum depth of the nested list, d.
- At most, d recursive calls will be on the call stack at any time.
- Therefore, the space complexity is O(d).
"""

# Topic: Recursion