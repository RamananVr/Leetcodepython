"""
LeetCode Question #2724: Sort By

Problem Statement:
Given an array `arr` and a function `fn`, return a sorted array `sortedArr`. You can assume `fn` only returns numbers and those numbers determine the sort order of `sortedArr`. `sortedArray` should be sorted in ascending order by `fn` output.

You may assume that `fn` will never return duplicate values for any array passed to it.

Constraints:
- `arr` is a valid JSON array
- `fn` is a function that returns a number
- `1 <= arr.length <= 5 * 10^5`

Example:
Input: arr = [5, 4, 1, 2, 3], fn = (x) => x
Output: [1, 2, 3, 4, 5]
Explanation: fn simply returns the value passed to it so the array is sorted in ascending order.

Input: arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = (d) => d.x
Output: [{"x": -1}, {"x": 0}, {"x": 1}]
Explanation: fn returns the value of the "x" key. So the array is sorted based on that value.

Input: arr = [[3, 4], [5, 2], [10, 1]], fn = (x) => x[1]
Output: [[10, 1], [5, 2], [3, 4]]
Explanation: arr is sorted in ascending order by number at index=1.
"""

def sortBy(arr, fn):
    """
    Sort array by the result of applying function fn to each element.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output
    """
    return sorted(arr, key=fn)

def sortBy_custom_implementation(arr, fn):
    """
    Custom implementation using manual sorting with key function.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output
    """
    # Create list of (fn_result, original_element) pairs
    pairs = [(fn(element), element) for element in arr]
    
    # Sort by fn_result
    pairs.sort(key=lambda x: x[0])
    
    # Extract original elements
    return [element for _, element in pairs]

def sortBy_merge_sort(arr, fn):
    """
    Implementation using merge sort algorithm.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output
    """
    def merge_sort(arr_copy):
        if len(arr_copy) <= 1:
            return arr_copy
        
        mid = len(arr_copy) // 2
        left = merge_sort(arr_copy[:mid])
        right = merge_sort(arr_copy[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if fn(left[i]) <= fn(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    return merge_sort(arr.copy())

def sortBy_quick_sort(arr, fn):
    """
    Implementation using quick sort algorithm.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output
    """
    def quick_sort(arr_copy):
        if len(arr_copy) <= 1:
            return arr_copy
        
        pivot = arr_copy[len(arr_copy) // 2]
        pivot_value = fn(pivot)
        
        left = [x for x in arr_copy if fn(x) < pivot_value]
        middle = [x for x in arr_copy if fn(x) == pivot_value]
        right = [x for x in arr_copy if fn(x) > pivot_value]
        
        return quick_sort(left) + middle + quick_sort(right)
    
    return quick_sort(arr.copy())

def sortBy_heap_sort(arr, fn):
    """
    Implementation using heap sort algorithm.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output
    """
    import heapq
    
    # Create heap with (fn_value, element) pairs
    heap = [(fn(element), element) for element in arr]
    heapq.heapify(heap)
    
    # Extract elements in sorted order
    result = []
    while heap:
        fn_value, element = heapq.heappop(heap)
        result.append(element)
    
    return result

def sortBy_stable(arr, fn):
    """
    Stable sort implementation preserving original order for equal elements.
    
    Args:
        arr: List of elements to sort
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        New sorted list based on fn output (stable)
    """
    # Add original index to maintain stability
    indexed_arr = [(fn(element), i, element) for i, element in enumerate(arr)]
    
    # Sort by fn_value first, then by original index for stability
    indexed_arr.sort(key=lambda x: (x[0], x[1]))
    
    return [element for _, _, element in indexed_arr]

def sortBy_in_place(arr, fn):
    """
    In-place sorting (modifies original array).
    
    Args:
        arr: List of elements to sort (modified in place)
        fn: Function that takes an element and returns a number for sorting
    
    Returns:
        Reference to the modified original array
    """
    arr.sort(key=fn)
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 - Simple numeric array
    arr = [5, 4, 1, 2, 3]
    fn = lambda x: x
    result = sortBy(arr, fn)
    expected = [1, 2, 3, 4, 5]
    print(f"Test 1 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 2 - Dictionary array sorted by key
    arr = [{"x": 1}, {"x": 0}, {"x": -1}]
    fn = lambda d: d["x"]
    result = sortBy(arr, fn)
    expected = [{"x": -1}, {"x": 0}, {"x": 1}]
    print(f"Test 2 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 3 - Array of arrays sorted by index
    arr = [[3, 4], [5, 2], [10, 1]]
    fn = lambda x: x[1]
    result = sortBy(arr, fn)
    expected = [[10, 1], [5, 2], [3, 4]]
    print(f"Test 3 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 4 - String array sorted by length
    arr = ["apple", "pie", "washington", "cat"]
    fn = lambda s: len(s)
    result = sortBy(arr, fn)
    expected = ["pie", "cat", "apple", "washington"]
    print(f"Test 4 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 5 - Negative numbers
    arr = [{"val": -5}, {"val": 10}, {"val": -3}, {"val": 0}]
    fn = lambda obj: obj["val"]
    result = sortBy(arr, fn)
    expected = [{"val": -5}, {"val": -3}, {"val": 0}, {"val": 10}]
    print(f"Test 5 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 6 - Complex sorting function
    arr = [1, 2, 3, 4, 5]
    fn = lambda x: -x  # Sort in descending order
    result = sortBy(arr, fn)
    expected = [5, 4, 3, 2, 1]
    print(f"Test 6 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 7 - Single element
    arr = [42]
    fn = lambda x: x
    result = sortBy(arr, fn)
    expected = [42]
    print(f"Test 7 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test all implementations produce same results
    test_arr = [{"id": 3, "val": 30}, {"id": 1, "val": 10}, {"id": 2, "val": 20}]
    test_fn = lambda obj: obj["val"]
    
    results = [
        sortBy(test_arr, test_fn),
        sortBy_custom_implementation(test_arr, test_fn),
        sortBy_merge_sort(test_arr, test_fn),
        sortBy_quick_sort(test_arr, test_fn),
        sortBy_heap_sort(test_arr, test_fn),
        sortBy_stable(test_arr, test_fn)
    ]
    
    expected_result = [{"id": 1, "val": 10}, {"id": 2, "val": 20}, {"id": 3, "val": 30}]
    
    for i, result in enumerate(results):
        assert result == expected_result, f"Implementation {i} differs"
    
    # Test original array is not modified
    original = [3, 1, 2]
    sorted_result = sortBy(original, lambda x: x)
    assert original == [3, 1, 2], "Original array was modified"
    assert sorted_result == [1, 2, 3], "Sorted result is incorrect"
    
    print("All test cases and implementations passed!")

"""
Time and Space Complexity Analysis:

Built-in sorted() Solution:
1. Time Complexity: O(n * log(n))
   - Python's sorted() uses Timsort algorithm
   - Each comparison calls fn(), which we assume is O(1)
   - Overall: O(n * log(n))

2. Space Complexity: O(n)
   - Creates new list for sorted result
   - Additional space for sorting algorithm

Custom Implementation:
1. Time Complexity: O(n * log(n))
   - Creating pairs: O(n)
   - Sorting pairs: O(n * log(n))
   - Extracting results: O(n)

2. Space Complexity: O(n)
   - Storage for pairs and result

Merge Sort Implementation:
1. Time Complexity: O(n * log(n))
   - Divide: O(log(n)) levels
   - Conquer: O(n) work per level
   - fn() called O(n * log(n)) times in merge operations

2. Space Complexity: O(n)
   - Recursion stack: O(log(n))
   - Temporary arrays: O(n)

Quick Sort Implementation:
1. Time Complexity: O(n * log(n)) average, O(n²) worst case
   - Average case with good pivot selection
   - Worst case when pivot is always min/max

2. Space Complexity: O(log(n)) average, O(n) worst case
   - Recursion stack depth

Heap Sort Implementation:
1. Time Complexity: O(n * log(n))
   - Building heap: O(n)
   - Extracting n elements: O(n * log(n))

2. Space Complexity: O(n)
   - Storage for heap with (fn_value, element) pairs

Key Insights:
- Python's sorted() is highly optimized (Timsort)
- Custom implementations useful for learning algorithms
- Function fn should be efficient as it's called many times
- Stable sorting preserves relative order of equal elements
- In-place sorting modifies original array

Topic: Sorting Algorithms, Higher-Order Functions, Algorithm Implementation
"""
