"""
LeetCode Problem 2742: Painting the Walls

You are given two 0-indexed integer arrays, cost and time, of size n representing n different walls. 
The ith wall takes time[i] units of time to paint and costs cost[i] units of money to paint.

You have two painters available:
- A paid painter that will paint the ith wall in time[i] units of time and will cost you cost[i] units of money.
- A free painter that will paint any wall in 1 unit of time at no cost. However, the free painter can only be used 
  if the paid painter is currently painting a wall.

Return the minimum amount of money required to paint n walls.

Example 1:
Input: cost = [1,2,3,2], time = [1,2,3,2]
Output: 3
Explanation: The walls are painted as follows:
- Paint wall 0 using paid painter, taking 1 unit of time, costing 1 unit of money.
- Paint wall 1 using free painter, taking 1 unit of time, costing 0 units of money.
- Paint wall 2 using paid painter, taking 3 units of time, costing 3 units of money.
- Paint wall 3 using free painter, taking 1 unit of time, costing 0 units of money.
The total time is 1 + 1 + 3 + 1 = 6 units of time.
The total cost is 1 + 0 + 3 + 0 = 4 units of money.
However, you can paint the walls in less time for less money:
- Paint wall 0 using paid painter, taking 1 unit of time, costing 1 unit of money.
- Paint wall 2 using paid painter, taking 3 units of time, costing 3 units of money.
- Paint wall 1 using free painter, taking 1 unit of time, costing 0 units of money.
- Paint wall 3 using free painter, taking 1 unit of time, costing 0 units of money.
The total time is 1 + 3 + 1 + 1 = 6 units of time.
The total cost is 1 + 3 + 0 + 0 = 4 units of money.
Actually, you can do better:
- Paint wall 1 using paid painter, taking 2 units of time, costing 2 units of money.
- Paint wall 2 using paid painter, taking 3 units of time, costing 3 units of money.
- Paint walls 0 and 3 using free painter while paid painter works, costing 0 units of money.
The total cost is 2 + 3 + 0 + 0 = 5 units of money.
Wait, let me recalculate:
- Paint wall 0 using paid painter, costing 1, time 1. Free painter can paint 1 wall.
- Paint wall 1 using paid painter, costing 2, time 2. Free painter can paint 2 walls.
So we can paint all 4 walls for cost 1 + 2 = 3.

Example 2:
Input: cost = [2,3,4,2], time = [1,1,1,1]
Output: 4
Explanation: Paint walls 0 and 3 using paid painter for a total cost of 2 + 2 = 4. 
Free painter paints walls 1 and 2.

Constraints:
- 1 <= cost.length <= 500
- cost.length == time.length
- 1 <= cost[i] <= 10^6
- 1 <= time[i] <= 500
"""

from typing import List
from functools import lru_cache


def paintWalls(cost: List[int], time: List[int]) -> int:
    """
    Find minimum cost to paint all walls using paid and free painters.
    
    Key insight: If we use paid painter for wall i (cost[i], time[i]), 
    the free painter can paint time[i] additional walls during that time.
    
    This is a 0/1 knapsack problem where we need to select walls for paid painter
    such that total time >= n-1 (to cover all remaining walls with free painter).
    
    Args:
        cost: List of costs for each wall
        time: List of time needed for each wall
        
    Returns:
        Minimum cost to paint all walls
        
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(cost)
    
    @lru_cache(maxsize=None)
    def dp(i: int, remain: int) -> int:
        """
        Minimum cost to paint 'remain' walls starting from wall i.
        
        Args:
            i: Current wall index
            remain: Number of walls remaining to be painted
            
        Returns:
            Minimum cost
        """
        if remain <= 0:
            return 0
        if i == n:
            return float('inf')
        
        # Option 1: Use paid painter for wall i
        # This wall + time[i] additional walls can be painted
        paint_paid = cost[i] + dp(i + 1, remain - 1 - time[i])
        
        # Option 2: Skip wall i (will be painted by free painter)
        skip = dp(i + 1, remain)
        
        return min(paint_paid, skip)
    
    return dp(0, n)


def paintWallsBottomUp(cost: List[int], time: List[int]) -> int:
    """
    Bottom-up DP solution for painting walls.
    
    Args:
        cost: List of costs for each wall
        time: List of time needed for each wall
        
    Returns:
        Minimum cost to paint all walls
        
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(cost)
    
    # dp[j] = minimum cost to paint j walls
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(n):
        new_dp = dp[:]
        for j in range(n + 1):
            if dp[j] != float('inf'):
                # Use paid painter for wall i
                # Can paint 1 + time[i] walls total
                walls_painted = min(n, j + 1 + time[i])
                new_dp[walls_painted] = min(new_dp[walls_painted], dp[j] + cost[i])
        dp = new_dp
    
    return dp[n]


def paintWallsGreedy(cost: List[int], time: List[int]) -> int:
    """
    Greedy approach: sort by efficiency (time[i] / cost[i]) in descending order.
    
    Args:
        cost: List of costs for each wall
        time: List of time needed for each wall
        
    Returns:
        Minimum cost to paint all walls
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(cost)
    
    # Create (efficiency, cost, time) tuples and sort by efficiency descending
    walls = [(time[i] / cost[i], cost[i], time[i]) for i in range(n)]
    walls.sort(reverse=True)
    
    total_cost = 0
    free_time = 0
    walls_painted = 0
    
    for efficiency, c, t in walls:
        if walls_painted >= n:
            break
        
        # Use paid painter
        total_cost += c
        walls_painted += 1  # This wall
        free_time += t      # Free painter can work for this much time
        
        # Free painter paints as many walls as possible
        free_walls = min(free_time, n - walls_painted)
        walls_painted += free_walls
        free_time -= free_walls
    
    return total_cost


# Test cases
def test_paintWalls():
    """Test the paintWalls function with various inputs."""
    
    test_cases = [
        {
            "cost": [1, 2, 3, 2],
            "time": [1, 2, 3, 2],
            "expected": 3,
            "description": "Example 1: Paint walls 0 and 1 with paid painter"
        },
        {
            "cost": [2, 3, 4, 2],
            "time": [1, 1, 1, 1],
            "expected": 4,
            "description": "Example 2: Paint walls 0 and 3 with paid painter"
        },
        {
            "cost": [1],
            "time": [1],
            "expected": 1,
            "description": "Single wall"
        },
        {
            "cost": [26, 53, 10, 24, 25, 20, 63, 51, 40, 37],
            "time": [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
            "expected": 55,
            "description": "Larger example with varying times"
        },
        {
            "cost": [42, 8, 28, 35, 21, 13, 21, 35],
            "time": [2, 1, 1, 1, 2, 1, 1, 1],
            "expected": 63,
            "description": "Another complex example"
        }
    ]
    
    for i, test in enumerate(test_cases):
        cost = test["cost"]
        time = test["time"]
        expected = test["expected"]
        
        # Test main solution
        result1 = paintWalls(cost, time)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: cost = {cost}, time = {time}")
        print(f"  Expected: {expected}")
        print(f"  Top-down DP: {result1}")
        
        # Test bottom-up solution
        result2 = paintWallsBottomUp(cost, time)
        print(f"  Bottom-up DP: {result2}")
        
        # Verify results
        assert result1 == expected, f"Top-down DP failed for test {i+1}"
        assert result2 == expected, f"Bottom-up DP failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_paintWalls()

"""
Complexity Analysis:

1. Top-down DP (paintWalls):
   - Time Complexity: O(n^2) - we have n*n states (i, remain)
   - Space Complexity: O(n^2) - memoization table + recursion stack

2. Bottom-up DP (paintWallsBottomUp):
   - Time Complexity: O(n^2) - nested loops over walls and remaining count
   - Space Complexity: O(n) - DP array of size n+1

3. Greedy (paintWallsGreedy):
   - Time Complexity: O(n log n) - sorting step
   - Space Complexity: O(n) - for storing wall tuples

Key Insights:
- This is essentially a variant of the knapsack problem
- We need to select walls for paid painter such that total time >= n-1
- The free painter can paint time[i] walls while paid painter works on wall i
- Dynamic programming gives optimal solution
- Greedy approach may not always give optimal result but can be good approximation

Topics: Arrays, Dynamic Programming, Knapsack Problem, Greedy Algorithms
"""
