"""
LeetCode Problem #2705: Compact Object Python Solution

Problem Statement:
You are given an object `obj`. Write a function `compactObject(obj)` that takes in the object and removes all falsy values (e.g., `false`, `null`, `undefined`, `0`, `NaN`, `""`) while preserving the structure of the object. If the object is an array, it should remove falsy values from the array. If the object is a nested object, it should recursively compact the nested object.

The function should return the compacted object.

Constraints:
- The input object can be deeply nested.
- The input object can contain arrays, objects, and primitive values.
- Falsy values include: `false`, `null`, `undefined`, `0`, `NaN`, and `""`.

Example:
Input: obj = {"a": null, "b": [false, 1, 0], "c": {"d": 0, "e": "test"}}
Output: {"b": [1], "c": {"e": "test"}}
"""

# Solution
def compactObject(obj):
    if isinstance(obj, list):
        # If obj is a list, filter out falsy values and recursively compact each element
        return [compactObject(item) for item in obj if item]
    elif isinstance(obj, dict):
        # If obj is a dictionary, recursively compact each value and remove falsy values
        return {key: compactObject(value) for key, value in obj.items() if value}
    else:
        # If obj is a primitive value, return it as is
        return obj

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Nested dictionary and array
    obj1 = {"a": None, "b": [False, 1, 0], "c": {"d": 0, "e": "test"}}
    print(compactObject(obj1))  # Expected Output: {"b": [1], "c": {"e": "test"}}

    # Test Case 2: Empty dictionary
    obj2 = {}
    print(compactObject(obj2))  # Expected Output: {}

    # Test Case 3: Array with falsy values
    obj3 = [0, False, "", None, 5, "hello"]
    print(compactObject(obj3))  # Expected Output: [5, "hello"]

    # Test Case 4: Deeply nested structure
    obj4 = {"x": {"y": {"z": [0, None, "value"]}}, "a": False}
    print(compactObject(obj4))  # Expected Output: {"x": {"y": {"z": ["value"]}}}

    # Test Case 5: Primitive value
    obj5 = 0
    print(compactObject(obj5))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the total number of elements in the input object (including nested elements).
- The function processes each element once, so the time complexity is O(n).

Space Complexity:
- The space complexity depends on the depth of the nested structure.
- In the worst case, the recursion stack can grow to the depth of the nested structure, so the space complexity is O(d), where d is the maximum depth of the input object.
"""

# Topic: Recursion, Hashmap, Arrays