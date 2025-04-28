"""
LeetCode Problem #1064: Fixed Point

Problem Statement:
Given an array of distinct integers `arr`, where `arr` is sorted in ascending order, 
return the smallest index `i` that satisfies `arr[i] == i`. If no such `i` exists, return `-1`.

Example 1:
Input: arr = [-10, -5, 0, 3, 7]
Output: 3
Explanation: For the given array, arr[3] == 3, so the answer is 3.

Example 2:
Input: arr = [0, 2, 5, 8, 17]
Output: 0
Explanation: For the given array, arr[0] == 0, so the answer is 0.

Example 3:
Input: arr = [-10, -5, 3, 4, 7, 9]
Output: -1
Explanation: There is no index `i` such that arr[i] == i, so the answer is -1.

Constraints:
- 1 <= arr.length <= 10^4
- -10^4 <= arr[i] <= 10^4
- arr contains distinct integers sorted in ascending order.
"""

def fixedPoint(arr):
    """
    Finds the smallest index i such that arr[i] == i in a sorted array of distinct integers.

    :param arr: List[int] - A sorted list of distinct integers.
    :return: int - The smallest index i such that arr[i] == i, or -1 if no such index exists.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            # Check if it's the smallest index satisfying the condition
            if mid == 0 or arr[mid - 1] != mid - 1:
                return mid
            right = mid - 1
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [-10, -5, 0, 3, 7]
    print(fixedPoint(arr1))  # Output: 3

    # Test Case 2
    arr2 = [0, 2, 5, 8, 17]
    print(fixedPoint(arr2))  # Output: 0

    # Test Case 3
    arr3 = [-10, -5, 3, 4, 7, 9]
    print(fixedPoint(arr3))  # Output: -1

    # Test Case 4
    arr4 = [-10, -5, -2, 3, 4, 5]
    print(fixedPoint(arr4))  # Output: 3

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print(fixedPoint(arr5))  # Output: -1

"""
Time Complexity:
- The algorithm uses binary search, which has a time complexity of O(log n), where n is the length of the array.

Space Complexity:
- The algorithm uses O(1) additional space since it operates in-place without requiring extra data structures.

Topic: Binary Search
"""