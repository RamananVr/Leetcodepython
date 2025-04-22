"""
LeetCode Problem #978: Longest Turbulent Subarray

Problem Statement:
Given an integer array `arr`, return the length of a maximum size turbulent subarray of `arr`.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i+1], ..., arr[j]]` of `arr` is turbulent if and only if:
- For `i <= k < j`:
  - `arr[k] > arr[k+1]` when `k` is odd, and `arr[k] < arr[k+1]` when `k` is even.
  OR
  - `arr[k] < arr[k+1]` when `k` is odd, and `arr[k] > arr[k+1]` when `k` is even.

Return the length of the longest turbulent subarray.

Constraints:
- `1 <= arr.length <= 4 * 10^4`
- `0 <= arr[i] <= 10^9`
"""

def maxTurbulenceSize(arr):
    """
    Finds the length of the longest turbulent subarray in the given array.

    :param arr: List[int] - The input array
    :return: int - The length of the longest turbulent subarray
    """
    n = len(arr)
    if n == 1:
        return 1

    # Initialize variables
    max_length = 1
    inc = 1  # Length of subarray ending with an increasing comparison
    dec = 1  # Length of subarray ending with a decreasing comparison

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc = dec + 1
            dec = 1
        elif arr[i] < arr[i - 1]:
            dec = inc + 1
            inc = 1
        else:
            inc = 1
            dec = 1

        max_length = max(max_length, inc, dec)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    print(maxTurbulenceSize(arr1))  # Expected Output: 5

    # Test Case 2
    arr2 = [4, 8, 12, 16]
    print(maxTurbulenceSize(arr2))  # Expected Output: 2

    # Test Case 3
    arr3 = [100]
    print(maxTurbulenceSize(arr3))  # Expected Output: 1

    # Test Case 4
    arr4 = [9, 9, 9, 9, 9]
    print(maxTurbulenceSize(arr4))  # Expected Output: 1

    # Test Case 5
    arr5 = [1, 2, 1, 2, 1, 2, 1]
    print(maxTurbulenceSize(arr5))  # Expected Output: 7

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables (`inc`, `dec`, `max_length`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""