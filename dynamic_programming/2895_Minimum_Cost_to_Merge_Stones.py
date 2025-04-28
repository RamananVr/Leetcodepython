"""
LeetCode Problem #2895: Minimum Cost to Merge Stones

Problem Statement:
There are `n` stones arranged in a row. You are given an integer array `stones` of length `n` where `stones[i]` is the weight of the `i-th` stone. You are also given an integer `k`.

A move consists of merging exactly `k` consecutive stones into a single stone. The cost of this move is equal to the total weight of the `k` stones. After the merge, the new stone's weight is equal to the total weight of the merged stones.

Return the minimum cost to merge all the stones into one stone. If it is impossible to merge all the stones into one, return `-1`.

Constraints:
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 100`
- `2 <= k <= 30`

Example:
Input: stones = [3, 2, 4, 1], k = 2
Output: 20
Explanation: We start with stones = [3, 2, 4, 1].
1. Merge [3, 2] -> [5, 4, 1], cost = 5.
2. Merge [4, 1] -> [5, 5], cost = 5.
3. Merge [5, 5] -> [10], cost = 10.
Total cost = 5 + 5 + 10 = 20.

Input: stones = [3, 2, 4, 1], k = 3
Output: -1
Explanation: After any merge, we will have 3 stones left. It is impossible to merge into one stone.

Input: stones = [3, 5, 1, 2, 6], k = 3
Output: 25
Explanation: We start with stones = [3, 5, 1, 2, 6].
1. Merge [3, 5, 1] -> [9, 2, 6], cost = 9.
2. Merge [9, 2, 6] -> [17], cost = 17.
Total cost = 9 + 17 = 25.
"""

# Python Solution
from functools import lru_cache
from itertools import accumulate

def mergeStones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1

    # Prefix sum for quick range sum calculation
    prefix = [0] + list(accumulate(stones))

    @lru_cache(None)
    def dp(i, j, piles):
        if (j - i + 1 - piles) % (k - 1) != 0:
            return float('inf')
        if i == j:
            return 0 if piles == 1 else float('inf')
        if piles == 1:
            return dp(i, j, k) + prefix[j + 1] - prefix[i]
        return min(dp(i, mid, 1) + dp(mid + 1, j, piles - 1) for mid in range(i, j, k - 1))

    return dp(0, n - 1, 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones = [3, 2, 4, 1]
    k = 2
    print(mergeStones(stones, k))  # Output: 20

    # Test Case 2
    stones = [3, 2, 4, 1]
    k = 3
    print(mergeStones(stones, k))  # Output: -1

    # Test Case 3
    stones = [3, 5, 1, 2, 6]
    k = 3
    print(mergeStones(stones, k))  # Output: 25

    # Test Case 4
    stones = [1, 2, 3]
    k = 3
    print(mergeStones(stones, k))  # Output: 6

    # Test Case 5
    stones = [1, 2, 3, 4]
    k = 2
    print(mergeStones(stones, k))  # Output: 19

"""
Time Complexity:
- The `dp` function is called for every subarray (i, j) and for every possible number of piles.
- There are O(n^2) subarrays and O(k) possible pile values.
- For each subarray, we iterate over O(n) midpoints.
- Total complexity: O(n^3 * k).

Space Complexity:
- The `dp` function uses memoization, storing results for O(n^2 * k) states.
- Space complexity: O(n^2 * k).

Topic: Dynamic Programming
"""