"""
LeetCode Problem #377: Combination Sum IV

Problem Statement:
Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1, 2, 3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of `nums` are unique.
- 1 <= target <= 1000

Follow-up:
What if the given `nums` array is sorted? Could you optimize your algorithm?
"""

# Clean and Correct Python Solution
def combinationSum4(nums, target):
    """
    Function to calculate the number of combinations that sum up to the target.
    Uses dynamic programming to solve the problem efficiently.

    :param nums: List[int] - Array of distinct integers
    :param target: int - Target sum
    :return: int - Number of possible combinations
    """
    # Initialize a DP array where dp[i] represents the number of ways to form sum i
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: There's one way to form the sum 0 (using no elements)

    # Iterate through all possible sums from 1 to target
    for t in range(1, target + 1):
        for num in nums:
            if t >= num:  # If the current number can contribute to the sum
                dp[t] += dp[t - num]

    return dp[target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    target1 = 4
    print(f"Test Case 1: {combinationSum4(nums1, target1)}")  # Expected Output: 7

    # Test Case 2
    nums2 = [9]
    target2 = 3
    print(f"Test Case 2: {combinationSum4(nums2, target2)}")  # Expected Output: 0

    # Test Case 3
    nums3 = [2, 1]
    target3 = 5
    print(f"Test Case 3: {combinationSum4(nums3, target3)}")  # Expected Output: 8

    # Test Case 4
    nums4 = [10, 20, 30]
    target4 = 40
    print(f"Test Case 4: {combinationSum4(nums4, target4)}")  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `target` iterations.
- The inner loop iterates over the `nums` array, which has a length of `n`.
- Therefore, the time complexity is O(target * n), where `n` is the length of `nums`.

Space Complexity:
- The space complexity is O(target) due to the DP array of size `target + 1`.

Overall:
Time Complexity: O(target * n)
Space Complexity: O(target)
"""

# Topic: Dynamic Programming