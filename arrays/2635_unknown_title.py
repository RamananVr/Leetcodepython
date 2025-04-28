"""
LeetCode Problem #2635: Apply Transform Over Each Element in Array

Problem Statement:
Given an integer array `arr` and a function `fn`, return a new array with a transformation applied to each element.

The transformation is defined as:
    newArray[i] = fn(arr[i])

You are guaranteed that the input function `fn` takes an integer as input and returns an integer.

Example 1:
Input: arr = [1, 2, 3], fn = lambda x: x + 1
Output: [2, 3, 4]

Example 2:
Input: arr = [1, 2, 3], fn = lambda x: x * 2
Output: [2, 4, 6]

Constraints:
- 1 <= arr.length <= 1000
- -10^6 <= arr[i] <= 10^6
"""

# Solution
def map_array(arr, fn):
    """
    Applies the given transformation function `fn` to each element in the array `arr`.

    Args:
    arr (List[int]): The input array of integers.
    fn (Callable[[int], int]): A function that takes an integer and returns an integer.

    Returns:
    List[int]: A new array with the transformation applied to each element.
    """
    return [fn(x) for x in arr]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Increment each element by 1
    arr1 = [1, 2, 3]
    fn1 = lambda x: x + 1
    print(map_array(arr1, fn1))  # Output: [2, 3, 4]

    # Test Case 2: Multiply each element by 2
    arr2 = [1, 2, 3]
    fn2 = lambda x: x * 2
    print(map_array(arr2, fn2))  # Output: [2, 4, 6]

    # Test Case 3: Square each element
    arr3 = [-2, -1, 0, 1, 2]
    fn3 = lambda x: x ** 2
    print(map_array(arr3, fn3))  # Output: [4, 1, 0, 1, 4]

    # Test Case 4: Negate each element
    arr4 = [5, -3, 0, 7]
    fn4 = lambda x: -x
    print(map_array(arr4, fn4))  # Output: [-5, 3, 0, -7]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each element of the array `arr` once.
- For an array of size `n`, the time complexity is O(n).

Space Complexity:
- The function creates a new array to store the transformed elements.
- The space complexity is O(n), where `n` is the size of the input array.
"""

# Topic: Arrays