"""
LeetCode Problem #2634: Filter Elements from Array

Problem Statement:
Given an integer array `arr` and a filtering function `fn`, return a new array with a subset of the elements from the original array such that `fn(arr[i], i)` evaluates to `True`.

The function `fn` takes two arguments:
1. `arr[i]` - the value of the element at index `i`.
2. `i` - the index of the element.

You must write a function `filterArray(arr, fn)` that implements this functionality.

Example:
Input: arr = [1, 2, 3], fn = lambda x, i: x % 2 == 1
Output: [1, 3]

Constraints:
- `arr` is a valid array of integers.
- `fn` is a valid function.
- The length of `arr` is in the range [0, 1000].
"""

# Solution
def filterArray(arr, fn):
    """
    Filters elements from the array based on the filtering function.

    Args:
    arr (List[int]): The input array of integers.
    fn (Callable[[int, int], bool]): The filtering function.

    Returns:
    List[int]: A new array containing elements that satisfy the filtering function.
    """
    return [arr[i] for i in range(len(arr)) if fn(arr[i], i)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Filter odd numbers
    arr1 = [1, 2, 3]
    fn1 = lambda x, i: x % 2 == 1
    print(filterArray(arr1, fn1))  # Output: [1, 3]

    # Test Case 2: Filter elements at even indices
    arr2 = [10, 20, 30, 40, 50]
    fn2 = lambda x, i: i % 2 == 0
    print(filterArray(arr2, fn2))  # Output: [10, 30, 50]

    # Test Case 3: Filter elements greater than 15
    arr3 = [5, 15, 25, 35]
    fn3 = lambda x, i: x > 15
    print(filterArray(arr3, fn3))  # Output: [25, 35]

    # Test Case 4: Empty array
    arr4 = []
    fn4 = lambda x, i: x > 0
    print(filterArray(arr4, fn4))  # Output: []

    # Test Case 5: Filter elements divisible by their index
    arr5 = [0, 2, 4, 6, 8]
    fn5 = lambda x, i: i != 0 and x % i == 0
    print(filterArray(arr5, fn5))  # Output: [2, 4, 6]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, applying the filtering function to each element.
- Let `n` be the length of the array. The time complexity is O(n).

Space Complexity:
- The function creates a new list to store the filtered elements. In the worst case, the new list could contain all elements of the original array.
- The space complexity is O(n).
"""

# Topic: Arrays