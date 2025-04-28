"""
LeetCode Problem #845: Longest Mountain in Array

Problem Statement:
You may recall that an array `arr` is a mountain array if and only if:

- `arr.length >= 3`
- There exists some index `i` (0-indexed) with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `arr`, return the length of the longest mountain. 
If there is no mountain, return `0`.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The longest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4

Follow up:
Can you solve it using only one pass?
Can you solve it in O(1) space?
"""

def longestMountain(arr):
    """
    Function to find the length of the longest mountain in the array.

    :param arr: List[int] - The input array
    :return: int - The length of the longest mountain
    """
    n = len(arr)
    if n < 3:
        return 0

    longest = 0
    i = 1  # Start from the second element

    while i < n - 1:
        # Check if arr[i] is a peak
        if arr[i - 1] < arr[i] > arr[i + 1]:
            # Expand left
            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            # Expand right
            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            # Calculate the length of the mountain
            current_length = right - left + 1
            longest = max(longest, current_length)

            # Move `i` to the end of the current mountain
            i = right
        else:
            i += 1

    return longest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 1, 4, 7, 3, 2, 5]
    print(longestMountain(arr1))  # Output: 5

    # Test Case 2
    arr2 = [2, 2, 2]
    print(longestMountain(arr2))  # Output: 0

    # Test Case 3
    arr3 = [0, 1, 0]
    print(longestMountain(arr3))  # Output: 3

    # Test Case 4
    arr4 = [2, 1, 4, 7, 3, 2, 1, 0, 1, 2, 3]
    print(longestMountain(arr4))  # Output: 8

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print(longestMountain(arr5))  # Output: 0

"""
Time Complexity Analysis:
- The algorithm uses a single pass through the array with a while loop.
- For each peak, it expands left and right to find the boundaries of the mountain.
- Each element is processed at most twice (once during the peak check and once during the expansion).
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables like `left`, `right`, `longest`, etc.).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""