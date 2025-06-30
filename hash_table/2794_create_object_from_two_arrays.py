"""
2794. Create Object from Two Arrays

Problem Statement:
Given two arrays keys and values, return an object associated with the given keys and values.

If a key appears multiple times, the value appearing later in the values array should be used.

Constraints:
- keys.length == values.length
- 1 <= keys.length <= 100
- keys[i] is a string
- values[i] can be a string, number, boolean, or null

Test Cases:
1. Input: keys = ["name","age","gender"], values = ["Alice",25,"female"]
   Output: {"name":"Alice","age":25,"gender":"female"}
   
2. Input: keys = ["a","b","c","a"], values = [1,2,3,4]
   Output: {"a":4,"b":2,"c":3}
"""

from typing import List, Union, Any, Dict

def createObject(keys: List[str], values: List[Union[str, int, bool, None]]) -> Dict[str, Any]:
    """
    Create object from two arrays with later values overriding earlier ones.
    
    Algorithm:
    1. Iterate through keys and values simultaneously
    2. For duplicate keys, later values override earlier ones
    3. Return the resulting dictionary
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = {}
    
    for key, value in zip(keys, values):
        result[key] = value
    
    return result

def createObjectWithOrderTracking(keys: List[str], values: List[Union[str, int, bool, None]]) -> Dict[str, Any]:
    """
    Create object while tracking insertion order (Python 3.7+ maintains order).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import OrderedDict
    
    result = OrderedDict()
    
    for key, value in zip(keys, values):
        result[key] = value
    
    return dict(result)

def createObjectWithDuplicateHandling(keys: List[str], values: List[Union[str, int, bool, None]]) -> tuple:
    """
    Create object and return info about duplicates.
    
    Returns:
        (object, duplicate_keys, override_info)
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = {}
    seen_keys = set()
    duplicate_keys = set()
    override_info = {}
    
    for i, (key, value) in enumerate(zip(keys, values)):
        if key in seen_keys:
            duplicate_keys.add(key)
            if key not in override_info:
                override_info[key] = []
            override_info[key].append((i, result[key], value))
        else:
            seen_keys.add(key)
        
        result[key] = value
    
    return result, list(duplicate_keys), override_info

def createObjectReversed(keys: List[str], values: List[Union[str, int, bool, None]]) -> Dict[str, Any]:
    """
    Alternative approach: process from end to beginning to handle duplicates.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = {}
    
    # Process from end to beginning, only add if key not seen
    for i in range(len(keys) - 1, -1, -1):
        key, value = keys[i], values[i]
        if key not in result:
            result[key] = value
    
    return result

def createObjectWithValidation(keys: List[str], values: List[Union[str, int, bool, None]]) -> Dict[str, Any]:
    """
    Create object with input validation.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(keys) != len(values):
        raise ValueError("Keys and values arrays must have the same length")
    
    if not keys:
        return {}
    
    result = {}
    
    for key, value in zip(keys, values):
        if not isinstance(key, str):
            raise TypeError("All keys must be strings")
        result[key] = value
    
    return result

def createObjectJS(keys: List[str], values: List[Union[str, int, bool, None]]) -> str:
    """
    Create JavaScript object string representation.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def format_value(value):
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, str):
            return f'"{value}"'
        else:
            return str(value)
    
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    
    # Convert to JavaScript object string
    items = []
    for key, value in result.items():
        formatted_value = format_value(value)
        items.append(f'"{key}":{formatted_value}')
    
    return "{" + ",".join(items) + "}"

# Test cases
def test_create_object():
    # Test case 1: Basic functionality
    keys1 = ["name", "age", "gender"]
    values1 = ["Alice", 25, "female"]
    result1 = createObject(keys1, values1)
    print(f"Test 1 - Expected: {{'name':'Alice','age':25,'gender':'female'}}")
    print(f"Test 1 - Got: {result1}")
    
    # Test case 2: Duplicate keys
    keys2 = ["a", "b", "c", "a"]
    values2 = [1, 2, 3, 4]
    result2 = createObject(keys2, values2)
    print(f"Test 2 - Expected: {{'a':4,'b':2,'c':3}}")
    print(f"Test 2 - Got: {result2}")
    
    # Test case 3: Various data types
    keys3 = ["str", "num", "bool", "null"]
    values3 = ["hello", 42, True, None]
    result3 = createObject(keys3, values3)
    print(f"Test 3 - Mixed types: {result3}")
    
    # Test case 4: Empty arrays
    keys4 = []
    values4 = []
    result4 = createObject(keys4, values4)
    print(f"Test 4 - Empty arrays: {result4}")

def test_duplicate_handling():
    keys = ["x", "y", "x", "z", "y"]
    values = [1, 2, 3, 4, 5]
    
    obj, duplicates, override_info = createObjectWithDuplicateHandling(keys, values)
    
    print(f"Object: {obj}")
    print(f"Duplicate keys: {duplicates}")
    print(f"Override info: {override_info}")

def test_js_format():
    keys = ["name", "age", "active", "data"]
    values = ["John", 30, True, None]
    
    js_obj = createObjectJS(keys, values)
    print(f"JavaScript object: {js_obj}")

def test_validation():
    try:
        # Test mismatched lengths
        createObjectWithValidation(["a", "b"], [1])
    except ValueError as e:
        print(f"Validation error: {e}")
    
    try:
        # Test non-string key
        createObjectWithValidation([1, "b"], [1, 2])
    except TypeError as e:
        print(f"Type error: {e}")

if __name__ == "__main__":
    test_create_object()
    print()
    test_duplicate_handling()
    print()
    test_js_format()
    print()
    test_validation()

"""
Topic Classification: Hash Table, Arrays, Data Structures

Key Insights:
1. Simple dictionary creation with zip function
2. Later values automatically override earlier ones in Python dictionaries
3. Can track duplicates and override information if needed
4. Input validation important for robust implementation

Complexity Analysis:
- Time Complexity: O(n) where n is length of arrays
- Space Complexity: O(n) for the resulting dictionary
"""
