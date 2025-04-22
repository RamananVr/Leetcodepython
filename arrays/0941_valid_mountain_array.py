"""
LeetCode Question #941: Valid Mountain Array

Problem Statement:
Given an array of integers `arr`, return `true` if and only if it is a valid mountain array.

Recall that `arr` is a mountain array if and only if:
- `arr.length >= 3`
- There exists some index `i` (0 < i < arr.length - 1) such that:
  - `arr[0] < arr[1] < ... < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Example 1:
Input: arr = [2, 1]
Output: false

Example 2:
Input: arr = [3, 5, 5]
Output: false

Example 3:
Input: arr = [0, 3, 2, 1]
Output: true

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4
"""

def validMountainArray(arr):
    """
    Determines if the given array is a valid mountain array.

    :param arr: List[int] - The input array
    :return: bool - True if the array is a valid mountain array, False otherwise
    """
    n = len(arr)
    if n < 3:
        return False

    # Find the peak index
    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Peak cannot be the first or last element
    if i == 0 or i == n - 1:
        return False

    # Check if the elements after the peak are strictly decreasing
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    # If we reached the end, it's a valid mountain array
    return i == n - 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Not a mountain array (too short)
    print(validMountainArray([2, 1]))  # Output: False

    # Test Case 2: Not a mountain array (plateau at the peak)
    print(validMountainArray([3, 5, 5]))  # Output: False

    # Test Case 3: Valid mountain array
    print(validMountainArray([0, 3, 2, 1]))  # Output: True

    # Test Case 4: Not a mountain array (no peak)
    print(validMountainArray([1, 2, 3, 4, 5]))  # Output: False

    # Test Case 5: Not a mountain array (no descent)
    print(validMountainArray([5, 4, 3, 2, 1]))  # Output: False

    # Test Case 6: Valid mountain array
    print(validMountainArray([1, 3, 2]))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array twice: once to find the peak and once to check the descent.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few variables).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""