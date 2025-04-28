"""
LeetCode Question #2911: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine whether there exists a subset of `nums` whose sum is equal to `target`. Return `True` if such a subset exists, otherwise return `False`.

Constraints:
- The length of `nums` is between 1 and 100.
- Each integer in `nums` is between -10^4 and 10^4.
- The `target` is between -10^4 and 10^4.

Example:
Input: nums = [1, 2, 3, 7], target = 6
Output: True
Explanation: The subset [1, 2, 3] has a sum of 6.

Input: nums = [1, 2, 3, 7], target = 10
Output: False
Explanation: No subset of nums has a sum of 10.

Topic: Dynamic Programming
"""

# Solution
def subset_sum(nums, target):
    """
    Determines whether there exists a subset of nums whose sum equals target.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    bool: True if a subset exists with sum equal to target, False otherwise.
    """
    n = len(nums)
    # Create a DP table where dp[i][j] represents whether a sum of j can be achieved using the first i elements.
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: A sum of 0 can always be achieved with an empty subset.
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(target + 1):
            # If we don't include nums[i-1]
            dp[i][j] = dp[i-1][j]
            # If we include nums[i-1], check if the remaining sum can be achieved
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

    return dp[n][target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 7]
    target1 = 6
    print(subset_sum(nums1, target1))  # Expected Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 7]
    target2 = 10
    print(subset_sum(nums2, target2))  # Expected Output: False

    # Test Case 3
    nums3 = [5, 3, 2, 8]
    target3 = 11
    print(subset_sum(nums3, target3))  # Expected Output: True

    # Test Case 4
    nums4 = [1, 2, 3]
    target4 = 7
    print(subset_sum(nums4, target4))  # Expected Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity of this solution is O(n * target), where n is the number of elements in nums and target is the target sum. This is because we iterate through all elements of nums and all possible sums up to target.

Space Complexity:
The space complexity is O(n * target) due to the DP table used to store intermediate results.

Topic: Dynamic Programming
"""