"""
LeetCode Problem #1287: Element Appearing More Than 25% In Sorted Array

Problem Statement:
Given an integer array `arr` sorted in non-decreasing order, there is exactly one integer in the array that appears more than 25% of the time, i.e., its frequency is greater than `len(arr) // 4`.

Return that integer.

Constraints:
1. 1 <= arr.length <= 10^4
2. 0 <= arr[i] <= 10^5
3. arr is sorted in non-decreasing order.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
"""

def findSpecialInteger(arr):
    """
    Finds the element that appears more than 25% of the time in a sorted array.

    :param arr: List[int] - A sorted list of integers
    :return: int - The integer that appears more than 25% of the time
    """
    n = len(arr)
    threshold = n // 4

    for i in range(n - threshold):
        # If the element at index i is the same as the element at index i + threshold,
        # it means this element appears more than 25% of the time.
        if arr[i] == arr[i + threshold]:
            return arr[i]

    # The problem guarantees that there is always an answer, so we should never reach here.
    return -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(findSpecialInteger(arr1))  # Output: 6

    # Test Case 2
    arr2 = [1, 1]
    print(findSpecialInteger(arr2))  # Output: 1

    # Test Case 3
    arr3 = [1, 1, 2, 2, 3, 3, 3, 3]
    print(findSpecialInteger(arr3))  # Output: 3

    # Test Case 4
    arr4 = [4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6]
    print(findSpecialInteger(arr4))  # Output: 4

    # Test Case 5
    arr5 = [10, 10, 10, 20, 20, 20, 20, 20, 30, 30]
    print(findSpecialInteger(arr5))  # Output: 20


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The loop iterates through the array up to `n - threshold` times, where `threshold = n // 4`.
   - This results in a time complexity of O(n), where n is the length of the array.

2. Space Complexity:
   - The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""