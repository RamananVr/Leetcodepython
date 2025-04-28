"""
LeetCode Problem #1770: Maximum Score from Performing Multiplication Operations

Problem Statement:
You are given two integer arrays `nums` and `multipliers` of size `n` and `m` respectively, where `n >= m`. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly `m` operations. On the i-th operation (1-indexed), you will:
- Choose one integer `nums[left]` or `nums[right]` from the array `nums`.
- Add `multipliers[i] * nums[left]` or `multipliers[i] * nums[right]` to your score.
- Remove the chosen integer from the array `nums`.

Return the maximum score you can achieve after performing `m` operations.

Constraints:
- `n == nums.length`
- `m == multipliers.length`
- `1 <= m <= 10^3`
- `m <= n <= 10^5`
- `-1000 <= nums[i], multipliers[i] <= 1000`
"""

# Clean, Correct Python Solution
def maximumScore(nums, multipliers):
    # Use dynamic programming with memoization
    from functools import lru_cache

    n, m = len(nums), len(multipliers)

    @lru_cache(None)
    def dp(left, i):
        # Base case: if we've used all multipliers
        if i == m:
            return 0

        # Calculate the right index based on the left index and i
        right = n - 1 - (i - left)

        # Recursively calculate the maximum score
        pick_left = multipliers[i] * nums[left] + dp(left + 1, i + 1)
        pick_right = multipliers[i] * nums[right] + dp(left, i + 1)

        return max(pick_left, pick_right)

    # Start the recursion with left index 0 and multiplier index 0
    return dp(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    multipliers1 = [3, 2, 1]
    print(maximumScore(nums1, multipliers1))  # Expected Output: 14

    # Test Case 2
    nums2 = [-5, -3, -3, -2, 7, 1]
    multipliers2 = [-10, -5, 3, 4, 6]
    print(maximumScore(nums2, multipliers2))  # Expected Output: 102

    # Test Case 3
    nums3 = [10, -5, 3, 4, 6]
    multipliers3 = [2, 1, -1]
    print(maximumScore(nums3, multipliers3))  # Expected Output: 27

# Time and Space Complexity Analysis
"""
Time Complexity:
- The recursive function `dp(left, i)` is called at most `m * m` times, where `m` is the length of the `multipliers` array.
- Each call takes O(1) time due to simple arithmetic operations.
- Therefore, the overall time complexity is O(m^2).

Space Complexity:
- The memoization table stores results for at most `m * m` states, so the space complexity for memoization is O(m^2).
- Additionally, the recursion stack can go up to a depth of `m`, so the space complexity for the stack is O(m).
- Overall space complexity is O(m^2).
"""

# Topic: Dynamic Programming