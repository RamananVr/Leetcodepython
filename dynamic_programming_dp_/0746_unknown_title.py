"""
LeetCode Problem #746: Min Cost Climbing Stairs

Problem Statement:
You are given an integer array `cost` where `cost[i]` is the cost of the ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps. You can either start from the step 
with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach the top.
The total cost is 6.

Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""

def minCostClimbingStairs(cost):
    """
    Function to calculate the minimum cost to reach the top of the floor.

    :param cost: List[int] - The cost array where cost[i] is the cost of the ith step.
    :return: int - The minimum cost to reach the top of the floor.
    """
    n = len(cost)
    if n == 2:
        return min(cost[0], cost[1])
    
    # Initialize dp array to store the minimum cost to reach each step
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # Fill the dp array
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
    # The result is the minimum cost to reach the top from the last two steps
    return min(dp[n - 1], dp[n - 2])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost1 = [10, 15, 20]
    print(minCostClimbingStairs(cost1))  # Output: 15

    # Test Case 2
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost2))  # Output: 6

    # Test Case 3
    cost3 = [0, 0, 1, 1]
    print(minCostClimbingStairs(cost3))  # Output: 1

    # Test Case 4
    cost4 = [10, 15]
    print(minCostClimbingStairs(cost4))  # Output: 10

    # Test Case 5
    cost5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(minCostClimbingStairs(cost5))  # Output: 25

"""
Time Complexity:
- O(n), where n is the length of the `cost` array. We iterate through the array once to compute the dp values.

Space Complexity:
- O(n), where n is the length of the `cost` array. We use an additional dp array of size n to store intermediate results.

Topic: Dynamic Programming (DP)
"""