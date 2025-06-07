"""
LeetCode Question #2675: Array of Objects to Matrix

Problem Statement:
Write a function that converts an array of objects arr into a matrix m.

arr is an array of objects or primitives. Each object can contain keys which have the value of strings, integers, booleans, objects, arrays, and null. Each object can also contain nested objects and arrays.

Return a matrix m. The matrix should contain the same number of rows as there are objects in arr. It should have as many columns as there are unique keys across all the objects in arr.

The first row m[0] should be the header row containing all the keys. For each subsequent row m[i], it should contain the value of the object arr[i-1] corresponding to that column's key. If a particular object doesn't contain a value for a given key, the cell should contain an empty string "".

The columns should be ordered lexicographically by key name.

Examples:
Example 1:
Input: arr = [{"b": 1, "a": 2}, {"c": 3, "d": 4}]
Output: [["a", "b", "c", "d"], ["2", "1", "", ""], ["", "", "3", "4"]]
Explanation:
There are 2 objects with 4 unique keys "a", "b", "c", "d".
The first row contains all the keys in lexicographically sorted order.
For the first object {"b": 1, "a": 2}, row 1 contains ["2", "1", "", ""].
For the second object {"c": 3, "d": 4}, row 2 contains ["", "", "3", "4"].

Example 2:
Input: arr = [{"a": 1, "b": 2}, {"c": 3, "b": 4}]
Output: [["a", "b", "c"], ["1", "2", ""], ["", "4", "3"]]

Example 3:
Input: arr = [{"a": {"b": 1, "c": 2}}, {"a": {"b": 3, "d": 4}}]
Output: [["a.b", "a.c", "a.d"], ["1", "2", ""], ["3", "", "4"]]
Explanation: In this example, the objects contain nested objects. The keys represent the full path to each value separated by periods.

Constraints:
- 1 <= arr.length <= 1000
- unique keys <= 1000
"""

from typing import List, Dict, Any, Union
import json

def jsonToMatrix(arr: List[Dict[str, Any]]) -> List[List[str]]:
    """
    Convert array of objects to matrix format.
    
    Time: O(n * k * d) where n is number of objects, k is average keys per object, d is max depth
    Space: O(k) where k is total unique keys
    """
    if not arr:
        return []
    
    # Collect all unique keys from all objects
    all_keys = set()
    flattened_objects = []
    
    for obj in arr:
        flattened = flatten_object(obj)
        flattened_objects.append(flattened)
        all_keys.update(flattened.keys())
    
    # Sort keys lexicographically
    sorted_keys = sorted(all_keys)
    
    # Create matrix
    matrix = []
    
    # Header row
    matrix.append(sorted_keys)
    
    # Data rows
    for flattened_obj in flattened_objects:
        row = []
        for key in sorted_keys:
            value = flattened_obj.get(key, "")
            row.append(str(value) if value != "" else "")
        matrix.append(row)
    
    return matrix

def flatten_object(obj: Any, prefix: str = "") -> Dict[str, Any]:
    """
    Flatten a nested object using dot notation.
    """
    result = {}
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_key = f"{prefix}.{key}" if prefix else key
            
            if isinstance(value, (dict, list)):
                result.update(flatten_object(value, new_key))
            else:
                result[new_key] = value
    
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            new_key = f"{prefix}.{i}" if prefix else str(i)
            
            if isinstance(value, (dict, list)):
                result.update(flatten_object(value, new_key))
            else:
                result[new_key] = value
    
    else:
        # Primitive value
        result[prefix] = obj
    
    return result

def jsonToMatrixSimple(arr: List[Dict[str, Any]]) -> List[List[str]]:
    """
    Simplified version for objects without nesting.
    
    Time: O(n * k) where n is number of objects, k is average keys per object
    Space: O(k) where k is total unique keys
    """
    if not arr:
        return []
    
    # Collect all unique keys
    all_keys = set()
    for obj in arr:
        all_keys.update(obj.keys())
    
    # Sort keys lexicographically
    sorted_keys = sorted(all_keys)
    
    # Create matrix
    matrix = [sorted_keys]  # Header row
    
    # Data rows
    for obj in arr:
        row = []
        for key in sorted_keys:
            value = obj.get(key, "")
            row.append(str(value) if value != "" else "")
        matrix.append(row)
    
    return matrix

def jsonToMatrixRecursive(arr: List[Dict[str, Any]]) -> List[List[str]]:
    """
    Recursive approach for handling deeply nested structures.
    
    Time: O(n * k * d) where d is maximum depth
    Space: O(k + d) for keys storage and recursion stack
    """
    def extract_all_paths(obj: Any, current_path: str = "") -> List[str]:
        """Extract all possible paths from an object."""
        paths = []
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{current_path}.{key}" if current_path else key
                
                if isinstance(value, (dict, list)) and value:
                    paths.extend(extract_all_paths(value, new_path))
                else:
                    paths.append(new_path)
        
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                new_path = f"{current_path}.{i}" if current_path else str(i)
                
                if isinstance(value, (dict, list)) and value:
                    paths.extend(extract_all_paths(value, new_path))
                else:
                    paths.append(new_path)
        
        else:
            paths.append(current_path)
        
        return paths
    
    def get_value_at_path(obj: Any, path: str) -> str:
        """Get value at a specific path in the object."""
        if not path:
            return str(obj) if obj is not None else ""
        
        parts = path.split('.')
        current = obj
        
        try:
            for part in parts:
                if isinstance(current, dict):
                    current = current[part]
                elif isinstance(current, list):
                    current = current[int(part)]
                else:
                    return ""
            
            return str(current) if current is not None else ""
        except (KeyError, IndexError, ValueError):
            return ""
    
    if not arr:
        return []
    
    # Collect all unique paths
    all_paths = set()
    for obj in arr:
        paths = extract_all_paths(obj)
        all_paths.update(paths)
    
    # Sort paths lexicographically
    sorted_paths = sorted(all_paths)
    
    # Create matrix
    matrix = [sorted_paths]  # Header row
    
    # Data rows
    for obj in arr:
        row = []
        for path in sorted_paths:
            value = get_value_at_path(obj, path)
            row.append(value)
        matrix.append(row)
    
    return matrix

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (
            [{"b": 1, "a": 2}, {"c": 3, "d": 4}],
            [["a", "b", "c", "d"], ["2", "1", "", ""], ["", "", "3", "4"]]
        ),
        (
            [{"a": 1, "b": 2}, {"c": 3, "b": 4}],
            [["a", "b", "c"], ["1", "2", ""], ["", "4", "3"]]
        ),
        (
            [{"a": {"b": 1, "c": 2}}, {"a": {"b": 3, "d": 4}}],
            [["a.b", "a.c", "a.d"], ["1", "2", ""], ["3", "", "4"]]
        ),
        (
            [{"x": 1}],
            [["x"], ["1"]]
        ),
        (
            [{}],
            [[]]
        ),
    ]
    
    print("Testing main approach:")
    for arr, expected in test_cases:
        result = jsonToMatrix(arr)
        print(f"Input: {arr}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Match: {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing simple approach (for non-nested objects):")
    simple_test_cases = test_cases[:2]  # Only non-nested cases
    for arr, expected in simple_test_cases:
        result = jsonToMatrixSimple(arr)
        print(f"Input: {arr}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Match: {'✓' if result == expected else '✗'}")
        print()
    
    # Test flattening function
    print("Testing object flattening:")
    test_obj = {"a": {"b": 1, "c": 2}, "d": [3, {"e": 4}]}
    flattened = flatten_object(test_obj)
    print(f"Original: {test_obj}")
    print(f"Flattened: {flattened}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n * k * d) where n is number of objects, k is average keys per object, d is max depth
Space Complexity: O(k) where k is total unique keys across all objects

Simple Approach (no nesting):
Time Complexity: O(n * k) where n is number of objects, k is average keys per object
Space Complexity: O(k) where k is total unique keys

Recursive Approach:
Time Complexity: O(n * k * d) where d is maximum nesting depth
Space Complexity: O(k + d) for keys storage and recursion stack

Key Insights:
1. The problem requires flattening nested objects using dot notation
2. All unique keys must be collected and sorted lexicographically
3. Missing values should be represented as empty strings
4. Handling nested objects and arrays requires recursive traversal
5. Path construction is crucial for maintaining object hierarchy

Topic: Object Processing, Matrix Transformation, Recursion, Data Structure Conversion
"""
