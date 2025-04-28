"""
LeetCode Problem #2724: Sort By

Problem Statement:
You are given an array of objects `arr` and a function `fn`. Your task is to sort the array in ascending order based on the result of applying the function `fn` to each element. Return the sorted array.

Example 1:
Input: arr = [5, 4, 1, 2, 3], fn = lambda x: x
Output: [1, 2, 3, 4, 5]

Example 2:
Input: arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = lambda d: d["x"]
Output: [{"x": -1}, {"x": 0}, {"x": 1}]

Example 3:
Input: arr = [[3, 4], [5, 2], [10, 1]], fn = lambda x: x[1]
Output: [[10, 1], [5, 2], [3, 4]]

Constraints:
- `arr` is a list of objects.
- `fn` is a function that takes one argument and returns a value that can be compared.
- The function `fn` will not modify the input array.
- The input array may contain duplicate elements.
"""

# Solution
from typing import List, Callable, Any

def sortBy(arr: List[Any], fn: Callable[[Any], Any]) -> List[Any]:
    """
    Sorts the array `arr` in ascending order based on the result of applying the function `fn` to each element.

    :param arr: List of objects to be sorted.
    :param fn: Function that takes an element of `arr` and returns a value to sort by.
    :return: Sorted list.
    """
    return sorted(arr, key=fn)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [5, 4, 1, 2, 3]
    fn1 = lambda x: x
    print(sortBy(arr1, fn1))  # Output: [1, 2, 3, 4, 5]

    # Test Case 2
    arr2 = [{"x": 1}, {"x": 0}, {"x": -1}]
    fn2 = lambda d: d["x"]
    print(sortBy(arr2, fn2))  # Output: [{"x": -1}, {"x": 0}, {"x": 1}]

    # Test Case 3
    arr3 = [[3, 4], [5, 2], [10, 1]]
    fn3 = lambda x: x[1]
    print(sortBy(arr3, fn3))  # Output: [[10, 1], [5, 2], [3, 4]]

    # Test Case 4 (Edge Case: Empty Array)
    arr4 = []
    fn4 = lambda x: x
    print(sortBy(arr4, fn4))  # Output: []

    # Test Case 5 (Edge Case: Single Element)
    arr5 = [42]
    fn5 = lambda x: x
    print(sortBy(arr5, fn5))  # Output: [42]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting an array of size `n` takes O(n log n) time.
- Applying the function `fn` to each element during sorting is O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `sorted` function creates a new list, so the space complexity is O(n) for the new list.
- If the input array is large, additional space may be used for the sorting algorithm (e.g., Timsort).

Overall space complexity: O(n).
"""

# Topic: Sorting