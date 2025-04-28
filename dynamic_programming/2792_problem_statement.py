"""
LeetCode Question #2792: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine whether there exists a subset of `nums` such that the sum of the subset equals `target`. Return `True` if such a subset exists, otherwise return `False`.

Constraints:
- 1 <= len(nums) <= 100
- -10^4 <= nums[i] <= 10^4
- -10^4 <= target <= 10^4

Example:
Input: nums = [1, 2, 3, 4], target = 6
Output: True
Explanation: The subset [2, 4] sums to 6.

Input: nums = [1, 2, 3, 4], target = 10
Output: False
Explanation: No subset sums to 10.
"""

# Solution
def subset_sum(nums, target):
    """
    Determines whether there exists a subset of nums that sums to target.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    bool: True if a subset exists that sums to target, False otherwise.
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: A sum of 0 can always be achieved with an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3, 4]
    target = 6
    print(subset_sum(nums, target))  # Output: True

    # Test Case 2
    nums = [1, 2, 3, 4]
    target = 10
    print(subset_sum(nums, target))  # Output: False

    # Test Case 3
    nums = [5, 3, 2, 7]
    target = 10
    print(subset_sum(nums, target))  # Output: True

    # Test Case 4
    nums = [1, 1, 1, 1]
    target = 3
    print(subset_sum(nums, target))  # Output: True

    # Test Case 5
    nums = [1, 2, 3, 4]
    target = 0
    print(subset_sum(nums, target))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses a dynamic programming approach with a 2D table of size (n+1) x (target+1), where n is the length of nums.
- Filling the table requires O(n * target) operations.
Thus, the time complexity is O(n * target).

Space Complexity:
The space complexity is determined by the size of the DP table, which is O(n * target).
"""

# Topic: Dynamic Programming