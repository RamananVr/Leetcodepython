"""
LeetCode Problem #1000: Minimum Cost to Merge Stones

Problem Statement:
There are `n` piles of stones arranged in a row. The i-th pile has `stones[i]` stones. A move consists of merging `k` consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these `k` piles.

Return the minimum cost to merge all piles into one pile. If it is impossible to merge all piles into one pile, return -1.

Constraints:
1. 1 <= stones.length <= 30
2. 2 <= k <= 30
3. 1 <= stones[i] <= 100

Example 1:
Input: stones = [3, 2, 4, 1], k = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
- Merge [3, 2] -> [5, 4, 1], cost = 5
- Merge [4, 1] -> [5, 5], cost = 5
- Merge [5, 5] -> [10], cost = 10
Total cost = 5 + 5 + 10 = 20.

Example 2:
Input: stones = [3, 2, 4, 1], k = 3
Output: -1
Explanation: After any merge, there are fewer than k piles left, so it's impossible to merge into one pile.

Example 3:
Input: stones = [3, 5, 1, 2, 6], k = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
- Merge [3, 5, 1] -> [9, 2, 6], cost = 9
- Merge [2, 6, 9] -> [17], cost = 17
Total cost = 9 + 17 = 25.
"""

from functools import lru_cache
from itertools import accumulate

def mergeStones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1  # Impossible to merge into one pile

    # Prefix sum for quick range sum calculation
    prefix_sum = [0] + list(accumulate(stones))

    @lru_cache(None)
    def dp(i, j, piles):
        if (j - i + 1 - piles) % (k - 1) != 0:
            return float('inf')  # Invalid state
        if i == j:
            return 0 if piles == 1 else float('inf')  # Base case

        if piles == 1:
            return dp(i, j, k) + prefix_sum[j + 1] - prefix_sum[i]

        # Try all possible partitions
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

"""
Time Complexity:
- The number of states in the DP is O(n^2 * k), where n is the length of the stones array.
- For each state, we iterate over a range of size O(n) to find the minimum cost.
- Thus, the overall time complexity is O(n^3 * k).

Space Complexity:
- The space complexity is O(n^2 * k) due to the memoization table.

Topic: Dynamic Programming (DP)
"""