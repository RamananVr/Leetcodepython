"""
LeetCode Problem #2633: Convert Object to JSON String

Problem Statement:
Given an object, write a function that converts it to a JSON string. The object can contain 
nested objects, arrays, strings, numbers, booleans, and null values. You must not use the 
built-in `JSON.stringify` method in JavaScript or any equivalent library function in Python.

Constraints:
- The input object is guaranteed to be serializable.
- The object keys are strings.
- The object values can be one of the following types: string, number, boolean, null, array, or another object.

Your task is to implement a function `json_stringify` that takes an object as input and returns 
its JSON string representation.

Example:
Input: obj = {"key": "value", "key2": {"nestedKey": "nestedValue"}, "key3": [1, 2, 3]}
Output: '{"key":"value","key2":{"nestedKey":"nestedValue"},"key3":[1,2,3]}'
"""

# Solution
def json_stringify(obj):
    """
    Converts a Python object to a JSON string representation.
    
    :param obj: The input object to be converted.
    :return: A JSON string representation of the object.
    """
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return f'"{obj}"'
    elif isinstance(obj, list):
        return "[" + ",".join(json_stringify(item) for item in obj) + "]"
    elif isinstance(obj, dict):
        items = [f'"{key}":{json_stringify(value)}' for key, value in obj.items()]
        return "{" + ",".join(items) + "}"
    else:
        raise TypeError("Unsupported data type")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple object
    obj1 = {"key": "value", "key2": {"nestedKey": "nestedValue"}, "key3": [1, 2, 3]}
    print(json_stringify(obj1))  # Expected: '{"key":"value","key2":{"nestedKey":"nestedValue"},"key3":[1,2,3]}'

    # Test Case 2: Object with null and boolean values
    obj2 = {"isActive": True, "isDeleted": False, "data": None}
    print(json_stringify(obj2))  # Expected: '{"isActive":true,"isDeleted":false,"data":null}'

    # Test Case 3: Array of mixed types
    obj3 = [1, "string", True, None, {"nested": "object"}]
    print(json_stringify(obj3))  # Expected: '[1,"string",true,null,{"nested":"object"}]'

    # Test Case 4: Empty object and array
    obj4 = {}
    obj5 = []
    print(json_stringify(obj4))  # Expected: '{}'
    print(json_stringify(obj5))  # Expected: '[]'

    # Test Case 5: Nested arrays
    obj6 = {"array": [[1, 2], [3, 4]]}
    print(json_stringify(obj6))  # Expected: '{"array":[[1,2],[3,4]]}'

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function recursively processes each element in the object, array, or dictionary.
- For a nested object or array of depth `d` and size `n`, the time complexity is O(n), 
  where `n` is the total number of elements (keys + values).

Space Complexity:
- The space complexity is O(d), where `d` is the depth of the nested structure, due to 
  the recursive call stack.

Overall:
Time Complexity: O(n)
Space Complexity: O(d)
"""

# Topic: Strings, Recursion, JSON Serialization