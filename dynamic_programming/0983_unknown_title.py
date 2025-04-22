"""
LeetCode Problem #983: Minimum Cost For Tickets

Problem Statement:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for `costs[0]` dollars,
- a 7-day pass is sold for `costs[1]` dollars, and
- a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel. For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, ..., 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Constraints:
- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is in strictly increasing order.
- costs.length == 3
- 1 <= costs[i] <= 1000
"""

# Solution
from typing import List

def mincostTickets(days: List[int], costs: List[int]) -> int:
    # Use dynamic programming to solve the problem
    n = len(days)
    dp = [0] * (n + 1)  # dp[i] represents the minimum cost to cover days[i:]
    
    for i in range(n - 1, -1, -1):
        # Option 1: Buy a 1-day pass
        j1 = i
        while j1 < n and days[j1] < days[i] + 1:
            j1 += 1
        cost1 = costs[0] + dp[j1]
        
        # Option 2: Buy a 7-day pass
        j7 = i
        while j7 < n and days[j7] < days[i] + 7:
            j7 += 1
        cost7 = costs[1] + dp[j7]
        
        # Option 3: Buy a 30-day pass
        j30 = i
        while j30 < n and days[j30] < days[i] + 30:
            j30 += 1
        cost30 = costs[2] + dp[j30]
        
        # Take the minimum of the three options
        dp[i] = min(cost1, cost7, cost30)
    
    return dp[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))  # Output: 11

    # Test Case 2
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))  # Output: 17

    # Test Case 3
    days = [1, 365]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over the `days` array, which has a length of `n`.
- For each day, we perform three binary searches (or linear scans in this case) to find the next valid day for 1-day, 7-day, and 30-day passes.
- In the worst case, the total complexity is O(n^2) due to the nested loops.

Space Complexity:
- The space complexity is O(n) for the `dp` array.

Overall:
- Time Complexity: O(n^2)
- Space Complexity: O(n)
"""

# Topic: Dynamic Programming