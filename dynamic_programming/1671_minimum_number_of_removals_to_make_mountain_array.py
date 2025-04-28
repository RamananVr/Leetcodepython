"""
LeetCode Question #1671: Minimum Number of Removals to Make Mountain Array

Problem Statement:
You may recall that an array `arr` is a mountain array if and only if:
- `arr.length >= 3`
- There exists some index `i` (0-indexed) with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `arr`, return the minimum number of elements that need to be removed to make `arr` a mountain array.

Example 1:
Input: arr = [1,3,1]
Output: 0
Explanation: The array is already a mountain array.

Example 2:
Input: arr = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: Remove the elements [2, 3, 1] to make the array [1, 5, 6, 2, 1] a mountain array.

Constraints:
- 3 <= arr.length <= 1000
- 1 <= arr[i] <= 10^9
"""

# Solution
def minimumMountainRemovals(arr):
    """
    Function to calculate the minimum number of removals to make the array a mountain array.
    :param arr: List[int] - Input array
    :return: int - Minimum number of removals
    """
    n = len(arr)
    
    # Step 1: Compute LIS (Longest Increasing Subsequence) from left to right
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Step 2: Compute LIS from right to left (Longest Decreasing Subsequence)
    lds = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    # Step 3: Find the maximum mountain length
    max_mountain_length = 0
    for i in range(1, n - 1):  # A valid peak must be between the first and last elements
        if lis[i] > 1 and lds[i] > 1:  # Both sides must have a valid subsequence
            max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)
    
    # Step 4: Calculate the minimum removals
    return n - max_mountain_length


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 3, 1]
    print(minimumMountainRemovals(arr1))  # Output: 0

    # Test Case 2
    arr2 = [2, 1, 1, 5, 6, 2, 3, 1]
    print(minimumMountainRemovals(arr2))  # Output: 3

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minimumMountainRemovals(arr3))  # Output: 8

    # Test Case 4
    arr4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(minimumMountainRemovals(arr4))  # Output: 8


"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing LIS takes O(n^2) due to the nested loops.
- Computing LDS also takes O(n^2).
- Combining LIS and LDS to find the maximum mountain length takes O(n).
- Overall time complexity: O(n^2).

Space Complexity:
- LIS and LDS arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Dynamic Programming
"""