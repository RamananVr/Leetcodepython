"""
LeetCode Problem #2625: Flatten Deeply Nested Array

Problem Statement:
Given a multi-dimensional array `arr` and a depth level `n`, implement a function `flat(arr, n)` that flattens the array up to the specified depth `n`.

The function should recursively flatten the array up to `n` levels deep. If `n` is 0, the array should remain unchanged. If `n` is greater than the depth of the array, the array should be completely flattened.

Example:
Input: arr = [1, [2, [3, [4]], 5]], n = 2
Output: [1, 2, 3, [4], 5]

Constraints:
- The input array `arr` can contain integers, other arrays, or a mix of both.
- The depth level `n` is a non-negative integer.
"""

# Solution
def flat(arr, n):
    """
    Flattens a multi-dimensional array up to a specified depth level n.

    :param arr: List[int | List], the input array to flatten
    :param n: int, the depth level to flatten the array
    :return: List[int | List], the flattened array
    """
    if n == 0:
        return arr
    result = []
    for element in arr:
        if isinstance(element, list):
            result.extend(flat(element, n - 1))
        else:
            result.append(element)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, [2, [3, [4]], 5]]
    n1 = 2
    print(flat(arr1, n1))  # Output: [1, 2, 3, [4], 5]

    # Test Case 2
    arr2 = [1, [2, [3, [4, [5]]]]]
    n2 = 1
    print(flat(arr2, n2))  # Output: [1, 2, [3, [4, [5]]]]

    # Test Case 3
    arr3 = [1, [2, [3, [4, [5]]]]]
    n3 = 0
    print(flat(arr3, n3))  # Output: [1, [2, [3, [4, [5]]]]]

    # Test Case 4
    arr4 = [1, [2, [3, [4, [5]]]]]
    n4 = 10
    print(flat(arr4, n4))  # Output: [1, 2, 3, 4, 5]

    # Test Case 5
    arr5 = []
    n5 = 3
    print(flat(arr5, n5))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `m` be the total number of elements in the array (including nested elements).
- In the worst case, we traverse all elements in the array up to `n` levels deep.
- Therefore, the time complexity is O(m).

Space Complexity:
- The space complexity is determined by the recursion stack.
- In the worst case, the recursion depth is equal to `n`, so the space complexity is O(n).
"""

# Topic: Arrays, Recursion