"""
2700. Differences Between Two Objects

PROBLEM STATEMENT:
Write a function that compares two objects and returns an object representing the differences.
The function should:
1. Find properties that exist in one object but not the other
2. Find properties that exist in both but have different values
3. Recursively compare nested objects
4. Handle arrays by comparing element by element
5. Return a structured diff object showing the changes

EXAMPLES:
Example 1:
obj1 = {"a": 1, "b": 2}
obj2 = {"a": 1, "c": 3}
Output: {"b": [2, undefined], "c": [undefined, 3]}

Example 2:
obj1 = {"a": {"x": 1}, "b": 2}
obj2 = {"a": {"x": 2}, "b": 2}
Output: {"a": {"x": [1, 2]}}

Example 3:
obj1 = [1, 2, 3]
obj2 = [1, 2, 4, 5]
Output: {"2": [3, 4], "3": [undefined, 5]}

CONSTRAINTS:
- Objects can be nested to any depth
- Arrays should be treated as objects with numeric indices
- Primitive values should be compared directly
- Use [old_value, new_value] format for differences
"""

def differences_between_objects(obj1, obj2):
    """
    Find differences between two objects.
    
    Args:
        obj1: First object to compare
        obj2: Second object to compare
    
    Returns:
        Object representing the differences
    """
    
    def get_type(obj):
        """Get the type of an object for comparison purposes."""
        if obj is None:
            return "null"
        elif isinstance(obj, bool):
            return "boolean" 
        elif isinstance(obj, int):
            return "number"
        elif isinstance(obj, float):
            return "number"
        elif isinstance(obj, str):
            return "string"
        elif isinstance(obj, list):
            return "array"
        elif isinstance(obj, dict):
            return "object"
        else:
            return "unknown"
    
    def is_primitive(obj):
        """Check if object is a primitive type."""
        return get_type(obj) in ["null", "boolean", "number", "string"]
    
    def deep_equal(a, b):
        """Check if two objects are deeply equal."""
        if get_type(a) != get_type(b):
            return False
        
        if is_primitive(a):
            return a == b
        
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                return False
            return all(deep_equal(a[i], b[i]) for i in range(len(a)))
        
        if isinstance(a, dict) and isinstance(b, dict):
            if set(a.keys()) != set(b.keys()):
                return False
            return all(deep_equal(a[key], b[key]) for key in a.keys())
        
        return False
    
    def compare_objects(o1, o2):
        """
        Recursively compare two objects and return differences.
        
        Args:
            o1: First object
            o2: Second object
        
        Returns:
            Dictionary of differences or None if no differences
        """
        # If objects are primitives, compare directly
        if is_primitive(o1) and is_primitive(o2):
            return [o1, o2] if o1 != o2 else None
        
        if is_primitive(o1) or is_primitive(o2):
            return [o1, o2]
        
        # Convert arrays to dict-like format for uniform processing
        if isinstance(o1, list):
            o1 = {str(i): v for i, v in enumerate(o1)}
        if isinstance(o2, list):
            o2 = {str(i): v for i, v in enumerate(o2)}
        
        # Ensure both are dict-like
        if not isinstance(o1, dict):
            o1 = {}
        if not isinstance(o2, dict):
            o2 = {}
        
        diff = {}
        all_keys = set(o1.keys()) | set(o2.keys())
        
        for key in all_keys:
            val1 = o1.get(key, "undefined")
            val2 = o2.get(key, "undefined")
            
            if val1 == "undefined" and val2 == "undefined":
                continue
            elif val1 == "undefined":
                diff[key] = ["undefined", val2]
            elif val2 == "undefined":
                diff[key] = [val1, "undefined"]
            else:
                # Both values exist, compare them
                if deep_equal(val1, val2):
                    continue
                
                # If both are objects/arrays, recurse
                if not is_primitive(val1) and not is_primitive(val2):
                    nested_diff = compare_objects(val1, val2)
                    if nested_diff is not None:
                        diff[key] = nested_diff
                else:
                    # At least one is primitive, just record the difference
                    diff[key] = [val1, val2]
        
        return diff if diff else None
    
    result = compare_objects(obj1, obj2)
    return result if result is not None else {}

def differences_with_path_tracking(obj1, obj2):
    """
    Find differences with full path tracking for debugging.
    
    Args:
        obj1: First object
        obj2: Second object
    
    Returns:
        Tuple of (differences, paths_changed)
    """
    
    def compare_with_path(o1, o2, path=""):
        """Compare objects and track paths of changes."""
        changes = {}
        paths = []
        
        if isinstance(o1, (int, float, str, bool, type(None))) and isinstance(o2, (int, float, str, bool, type(None))):
            if o1 != o2:
                changes[path or "root"] = [o1, o2]
                paths.append(path or "root")
            return changes, paths
        
        # Convert arrays to dicts for uniform processing
        if isinstance(o1, list):
            o1_dict = {str(i): v for i, v in enumerate(o1)}
        else:
            o1_dict = o1 if isinstance(o1, dict) else {}
        
        if isinstance(o2, list):
            o2_dict = {str(i): v for i, v in enumerate(o2)}
        else:
            o2_dict = o2 if isinstance(o2, dict) else {}
        
        all_keys = set(o1_dict.keys()) | set(o2_dict.keys())
        
        for key in all_keys:
            current_path = f"{path}.{key}" if path else key
            val1 = o1_dict.get(key, "undefined")
            val2 = o2_dict.get(key, "undefined")
            
            if val1 == "undefined" or val2 == "undefined":
                changes[current_path] = [val1, val2]
                paths.append(current_path)
            else:
                nested_changes, nested_paths = compare_with_path(val1, val2, current_path)
                changes.update(nested_changes)
                paths.extend(nested_paths)
        
        return changes, paths
    
    changes, paths = compare_with_path(obj1, obj2)
    
    # Convert flat changes back to nested structure
    result = {}
    for path, change in changes.items():
        keys = path.split('.')
        current = result
        
        for i, key in enumerate(keys[:-1]):
            if key not in current:
                current[key] = {}
            current = current[key]
        
        current[keys[-1]] = change
    
    return result, paths

def create_patch_object(differences):
    """
    Create a patch object that can be applied to transform obj1 to obj2.
    
    Args:
        differences: Differences object from differences_between_objects
    
    Returns:
        Patch object with operations
    """
    
    def extract_operations(diff, path=""):
        """Extract atomic operations from differences."""
        operations = []
        
        if isinstance(diff, list) and len(diff) == 2:
            # This is a value change
            old_val, new_val = diff
            if old_val == "undefined":
                operations.append({"op": "add", "path": path, "value": new_val})
            elif new_val == "undefined":
                operations.append({"op": "remove", "path": path})
            else:
                operations.append({"op": "replace", "path": path, "from": old_val, "to": new_val})
        
        elif isinstance(diff, dict):
            # This is a nested difference
            for key, value in diff.items():
                new_path = f"{path}.{key}" if path else key
                operations.extend(extract_operations(value, new_path))
        
        return operations
    
    return extract_operations(differences)

def test_differences_between_objects():
    """Test the object differences implementation."""
    
    # Test 1: Example 1 - Simple object differences
    obj1 = {"a": 1, "b": 2}
    obj2 = {"a": 1, "c": 3}
    result1 = differences_between_objects(obj1, obj2)
    expected1 = {"b": [2, "undefined"], "c": ["undefined", 3]}
    assert result1 == expected1
    
    # Test 2: Example 2 - Nested object differences
    obj1 = {"a": {"x": 1}, "b": 2}
    obj2 = {"a": {"x": 2}, "b": 2}
    result2 = differences_between_objects(obj1, obj2)
    expected2 = {"a": {"x": [1, 2]}}
    assert result2 == expected2
    
    # Test 3: Array differences
    obj1 = [1, 2, 3]
    obj2 = [1, 2, 4, 5]
    result3 = differences_between_objects(obj1, obj2)
    expected3 = {"2": [3, 4], "3": ["undefined", 5]}
    assert result3 == expected3
    
    # Test 4: No differences
    obj1 = {"a": 1, "b": {"c": 2}}
    obj2 = {"a": 1, "b": {"c": 2}}
    result4 = differences_between_objects(obj1, obj2)
    assert result4 == {}
    
    # Test 5: Completely different objects
    obj1 = {"x": 1}
    obj2 = {"y": 2}
    result5 = differences_between_objects(obj1, obj2)
    expected5 = {"x": [1, "undefined"], "y": ["undefined", 2]}
    assert result5 == expected5
    
    # Test 6: Mixed types
    obj1 = {"a": 1, "b": "hello", "c": [1, 2]}
    obj2 = {"a": 2, "b": "hello", "c": [1, 3]}
    result6 = differences_between_objects(obj1, obj2)
    expected6 = {"a": [1, 2], "c": {"1": [2, 3]}}
    assert result6 == expected6
    
    # Test 7: Deep nesting
    obj1 = {"level1": {"level2": {"level3": {"value": 1}}}}
    obj2 = {"level1": {"level2": {"level3": {"value": 2}}}}
    result7 = differences_between_objects(obj1, obj2)
    expected7 = {"level1": {"level2": {"level3": {"value": [1, 2]}}}}
    assert result7 == expected7
    
    # Test 8: Empty objects
    obj1 = {}
    obj2 = {"a": 1}
    result8 = differences_between_objects(obj1, obj2)
    expected8 = {"a": ["undefined", 1]}
    assert result8 == expected8
    
    # Test 9: Path tracking
    obj1 = {"a": {"b": {"c": 1}}, "x": 2}
    obj2 = {"a": {"b": {"c": 2}}, "x": 2}
    result9, paths9 = differences_with_path_tracking(obj1, obj2)
    assert "a.b.c" in paths9
    
    # Test 10: Patch generation
    diff = {"a": [1, 2], "b": ["undefined", 3]}
    patch = create_patch_object(diff)
    assert len(patch) == 2
    assert any(op["op"] == "replace" for op in patch)
    assert any(op["op"] == "add" for op in patch)
    
    print("All test cases passed!")

def demonstrate_object_comparison():
    """Demonstrate the object comparison algorithm."""
    
    print("Object Differences Detection Algorithm")
    print("=" * 50)
    
    # Complex example
    obj1 = {
        "user": {
            "name": "John",
            "age": 25,
            "hobbies": ["reading", "gaming"],
            "address": {
                "street": "123 Main St",
                "city": "New York"
            }
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
    
    obj2 = {
        "user": {
            "name": "John",
            "age": 26,
            "hobbies": ["reading", "swimming"],
            "address": {
                "street": "456 Oak Ave",
                "city": "New York"
            }
        },
        "settings": {
            "theme": "light",
            "language": "en"
        }
    }
    
    print("Object 1:")
    print(obj1)
    print("\nObject 2:")
    print(obj2)
    
    differences = differences_between_objects(obj1, obj2)
    print("\nDifferences:")
    print(differences)
    
    diff_with_paths, paths = differences_with_path_tracking(obj1, obj2)
    print(f"\nChanged paths: {paths}")
    
    patch = create_patch_object(differences)
    print(f"\nPatch operations:")
    for op in patch:
        print(f"  {op}")

if __name__ == "__main__":
    test_differences_between_objects()
    demonstrate_object_comparison()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(n) where n is the total number of properties across all nested levels
- Space Complexity: O(d * k) where d is the maximum depth and k is the number of differences

TOPICS: Object Comparison, Recursive Algorithms, Data Structure Traversal, Diff Algorithms

KEY INSIGHTS:
1. Recursive comparison handles arbitrarily nested structures
2. Treating arrays as objects with numeric keys provides uniform processing
3. Path tracking enables precise identification of change locations
4. Patch generation allows transformation between object states
5. Deep equality checking prevents false positives on equivalent nested structures
"""
