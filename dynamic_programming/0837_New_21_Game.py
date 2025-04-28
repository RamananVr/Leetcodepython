"""
LeetCode Problem #837: New 21 Game

Problem Statement:
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than `k` points. 
During each draw, she gains an integer number of points randomly from the range [1, maxPts], 
where `maxPts` is an integer. Each draw is independent and the outcomes have equal probability.

Alice stops drawing numbers when she reaches or exceeds `k` points. 
What is the probability that Alice has `n` or fewer points?

Given integers `n`, `k`, and `maxPts`, return the probability that Alice has `n` or fewer points.

Constraints:
- 0 <= k <= n <= 10^4
- 1 <= maxPts <= 10^4
"""

# Solution
def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    window_sum = 1.0
    result = 0.0

    for i in range(1, n + 1):
        dp[i] = window_sum / maxPts
        if i < k:
            window_sum += dp[i]
        else:
            result += dp[i]
        if i >= maxPts:
            window_sum -= dp[i - maxPts]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1, maxPts1 = 10, 1, 10
    print(new21Game(n1, k1, maxPts1))  # Expected Output: 1.0

    # Test Case 2
    n2, k2, maxPts2 = 6, 1, 10
    print(new21Game(n2, k2, maxPts2))  # Expected Output: 0.6

    # Test Case 3
    n3, k3, maxPts3 = 21, 17, 10
    print(new21Game(n3, k3, maxPts3))  # Expected Output: 0.73278 (approximately)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through all points from 1 to n, resulting in O(n) iterations.
- Each iteration involves constant-time operations, so the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a list `dp` of size n + 1 to store probabilities, resulting in O(n) space usage.
- Additionally, a few variables are used for calculations, which take O(1) space.
- Therefore, the overall space complexity is O(n).
"""

# Topic: Dynamic Programming