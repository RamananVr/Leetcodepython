"""
LeetCode Problem #2741: Special Permutations

Problem Statement:
You are given a 0-indexed integer array `nums` containing `n` distinct positive integers. A permutation of `nums` is called special if:

- For every index `i` in the range `[0, n - 2]`, either `perm[i] % perm[i + 1] == 0` or `perm[i + 1] % perm[i] == 0`.

Return the total number of special permutations. Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- `2 <= nums.length <= 14`
- `1 <= nums[i] <= 10^9`
- All the integers in `nums` are distinct.
"""

from functools import lru_cache

def specialPerm(nums):
    MOD = 10**9 + 7
    n = len(nums)

    @lru_cache(None)
    def dfs(mask, prev):
        """
        Perform a depth-first search to count special permutations.
        :param mask: A bitmask representing which elements are used.
        :param prev: The index of the previous element in the permutation.
        :return: The count of special permutations starting with the given state.
        """
        if mask == (1 << n) - 1:  # All elements are used
            return 1

        total = 0
        for i in range(n):
            if not (mask & (1 << i)):  # If nums[i] is not used
                if prev == -1 or nums[prev] % nums[i] == 0 or nums[i] % nums[prev] == 0:
                    total += dfs(mask | (1 << i), i)
                    total %= MOD

        return total

    return dfs(0, -1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 6]
    print(specialPerm(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 4, 3]
    print(specialPerm(nums2))  # Expected Output: 2

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(specialPerm(nums3))  # Expected Output: 8

"""
Time Complexity Analysis:
- There are `n!` permutations of the array `nums`, and for each permutation, we check the divisibility condition.
- Using bitmasking and memoization, the number of states is `O(n * 2^n)` (n choices for the previous element and 2^n possible masks).
- For each state, we iterate over `n` elements, leading to a total complexity of `O(n^2 * 2^n)`.

Space Complexity Analysis:
- The space complexity is determined by the memoization table, which stores `O(n * 2^n)` states.
- The recursive call stack can go up to `O(n)` depth.
- Overall space complexity: `O(n * 2^n)`.

Topic: Dynamic Programming (DP) with Bitmasking
"""