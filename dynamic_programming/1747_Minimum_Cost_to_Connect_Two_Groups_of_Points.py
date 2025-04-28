"""
LeetCode Problem #1747: Minimum Cost to Connect Two Groups of Points

Problem Statement:
You are given two groups of points represented as two arrays `group1` and `group2` of size `m` and `n` respectively. 
The cost of connecting any point in `group1` to any point in `group2` is given in a 2D array `cost` where `cost[i][j]` 
is the cost of connecting the ith point in `group1` to the jth point in `group2`.

The task is to connect each point in `group1` to at least one point in `group2` and each point in `group2` to at least 
one point in `group1`. Return the minimum cost required to achieve this.

Constraints:
- `group1` and `group2` are not explicitly given; only the `cost` matrix is provided.
- `cost` is a 2D array of size `m x n` where `1 <= m, n <= 50` and `1 <= cost[i][j] <= 100`.

Example:
Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: Connect group1[0] to group2[0] with cost 15 and group1[1] to group2[1] with cost 2. Total cost = 15 + 2 = 17.

Approach:
This problem can be solved using dynamic programming. We use a bitmask to represent the connection state of `group2` 
and minimize the cost using a recursive approach.

"""

# Python Solution
from functools import lru_cache

def connectTwoGroups(cost):
    m, n = len(cost), len(cost[0])
    
    # Precompute the minimum cost to connect each point in group2 to any point in group1
    min_cost_group2 = [min(cost[i][j] for i in range(m)) for j in range(n)]
    
    @lru_cache(None)
    def dp(i, mask):
        # Base case: if all points in group1 are processed
        if i == m:
            # Add the cost of connecting remaining unconnected points in group2
            return sum(min_cost_group2[j] for j in range(n) if not (mask & (1 << j)))
        
        # Recursive case: try connecting group1[i] to each point in group2
        res = float('inf')
        for j in range(n):
            res = min(res, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return res
    
    # Start the recursion with the first point in group1 and an empty mask
    return dp(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost1 = [[15, 96], [36, 2]]
    print(connectTwoGroups(cost1))  # Output: 17

    # Test Case 2
    cost2 = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    print(connectTwoGroups(cost2))  # Output: 4

    # Test Case 3
    cost3 = [[2, 5, 1], [3, 8, 1], [1, 3, 2]]
    print(connectTwoGroups(cost3))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the DP is O(m * 2^n), where `m` is the number of points in group1 and `2^n` is the number of 
  possible masks for group2.
- For each state, we iterate over `n` points in group2, resulting in a total complexity of O(m * n * 2^n).

Space Complexity:
- The space complexity is dominated by the memoization table, which stores O(m * 2^n) states.
- Additionally, the recursion stack can go up to O(m) depth.
- Total space complexity: O(m * 2^n).

Topic: Dynamic Programming
"""