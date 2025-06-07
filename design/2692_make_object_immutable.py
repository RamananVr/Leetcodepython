"""
2692. Make Object Immutable

PROBLEM STATEMENT:
Write a function that takes an object and returns a new immutable version of it. The immutable object should:
1. Prevent any modifications to its properties
2. Recursively make all nested objects and arrays immutable
3. Throw an error when attempting to modify the object
4. Allow reading properties normally

EXAMPLES:
Example 1:
obj = {"x": 1, "y": 2}
immutableObj = makeImmutable(obj)
console.log(immutableObj.x) // 1
immutableObj.x = 10 // Error: Cannot modify immutable object

Example 2:
obj = {"arr": [1, 2], "nested": {"a": 1}}
immutableObj = makeImmutable(obj)
console.log(immutableObj.arr[0]) // 1
immutableObj.arr.push(3) // Error: Cannot modify immutable object

CONSTRAINTS:
- The object can contain nested objects and arrays
- All primitive values should remain accessible
- Modifications should throw appropriate errors
"""

def make_object_immutable():
    """
    Implementation to make objects immutable with deep freezing.
    """
    
    class ImmutableObject:
        def __init__(self, obj):
            self._data = self._deep_freeze(obj)
            self._frozen = True
        
        def _deep_freeze(self, obj):
            """Recursively create immutable version of object"""
            if obj is None or isinstance(obj, (int, float, str, bool)):
                return obj
            elif isinstance(obj, list):
                return ImmutableList([self._deep_freeze(item) for item in obj])
            elif isinstance(obj, dict):
                frozen_dict = {}
                for key, value in obj.items():
                    frozen_dict[key] = self._deep_freeze(value)
                return ImmutableDict(frozen_dict)
            else:
                return obj
        
        def __getattr__(self, name):
            if name.startswith('_'):
                return object.__getattribute__(self, name)
            if hasattr(self._data, name):
                return getattr(self._data, name)
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        def __setattr__(self, name, value):
            if name.startswith('_') and not hasattr(self, '_frozen'):
                object.__setattr__(self, name, value)
            else:
                raise TypeError("Cannot modify immutable object")
        
        def __getitem__(self, key):
            return self._data[key]
        
        def __setitem__(self, key, value):
            raise TypeError("Cannot modify immutable object")
    
    class ImmutableDict:
        def __init__(self, data):
            object.__setattr__(self, '_data', data)
            object.__setattr__(self, '_frozen', True)
        
        def __getitem__(self, key):
            return self._data[key]
        
        def __setitem__(self, key, value):
            raise TypeError("Cannot modify immutable object")
        
        def __getattr__(self, name):
            if name.startswith('_'):
                return object.__getattribute__(self, name)
            if name in self._data:
                return self._data[name]
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        def __setattr__(self, name, value):
            if name.startswith('_') and not hasattr(self, '_frozen'):
                object.__setattr__(self, name, value)
            else:
                raise TypeError("Cannot modify immutable object")
        
        def keys(self):
            return self._data.keys()
        
        def values(self):
            return self._data.values()
        
        def items(self):
            return self._data.items()
        
        def get(self, key, default=None):
            return self._data.get(key, default)
        
        def __repr__(self):
            return f"ImmutableDict({self._data})"
    
    class ImmutableList:
        def __init__(self, data):
            object.__setattr__(self, '_data', list(data))
            object.__setattr__(self, '_frozen', True)
        
        def __getitem__(self, index):
            return self._data[index]
        
        def __setitem__(self, index, value):
            raise TypeError("Cannot modify immutable object")
        
        def __len__(self):
            return len(self._data)
        
        def __iter__(self):
            return iter(self._data)
        
        def append(self, value):
            raise TypeError("Cannot modify immutable object")
        
        def extend(self, values):
            raise TypeError("Cannot modify immutable object")
        
        def insert(self, index, value):
            raise TypeError("Cannot modify immutable object")
        
        def remove(self, value):
            raise TypeError("Cannot modify immutable object")
        
        def pop(self, index=-1):
            raise TypeError("Cannot modify immutable object")
        
        def push(self, value):
            raise TypeError("Cannot modify immutable object")
        
        def __repr__(self):
            return f"ImmutableList({self._data})"
    
    def make_immutable(obj):
        """Make an object immutable"""
        return ImmutableObject(obj)._data
    
    return make_immutable

def test_make_object_immutable():
    """Test the immutable object implementation."""
    make_immutable = make_object_immutable()
    
    # Test 1: Basic object immutability
    obj1 = {"x": 1, "y": 2}
    immutable_obj1 = make_immutable(obj1)
    
    # Should be able to read
    assert immutable_obj1["x"] == 1
    assert immutable_obj1["y"] == 2
    
    # Should not be able to modify
    try:
        immutable_obj1["x"] = 10
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    # Test 2: Nested object immutability
    obj2 = {"arr": [1, 2, 3], "nested": {"a": 1, "b": 2}}
    immutable_obj2 = make_immutable(obj2)
    
    # Should be able to read nested values
    assert immutable_obj2["arr"][0] == 1
    assert immutable_obj2["nested"]["a"] == 1
    
    # Should not be able to modify nested arrays
    try:
        immutable_obj2["arr"].append(4)
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    # Should not be able to modify nested objects
    try:
        immutable_obj2["nested"]["c"] = 3
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    # Test 3: Array immutability
    arr = [1, 2, [3, 4]]
    immutable_arr = make_immutable(arr)
    
    # Should be able to read
    assert immutable_arr[0] == 1
    assert immutable_arr[2][0] == 3
    
    # Should not be able to modify
    try:
        immutable_arr[0] = 10
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    try:
        immutable_arr.append(5)
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    # Test 4: Deep nesting
    obj3 = {"level1": {"level2": {"level3": [1, 2, 3]}}}
    immutable_obj3 = make_immutable(obj3)
    
    assert immutable_obj3["level1"]["level2"]["level3"][0] == 1
    
    try:
        immutable_obj3["level1"]["level2"]["level3"].append(4)
        assert False, "Should have thrown error"
    except TypeError:
        pass
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_make_object_immutable()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(n) where n is the total number of elements in the object tree
- Space Complexity: O(n) for creating the immutable copies

TOPICS: Design, Object-Oriented Programming, Immutability, Proxy Pattern

KEY INSIGHTS:
1. True immutability requires preventing all modification operations
2. Recursive freezing ensures nested structures are also immutable
3. Proxy-like behavior allows normal reading while blocking writes
4. Error handling provides clear feedback when modifications are attempted
5. Custom classes can override built-in methods to control behavior
"""
