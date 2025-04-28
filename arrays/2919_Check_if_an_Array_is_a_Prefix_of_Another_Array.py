"""
LeetCode Problem #2919: Check if an Array is a Prefix of Another Array

Problem Statement:
You are given two integer arrays `arr1` and `arr2`. Write a function to determine if `arr1` is a prefix of `arr2`.

An array `arr1` is considered a prefix of `arr2` if:
- The length of `arr1` is less than or equal to the length of `arr2`, and
- All elements of `arr1` match the corresponding elements in `arr2`.

Return `True` if `arr1` is a prefix of `arr2`, otherwise return `False`.

Example 1:
Input: arr1 = [1, 2], arr2 = [1, 2, 3]
Output: True

Example 2:
Input: arr1 = [1, 3], arr2 = [1, 2, 3]
Output: False

Example 3:
Input: arr1 = [1, 2, 3], arr2 = [1, 2]
Output: False

Constraints:
- 1 <= len(arr1), len(arr2) <= 1000
- 0 <= arr1[i], arr2[i] <= 10^6
"""

def isPrefix(arr1, arr2):
    """
    Determines if arr1 is a prefix of arr2.

    :param arr1: List[int] - The first array
    :param arr2: List[int] - The second array
    :return: bool - True if arr1 is a prefix of arr2, False otherwise
    """
    # Check if arr1 matches the first len(arr1) elements of arr2
    return arr1 == arr2[:len(arr1)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2]
    arr2 = [1, 2, 3]
    print(isPrefix(arr1, arr2))  # Output: True

    # Test Case 2
    arr1 = [1, 3]
    arr2 = [1, 2, 3]
    print(isPrefix(arr1, arr2))  # Output: False

    # Test Case 3
    arr1 = [1, 2, 3]
    arr2 = [1, 2]
    print(isPrefix(arr1, arr2))  # Output: False

    # Test Case 4
    arr1 = []
    arr2 = [1, 2, 3]
    print(isPrefix(arr1, arr2))  # Output: True

    # Test Case 5
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    print(isPrefix(arr1, arr2))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The slicing operation `arr2[:len(arr1)]` takes O(len(arr1)) time.
- The comparison `arr1 == arr2[:len(arr1)]` also takes O(len(arr1)) time.
- Therefore, the overall time complexity is O(len(arr1)).

Space Complexity:
- The slicing operation creates a new array of size len(arr1), which takes O(len(arr1)) space.
- No additional space is used apart from the input arrays and the slice.
- Therefore, the space complexity is O(len(arr1)).

Topic: Arrays
"""