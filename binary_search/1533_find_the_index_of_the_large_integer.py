"""
LeetCode Question #1533: Find the Index of the Large Integer

Problem Statement:
You are given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `threshold`.

You need to find the index of the first integer in `arr` that is greater than or equal to `threshold`. If no such integer exists, return -1.

The array is guaranteed to be strictly increasing, meaning that `arr[i] < arr[i+1]` for all valid `i`.

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i], threshold <= 10^9

Example:
Input: arr = [1, 3, 5, 7, 9], threshold = 6
Output: 3
Explanation: The first integer greater than or equal to 6 is 7, which is at index 3.

Input: arr = [1, 3, 5, 7, 9], threshold = 10
Output: -1
Explanation: No integer in the array is greater than or equal to 10.

Input: arr = [1, 3, 5, 7, 9], threshold = 1
Output: 0
Explanation: The first integer greater than or equal to 1 is 1, which is at index 0.
"""

# Clean, Correct Python Solution
def findIndex(arr, threshold):
    """
    Finds the index of the first integer in arr that is greater than or equal to threshold.
    If no such integer exists, returns -1.

    :param arr: List[int] - A strictly increasing array of positive integers.
    :param threshold: int - The threshold value.
    :return: int - The index of the first integer >= threshold, or -1 if no such integer exists.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= threshold:
            right = mid - 1
        else:
            left = mid + 1

    # Check if left is within bounds and satisfies the condition
    if left < len(arr) and arr[left] >= threshold:
        return left
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 3, 5, 7, 9]
    threshold1 = 6
    print(findIndex(arr1, threshold1))  # Output: 3

    # Test Case 2
    arr2 = [1, 3, 5, 7, 9]
    threshold2 = 10
    print(findIndex(arr2, threshold2))  # Output: -1

    # Test Case 3
    arr3 = [1, 3, 5, 7, 9]
    threshold3 = 1
    print(findIndex(arr3, threshold3))  # Output: 0

    # Test Case 4
    arr4 = [2, 4, 6, 8, 10]
    threshold4 = 5
    print(findIndex(arr4, threshold4))  # Output: 2

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    threshold5 = 0
    print(findIndex(arr5, threshold5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses binary search, which operates in O(log n) time, where n is the length of the array.

Space Complexity:
The solution uses constant space, O(1), as no additional data structures are used.
"""

# Topic: Binary Search