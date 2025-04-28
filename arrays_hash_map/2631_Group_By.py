"""
LeetCode Problem #2631: Group By

Problem Statement:
Given an array `arr` and a function `fn`, write a function `groupBy` that groups the elements of `arr` based on the return value of `fn`. The function should return an object where each key is the output of `fn` and the corresponding value is an array of elements that returned that key.

Example 1:
Input: 
    arr = [6.1, 4.2, 6.3], 
    fn = Math.floor
Output: 
    {6: [6.1, 6.3], 4: [4.2]}

Example 2:
Input: 
    arr = ['one', 'two', 'three'], 
    fn = x => x.length
Output: 
    {3: ['one', 'two'], 5: ['three']}

Constraints:
- `arr` is an array of elements.
- `fn` is a function that takes one argument and returns a value.
"""

from collections import defaultdict
from typing import List, Callable, Dict, Any

def groupBy(arr: List[Any], fn: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    """
    Groups elements of the array `arr` based on the return value of the function `fn`.

    Args:
    - arr: List of elements to be grouped.
    - fn: A function that takes an element and returns a key.

    Returns:
    - A dictionary where keys are the return values of `fn` and values are lists of elements.
    """
    grouped = defaultdict(list)
    for item in arr:
        key = fn(item)
        grouped[key].append(item)
    return dict(grouped)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [6.1, 4.2, 6.3]
    fn1 = lambda x: int(x)  # Equivalent to Math.floor in Python
    print(groupBy(arr1, fn1))  # Expected Output: {6: [6.1, 6.3], 4: [4.2]}

    # Test Case 2
    arr2 = ['one', 'two', 'three']
    fn2 = lambda x: len(x)
    print(groupBy(arr2, fn2))  # Expected Output: {3: ['one', 'two'], 5: ['three']}

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5, 6]
    fn3 = lambda x: x % 2  # Group by even (0) and odd (1)
    print(groupBy(arr3, fn3))  # Expected Output: {1: [1, 3, 5], 0: [2, 4, 6]}

    # Test Case 4
    arr4 = ['apple', 'banana', 'cherry', 'date']
    fn4 = lambda x: x[0]  # Group by the first letter
    print(groupBy(arr4, fn4))  # Expected Output: {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date']}

"""
Time Complexity:
- Let `n` be the length of the input array `arr`.
- The function iterates through each element of `arr` once, and for each element, it computes the key using `fn` (assumed to be O(1)).
- Insertion into the dictionary is O(1) on average.
- Overall time complexity: O(n).

Space Complexity:
- The space complexity is O(n) for storing the grouped elements in the dictionary.

Topic: Arrays, Hash Map
"""