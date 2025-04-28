"""
LeetCode Problem #1230: Toss Strange Coins

Problem Statement:
You have some coins. The `i`-th coin has a probability `prob[i]` of facing heads when tossed.
Return the probability that the number of heads equals `target` if you toss all the coins.

Example:
Input: prob = [0.4, 0.5, 0.6], target = 2
Output: 0.24

Constraints:
- 1 <= prob.length <= 1000
- 0 <= prob[i] <= 1
- 0 <= target <= prob.length
"""

def probabilityOfHeads(prob, target):
    """
    Calculate the probability of getting exactly `target` heads when tossing coins with given probabilities.

    :param prob: List[float], probabilities of each coin facing heads
    :param target: int, the desired number of heads
    :return: float, the probability of getting exactly `target` heads
    """
    n = len(prob)
    # Initialize a DP table with dimensions (n+1) x (target+1)
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 0 coins and 0 heads has probability 1

    for i in range(1, n + 1):
        for j in range(target + 1):
            # Probability of not getting heads for the i-th coin
            dp[i][j] = dp[i - 1][j] * (1 - prob[i - 1])
            # Probability of getting heads for the i-th coin
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * prob[i - 1]

    return dp[n][target]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prob = [0.4, 0.5, 0.6]
    target = 2
    print(probabilityOfHeads(prob, target))  # Expected Output: 0.24

    # Test Case 2
    prob = [0.3, 0.7, 0.8]
    target = 1
    print(probabilityOfHeads(prob, target))  # Expected Output: 0.38

    # Test Case 3
    prob = [0.1, 0.2, 0.3, 0.4]
    target = 3
    print(probabilityOfHeads(prob, target))  # Expected Output: 0.024

    # Test Case 4
    prob = [0.5, 0.5, 0.5, 0.5]
    target = 4
    print(probabilityOfHeads(prob, target))  # Expected Output: 0.0625

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DP table has dimensions (n+1) x (target+1), where `n` is the number of coins and `target` is the desired number of heads.
- Filling each cell in the table takes constant time.
- Therefore, the time complexity is O(n * target).

Space Complexity:
- The DP table requires O(n * target) space.
- No additional space is used apart from the DP table.
- Therefore, the space complexity is O(n * target).

Topic: Dynamic Programming (DP)
"""