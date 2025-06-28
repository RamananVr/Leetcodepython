"""
LeetCode Problem 2775: Undefined to Null

Write a function that takes a deeply nested object or array obj and returns a copy with all undefined values replaced with null.

This operation should be applied recursively to all nested objects and arrays.

Constraints:
- obj is a valid JSON object or array
- 2 <= JSON.stringify(obj).length <= 10^5

Example 1:
Input: obj = {"a": undefined, "b": 3}
Output: {"a": null, "b": 3}

Example 2:
Input: obj = {"a": undefined, "b": {"c": undefined}}
Output: {"a": null, "b": {"c": null}}

Example 3:
Input: obj = [undefined, 1, undefined, 2]
Output: [null, 1, null, 2]

Topics: Recursion, Object Manipulation, JavaScript
"""

class Solution:
    def undefinedToNull(self, obj):
        """
        Approach 1: Recursive Deep Traversal
        
        Recursively traverse the object/array and replace undefined with null.
        Handle objects, arrays, and primitive values.
        
        Time: O(n) where n is total number of elements/properties
        Space: O(d) where d is the maximum depth of nesting
        """
        # In Python, we'll simulate JavaScript undefined with a special value
        # For this implementation, we'll use a custom Undefined class
        
        if obj is None or obj == "undefined" or isinstance(obj, type(self.Undefined)):
            return None
        
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                result[key] = self.undefinedToNull(value)
            return result
        
        elif isinstance(obj, list):
            result = []
            for item in obj:
                result.append(self.undefinedToNull(item))
            return result
        
        else:
            # Primitive value (string, number, boolean)
            return obj
    
    class Undefined:
        """Custom class to represent JavaScript undefined in Python."""
        pass
    
    def undefinedToNull_iterative(self, obj):
        """
        Approach 2: Iterative with Stack
        
        Use a stack to iteratively process nested structures.
        
        Time: O(n)
        Space: O(n) for stack storage
        """
        from collections import deque
        
        # For iterative approach, we need to handle the root separately
        if obj is None or obj == "undefined" or isinstance(obj, type(self.Undefined)):
            return None
        
        # Stack contains (container, key, original_value) tuples
        stack = deque()
        result = None
        
        # Initialize based on root type
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                stack.append((result, key, value))
        elif isinstance(obj, list):
            result = [None] * len(obj)
            for i, value in enumerate(obj):
                stack.append((result, i, value))
        else:
            return obj
        
        while stack:
            container, key, value = stack.popleft()
            
            if value is None or value == "undefined" or isinstance(value, type(self.Undefined)):
                container[key] = None
            elif isinstance(value, dict):
                container[key] = {}
                for k, v in value.items():
                    stack.append((container[key], k, v))
            elif isinstance(value, list):
                container[key] = [None] * len(value)
                for i, v in enumerate(value):
                    stack.append((container[key], i, v))
            else:
                container[key] = value
        
        return result
    
    def undefinedToNull_json_approach(self, obj):
        """
        Approach 3: JSON-based approach (Python simulation)
        
        Convert to string representation, replace undefined, then parse back.
        This is more of a conceptual approach since Python doesn't have undefined.
        
        Time: O(n) for string operations
        Space: O(n) for string representation
        """
        import json
        
        def custom_replacer(o):
            if o is None or o == "undefined" or isinstance(o, type(self.Undefined)):
                return None
            elif isinstance(o, dict):
                return {k: custom_replacer(v) for k, v in o.items()}
            elif isinstance(o, list):
                return [custom_replacer(item) for item in o]
            else:
                return o
        
        return custom_replacer(obj)

def test_undefined_to_null():
    """Test the undefined to null solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Simple object with undefined
    undefined = solution.Undefined()
    obj1 = {"a": undefined, "b": 3}
    result1 = solution.undefinedToNull(obj1)
    expected1 = {"a": None, "b": 3}
    assert result1 == expected1
    
    # Test case 2: Nested object
    obj2 = {"a": undefined, "b": {"c": undefined}}
    result2 = solution.undefinedToNull(obj2)
    expected2 = {"a": None, "b": {"c": None}}
    assert result2 == expected2
    
    # Test case 3: Array with undefined
    obj3 = [undefined, 1, undefined, 2]
    result3 = solution.undefinedToNull(obj3)
    expected3 = [None, 1, None, 2]
    assert result3 == expected3
    
    # Test case 4: Primitive values
    assert solution.undefinedToNull(5) == 5
    assert solution.undefinedToNull("hello") == "hello"
    assert solution.undefinedToNull(True) == True
    assert solution.undefinedToNull(undefined) == None
    
    # Test case 5: Empty structures
    assert solution.undefinedToNull({}) == {}
    assert solution.undefinedToNull([]) == []
    
    # Test case 6: Deeply nested
    obj6 = {
        "level1": {
            "level2": {
                "level3": [undefined, {"deep": undefined}]
            }
        }
    }
    result6 = solution.undefinedToNull(obj6)
    expected6 = {
        "level1": {
            "level2": {
                "level3": [None, {"deep": None}]
            }
        }
    }
    assert result6 == expected6
    
    # Test case 7: Mixed array and object
    obj7 = [{"a": undefined}, [undefined, {"b": undefined}]]
    result7 = solution.undefinedToNull(obj7)
    expected7 = [{"a": None}, [None, {"b": None}]]
    assert result7 == expected7
    
    # Compare approaches
    test_cases = [
        {"a": undefined, "b": 3},
        {"a": undefined, "b": {"c": undefined}},
        [undefined, 1, undefined, 2],
        {},
        [],
        {"nested": [undefined, {"inner": undefined}]}
    ]
    
    for obj in test_cases:
        result1 = solution.undefinedToNull(obj)
        result2 = solution.undefinedToNull_iterative(obj)
        result3 = solution.undefinedToNull_json_approach(obj)
        assert result1 == result2 == result3, f"Mismatch for {obj}: {result1}, {result2}, {result3}"
    
    print("All undefined to null tests passed!")

if __name__ == "__main__":
    test_undefined_to_null()
