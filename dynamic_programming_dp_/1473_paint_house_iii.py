"""
LeetCode Question #1473: Paint House III

Problem Statement:
You are given an integer array `houses` where `houses[i]` represents the color of the house i. 
0 means the house is not painted yet. You are also given an integer `m` denoting the number of houses, 
an integer `n` denoting the number of colors, and an integer `target` denoting the number of neighborhoods 
required. A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example:
- houses = [1,2,2,3,3], target = 2 -> There are 2 neighborhoods: [1], [2,2,3,3].
- houses = [0,0,0,0,0], target = 1 -> There is 1 neighborhood: [0,0,0,0,0].

You are also given a 2D array `cost` where `cost[i][j]` is the cost of painting house i with color j+1. 
Return the minimum cost of painting all the houses such that there are exactly target neighborhoods. 
If it is not possible, return -1.

Constraints:
- `m == houses.length`
- `1 <= m <= 100`
- `1 <= n <= 20`
- `1 <= target <= m`
- `0 <= houses[i] <= n`
- `1 <= cost[i][j] <= 10^4`

"""

# Solution
from functools import lru_cache

def minCost(houses, cost, m, n, target):
    @lru_cache(None)
    def dp(index, neighborhoods, prev_color):
        # Base case: If we've painted all houses
        if index == m:
            return 0 if neighborhoods == target else float('inf')
        
        # If neighborhoods exceed target, return infinity
        if neighborhoods > target:
            return float('inf')
        
        # If the house is already painted
        if houses[index] != 0:
            return dp(index + 1, neighborhoods + (houses[index] != prev_color), houses[index])
        
        # If the house is not painted, try all colors
        min_cost = float('inf')
        for color in range(1, n + 1):
            cost_to_paint = cost[index][color - 1]
            min_cost = min(min_cost, cost_to_paint + dp(index + 1, neighborhoods + (color != prev_color), color))
        
        return min_cost
    
    result = dp(0, 0, 0)
    return result if result != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    houses = [0, 0, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    print(minCost(houses, cost, m, n, target))  # Output: 9

    # Test Case 2
    houses = [0, 2, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    print(minCost(houses, cost, m, n, target))  # Output: 11

    # Test Case 3
    houses = [3, 1, 2, 3]
    cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    m = 4
    n = 3
    target = 4
    print(minCost(houses, cost, m, n, target))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses memoization to avoid redundant calculations. The number of states in the DP table is O(m * target * n), 
  where m is the number of houses, target is the number of neighborhoods, and n is the number of colors.
- For each state, we iterate over n colors, resulting in a total complexity of O(m * target * n^2).

Space Complexity:
- The space complexity is dominated by the memoization table, which stores O(m * target * n) states.
- Additionally, there is a recursive call stack that can go up to O(m) depth.

Overall Space Complexity: O(m * target * n).
"""

# Topic: Dynamic Programming (DP)