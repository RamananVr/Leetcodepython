"""
LeetCode Problem #2628: JSON Deep Equal

Problem Statement:
Given two JSON objects `o1` and `o2`, write a function `areDeeplyEqual(o1, o2)` that determines if they are deeply equal. 
Two objects are considered deeply equal if they have the same structure and values.

- Two objects are deeply equal if:
  1. They are both arrays and their elements are deeply equal.
  2. They are both objects and their keys and values are deeply equal.
  3. They are both primitives and are strictly equal.

Constraints:
- The JSON objects can contain nested arrays, objects, strings, numbers, booleans, and null values.
- The function should handle edge cases like empty objects, empty arrays, and null values.

Write a function that returns `True` if the two JSON objects are deeply equal, otherwise return `False`.
"""

def areDeeplyEqual(o1, o2):
    """
    Determines if two JSON objects are deeply equal.

    :param o1: First JSON object
    :param o2: Second JSON object
    :return: True if the objects are deeply equal, False otherwise
    """
    # If both are primitives or None, check for strict equality
    if type(o1) != type(o2):
        return False
    if isinstance(o1, (int, float, str, bool)) or o1 is None:
        return o1 == o2

    # If both are lists, compare their elements recursively
    if isinstance(o1, list) and isinstance(o2, list):
        if len(o1) != len(o2):
            return False
        return all(areDeeplyEqual(x, y) for x, y in zip(o1, o2))

    # If both are dictionaries, compare their keys and values recursively
    if isinstance(o1, dict) and isinstance(o2, dict):
        if set(o1.keys()) != set(o2.keys()):
            return False
        return all(areDeeplyEqual(o1[key], o2[key]) for key in o1)

    # If none of the above, they are not deeply equal
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple primitives
    assert areDeeplyEqual(1, 1) == True
    assert areDeeplyEqual(1, 2) == False

    # Test Case 2: Nested arrays
    assert areDeeplyEqual([1, 2, [3, 4]], [1, 2, [3, 4]]) == True
    assert areDeeplyEqual([1, 2, [3, 4]], [1, 2, [4, 3]]) == False

    # Test Case 3: Nested dictionaries
    assert areDeeplyEqual({"a": 1, "b": {"c": 2}}, {"a": 1, "b": {"c": 2}}) == True
    assert areDeeplyEqual({"a": 1, "b": {"c": 2}}, {"a": 1, "b": {"c": 3}}) == False

    # Test Case 4: Mixed types
    assert areDeeplyEqual({"a": [1, 2]}, {"a": [1, 2]}) == True
    assert areDeeplyEqual({"a": [1, 2]}, {"a": [2, 1]}) == False

    # Test Case 5: Null values
    assert areDeeplyEqual(None, None) == True
    assert areDeeplyEqual(None, 0) == False

    # Test Case 6: Empty structures
    assert areDeeplyEqual([], []) == True
    assert areDeeplyEqual({}, {}) == True
    assert areDeeplyEqual([], {}) == False

    print("All test cases passed!")

"""
Time Complexity:
- Let `n` be the total number of elements (including nested elements) in the JSON objects.
- In the worst case, we compare every element in both objects, so the time complexity is O(n).

Space Complexity:
- The space complexity is O(d), where `d` is the maximum depth of the nested structure, due to the recursive call stack.

Topic: Recursion, JSON, Deep Comparison
"""