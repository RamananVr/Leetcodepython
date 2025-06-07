"""
2695. Array Wrapper

PROBLEM STATEMENT:
Create an ArrayWrapper class that wraps an array and provides additional functionality:
1. Addition operation should sum all elements from both arrays
2. String representation should show comma-separated values in brackets
3. The wrapper should behave like the original array for indexing and iteration
4. Support for length property and other array-like operations

EXAMPLES:
Example 1:
arr1 = ArrayWrapper([1, 2, 3])
arr2 = ArrayWrapper([4, 5, 6])
result = arr1 + arr2  # Should return 21 (1+2+3+4+5+6)

Example 2:
arr = ArrayWrapper([1, 2, 3])
str(arr)  # Should return "[1,2,3]"

Example 3:
arr = ArrayWrapper([1, 2, 3])
arr[0]  # Should return 1
len(arr)  # Should return 3

CONSTRAINTS:
- The array can contain any numeric values
- Addition should work with other ArrayWrapper instances
- String representation should match the specified format
"""

def create_array_wrapper():
    """
    Implementation of an Array Wrapper with custom operations.
    """
    
    class ArrayWrapper:
        def __init__(self, array):
            """
            Initialize the ArrayWrapper with an array.
            
            Args:
                array: List of numbers to wrap
            """
            self.array = list(array)  # Create a copy to avoid external modifications
        
        def __add__(self, other):
            """
            Add two ArrayWrapper instances by summing all their elements.
            
            Args:
                other: Another ArrayWrapper instance
            
            Returns:
                Sum of all elements from both arrays
            """
            if isinstance(other, ArrayWrapper):
                return sum(self.array) + sum(other.array)
            elif isinstance(other, (list, tuple)):
                return sum(self.array) + sum(other)
            elif isinstance(other, (int, float)):
                return sum(self.array) + other
            else:
                raise TypeError(f"Cannot add ArrayWrapper with {type(other)}")
        
        def __radd__(self, other):
            """Reverse addition - when ArrayWrapper is on the right side"""
            return self.__add__(other)
        
        def __str__(self):
            """
            String representation of the array.
            
            Returns:
                String in format "[element1,element2,element3]"
            """
            return "[" + ",".join(str(x) for x in self.array) + "]"
        
        def __repr__(self):
            """Representation for debugging"""
            return f"ArrayWrapper({self.array})"
        
        def __getitem__(self, index):
            """
            Get item at index.
            
            Args:
                index: Index to access
            
            Returns:
                Element at the specified index
            """
            return self.array[index]
        
        def __setitem__(self, index, value):
            """
            Set item at index.
            
            Args:
                index: Index to set
                value: Value to set
            """
            self.array[index] = value
        
        def __len__(self):
            """
            Get length of the array.
            
            Returns:
                Length of the wrapped array
            """
            return len(self.array)
        
        def __iter__(self):
            """
            Make the wrapper iterable.
            
            Returns:
                Iterator over the array elements
            """
            return iter(self.array)
        
        def __contains__(self, item):
            """
            Check if item is in the array.
            
            Args:
                item: Item to check for
            
            Returns:
                True if item is in array, False otherwise
            """
            return item in self.array
        
        def __eq__(self, other):
            """
            Check equality with another ArrayWrapper or list.
            
            Args:
                other: Other object to compare with
            
            Returns:
                True if arrays are equal, False otherwise
            """
            if isinstance(other, ArrayWrapper):
                return self.array == other.array
            elif isinstance(other, list):
                return self.array == other
            else:
                return False
        
        def __bool__(self):
            """
            Boolean representation (True if not empty).
            
            Returns:
                False if array is empty, True otherwise
            """
            return bool(self.array)
        
        # Array-like methods
        def append(self, item):
            """Add item to the end of the array"""
            self.array.append(item)
        
        def extend(self, items):
            """Extend array with items"""
            self.array.extend(items)
        
        def insert(self, index, item):
            """Insert item at index"""
            self.array.insert(index, item)
        
        def remove(self, item):
            """Remove first occurrence of item"""
            self.array.remove(item)
        
        def pop(self, index=-1):
            """Remove and return item at index"""
            return self.array.pop(index)
        
        def index(self, item):
            """Find index of item"""
            return self.array.index(item)
        
        def count(self, item):
            """Count occurrences of item"""
            return self.array.count(item)
        
        def sort(self, key=None, reverse=False):
            """Sort the array in place"""
            self.array.sort(key=key, reverse=reverse)
        
        def reverse(self):
            """Reverse the array in place"""
            self.array.reverse()
        
        def copy(self):
            """Create a copy of the ArrayWrapper"""
            return ArrayWrapper(self.array.copy())
        
        def sum(self):
            """Get sum of all elements"""
            return sum(self.array)
        
        def max(self):
            """Get maximum element"""
            return max(self.array) if self.array else None
        
        def min(self):
            """Get minimum element"""
            return min(self.array) if self.array else None
        
        def average(self):
            """Get average of all elements"""
            return sum(self.array) / len(self.array) if self.array else 0
        
        def to_list(self):
            """Convert to regular list"""
            return self.array.copy()
    
    return ArrayWrapper

def test_array_wrapper():
    """Test the Array Wrapper implementation."""
    ArrayWrapper = create_array_wrapper()
    
    # Test 1: Basic addition
    arr1 = ArrayWrapper([1, 2, 3])
    arr2 = ArrayWrapper([4, 5, 6])
    result = arr1 + arr2
    assert result == 21  # 1+2+3+4+5+6 = 21
    
    # Test 2: String representation
    arr = ArrayWrapper([1, 2, 3])
    assert str(arr) == "[1,2,3]"
    
    arr_empty = ArrayWrapper([])
    assert str(arr_empty) == "[]"
    
    arr_single = ArrayWrapper([42])
    assert str(arr_single) == "[42]"
    
    # Test 3: Indexing
    arr = ArrayWrapper([10, 20, 30])
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30
    assert arr[-1] == 30
    
    # Test 4: Setting items
    arr[1] = 99
    assert arr[1] == 99
    assert str(arr) == "[10,99,30]"
    
    # Test 5: Length
    arr = ArrayWrapper([1, 2, 3, 4, 5])
    assert len(arr) == 5
    
    empty_arr = ArrayWrapper([])
    assert len(empty_arr) == 0
    
    # Test 6: Iteration
    arr = ArrayWrapper([1, 2, 3])
    result = []
    for item in arr:
        result.append(item * 2)
    assert result == [2, 4, 6]
    
    # Test 7: Contains
    arr = ArrayWrapper([1, 2, 3])
    assert 2 in arr
    assert 5 not in arr
    
    # Test 8: Equality
    arr1 = ArrayWrapper([1, 2, 3])
    arr2 = ArrayWrapper([1, 2, 3])
    arr3 = ArrayWrapper([1, 2, 4])
    
    assert arr1 == arr2
    assert arr1 != arr3
    assert arr1 == [1, 2, 3]
    
    # Test 9: Boolean representation
    arr_with_items = ArrayWrapper([1, 2, 3])
    arr_empty = ArrayWrapper([])
    
    assert bool(arr_with_items) == True
    assert bool(arr_empty) == False
    
    # Test 10: Array methods
    arr = ArrayWrapper([1, 2, 3])
    arr.append(4)
    assert arr.to_list() == [1, 2, 3, 4]
    
    arr.extend([5, 6])
    assert arr.to_list() == [1, 2, 3, 4, 5, 6]
    
    arr.insert(0, 0)
    assert arr.to_list() == [0, 1, 2, 3, 4, 5, 6]
    
    # Test 11: Mathematical methods
    arr = ArrayWrapper([10, 20, 30, 40])
    assert arr.sum() == 100
    assert arr.max() == 40
    assert arr.min() == 10
    assert arr.average() == 25.0
    
    # Test 12: Addition with different types
    arr = ArrayWrapper([1, 2, 3])
    assert arr + ArrayWrapper([4, 5]) == 15  # 1+2+3+4+5
    assert arr + [4, 5] == 15  # Should work with regular lists
    assert arr + 10 == 16  # 1+2+3+10
    
    # Test 13: Copy
    arr1 = ArrayWrapper([1, 2, 3])
    arr2 = arr1.copy()
    arr2[0] = 99
    
    assert arr1[0] == 1  # Original unchanged
    assert arr2[0] == 99  # Copy changed
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_array_wrapper()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: 
  - Addition: O(n + m) where n and m are array lengths
  - String representation: O(n) where n is array length
  - Most operations: O(1) or O(n) depending on operation
- Space Complexity: O(n) to store the wrapped array

TOPICS: Design, Object-Oriented Programming, Operator Overloading, Array Manipulation

KEY INSIGHTS:
1. Operator overloading allows custom behavior for built-in operations
2. Magic methods (__str__, __add__, etc.) provide Pythonic interfaces
3. Wrapping allows extending functionality while maintaining compatibility
4. Copy semantics prevent external modifications of internal state
5. Comprehensive method support makes wrapper feel like native array
"""
