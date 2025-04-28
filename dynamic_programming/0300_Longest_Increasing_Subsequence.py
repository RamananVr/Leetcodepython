"""
LeetCode Problem #300: Longest Increasing Subsequence

Problem Statement:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Follow up:
Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

# Clean, Correct Python Solution
def lengthOfLIS(nums):
    """
    Function to find the length of the longest increasing subsequence in an array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The length of the longest strictly increasing subsequence.
    """
    if not nums:
        return 0

    # Initialize an array to store the length of the LIS ending at each index
    dp = [1] * len(nums)

    # Iterate through the array to calculate LIS for each index
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The result is the maximum value in the dp array
    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Test Case 1 Output:", lengthOfLIS(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print("Test Case 2 Output:", lengthOfLIS(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print("Test Case 3 Output:", lengthOfLIS(nums3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print("Test Case 4 Output:", lengthOfLIS(nums4))  # Expected Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses a nested loop to calculate the LIS for each index.
- The outer loop runs O(n) times, and the inner loop runs O(n) times in the worst case.
- Therefore, the time complexity is O(n^2).

Space Complexity:
- The solution uses a dp array of size n to store the LIS for each index.
- Therefore, the space complexity is O(n).
"""

# Topic: Dynamic Programming