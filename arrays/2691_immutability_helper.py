"""
2691. Immutability Helper

PROBLEM STATEMENT:
You are given an object obj and an array of strings operations where operations[i] is a string 
representing a method name that should be called on obj. The methods can be:
- get(key) - returns the value at the given key
- set(key, value) - sets the value at the given key and returns the updated object
- push(value) - pushes a value to the array and returns the updated array

The object should be immutable, meaning that calling set or push should return a new object/array 
rather than modifying the original.

EXAMPLES:
Example 1:
obj = {"a": 1, "b": 2}
operations = ["get", "a"]
Output: 1

Example 2:
obj = [1, 2, 3]
operations = ["push", 4]
Output: [1, 2, 3, 4]

Example 3:
obj = {"x": {"y": 1}}
operations = ["set", "x.z", 5]
Output: {"x": {"y": 1, "z": 5}}

CONSTRAINTS:
- 1 <= operations.length <= 1000
- obj can be an object, array, or primitive value
- All operations are valid for the given object type
"""

def immutability_helper():
    """
    Implementation of immutable helper for objects and arrays.
    """
    
    class ImmutableHelper:
        def __init__(self, obj):
            self.obj = obj
        
        def get(self, path):
            """Get value at given path"""
            current = self.obj
            keys = path.split('.')
            
            for key in keys:
                if isinstance(current, dict):
                    current = current[key]
                elif isinstance(current, list):
                    current = current[int(key)]
                else:
                    raise ValueError("Invalid path")
            
            return current
        
        def set(self, path, value):
            """Set value at given path and return new object"""
            import copy
            new_obj = copy.deepcopy(self.obj)
            
            keys = path.split('.')
            current = new_obj
            
            for i, key in enumerate(keys[:-1]):
                if isinstance(current, dict):
                    if key not in current:
                        current[key] = {}
                    current = current[key]
                elif isinstance(current, list):
                    current = current[int(key)]
            
            final_key = keys[-1]
            if isinstance(current, dict):
                current[final_key] = value
            elif isinstance(current, list):
                current[int(final_key)] = value
            
            return ImmutableHelper(new_obj)
        
        def push(self, value):
            """Push value to array and return new array"""
            if not isinstance(self.obj, list):
                raise ValueError("Push can only be called on arrays")
            
            new_array = self.obj + [value]
            return ImmutableHelper(new_array)
        
        def get_value(self):
            return self.obj
    
    return ImmutableHelper

def test_immutability_helper():
    """Test the immutable helper implementation."""
    Helper = immutability_helper()
    
    # Test 1: Basic object get
    obj1 = Helper({"a": 1, "b": 2})
    assert obj1.get("a") == 1
    assert obj1.get("b") == 2
    
    # Test 2: Array push
    obj2 = Helper([1, 2, 3])
    new_obj2 = obj2.push(4)
    assert new_obj2.get_value() == [1, 2, 3, 4]
    assert obj2.get_value() == [1, 2, 3]  # Original unchanged
    
    # Test 3: Nested object set
    obj3 = Helper({"x": {"y": 1}})
    new_obj3 = obj3.set("x.z", 5)
    expected = {"x": {"y": 1, "z": 5}}
    assert new_obj3.get_value() == expected
    assert obj3.get_value() == {"x": {"y": 1}}  # Original unchanged
    
    # Test 4: Array access
    obj4 = Helper([10, 20, 30])
    assert obj4.get("0") == 10
    assert obj4.get("1") == 20
    assert obj4.get("2") == 30
    
    # Test 5: Set in array
    obj5 = Helper([1, 2, 3])
    new_obj5 = obj5.set("1", 99)
    assert new_obj5.get_value() == [1, 99, 3]
    assert obj5.get_value() == [1, 2, 3]  # Original unchanged
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_immutability_helper()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: 
  - get(): O(d) where d is the depth of the path
  - set(): O(n) where n is the size of the object (due to deep copy)
  - push(): O(n) where n is the length of the array
- Space Complexity: O(n) for creating copies of the object/array

TOPICS: Design, Object-Oriented Programming, Immutability, Deep Copy

KEY INSIGHTS:
1. Immutability requires creating new objects instead of modifying existing ones
2. Deep copying ensures complete isolation from original objects
3. Path-based access allows navigation through nested structures
4. Type checking is important for different operations on different data types
"""
