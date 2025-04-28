"""
LeetCode Problem #1218: Longest Arithmetic Subsequence of Given Difference

Problem Statement:
Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence in `arr` which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals `difference`.

A subsequence is a sequence that can be derived from `arr` by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest subsequence is [1,2,3,4].

Example 2:
Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: There is no subsequence with a difference of 1.

Example 3:
Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest subsequence is [7,5,3,1].

Constraints:
- 1 <= arr.length <= 10^5
- -10^4 <= arr[i], difference <= 10^4
"""

# Solution
def longestSubsequence(arr, difference):
    """
    Finds the length of the longest arithmetic subsequence with a given difference.

    :param arr: List[int] - The input array of integers.
    :param difference: int - The target difference for the arithmetic subsequence.
    :return: int - The length of the longest arithmetic subsequence.
    """
    dp = {}
    max_length = 0

    for num in arr:
        # If num - difference exists in dp, extend the subsequence
        if num - difference in dp:
            dp[num] = dp[num - difference] + 1
        else:
            # Otherwise, start a new subsequence with length 1
            dp[num] = 1
        # Update the maximum length
        max_length = max(max_length, dp[num])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4]
    difference1 = 1
    print(longestSubsequence(arr1, difference1))  # Output: 4

    # Test Case 2
    arr2 = [1, 3, 5, 7]
    difference2 = 1
    print(longestSubsequence(arr2, difference2))  # Output: 1

    # Test Case 3
    arr3 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference3 = -2
    print(longestSubsequence(arr3, difference3))  # Output: 4

    # Test Case 4
    arr4 = [3, 0, -3, -6, -9, -12]
    difference4 = -3
    print(longestSubsequence(arr4, difference4))  # Output: 6

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    difference5 = 2
    print(longestSubsequence(arr5, difference5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a dictionary `dp` to store the length of the longest subsequence ending at each number.
- In the worst case, the dictionary could store up to n entries (one for each unique number in the array).
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming
"""