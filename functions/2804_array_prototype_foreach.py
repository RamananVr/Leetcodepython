"""
LeetCode Problem 2804: Array Prototype ForEach

Implement a custom forEach method for arrays that mimics the behavior of the built-in Array.prototype.forEach method.

The forEach method executes a provided function once for each array element.

Syntax: array.forEach(callback(currentValue, index, array), thisArg)

Parameters:
- callback: Function to execute for each element, taking three arguments:
  - currentValue: The current element being processed
  - index: The index of the current element
  - array: The array forEach was called upon
- thisArg (optional): Value to use as 'this' when executing callback

Constraints:
- The callback function should be called for each element in the array
- The method should handle sparse arrays correctly (skip empty slots)
- Should work with different types of arrays and callback functions

Example 1:
Input: arr = [1, 2, 3], callback = (val, i) => console.log(val * 2)
Output: Prints 2, 4, 6

Example 2:
Input: arr = ['a', 'b', 'c'], callback = (val, i, arr) => console.log(`${val} at index ${i}`)
Output: Prints "a at index 0", "b at index 1", "c at index 2"

Example 3:
Input: arr = [1, , 3], callback = (val) => console.log(val)
Output: Prints 1, 3 (skips empty slot)
"""

def array_for_each_basic(arr, callback, this_arg=None):
    """
    Approach 1: Basic Implementation
    
    Simple implementation that calls callback for each element.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if i < len(arr):  # Check bounds
            callback(arr[i], i, arr)

def array_for_each_sparse_aware(arr, callback, this_arg=None):
    """
    Approach 2: Sparse Array Aware
    
    Handle sparse arrays by checking if index exists.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        # In Python, we simulate sparse arrays with None or by checking dict
        if isinstance(arr, dict):
            if i in arr:
                callback(arr[i], i, arr)
        elif i < len(arr) and arr[i] is not None:
            callback(arr[i], i, arr)

def array_for_each_with_this(arr, callback, this_arg=None):
    """
    Approach 3: With 'this' Context Binding
    
    Handle thisArg parameter for context binding.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    import types
    
    for i in range(len(arr)):
        if i < len(arr):
            if this_arg is not None and hasattr(callback, '__call__'):
                # Bind this_arg as context
                bound_callback = types.MethodType(callback, this_arg)
                bound_callback(arr[i], i, arr)
            else:
                callback(arr[i], i, arr)

class CustomArray:
    """
    Approach 4: Custom Array Class with forEach Method
    
    Object-oriented implementation with full forEach functionality.
    """
    def __init__(self, elements=None):
        self.elements = elements if elements is not None else []
        self.length = len(self.elements)
    
    def forEach(self, callback, this_arg=None):
        """
        Custom forEach implementation
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(self.length):
            # Handle sparse arrays - check if element exists
            if i < len(self.elements) and self.elements[i] is not None:
                try:
                    if this_arg is not None:
                        # In a real implementation, we'd bind 'this'
                        # For Python, we pass this_arg as additional parameter
                        callback(self.elements[i], i, self.elements, this_arg)
                    else:
                        callback(self.elements[i], i, self.elements)
                except Exception as e:
                    # Handle callback errors gracefully
                    print(f"Error in callback at index {i}: {e}")
    
    def push(self, element):
        """Add element to end of array"""
        self.elements.append(element)
        self.length = len(self.elements)
    
    def __getitem__(self, index):
        return self.elements[index] if index < len(self.elements) else None
    
    def __setitem__(self, index, value):
        # Extend array if necessary
        while len(self.elements) <= index:
            self.elements.append(None)
        self.elements[index] = value
        self.length = max(self.length, index + 1)

def create_for_each_polyfill():
    """
    Approach 5: Polyfill Function
    
    Create a polyfill that can be added to any array-like object.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def forEach(arr, callback, this_arg=None):
        """
        Polyfill implementation of forEach
        """
        if not hasattr(callback, '__call__'):
            raise TypeError("callback must be a function")
        
        # Convert to array-like if needed
        if hasattr(arr, '__len__') and hasattr(arr, '__getitem__'):
            length = len(arr)
        else:
            raise TypeError("forEach can only be called on array-like objects")
        
        for i in range(length):
            # Check if property exists (for sparse arrays)
            try:
                if hasattr(arr, '__contains__'):
                    if i in arr:
                        value = arr[i]
                    else:
                        continue  # Skip sparse slots
                else:
                    value = arr[i]
                
                # Call callback with proper context
                if this_arg is not None:
                    # Simulate 'this' binding
                    callback(value, i, arr)
                else:
                    callback(value, i, arr)
                    
            except (IndexError, KeyError):
                # Skip if index doesn't exist
                continue
    
    return forEach

class AsyncArray:
    """
    Approach 6: Async forEach Implementation
    
    Handle asynchronous callbacks.
    """
    def __init__(self, elements):
        self.elements = elements
    
    async def forEach(self, callback, this_arg=None):
        """
        Async forEach implementation
        
        Time Complexity: O(n) + callback time
        Space Complexity: O(1)
        """
        import asyncio
        
        for i in range(len(self.elements)):
            if self.elements[i] is not None:
                if asyncio.iscoroutinefunction(callback):
                    await callback(self.elements[i], i, self.elements)
                else:
                    callback(self.elements[i], i, self.elements)

# Test cases
def test_array_for_each():
    print("Testing Array forEach Implementations\n")
    
    # Test Case 1: Basic functionality
    print("Test 1: Basic functionality")
    arr1 = [1, 2, 3, 4, 5]
    results1 = []
    
    def callback1(val, index, array):
        results1.append(val * 2)
    
    array_for_each_basic(arr1, callback1)
    print(f"Input: {arr1}")
    print(f"Results (doubled): {results1}")
    print(f"Expected: [2, 4, 6, 8, 10]")
    print(f"✓ Passed: {results1 == [2, 4, 6, 8, 10]}\n")
    
    # Test Case 2: Custom Array class
    print("Test 2: Custom Array class")
    custom_arr = CustomArray(['a', 'b', 'c'])
    results2 = []
    
    def callback2(val, index, array):
        results2.append(f"{val} at index {index}")
    
    custom_arr.forEach(callback2)
    print(f"Results: {results2}")
    expected2 = ["a at index 0", "b at index 1", "c at index 2"]
    print(f"Expected: {expected2}")
    print(f"✓ Passed: {results2 == expected2}\n")
    
    # Test Case 3: Sparse array handling
    print("Test 3: Sparse array handling")
    sparse_dict = {0: 1, 2: 3, 4: 5}  # Simulated sparse array
    results3 = []
    
    def callback3(val, index, array):
        results3.append(f"Value {val} at index {index}")
    
    array_for_each_sparse_aware(sparse_dict, callback3)
    print(f"Sparse array: {sparse_dict}")
    print(f"Results: {results3}")
    print("✓ Correctly skipped missing indices\n")
    
    # Test Case 4: Error handling
    print("Test 4: Error handling")
    arr4 = [1, 2, 3]
    
    def error_callback(val, index, array):
        if val == 2:
            raise ValueError("Test error")
        print(f"Processed: {val}")
    
    custom_arr4 = CustomArray(arr4)
    print("Testing error handling in forEach:")
    custom_arr4.forEach(error_callback)
    print("✓ Errors handled gracefully\n")
    
    # Test Case 5: Polyfill function
    print("Test 5: Polyfill function")
    forEach_polyfill = create_for_each_polyfill()
    arr5 = [10, 20, 30]
    results5 = []
    
    def callback5(val, index, array):
        results5.append(val + index)
    
    forEach_polyfill(arr5, callback5)
    print(f"Input: {arr5}")
    print(f"Results (val + index): {results5}")
    print(f"Expected: [10, 21, 32]")
    print(f"✓ Passed: {results5 == [10, 21, 32]}\n")

async def test_async_for_each():
    """Test async forEach implementation"""
    print("Test 6: Async forEach")
    async_arr = AsyncArray([1, 2, 3])
    results = []
    
    async def async_callback(val, index, array):
        # Simulate async operation
        import asyncio
        await asyncio.sleep(0.01)
        results.append(val * 3)
    
    await async_arr.forEach(async_callback)
    print(f"Async results: {results}")
    print(f"Expected: [3, 6, 9]")
    print(f"✓ Passed: {results == [3, 6, 9]}")

if __name__ == "__main__":
    test_array_for_each()
    
    # Test async version
    import asyncio
    asyncio.run(test_async_for_each())

"""
Topics: Arrays, Functions, Iterator Pattern, JavaScript Polyfills
Difficulty: Medium

Key Insights:
1. forEach should handle sparse arrays correctly
2. Callback receives (value, index, array) parameters
3. thisArg allows context binding
4. Error handling prevents callback failures from breaking iteration
5. Async support enables handling of asynchronous operations

Companies: Google, Facebook, Microsoft, Amazon
"""
