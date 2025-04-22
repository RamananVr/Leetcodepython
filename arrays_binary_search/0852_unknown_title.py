"""
LeetCode Problem #852: Peak Index in a Mountain Array

Problem Statement:
An array `arr` is a mountain if the following properties hold:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `arr`, return the index `i` such that `arr[i]` is the peak of the mountain. 
The peak is guaranteed to exist.

Constraints:
- `3 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a mountain array.

Example:
Input: arr = [0, 2, 1, 0]
Output: 1

Input: arr = [0, 10, 5, 2]
Output: 1

Follow-up:
Can you solve it using O(log n) time complexity?
"""

def peakIndexInMountainArray(arr):
    """
    Finds the peak index in a mountain array using binary search.

    :param arr: List[int] - The mountain array
    :return: int - The index of the peak element
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            # Peak is to the right
            left = mid + 1
        else:
            # Peak is to the left or at mid
            right = mid

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [0, 2, 1, 0]
    print(peakIndexInMountainArray(arr1))  # Output: 1

    # Test Case 2
    arr2 = [0, 10, 5, 2]
    print(peakIndexInMountainArray(arr2))  # Output: 1

    # Test Case 3
    arr3 = [3, 4, 5, 1]
    print(peakIndexInMountainArray(arr3))  # Output: 2

    # Test Case 4
    arr4 = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    print(peakIndexInMountainArray(arr4))  # Output: 2

    # Test Case 5
    arr5 = [0, 1, 0]
    print(peakIndexInMountainArray(arr5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm uses binary search, which divides the search space in half at each step.
- Therefore, the time complexity is O(log n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (only a few variables for indices).
- Therefore, the space complexity is O(1).

Topic: Arrays, Binary Search
"""