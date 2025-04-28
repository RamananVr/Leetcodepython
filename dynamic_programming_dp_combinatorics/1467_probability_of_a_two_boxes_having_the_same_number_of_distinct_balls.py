"""
LeetCode Question #1467: Probability of a Two Boxes Having The Same Number of Distinct Balls

Problem Statement:
Given `n` balls of `k` different colors, where the `i-th` color has `balls[i]` balls. 
You are tasked to distribute all the balls into two boxes such that the probability of 
the two boxes having the same number of distinct colors is maximized.

Return the probability as a floating-point number.

Constraints:
- `1 <= balls.length <= 8`
- `1 <= balls[i] <= 6`
- The sum of balls[i] is even.

The probability is calculated as the number of valid distributions divided by the total number of distributions.
"""

from math import comb
from functools import lru_cache

def getProbability(balls):
    """
    Calculate the probability of two boxes having the same number of distinct colors.
    """
    total_balls = sum(balls)
    half_balls = total_balls // 2

    @lru_cache(None)
    def dfs(index, box1_count, box2_count, box1_distinct, box2_distinct):
        # Base case: all balls are distributed
        if index == len(balls):
            if box1_count == box2_count and box1_distinct == box2_distinct:
                return 1
            return 0

        total_ways = 0
        for i in range(balls[index] + 1):
            # i balls go to box1, the rest go to box2
            new_box1_distinct = box1_distinct + (1 if i > 0 else 0)
            new_box2_distinct = box2_distinct + (1 if balls[index] - i > 0 else 0)
            total_ways += dfs(
                index + 1,
                box1_count + i,
                box2_count + (balls[index] - i),
                new_box1_distinct,
                new_box2_distinct,
            ) * comb(balls[index], i)

        return total_ways

    # Total number of ways to distribute the balls
    total_distributions = dfs(0, 0, 0, 0, 0)

    # Valid distributions where both boxes have the same number of distinct colors
    valid_distributions = dfs(0, 0, 0, 0, 0)

    return valid_distributions / total_distributions


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    balls = [1, 1]
    print(getProbability(balls))  # Expected Output: 1.0

    # Test Case 2
    balls = [2, 1, 1]
    print(getProbability(balls))  # Expected Output: 0.6666666666666666

    # Test Case 3
    balls = [1, 2, 1, 2]
    print(getProbability(balls))  # Expected Output: 0.6000000000000001

    # Test Case 4
    balls = [3, 2, 1]
    print(getProbability(balls))  # Expected Output: 0.3


"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the DFS is proportional to `O(k * total_balls^2 * 2^k)`, where `k` is the number of colors.
- For each state, we iterate over the number of balls of the current color, which is at most `balls[i]`.
- Thus, the overall complexity is exponential in the number of colors `k`.

Space Complexity:
- The space complexity is determined by the memoization table, which stores `O(k * total_balls^2 * 2^k)` states.
- Additionally, the recursion stack can go up to `O(k)` depth.

Topic: Dynamic Programming (DP), Combinatorics
"""