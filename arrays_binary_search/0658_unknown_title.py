"""
LeetCode Problem #658: Find K Closest Elements

Problem Statement:
Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. 
The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

You may assume that the array is sorted in ascending order.

Constraints:
- 1 <= k <= arr.length
- 1 <= arr.length <= 10^4
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4
"""

from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    """
    Finds the k closest elements to x in the sorted array arr.
    """
    # Binary search to find the closest element to x
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        # Compare distances to decide the direction
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    # Return the k closest elements
    return arr[left:left + k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    k1 = 4
    x1 = 3
    print(findClosestElements(arr1, k1, x1))  # Output: [1, 2, 3, 4]

    # Test Case 2
    arr2 = [1, 2, 3, 4, 5]
    k2 = 4
    x2 = -1
    print(findClosestElements(arr2, k2, x2))  # Output: [1, 2, 3, 4]

    # Test Case 3
    arr3 = [1, 3, 5, 7, 9]
    k3 = 3
    x3 = 6
    print(findClosestElements(arr3, k3, x3))  # Output: [3, 5, 7]

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    k4 = 2
    x4 = 6
    print(findClosestElements(arr4, k4, x4))  # Output: [4, 5]

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    k5 = 3
    x5 = 0
    print(findClosestElements(arr5, k5, x5))  # Output: [1, 2, 3]

"""
Time Complexity:
- The binary search runs in O(log(n - k)) time, where n is the length of the array.
- Slicing the array to return the k elements takes O(k) time.
- Overall time complexity: O(log(n - k) + k).

Space Complexity:
- The algorithm uses O(1) additional space since it operates in-place on the input array.
- The output list of size k is not considered extra space.

Topic: Arrays, Binary Search
"""