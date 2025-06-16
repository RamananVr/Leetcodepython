"""
LeetCode Question #2727: Is Object Empty

Problem Statement:
Given an object or an array, return if it is empty.

- An empty object contains no key-value pairs.
- An empty array contains no elements.

You may assume the object or array is the output of `JSON.parse`.

Constraints:
- `obj` is a valid JSON object or array
- `2 <= JSON.stringify(obj).length <= 10^5`

Example:
Input: obj = {"x": 5, "y": 42}
Output: false
Explanation: The object has 2 key-value pairs so it is not empty.

Input: obj = {}
Output: true
Explanation: The object doesn't have any key-value pairs so it is empty.

Input: obj = [null, false, 0]
Output: false
Explanation: The array has 3 elements so it is not empty.
"""

def isEmpty(obj):
    """
    Check if an object or array is empty.
    
    Args:
        obj: Dictionary (object) or list (array) to check
    
    Returns:
        Boolean indicating if the object/array is empty
    """
    if isinstance(obj, dict):
        return len(obj) == 0
    elif isinstance(obj, list):
        return len(obj) == 0
    else:
        # For other types, consider non-empty
        return False

def isEmpty_pythonic(obj):
    """
    Pythonic approach using truthiness.
    
    Args:
        obj: Dictionary or list to check
    
    Returns:
        Boolean indicating if empty
    """
    return not obj

def isEmpty_explicit_type_check(obj):
    """
    Explicit type checking approach.
    
    Args:
        obj: Object to check for emptiness
    
    Returns:
        Boolean indicating if empty
    """
    if isinstance(obj, dict):
        return not bool(obj)
    elif isinstance(obj, list):
        return not bool(obj)
    elif isinstance(obj, tuple):
        return not bool(obj)
    elif isinstance(obj, set):
        return not bool(obj)
    elif isinstance(obj, str):
        return obj == ""
    else:
        return False

def isEmpty_try_except(obj):
    """
    Try-except approach for error handling.
    
    Args:
        obj: Object to check
    
    Returns:
        Boolean indicating if empty
    """
    try:
        return len(obj) == 0
    except TypeError:
        # Object doesn't support len()
        return False

def isEmpty_comprehensive(obj):
    """
    Comprehensive check for various empty states.
    
    Args:
        obj: Object to check
    
    Returns:
        Boolean indicating if empty
    """
    # Handle None
    if obj is None:
        return True
    
    # Handle containers with len()
    try:
        return len(obj) == 0
    except TypeError:
        pass
    
    # Handle numeric types
    if isinstance(obj, (int, float, complex)):
        return obj == 0
    
    # Handle boolean
    if isinstance(obj, bool):
        return not obj
    
    # Default to non-empty for unknown types
    return False

def isEmpty_generator_aware(obj):
    """
    Generator-aware emptiness check.
    
    Args:
        obj: Object to check
    
    Returns:
        Boolean indicating if empty
    """
    import types
    
    if isinstance(obj, (dict, list, tuple, set, str)):
        return len(obj) == 0
    elif isinstance(obj, types.GeneratorType):
        # Check if generator is exhausted (careful - this consumes it)
        try:
            next(obj)
            return False  # Has at least one element
        except StopIteration:
            return True   # Generator is exhausted
    else:
        return not bool(obj)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 - Non-empty object
    obj = {"x": 5, "y": 42}
    result = isEmpty(obj)
    print(f"Test 1 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 2 - Empty object
    obj = {}
    result = isEmpty(obj)
    print(f"Test 2 - Expected: True, Got: {result}")
    assert result == True
    
    # Test Case 3 - Non-empty array
    obj = [None, False, 0]
    result = isEmpty(obj)
    print(f"Test 3 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 4 - Empty array
    obj = []
    result = isEmpty(obj)
    print(f"Test 4 - Expected: True, Got: {result}")
    assert result == True
    
    # Test Case 5 - Array with single element
    obj = [1]
    result = isEmpty(obj)
    print(f"Test 5 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 6 - Object with single key-value pair
    obj = {"a": 1}
    result = isEmpty(obj)
    print(f"Test 6 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 7 - Array with falsy values
    obj = [0, False, None, ""]
    result = isEmpty(obj)
    print(f"Test 7 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 8 - Object with falsy values
    obj = {"a": 0, "b": False, "c": None}
    result = isEmpty(obj)
    print(f"Test 8 - Expected: False, Got: {result}")
    assert result == False
    
    # Test Case 9 - Nested empty structures
    obj = {"empty_dict": {}, "empty_list": []}
    result = isEmpty(obj)
    print(f"Test 9 - Expected: False, Got: {result}")
    assert result == False  # Object itself is not empty
    
    # Test Case 10 - Complex nested structure
    obj = {"users": [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}], "count": 2}
    result = isEmpty(obj)
    print(f"Test 10 - Expected: False, Got: {result}")
    assert result == False
    
    # Test all implementations produce same results
    test_cases = [
        {"x": 5, "y": 42},
        {},
        [None, False, 0],
        [],
        [1, 2, 3],
        {"a": 1}
    ]
    
    for i, test_obj in enumerate(test_cases):
        results = [
            isEmpty(test_obj),
            isEmpty_pythonic(test_obj),
            isEmpty_explicit_type_check(test_obj),
            isEmpty_try_except(test_obj)
        ]
        
        # All should produce same result
        for j in range(1, len(results)):
            assert results[0] == results[j], f"Test case {i}, implementation {j} differs"
    
    # Test edge cases with comprehensive function
    edge_cases = [
        (None, True),
        (0, True),
        (False, True),
        ("", True),
        ("hello", False),
        (42, False),
        (True, False)
    ]
    
    for obj, expected in edge_cases:
        result = isEmpty_comprehensive(obj)
        print(f"Edge case {obj} - Expected: {expected}, Got: {result}")
        assert result == expected, f"Failed for {obj}"
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Basic Implementation:
1. Time Complexity: O(1)
   - len() operation is O(1) for dict and list in Python
   - Type checking is O(1)
   - No iteration through elements

2. Space Complexity: O(1)
   - No additional data structures created
   - Only uses constant extra space

Pythonic Approach:
1. Time Complexity: O(1)
   - Boolean evaluation of containers is O(1)
   - Uses built-in truthiness evaluation

2. Space Complexity: O(1)
   - Minimal memory overhead

Try-Except Approach:
1. Time Complexity: O(1)
   - Exception handling has minimal overhead for success case
   - Still O(1) for TypeError case

2. Space Complexity: O(1)
   - No additional memory allocation

Comprehensive Check:
1. Time Complexity: O(1)
   - Multiple type checks are still constant time
   - No loops or recursion

2. Space Complexity: O(1)
   - Only stores references, no copying

Key Insights:
- Python's len() is O(1) for built-in containers
- Empty containers are falsy in Python
- Type checking is important for robust handling
- JSON parsing guarantees dict/list types
- Truthiness vs explicit emptiness checking

Empty vs Falsy Distinction:
- Empty: len(obj) == 0
- Falsy: not obj (includes 0, False, None, "", [], {})
- Problem asks specifically about empty containers
- Content values don't affect container emptiness

Real-world Considerations:
- JSON parsing ensures valid dict/list types
- Custom objects might need special handling
- Generator exhaustion vs emptiness
- Thread safety for mutable objects
- Memory efficiency for large empty containers

Topic: Data Structures, Type Checking, Boolean Logic, Container Operations
"""
