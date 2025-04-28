"""
LeetCode Question #2727: Is Object Equal

Problem Statement:
You are given two objects `obj1` and `obj2`. Write a function `isObjectEqual(obj1, obj2)` that determines if the two objects are deeply equal. Two objects are deeply equal if they have the same keys and values, and the values are also deeply equal if they are objects themselves.

Constraints:
- Objects can contain nested objects, arrays, or primitive values (strings, numbers, booleans, null).
- Arrays are considered deeply equal if they have the same length and their elements are deeply equal.
- Primitive values are considered deeply equal if they are strictly equal (`===` in JavaScript terms, equivalent to `==` in Python for primitives).
- The input objects will not contain circular references.

Write a function that returns `True` if the objects are deeply equal, otherwise `False`.
"""

def isObjectEqual(obj1, obj2):
    """
    Determines if two objects are deeply equal.

    Args:
        obj1: The first object to compare.
        obj2: The second object to compare.

    Returns:
        bool: True if the objects are deeply equal, False otherwise.
    """
    if obj1 == obj2:
        return True

    if isinstance(obj1, dict) and isinstance(obj2, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if not isObjectEqual(obj1[key], obj2[key]):
                return False
        return True

    if isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not isObjectEqual(obj1[i], obj2[i]):
                return False
        return True

    return False


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple equality
    obj1 = {"a": 1, "b": 2}
    obj2 = {"a": 1, "b": 2}
    print(isObjectEqual(obj1, obj2))  # Expected: True

    # Test Case 2: Nested objects
    obj1 = {"a": {"b": 2, "c": 3}, "d": 4}
    obj2 = {"a": {"b": 2, "c": 3}, "d": 4}
    print(isObjectEqual(obj1, obj2))  # Expected: True

    # Test Case 3: Different keys
    obj1 = {"a": 1, "b": 2}
    obj2 = {"a": 1, "c": 2}
    print(isObjectEqual(obj1, obj2))  # Expected: False

    # Test Case 4: Different values
    obj1 = {"a": 1, "b": 2}
    obj2 = {"a": 1, "b": 3}
    print(isObjectEqual(obj1, obj2))  # Expected: False

    # Test Case 5: Arrays
    obj1 = {"a": [1, 2, 3], "b": {"c": 4}}
    obj2 = {"a": [1, 2, 3], "b": {"c": 4}}
    print(isObjectEqual(obj1, obj2))  # Expected: True

    # Test Case 6: Arrays with different lengths
    obj1 = {"a": [1, 2], "b": {"c": 4}}
    obj2 = {"a": [1, 2, 3], "b": {"c": 4}}
    print(isObjectEqual(obj1, obj2))  # Expected: False

    # Test Case 7: Primitive values
    obj1 = 5
    obj2 = 5
    print(isObjectEqual(obj1, obj2))  # Expected: True

    # Test Case 8: Primitive values (different)
    obj1 = 5
    obj2 = 6
    print(isObjectEqual(obj1, obj2))  # Expected: False

    # Test Case 9: Null values
    obj1 = None
    obj2 = None
    print(isObjectEqual(obj1, obj2))  # Expected: True

    # Test Case 10: Mixed types
    obj1 = {"a": [1, {"b": 2}], "c": 3}
    obj2 = {"a": [1, {"b": 2}], "c": 3}
    print(isObjectEqual(obj1, obj2))  # Expected: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the total number of keys and elements in the objects and arrays.
- The function recursively compares all keys and values, so the time complexity is O(n).

Space Complexity:
- The space complexity is O(d), where `d` is the depth of the nested objects/arrays due to the recursive call stack.

Topic: Recursion, Hash Table, Arrays
"""