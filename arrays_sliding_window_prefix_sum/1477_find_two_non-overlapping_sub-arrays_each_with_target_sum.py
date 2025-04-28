"""
LeetCode Question #1477: Find Two Non-overlapping Sub-arrays Each With Target Sum

Problem Statement:
Given an array of integers `arr` and an integer `target`, your goal is to find two non-overlapping sub-arrays such that the sum of each sub-array is equal to `target`, and the total length of the two sub-arrays is minimized.

Return the minimum total length of the two required sub-arrays, or -1 if it is not possible to find such two sub-arrays.

A sub-array is a contiguous part of the array.

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: The first sub-array is [3] with length 1, and the second sub-array is [3] with length 1.

Example 2:
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: The first sub-array is [7] with length 1, and the second sub-array is [7] with length 1.

Example 3:
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: There is no way to find two non-overlapping sub-arrays with a sum equal to target.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 1000
- 1 <= target <= 10^7
"""

# Python Solution
def minSumOfLengths(arr, target):
    n = len(arr)
    left = [float('inf')] * n
    min_len = float('inf')
    
    # Calculate the minimum subarray length ending at each index
    curr_sum = 0
    start = 0
    for end in range(n):
        curr_sum += arr[end]
        while curr_sum > target:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            left[end] = end - start + 1
        if end > 0:
            left[end] = min(left[end], left[end - 1])
    
    # Calculate the minimum subarray length starting at each index
    curr_sum = 0
    start = n - 1
    for end in range(n - 1, -1, -1):
        curr_sum += arr[end]
        while curr_sum > target:
            curr_sum -= arr[start]
            start -= 1
        if curr_sum == target:
            if end > 0:
                min_len = min(min_len, (start - end + 1) + left[end - 1])
    
    return min_len if min_len != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 2, 2, 4, 3]
    target1 = 3
    print(minSumOfLengths(arr1, target1))  # Output: 2

    # Test Case 2
    arr2 = [7, 3, 4, 7]
    target2 = 7
    print(minSumOfLengths(arr2, target2))  # Output: 2

    # Test Case 3
    arr3 = [4, 3, 2, 6, 2, 3, 4]
    target3 = 6
    print(minSumOfLengths(arr3, target3))  # Output: -1

    # Test Case 4
    arr4 = [5, 5, 4, 4, 5]
    target4 = 9
    print(minSumOfLengths(arr4, target4))  # Output: 4

    # Test Case 5
    arr5 = [1, 1, 1, 2, 2, 2, 4, 4]
    target5 = 6
    print(minSumOfLengths(arr5, target5))  # Output: 6

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - The algorithm involves two passes over the array: one to calculate the `left` array and another to find the minimum length using the `left` array.
# - Each pass involves a sliding window, which operates in O(n) time.
# - Thus, the overall time complexity is O(n).

# Space Complexity: O(n)
# - The algorithm uses an auxiliary array `left` of size n to store the minimum subarray lengths.
# - Therefore, the space complexity is O(n).

# Topic: Arrays, Sliding Window, Prefix Sum