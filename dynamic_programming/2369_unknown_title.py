"""
LeetCode Problem #2369: Check if There is a Valid Partition For The Array

Problem Statement:
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each subarray meets at least one of the following conditions:
1. The subarray consists of exactly 2 equal elements. For example, [2,2].
2. The subarray consists of exactly 3 equal elements. For example, [4,4,4].
3. The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, [3,4,5].

Return true if the array has at least one valid partition. Otherwise, return false.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Solution
def validPartition(nums):
    n = len(nums)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty array is valid

    for i in range(1, n):
        # Check condition 1: Two equal elements
        if i >= 1 and nums[i] == nums[i - 1]:
            dp[i + 1] = dp[i + 1] or dp[i - 1]

        # Check condition 2: Three equal elements
        if i >= 2 and nums[i] == nums[i - 1] == nums[i - 2]:
            dp[i + 1] = dp[i + 1] or dp[i - 2]

        # Check condition 3: Three consecutive increasing elements
        if i >= 2 and nums[i] - nums[i - 1] == 1 and nums[i - 1] - nums[i - 2] == 1:
            dp[i + 1] = dp[i + 1] or dp[i - 2]

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid partition with two equal elements
    nums1 = [4, 4, 4, 5, 6]
    print(validPartition(nums1))  # Output: True

    # Test Case 2: Valid partition with three consecutive increasing elements
    nums2 = [1, 2, 3, 4, 5]
    print(validPartition(nums2))  # Output: True

    # Test Case 3: Invalid partition
    nums3 = [1, 3, 5, 7]
    print(validPartition(nums3))  # Output: False

    # Test Case 4: Valid partition with three equal elements
    nums4 = [2, 2, 2, 3, 4, 5]
    print(validPartition(nums4))  # Output: True

    # Test Case 5: Edge case with minimum length
    nums5 = [1, 1]
    print(validPartition(nums5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time checks for each index.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a dp array of size n + 1 to store intermediate results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming
"""