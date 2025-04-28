"""
LeetCode Problem #1049: Last Stone Weight II

Problem Statement:
You are given an array of integers `stones` where `stones[i]` is the weight of the i-th stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left. Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 100
"""

# Solution
def lastStoneWeightII(stones):
    """
    This problem can be reduced to a variation of the "Partition Equal Subset Sum" problem.
    The goal is to split the stones into two groups such that the absolute difference
    between the sums of the two groups is minimized.

    We use a dynamic programming approach to solve this problem.
    """
    total_sum = sum(stones)
    target = total_sum // 2

    # DP set to store achievable sums
    dp = {0}

    for stone in stones:
        new_dp = dp.copy()
        for s in dp:
            new_dp.add(s + stone)
        dp = new_dp

    # Find the closest sum to target
    closest_sum = max(s for s in dp if s <= target)
    return total_sum - 2 * closest_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [2, 7, 4, 1, 8, 1]
    print("Test Case 1 Output:", lastStoneWeightII(stones1))  # Expected Output: 1

    # Test Case 2
    stones2 = [31, 26, 33, 21, 40]
    print("Test Case 2 Output:", lastStoneWeightII(stones2))  # Expected Output: 5

    # Test Case 3
    stones3 = [1, 2]
    print("Test Case 3 Output:", lastStoneWeightII(stones3))  # Expected Output: 1

    # Test Case 4
    stones4 = [1, 1, 4, 2, 2]
    print("Test Case 4 Output:", lastStoneWeightII(stones4))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(stones) and S = sum(stones).
- The DP approach iterates over all stones and updates a set of achievable sums.
- In the worst case, the size of the set can grow up to O(S), where S is the total sum of stones.
- Thus, the time complexity is O(n * S).

Space Complexity:
- The space complexity is O(S) because we store achievable sums in a set.

Overall:
Time Complexity: O(n * S)
Space Complexity: O(S)
"""

# Topic: Dynamic Programming