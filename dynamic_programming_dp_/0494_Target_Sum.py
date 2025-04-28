"""
LeetCode Problem #494: Target Sum

Problem Statement:
You are given an integer array `nums` and an integer `target`.

You want to build an expression out of nums by adding one of the symbols '+' or '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add the symbols to get "+2-1" or "-2+1".

Return the number of different expressions that you can build, which evaluates to `target`.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
"""

# Solution
def findTargetSumWays(nums, target):
    """
    This function calculates the number of ways to assign '+' and '-' to the elements of nums
    such that their sum equals the target.

    :param nums: List[int] - The list of integers.
    :param target: int - The target sum.
    :return: int - The number of ways to achieve the target sum.
    """
    from collections import defaultdict

    # Dictionary to store the number of ways to achieve each sum
    dp = defaultdict(int)
    dp[0] = 1  # Base case: one way to achieve sum 0 (by using no elements)

    for num in nums:
        next_dp = defaultdict(int)
        for current_sum, count in dp.items():
            next_dp[current_sum + num] += count
            next_dp[current_sum - num] += count
        dp = next_dp

    return dp[target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(findTargetSumWays(nums1, target1))  # Expected Output: 5

    # Test Case 2
    nums2 = [1]
    target2 = 1
    print(findTargetSumWays(nums2, target2))  # Expected Output: 1

    # Test Case 3
    nums3 = [1, 2, 1]
    target3 = 2
    print(findTargetSumWays(nums3, target3))  # Expected Output: 2

    # Test Case 4
    nums4 = [0, 0, 0, 0, 0]
    target4 = 0
    print(findTargetSumWays(nums4, target4))  # Expected Output: 32

    # Test Case 5
    nums5 = [1000]
    target5 = -1000
    print(findTargetSumWays(nums5, target5))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(nums) and S = sum(nums).
- At each step, we iterate over all possible sums in the range [-S, S].
- The total number of states is O(n * S), where S is the sum of all elements in nums.
- Therefore, the time complexity is O(n * S).

Space Complexity:
- We use a dictionary to store the number of ways to achieve each sum.
- The space complexity is O(S), where S is the sum of all elements in nums.
"""

# Topic: Dynamic Programming (DP)