"""
LeetCode Problem 2755: Deep Merge of Two Objects

Given two objects obj1 and obj2, return a deep merged object.

Objects are considered the same type if they are both arrays or both objects. Otherwise, they are considered different types.

The merge rules are as follows:
- If both values are objects, recursively merge them.
- If both values are arrays, concatenate them.
- If values are of different types or one is null/undefined, use the value from obj2.
- If only one object has the property, include it in the result.

Example 1:
Input: obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2}
Output: {"a": 2, "c": 3, "b": 2}
Explanation: obj2 overwrites obj1.a, and both objects contribute their unique keys.

Example 2:
Input: obj1 = {"a": 1, "b": {"x": 2, "y": 3}}, obj2 = {"b": {"y": 4, "z": 5}, "c": 6}
Output: {"a": 1, "b": {"x": 2, "y": 4, "z": 5}, "c": 6}
Explanation: Nested objects are merged recursively.

Example 3:
Input: obj1 = [1, 2, 3], obj2 = [4, 5]
Output: [1, 2, 3, 4, 5]
Explanation: Arrays are concatenated.

Example 4:
Input: obj1 = {"a": [1, 2]}, obj2 = {"a": [3, 4]}
Output: {"a": [1, 2, 3, 4]}
Explanation: Arrays within objects are concatenated.

Constraints:
- Both objects are valid JSON objects or arrays
- The depth of nesting will not exceed 100
- obj1 and obj2 do not contain functions, dates, or other non-serializable objects
"""

from typing import Any, Dict, List, Union
import copy


def deepMerge(obj1: Any, obj2: Any) -> Any:
    """
    Deep merge two objects according to specified rules.
    
    Rules:
    1. If both are objects (dicts), merge recursively
    2. If both are arrays (lists), concatenate
    3. If different types or one is None, use obj2
    4. Include unique properties from both objects
    
    Args:
        obj1: First object to merge
        obj2: Second object to merge
        
    Returns:
        Deep merged result
        
    Time Complexity: O(m + n) where m, n are sizes of objects
    Space Complexity: O(m + n) for the result object
    """
    # If obj2 is None, return obj1
    if obj2 is None:
        return copy.deepcopy(obj1) if obj1 is not None else None
    
    # If obj1 is None, return obj2
    if obj1 is None:
        return copy.deepcopy(obj2)
    
    # If both are dictionaries, merge recursively
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        result = copy.deepcopy(obj1)
        
        for key, value in obj2.items():
            if key in result:
                result[key] = deepMerge(result[key], value)
            else:
                result[key] = copy.deepcopy(value)
        
        return result
    
    # If both are lists, concatenate
    elif isinstance(obj1, list) and isinstance(obj2, list):
        return obj1 + obj2
    
    # For different types or other cases, use obj2
    else:
        return copy.deepcopy(obj2)


def deepMergeIterative(obj1: Any, obj2: Any) -> Any:
    """
    Iterative implementation to avoid deep recursion.
    
    Args:
        obj1: First object to merge
        obj2: Second object to merge
        
    Returns:
        Deep merged result
        
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    if obj2 is None:
        return copy.deepcopy(obj1) if obj1 is not None else None
    if obj1 is None:
        return copy.deepcopy(obj2)
    
    # Use stack for iterative processing
    stack = [(obj1, obj2, None, None, 'root')]  # (obj1, obj2, parent, key, type)
    result = None
    
    while stack:
        o1, o2, parent, key, merge_type = stack.pop()
        
        merged = None
        
        if isinstance(o1, dict) and isinstance(o2, dict):
            merged = copy.deepcopy(o1)
            
            # Add items from o2, processing conflicts via stack
            for k, v in o2.items():
                if k in merged:
                    stack.append((merged[k], v, merged, k, 'dict_key'))
                else:
                    merged[k] = copy.deepcopy(v)
        
        elif isinstance(o1, list) and isinstance(o2, list):
            merged = o1 + o2
        
        else:
            merged = copy.deepcopy(o2)
        
        # Set the result in parent or as root
        if merge_type == 'root':
            result = merged
        elif merge_type == 'dict_key':
            parent[key] = merged
        elif merge_type == 'list_item':
            parent.append(merged)
    
    return result


def deepMergeInPlace(obj1: Dict, obj2: Dict) -> Dict:
    """
    In-place merge that modifies obj1.
    
    Args:
        obj1: First object (will be modified)
        obj2: Second object
        
    Returns:
        Reference to modified obj1
        
    Time Complexity: O(n) where n is size of obj2
    Space Complexity: O(1) excluding input
    """
    if not isinstance(obj1, dict) or not isinstance(obj2, dict):
        raise ValueError("Both arguments must be dictionaries for in-place merge")
    
    for key, value in obj2.items():
        if key in obj1:
            if isinstance(obj1[key], dict) and isinstance(value, dict):
                deepMergeInPlace(obj1[key], value)
            elif isinstance(obj1[key], list) and isinstance(value, list):
                obj1[key].extend(value)
            else:
                obj1[key] = copy.deepcopy(value)
        else:
            obj1[key] = copy.deepcopy(value)
    
    return obj1


def deepMergeWithCustomRules(obj1: Any, obj2: Any, rules: Dict[str, Any] = None) -> Any:
    """
    Deep merge with customizable rules.
    
    Args:
        obj1: First object
        obj2: Second object  
        rules: Custom merge rules
        
    Returns:
        Merged result according to custom rules
        
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    default_rules = {
        'array_strategy': 'concatenate',  # 'concatenate', 'replace', 'merge_unique'
        'conflict_strategy': 'obj2_wins',  # 'obj2_wins', 'obj1_wins', 'error'
        'null_strategy': 'obj2_wins'  # 'obj2_wins', 'obj1_wins', 'keep_both'
    }
    
    if rules:
        default_rules.update(rules)
    
    def merge_recursive(o1, o2):
        if o2 is None:
            return copy.deepcopy(o1) if default_rules['null_strategy'] == 'obj1_wins' else None
        if o1 is None:
            return copy.deepcopy(o2)
        
        if isinstance(o1, dict) and isinstance(o2, dict):
            result = copy.deepcopy(o1)
            for key, value in o2.items():
                if key in result:
                    result[key] = merge_recursive(result[key], value)
                else:
                    result[key] = copy.deepcopy(value)
            return result
        
        elif isinstance(o1, list) and isinstance(o2, list):
            if default_rules['array_strategy'] == 'concatenate':
                return o1 + o2
            elif default_rules['array_strategy'] == 'replace':
                return copy.deepcopy(o2)
            elif default_rules['array_strategy'] == 'merge_unique':
                seen = set()
                result = []
                for item in o1 + o2:
                    if item not in seen:
                        result.append(item)
                        seen.add(item)
                return result
        
        else:
            if default_rules['conflict_strategy'] == 'obj2_wins':
                return copy.deepcopy(o2)
            elif default_rules['conflict_strategy'] == 'obj1_wins':
                return copy.deepcopy(o1)
            else:
                raise ValueError(f"Type conflict: {type(o1)} vs {type(o2)}")
    
    return merge_recursive(obj1, obj2)


# Test cases
def test_deepMerge():
    """Test the deepMerge function with various inputs."""
    
    test_cases = [
        {
            "obj1": {"a": 1, "c": 3},
            "obj2": {"a": 2, "b": 2},
            "expected": {"a": 2, "c": 3, "b": 2},
            "description": "Example 1: Simple object merge with conflict"
        },
        {
            "obj1": {"a": 1, "b": {"x": 2, "y": 3}},
            "obj2": {"b": {"y": 4, "z": 5}, "c": 6},
            "expected": {"a": 1, "b": {"x": 2, "y": 4, "z": 5}, "c": 6},
            "description": "Example 2: Nested object merge"
        },
        {
            "obj1": [1, 2, 3],
            "obj2": [4, 5],
            "expected": [1, 2, 3, 4, 5],
            "description": "Example 3: Array concatenation"
        },
        {
            "obj1": {"a": [1, 2]},
            "obj2": {"a": [3, 4]},
            "expected": {"a": [1, 2, 3, 4]},
            "description": "Example 4: Arrays within objects"
        },
        {
            "obj1": {"a": 1},
            "obj2": None,
            "expected": {"a": 1},
            "description": "One object is None"
        },
        {
            "obj1": None,
            "obj2": {"b": 2},
            "expected": {"b": 2},
            "description": "First object is None"
        },
        {
            "obj1": {"a": "string"},
            "obj2": {"a": 123},
            "expected": {"a": 123},
            "description": "Type conflict resolution"
        },
        {
            "obj1": {"nested": {"deep": {"value": 1}}},
            "obj2": {"nested": {"deep": {"other": 2}}},
            "expected": {"nested": {"deep": {"value": 1, "other": 2}}},
            "description": "Deep nesting"
        }
    ]
    
    for i, test in enumerate(test_cases):
        obj1 = test["obj1"]
        obj2 = test["obj2"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  obj1: {obj1}")
        print(f"  obj2: {obj2}")
        print(f"  Expected: {expected}")
        
        # Test main solution
        result1 = deepMerge(obj1, obj2)
        print(f"  Recursive merge: {result1}")
        
        # Test in-place merge for dict inputs
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            obj1_copy = copy.deepcopy(obj1)
            result2 = deepMergeInPlace(obj1_copy, obj2)
            print(f"  In-place merge: {result2}")
            assert result2 == expected, f"In-place merge failed for test {i+1}"
        
        # Test with custom rules
        result3 = deepMergeWithCustomRules(obj1, obj2)
        print(f"  Custom rules: {result3}")
        
        # Verify results
        assert result1 == expected, f"Recursive merge failed for test {i+1}"
        assert result3 == expected, f"Custom rules failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()
    
    # Test custom array merge strategy
    print("Testing custom array merge strategies:")
    obj1 = {"arr": [1, 2, 2]}
    obj2 = {"arr": [2, 3, 3]}
    
    # Concatenate (default)
    result_concat = deepMergeWithCustomRules(obj1, obj2, {"array_strategy": "concatenate"})
    print(f"  Concatenate: {result_concat}")
    
    # Replace
    result_replace = deepMergeWithCustomRules(obj1, obj2, {"array_strategy": "replace"})
    print(f"  Replace: {result_replace}")
    
    # Merge unique
    result_unique = deepMergeWithCustomRules(obj1, obj2, {"array_strategy": "merge_unique"})
    print(f"  Merge unique: {result_unique}")


if __name__ == "__main__":
    test_deepMerge()

"""
Complexity Analysis:

1. Recursive Merge (deepMerge):
   - Time Complexity: O(m + n) where m, n are total sizes of objects
   - Space Complexity: O(m + n) for result + O(d) for recursion depth

2. In-place Merge (deepMergeInPlace):
   - Time Complexity: O(n) where n is size of obj2
   - Space Complexity: O(1) excluding deep copies of new values

3. Custom Rules (deepMergeWithCustomRules):
   - Time Complexity: O(m + n) similar to basic merge
   - Space Complexity: O(m + n) for result

Key Insights:
- Deep merging requires recursive traversal of nested structures
- Different data types require different merge strategies
- Conflict resolution is important when both objects have same keys
- Arrays and objects are treated differently (concatenate vs merge)

Implementation Considerations:
- Use deep copy to avoid mutating input objects
- Handle null/undefined values appropriately
- Support different merge strategies for flexibility
- Consider iterative approach for very deep nesting

Merge Strategies:
1. Objects: Recursive merge with conflict resolution
2. Arrays: Concatenation (or custom strategy)
3. Primitives: Use second value (or custom rule)
4. Type conflicts: Use second value (or error)

Use Cases:
- Configuration merging
- API response combining
- State management in applications
- Data transformation pipelines

Topics: Recursion, Object Manipulation, Data Structures, Deep Copy
"""
