"""
LeetCode Problem #1799: Maximize Score After N Operations

Problem Statement:
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the i-th operation (1-indexed), you will:
1. Choose two elements, x and y.
2. Receive a score of i * gcd(x, y).
3. Remove x and y from nums.

Return the maximum score you can receive after performing n operations.

Constraints:
- 1 <= n <= 7
- nums.length == 2 * n
- 1 <= nums[i] <= 10^6
"""

from math import gcd
from functools import lru_cache
from itertools import combinations

def maxScore(nums):
    """
    Function to calculate the maximum score after performing n operations.

    Args:
    nums (List[int]): Array of positive integers of size 2 * n.

    Returns:
    int: Maximum score achievable.
    """
    n = len(nums) // 2

    @lru_cache(None)
    def dp(mask):
        # Count the number of pairs already formed
        pairs_formed = bin(mask).count('1') // 2

        # Base case: If all pairs are formed, return 0
        if pairs_formed == n:
            return 0

        max_score = 0

        # Try all combinations of two numbers that haven't been used yet
        for i in range(2 * n):
            if mask & (1 << i):  # If i-th number is already used, skip
                continue
            for j in range(i + 1, 2 * n):
                if mask & (1 << j):  # If j-th number is already used, skip
                    continue

                # Form a new mask with i and j marked as used
                new_mask = mask | (1 << i) | (1 << j)

                # Calculate the score for this pair
                current_score = (pairs_formed + 1) * gcd(nums[i], nums[j])

                # Recursively calculate the maximum score
                max_score = max(max_score, current_score + dp(new_mask))

        return max_score

    # Start with an empty mask (no numbers used)
    return dp(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2]
    print(maxScore(nums1))  # Expected Output: 1

    # Test Case 2
    nums2 = [3, 4, 6, 8]
    print(maxScore(nums2))  # Expected Output: 11

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6]
    print(maxScore(nums3))  # Expected Output: 14

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(maxScore(nums4))  # Expected Output: 23

"""
Time Complexity Analysis:
- There are 2 * n numbers, and we need to form n pairs.
- The number of states in the DP is 2^(2 * n) (all possible masks).
- For each state, we iterate over all pairs of numbers, which is O((2 * n)^2).
- Thus, the overall time complexity is O((2 * n)^2 * 2^(2 * n)).

Space Complexity Analysis:
- The space complexity is dominated by the DP cache, which has 2^(2 * n) states.
- Thus, the space complexity is O(2^(2 * n)).

Topic: Dynamic Programming (DP), Bitmasking
"""