"""
LeetCode Problem #2705: Compact Object

Problem Statement:
Given an object or array `obj`, return a compact object. A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when `Boolean(value)` returns `false`.

Constraints:
- `obj` is a valid JSON object or array
- 2 <= JSON.stringify(obj).length <= 10^6

Note: This is a JavaScript problem but we'll implement it in Python for consistency.
"""

def compactObject(obj):
    """
    Removes falsy values from an object or array recursively.
    
    :param obj: Object or list to compact
    :return: Compacted object or list
    """
    if isinstance(obj, dict):
        # Handle dictionary/object
        result = {}
        for key, value in obj.items():
            # Recursively compact the value first
            compacted_value = compactObject(value)
            # Only include if the compacted value is truthy
            if compacted_value or compacted_value == 0:  # 0 is falsy but should be kept
                result[key] = compacted_value
        return result
    
    elif isinstance(obj, list):
        # Handle array/list
        result = []
        for item in obj:
            # Recursively compact the item first
            compacted_item = compactObject(item)
            # Only include if the compacted item is truthy
            if compacted_item or compacted_item == 0:  # 0 is falsy but should be kept
                result.append(compacted_item)
        return result
    
    else:
        # Handle primitive values
        return obj

def compactObjectPythonic(obj):
    """
    More Pythonic version with better falsy value handling.
    
    :param obj: Object or list to compact
    :return: Compacted object or list
    """
    def is_truthy(value):
        """Check if value should be kept (not falsy)"""
        # In JavaScript: false, 0, -0, 0n, "", null, undefined, NaN are falsy
        # In Python: False, 0, 0.0, "", [], {}, None are falsy
        return bool(value) or value == 0 or value == 0.0
    
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            compacted_value = compactObjectPythonic(value)
            if is_truthy(compacted_value):
                result[key] = compacted_value
        return result
    
    elif isinstance(obj, list):
        result = []
        for item in obj:
            compacted_item = compactObjectPythonic(item)
            if is_truthy(compacted_item):
                result.append(compacted_item)
        return result
    
    else:
        return obj

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Object with falsy values
    obj1 = [None, 0, False, 1]
    result1 = compactObject(obj1)
    print(f"Input: {obj1}")
    print(f"Output: {result1}")  # Output: [0, 1]
    print()

    # Test Case 2: Nested object
    obj2 = {"a": None, "b": [False, 1]}
    result2 = compactObject(obj2)
    print(f"Input: {obj2}")
    print(f"Output: {result2}")  # Output: {"b": [1]}
    print()

    # Test Case 3: Complex nested structure
    obj3 = [None, 0, 5, [0], [False, 16]]
    result3 = compactObject(obj3)
    print(f"Input: {obj3}")
    print(f"Output: {result3}")  # Output: [0, 5, [0], [16]]
    print()

    # Test Case 4: Object with nested objects and arrays
    obj4 = {
        "a": 1,
        "b": None,
        "c": {
            "x": False,
            "y": 2,
            "z": [0, None, 3, False]
        },
        "d": []
    }
    result4 = compactObject(obj4)
    print(f"Input: {obj4}")
    print(f"Output: {result4}")  # Output: {"a": 1, "c": {"y": 2, "z": [0, 3]}}
    print()

    # Test Case 5: All falsy values
    obj5 = {"a": None, "b": False, "c": ""}
    result5 = compactObject(obj5)
    print(f"Input: {obj5}")
    print(f"Output: {result5}")  # Output: {}
    print()

    # Test Pythonic version
    print("Testing Pythonic version:")
    result6 = compactObjectPythonic(obj4)
    print(f"Pythonic result: {result6}")

    # Validation
    assert compactObject([None, 0, False, 1]) == [0, 1]
    assert compactObject({"a": None, "b": [False, 1]}) == {"b": [1]}
    assert compactObject([None, 0, 5, [0], [False, 16]]) == [0, 5, [0], [16]]
    print("All test cases passed!")

"""
Time Complexity Analysis:
- Time complexity: O(n) where n is the total number of elements in the object/array including nested elements.
- Each element is visited once during the recursive traversal.

Space Complexity Analysis:
- Space complexity: O(d + n) where d is the maximum depth of nesting (for recursion stack) and n is the size of the result.
- In the worst case, if no elements are removed, space complexity is O(n).

Topic: Recursion, Object Manipulation, Deep Traversal
"""
