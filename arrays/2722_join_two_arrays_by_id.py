"""
LeetCode Question #2722: Join Two Arrays by ID

Problem Statement:
Given two arrays `arr1` and `arr2`, return a new array `joinedArray`. All the objects in each array are guaranteed to have an `id` field with an integer value. `joinedArray` is an array formed by merging `arr1` and `arr2` based on their `id` key. The length of `joinedArray` should be the length of unique values of `id`. The returned array should be sorted in ascending order based on the `id` key.

When a given `id` exists in both arrays, the object from `arr2` should override the object from `arr1`. If a given `id` exists in only one array, that object should be included in the result array without modification.

Constraints:
- `arr1` and `arr2` are valid JSON arrays
- Each object contains at least an `id` field with an integer value
- `2 <= JSON.stringify(arr).length <= 10^6`

Example:
Input: arr1 = [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 3, "y": 6}], 
       arr2 = [{"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
Output: [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
Explanation: The two objects with id=1 and id=3 are included in the result array without modification. The two objects with id=2 are merged together. The object from arr2 overrides the object from arr1.

Input: arr1 = [{"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}], 
       arr2 = [{"id": 1, "b": {"c": 84}, "v": [1, 3]}]
Output: [{"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}]
Explanation: The two objects with id=1 are merged together. For the keys "b" and "v" the values from arr2 are used. Since the key "y" only exists in arr1, that value is taken from arr1.
"""

def join(arr1, arr2):
    """
    Join two arrays by ID, with arr2 values overriding arr1 values.
    
    Args:
        arr1: List of dictionaries with 'id' field
        arr2: List of dictionaries with 'id' field
    
    Returns:
        List of merged dictionaries sorted by id
    """
    # Create a dictionary to store merged objects by ID
    merged = {}
    
    # Add all objects from arr1
    for obj in arr1:
        obj_id = obj['id']
        merged[obj_id] = obj.copy()
    
    # Add/merge objects from arr2 (overriding arr1)
    for obj in arr2:
        obj_id = obj['id']
        if obj_id in merged:
            # Merge objects, arr2 values override arr1 values
            merged[obj_id].update(obj)
        else:
            # New object from arr2
            merged[obj_id] = obj.copy()
    
    # Convert to list and sort by id
    result = list(merged.values())
    result.sort(key=lambda x: x['id'])
    
    return result

def join_with_deep_merge(arr1, arr2):
    """
    Join arrays with deep merging of nested objects.
    
    Args:
        arr1: List of dictionaries with 'id' field
        arr2: List of dictionaries with 'id' field
    
    Returns:
        List of merged dictionaries sorted by id
    """
    def deep_merge(dict1, dict2):
        """Deep merge two dictionaries."""
        result = dict1.copy()
        
        for key, value in dict2.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result
    
    merged = {}
    
    # Add all objects from arr1
    for obj in arr1:
        obj_id = obj['id']
        merged[obj_id] = obj.copy()
    
    # Add/merge objects from arr2
    for obj in arr2:
        obj_id = obj['id']
        if obj_id in merged:
            merged[obj_id] = deep_merge(merged[obj_id], obj)
        else:
            merged[obj_id] = obj.copy()
    
    # Convert to list and sort by id
    result = list(merged.values())
    result.sort(key=lambda x: x['id'])
    
    return result

def join_functional(arr1, arr2):
    """
    Functional approach using dictionary comprehension.
    
    Args:
        arr1: List of dictionaries with 'id' field
        arr2: List of dictionaries with 'id' field
    
    Returns:
        List of merged dictionaries sorted by id
    """
    # Create mapping from arr1
    merged = {obj['id']: obj.copy() for obj in arr1}
    
    # Update with arr2 (automatic override)
    for obj in arr2:
        obj_id = obj['id']
        if obj_id in merged:
            merged[obj_id].update(obj)
        else:
            merged[obj_id] = obj.copy()
    
    return sorted(merged.values(), key=lambda x: x['id'])

def join_two_pass(arr1, arr2):
    """
    Two-pass approach for clarity.
    
    Args:
        arr1: List of dictionaries with 'id' field
        arr2: List of dictionaries with 'id' field
    
    Returns:
        List of merged dictionaries sorted by id
    """
    # First pass: collect all unique IDs
    all_ids = set()
    obj_map = {}
    
    for obj in arr1:
        obj_id = obj['id']
        all_ids.add(obj_id)
        obj_map[obj_id] = obj.copy()
    
    for obj in arr2:
        obj_id = obj['id']
        all_ids.add(obj_id)
        if obj_id in obj_map:
            obj_map[obj_id].update(obj)
        else:
            obj_map[obj_id] = obj.copy()
    
    # Second pass: create result array
    result = []
    for obj_id in sorted(all_ids):
        result.append(obj_map[obj_id])
    
    return result

def join_optimized(arr1, arr2):
    """
    Optimized approach minimizing copies.
    
    Args:
        arr1: List of dictionaries with 'id' field
        arr2: List of dictionaries with 'id' field
    
    Returns:
        List of merged dictionaries sorted by id
    """
    from collections import defaultdict
    
    # Track which IDs appear in arr2 for override
    arr2_ids = {obj['id'] for obj in arr2}
    merged = {}
    
    # Process arr1 (only copy if needed for merging)
    for obj in arr1:
        obj_id = obj['id']
        if obj_id in arr2_ids:
            merged[obj_id] = obj.copy()  # Will be updated
        else:
            merged[obj_id] = obj  # No copy needed
    
    # Process arr2 (override/add)
    for obj in arr2:
        obj_id = obj['id']
        if obj_id in merged:
            merged[obj_id].update(obj)
        else:
            merged[obj_id] = obj
    
    return sorted(merged.values(), key=lambda x: x['id'])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 - Basic merging
    arr1 = [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 3, "y": 6}]
    arr2 = [{"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
    result = join(arr1, arr2)
    expected = [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
    print(f"Test 1 - Expected: {expected}")
    print(f"Test 1 - Got: {result}")
    assert result == expected
    
    # Test Case 2 - Partial override
    arr1 = [{"id": 1, "b": {"b": 94}, "v": [4, 3], "y": 48}]
    arr2 = [{"id": 1, "b": {"c": 84}, "v": [1, 3]}]
    result = join(arr1, arr2)
    expected = [{"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}]
    print(f"Test 2 - Expected: {expected}")
    print(f"Test 2 - Got: {result}")
    assert result == expected
    
    # Test Case 3 - No overlap
    arr1 = [{"id": 1, "name": "Alice"}]
    arr2 = [{"id": 2, "name": "Bob"}]
    result = join(arr1, arr2)
    expected = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    print(f"Test 3 - Expected: {expected}")
    print(f"Test 3 - Got: {result}")
    assert result == expected
    
    # Test Case 4 - Empty arrays
    arr1 = []
    arr2 = [{"id": 1, "value": 100}]
    result = join(arr1, arr2)
    expected = [{"id": 1, "value": 100}]
    print(f"Test 4 - Expected: {expected}")
    print(f"Test 4 - Got: {result}")
    assert result == expected
    
    # Test Case 5 - Complete override
    arr1 = [{"id": 5, "a": 1, "b": 2}]
    arr2 = [{"id": 5, "a": 10, "b": 20, "c": 30}]
    result = join(arr1, arr2)
    expected = [{"id": 5, "a": 10, "b": 20, "c": 30}]
    print(f"Test 5 - Expected: {expected}")
    print(f"Test 5 - Got: {result}")
    assert result == expected
    
    # Test Case 6 - Multiple entries same ID in arr2 (last wins)
    arr1 = [{"id": 1, "x": 1}]
    arr2 = [{"id": 1, "y": 2}, {"id": 1, "z": 3}]
    result = join(arr1, arr2)
    expected = [{"id": 1, "x": 1, "y": 2, "z": 3}]
    print(f"Test 6 - Expected: {expected}")
    print(f"Test 6 - Got: {result}")
    assert result == expected
    
    # Test all implementations produce same results
    test_arr1 = [{"id": 3, "a": 1}, {"id": 1, "b": 2}]
    test_arr2 = [{"id": 2, "c": 3}, {"id": 1, "d": 4}]
    
    results = [
        join(test_arr1, test_arr2),
        join_functional(test_arr1, test_arr2),
        join_two_pass(test_arr1, test_arr2),
        join_optimized(test_arr1, test_arr2)
    ]
    
    for i in range(1, len(results)):
        assert results[0] == results[i], f"Implementation {i} differs"
    
    print("All test cases and implementations passed!")

"""
Time and Space Complexity Analysis:

Main Solution:
1. Time Complexity: O((n + m) + k*log(k))
   - O(n + m) to process both arrays where n = len(arr1), m = len(arr2)
   - O(k*log(k)) to sort by id where k is number of unique IDs
   - Update operations are O(1) on average for dictionary

2. Space Complexity: O(n + m)
   - Storage for merged dictionary with all objects
   - Additional space for result array

Functional Approach:
1. Time Complexity: O((n + m) + k*log(k))
   - Same as main solution
   - Dictionary comprehension is O(n)

2. Space Complexity: O(n + m)
   - Similar space requirements

Optimized Approach:
1. Time Complexity: O((n + m) + k*log(k))
   - Same time complexity but reduces unnecessary copying
   - Set operations for ID checking are O(1) average

2. Space Complexity: O(n + m)
   - Minimizes copying when no merge is needed
   - More memory efficient in practice

Key Insights:
- Dictionary provides O(1) average lookup and update
- Sorting is required for final result ordering
- arr2 values always override arr1 values for same ID
- Update() method performs shallow merge of dictionaries
- Deep merge would require recursive handling of nested objects

Topic: Arrays, Hash Tables, Object Manipulation, Merging
"""
