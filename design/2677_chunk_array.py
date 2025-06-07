"""
LeetCode Question #2677: Chunk Array

Problem Statement:
Given an array arr and a chunk size size, return a chunked array.

A chunked array contains the original elements in arr, but consists of subarrays each of length size. The length of the last subarray may be less than size if arr.length is not evenly divisible by size.

You may assume the array is a valid JSON array. If arr is empty, return an empty array [].

Examples:
Example 1:
Input: arr = [1,2,3,4,5], size = 1
Output: [[1],[2],[3],[4],[5]]
Explanation: The arr has been split into subarrays each with 1 element.

Example 2:
Input: arr = [1,9,6,3,2], size = 3
Output: [[1,9,6],[3,2]]
Explanation: The arr has been split into subarrays with 3 elements. However, only two elements are left for the 2nd subarray.

Example 3:
Input: arr = [8,5,3,2,6], size = 6
Output: [[8,5,3,2,6]]
Explanation: The size is greater than arr.length thus all elements are in the first subarray.

Example 4:
Input: arr = [], size = 1
Output: []
Explanation: There are no elements to be chunked so an empty array is returned.

Constraints:
- arr is a valid JSON array
- 2 <= size <= 1000
- 0 <= arr.length <= 1000
"""

from typing import List, Any

def chunk(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Chunk array into subarrays of given size.
    
    Time: O(n) where n is length of array
    Space: O(n) for the result array
    """
    if not arr or size <= 0:
        return []
    
    result = []
    for i in range(0, len(arr), size):
        chunk_subarray = arr[i:i + size]
        result.append(chunk_subarray)
    
    return result

def chunkIterative(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Iterative approach building chunks one by one.
    
    Time: O(n)
    Space: O(n)
    """
    if not arr or size <= 0:
        return []
    
    result = []
    current_chunk = []
    
    for element in arr:
        current_chunk.append(element)
        
        if len(current_chunk) == size:
            result.append(current_chunk)
            current_chunk = []
    
    # Add remaining elements if any
    if current_chunk:
        result.append(current_chunk)
    
    return result

def chunkRecursive(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Recursive approach to chunking.
    
    Time: O(n)
    Space: O(n) + O(n/size) for recursion stack
    """
    if not arr or size <= 0:
        return []
    
    if len(arr) <= size:
        return [arr]
    
    return [arr[:size]] + chunkRecursive(arr[size:], size)

def chunkWithGenerator(arr: List[Any], size: int):
    """
    Generator version for memory efficiency.
    
    Time: O(1) per chunk generated
    Space: O(size) per chunk
    """
    if not arr or size <= 0:
        return
    
    for i in range(0, len(arr), size):
        yield arr[i:i + size]

def chunkNumpy(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Using numpy for chunking (if available).
    
    Time: O(n)
    Space: O(n)
    """
    try:
        import numpy as np
        
        if not arr or size <= 0:
            return []
        
        # Convert to numpy array
        np_arr = np.array(arr)
        
        # Split into chunks
        chunks = []
        for i in range(0, len(np_arr), size):
            chunk_array = np_arr[i:i + size]
            chunks.append(chunk_array.tolist())
        
        return chunks
    
    except ImportError:
        # Fallback to regular implementation
        return chunk(arr, size)

def chunkWithValidation(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Version with input validation and error handling.
    
    Time: O(n)
    Space: O(n)
    """
    # Input validation
    if not isinstance(arr, list):
        raise ValueError("First argument must be a list")
    
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    if not arr:
        return []
    
    result = []
    
    try:
        for i in range(0, len(arr), size):
            chunk_subarray = arr[i:i + size]
            result.append(chunk_subarray)
    except Exception as e:
        raise RuntimeError(f"Error while chunking array: {e}")
    
    return result

def chunkFunctional(arr: List[Any], size: int) -> List[List[Any]]:
    """
    Functional programming approach using list comprehension.
    
    Time: O(n)
    Space: O(n)
    """
    if not arr or size <= 0:
        return []
    
    return [arr[i:i + size] for i in range(0, len(arr), size)]

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]),
        ([1, 9, 6, 3, 2], 3, [[1, 9, 6], [3, 2]]),
        ([8, 5, 3, 2, 6], 6, [[8, 5, 3, 2, 6]]),
        ([], 1, []),
        ([1, 2, 3, 4, 5, 6], 2, [[1, 2], [3, 4], [5, 6]]),
        ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [4, 5, 6], [7]]),
        (["a", "b", "c", "d"], 2, [["a", "b"], ["c", "d"]]),
    ]
    
    print("Testing main approach:")
    for arr, size, expected in test_cases:
        result = chunk(arr, size)
        print(f"chunk({arr}, {size}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing iterative approach:")
    for arr, size, expected in test_cases:
        result = chunkIterative(arr, size)
        print(f"chunkIterative({arr}, {size}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing recursive approach:")
    for arr, size, expected in test_cases:
        result = chunkRecursive(arr, size)
        print(f"chunkRecursive({arr}, {size}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing functional approach:")
    for arr, size, expected in test_cases:
        result = chunkFunctional(arr, size)
        print(f"chunkFunctional({arr}, {size}) = {result}")
        print(f"Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing generator approach:")
    arr, size = [1, 2, 3, 4, 5], 2
    chunks = list(chunkWithGenerator(arr, size))
    print(f"Generator chunks for {arr} with size {size}: {chunks}")
    
    print("\nTesting validation:")
    try:
        chunkWithValidation("invalid", 2)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        chunkWithValidation([1, 2, 3], 0)
    except ValueError as e:
        print(f"Caught expected error: {e}")

"""
Time and Space Complexity Analysis:

Main Approach (chunk):
Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - result array contains all elements

Iterative Approach:
Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - result array and temporary chunk storage

Recursive Approach:
Time Complexity: O(n) - each element processed once
Space Complexity: O(n) + O(n/size) - result array plus recursion stack

Generator Approach:
Time Complexity: O(1) per chunk generated, O(n) total
Space Complexity: O(size) per chunk - memory efficient

Functional Approach:
Time Complexity: O(n) - list comprehension with slicing
Space Complexity: O(n) - result array

Key Insights:
1. Array slicing in Python creates new sublists efficiently
2. Generator approach is memory-efficient for large arrays
3. Edge cases include empty arrays and size larger than array length
4. Different approaches offer trade-offs between readability and performance
5. List comprehension provides concise functional style

JavaScript Equivalent:
```javascript
function chunk(arr, size) {
    if (!arr.length || size <= 0) return [];
    
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
}
```

Topic: Arrays, Array Manipulation, Functional Programming
"""
