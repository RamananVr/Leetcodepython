"""
LeetCode Question #2473: Minimum Cost to Buy Apples

Problem Statement:
You are given an array `cost` where `cost[i]` is the cost of buying `i+1` apples. You want to buy exactly `n` apples. 
You can buy any number of apples in one transaction, but you cannot buy more than `n` apples in total. 
Find the minimum cost to buy exactly `n` apples.

Constraints:
- 1 <= cost.length <= 1000
- 1 <= cost[i] <= 10^6
- 1 <= n <= 1000
"""

def minCostToBuyApples(cost, n):
    """
    Function to calculate the minimum cost to buy exactly n apples.

    :param cost: List[int] - cost[i] is the cost of buying i+1 apples
    :param n: int - the number of apples to buy
    :return: int - the minimum cost to buy exactly n apples
    """
    # Initialize a dp array where dp[i] represents the minimum cost to buy i apples
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 apples cost 0

    # Iterate through each number of apples we can buy in one transaction
    for i in range(len(cost)):
        # Update dp array for each possible number of apples
        for j in range(i + 1, n + 1):
            dp[j] = min(dp[j], dp[j - (i + 1)] + cost[i])

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost = [2, 5, 7]
    n = 5
    print(minCostToBuyApples(cost, n))  # Expected Output: 10

    # Test Case 2
    cost = [3, 6, 8, 10]
    n = 7
    print(minCostToBuyApples(cost, n))  # Expected Output: 21

    # Test Case 3
    cost = [1, 2, 3]
    n = 4
    print(minCostToBuyApples(cost, n))  # Expected Output: 4

    # Test Case 4
    cost = [5, 10, 15]
    n = 3
    print(minCostToBuyApples(cost, n))  # Expected Output: 15

"""
Time Complexity Analysis:
- Let `m` be the length of the `cost` array and `n` be the number of apples to buy.
- The outer loop runs `m` times (once for each cost[i]).
- The inner loop runs up to `n` times for each `i`.
- Therefore, the time complexity is O(m * n).

Space Complexity Analysis:
- The space complexity is O(n) due to the `dp` array of size `n + 1`.

Topic: Dynamic Programming (DP)
"""