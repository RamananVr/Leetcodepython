"""
LeetCode Question #2720: Chunk Array

Problem Statement:
Given an array `arr` and a chunk size `size`, return a chunked array. A chunked array contains the original elements in `arr`, but consists of subarrays each of length `size`. The length of the last subarray may be less than `size` if `arr.length` is not evenly divisible by `size`.

You may assume the array is a valid JSON array and `size` is a positive integer.

Constraints:
- `arr` is a valid JSON array
- `2 <= JSON.stringify(arr).length <= 10^5`
- `1 <= size <= arr.length + 1`

Example:
Input: arr = [1,2,3,4,5], size = 1
Output: [[1],[2],[3],[4],[5]]
Explanation: The arr has been split into subarrays each with 1 element.

Input: arr = [1,9,6,3,2], size = 3
Output: [[1,9,6],[3,2]]
Explanation: The arr has been split into subarrays with 3 elements. However, only two elements are left for the 2nd subarray.

Input: arr = [8,5,3,2,6], size = 6
Output: [[8,5,3,2,6]]
Explanation: Size is greater than arr.length thus all elements are in the first subarray.

Input: arr = [], size = 1
Output: []
Explanation: There are no elements to be chunked so an empty array is returned.
"""

def chunk(arr, size):
    """
    Split array into chunks of specified size.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Returns:
        List of sublists where each sublist has at most 'size' elements
    """
    if not arr:
        return []
    
    result = []
    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])
    
    return result

def chunk_iterative(arr, size):
    """
    Iterative approach to chunk array.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Returns:
        List of sublists where each sublist has at most 'size' elements
    """
    if not arr:
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

def chunk_generator(arr, size):
    """
    Generator-based approach for memory efficiency.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Yields:
        Sublists where each sublist has at most 'size' elements
    """
    for i in range(0, len(arr), size):
        yield arr[i:i + size]

def chunk_list_comprehension(arr, size):
    """
    List comprehension approach.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Returns:
        List of sublists where each sublist has at most 'size' elements
    """
    return [arr[i:i + size] for i in range(0, len(arr), size)]

def chunk_recursive(arr, size):
    """
    Recursive approach to chunk array.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Returns:
        List of sublists where each sublist has at most 'size' elements
    """
    if not arr:
        return []
    
    if len(arr) <= size:
        return [arr]
    
    return [arr[:size]] + chunk_recursive(arr[size:], size)

def chunk_numpy_style(arr, size):
    """
    NumPy-style splitting approach.
    
    Args:
        arr: List of elements to be chunked
        size: Integer representing the chunk size
    
    Returns:
        List of sublists where each sublist has at most 'size' elements
    """
    if not arr:
        return []
    
    # Calculate split points
    num_chunks = (len(arr) + size - 1) // size  # Ceiling division
    chunks = []
    
    for i in range(num_chunks):
        start_idx = i * size
        end_idx = min(start_idx + size, len(arr))
        chunks.append(arr[start_idx:end_idx])
    
    return chunks

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr = [1, 2, 3, 4, 5]
    size = 1
    result = chunk(arr, size)
    expected = [[1], [2], [3], [4], [5]]
    print(f"Test 1 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 2
    arr = [1, 9, 6, 3, 2]
    size = 3
    result = chunk(arr, size)
    expected = [[1, 9, 6], [3, 2]]
    print(f"Test 2 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 3
    arr = [8, 5, 3, 2, 6]
    size = 6
    result = chunk(arr, size)
    expected = [[8, 5, 3, 2, 6]]
    print(f"Test 3 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 4
    arr = []
    size = 1
    result = chunk(arr, size)
    expected = []
    print(f"Test 4 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 5 - Perfect division
    arr = [1, 2, 3, 4, 5, 6]
    size = 2
    result = chunk(arr, size)
    expected = [[1, 2], [3, 4], [5, 6]]
    print(f"Test 5 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 6 - Single element array
    arr = [42]
    size = 1
    result = chunk(arr, size)
    expected = [[42]]
    print(f"Test 6 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 7 - Size larger than array
    arr = [1, 2, 3]
    size = 10
    result = chunk(arr, size)
    expected = [[1, 2, 3]]
    print(f"Test 7 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test all implementations produce same results
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_size = 4
    
    results = [
        chunk(test_arr, test_size),
        chunk_iterative(test_arr, test_size),
        list(chunk_generator(test_arr, test_size)),
        chunk_list_comprehension(test_arr, test_size),
        chunk_recursive(test_arr, test_size),
        chunk_numpy_style(test_arr, test_size)
    ]
    
    # All implementations should produce the same result
    for i in range(1, len(results)):
        assert results[0] == results[i], f"Implementation {i} differs from base implementation"
    
    print("All test cases and implementations passed!")

"""
Time and Space Complexity Analysis:

Slice-based Solution (Primary):
1. Time Complexity: O(n) where n is the length of the array
   - We iterate through the array once with step size
   - Each slice operation is O(k) where k is the chunk size
   - Total: O(n) as we process each element once

2. Space Complexity: O(n) for storing the result
   - Additional space for creating new sublists

Iterative Solution:
1. Time Complexity: O(n)
   - Single pass through the array
   - Constant time operations for each element

2. Space Complexity: O(n) for the result

Generator Solution:
1. Time Complexity: O(n) when fully consumed
   - Lazy evaluation, generates chunks on demand

2. Space Complexity: O(k) where k is chunk size
   - Only stores one chunk at a time (memory efficient)

Recursive Solution:
1. Time Complexity: O(n)
   - Each recursive call processes a chunk
   - Total calls: O(n/k) where k is chunk size

2. Space Complexity: O(n + n/k)
   - O(n) for result, O(n/k) for recursion stack

Key Insights:
- Slice-based approach is most readable and efficient
- Generator approach is memory-efficient for large arrays
- All approaches handle edge cases (empty array, size > length)
- List comprehension provides concise syntax

Topic: Arrays, Iteration, Slicing, Functional Programming
"""
