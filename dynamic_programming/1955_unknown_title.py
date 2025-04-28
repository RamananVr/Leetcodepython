"""
LeetCode Problem #1955: Count Number of Special Subsequences

Problem Statement:
You are given an array `nums` (0-indexed) consisting of integers 0, 1, and 2. 
A subsequence of `nums` is called special if it follows the pattern `[0, 1, 2]` 
(i.e., it consists of one or more 0s followed by one or more 1s, followed by one or more 2s).

Return the number of different special subsequences modulo 10^9 + 7.

A subsequence of an array is a new array generated from the original array by deleting some 
(can be none) of the elements without disturbing the relative order of the remaining elements. 
For example, `[2,1,3]` is a subsequence of `[2,3,1,3]`, but `[2,3,3]` is not.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 2
"""

# Python Solution
def countSpecialSubsequences(nums):
    MOD = 10**9 + 7
    count_0, count_1, count_2 = 0, 0, 0

    for num in nums:
        if num == 0:
            count_0 = (2 * count_0 + 1) % MOD
        elif num == 1:
            count_1 = (2 * count_1 + count_0) % MOD
        elif num == 2:
            count_2 = (2 * count_2 + count_1) % MOD

    return count_2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 2, 0, 1, 2]
    print(countSpecialSubsequences(nums1))  # Expected Output: 7

    # Test Case 2
    nums2 = [0, 0, 1, 1, 2, 2]
    print(countSpecialSubsequences(nums2))  # Expected Output: 36

    # Test Case 3
    nums3 = [2, 1, 0]
    print(countSpecialSubsequences(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [0, 1, 0, 2, 1, 2]
    print(countSpecialSubsequences(nums4))  # Expected Output: 10

    # Test Case 5
    nums5 = [0, 1, 2]
    print(countSpecialSubsequences(nums5))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `nums` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses only a constant amount of extra space to store the counts (`count_0`, `count_1`, `count_2`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""