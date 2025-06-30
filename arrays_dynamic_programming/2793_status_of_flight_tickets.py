"""
2793. Status of Flight Tickets

Problem Statement:
You are given a 2D integer array tickets where tickets[i] = [price_i, days_i] indicates that 
there is a flight ticket that costs price_i and is valid for days_i consecutive days.

You are also given an integer k.

Return the minimum cost to have at least one valid ticket for k consecutive days.

Constraints:
- 1 <= tickets.length <= 100
- tickets[i].length == 2
- 1 <= price_i <= 1000
- 1 <= days_i <= 1000
- 1 <= k <= 1000

Test Cases:
1. Input: tickets = [[10,2],[15,3],[8,4]], k = 4
   Output: 23
   
2. Input: tickets = [[5,1],[10,2],[12,3]], k = 2
   Output: 10
"""

from typing import List
import heapq

def mincostTickets(tickets: List[List[int]], k: int) -> int:
    """
    Find minimum cost to have valid tickets for k consecutive days.
    
    Algorithm:
    1. Use dynamic programming approach
    2. For each day, try all possible ticket options
    3. Choose the minimum cost option that covers the day
    
    Time Complexity: O(k * n) where n is number of ticket types
    Space Complexity: O(k)
    """
    # dp[i] = minimum cost to cover first i days
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    
    for day in range(1, k + 1):
        # Try each ticket type
        for price, duration in tickets:
            # If this ticket can cover day 'day'
            start_day = max(0, day - duration)
            dp[day] = min(dp[day], dp[start_day] + price)
    
    return dp[k]

def mincostTicketsGreedy(tickets: List[List[int]], k: int) -> int:
    """
    Greedy approach: always choose the most cost-effective ticket.
    
    Time Complexity: O(k * n)
    Space Complexity: O(1)
    """
    total_cost = 0
    days_covered = 0
    
    while days_covered < k:
        remaining_days = k - days_covered
        
        # Find the most cost-effective ticket for remaining days
        best_ratio = float('inf')
        best_ticket = None
        
        for price, duration in tickets:
            effective_days = min(duration, remaining_days)
            if effective_days > 0:
                ratio = price / effective_days
                if ratio < best_ratio:
                    best_ratio = ratio
                    best_ticket = (price, duration)
        
        if best_ticket:
            price, duration = best_ticket
            total_cost += price
            days_covered += min(duration, remaining_days)
        else:
            break
    
    return total_cost

def mincostTicketsOptimized(tickets: List[List[int]], k: int) -> int:
    """
    Optimized DP solution with space optimization.
    
    Time Complexity: O(k * n)
    Space Complexity: O(max_duration)
    """
    max_duration = max(duration for _, duration in tickets)
    
    # Only keep track of last max_duration days
    dp = [0] * (max_duration + 1)
    
    for day in range(1, k + 1):
        min_cost = float('inf')
        
        for price, duration in tickets:
            prev_day = max(0, min(max_duration, day - duration))
            cost = dp[prev_day % (max_duration + 1)] + price
            min_cost = min(min_cost, cost)
        
        dp[day % (max_duration + 1)] = min_cost
    
    return dp[k % (max_duration + 1)]

def mincostTicketsHeap(tickets: List[List[int]], k: int) -> int:
    """
    Using priority queue to always select cheapest valid option.
    
    Time Complexity: O(k * n * log(n))
    Space Complexity: O(n)
    """
    # Create heap with (cost_per_day, price, duration)
    heap = []
    for price, duration in tickets:
        cost_per_day = price / duration
        heapq.heappush(heap, (cost_per_day, price, duration))
    
    total_cost = 0
    days_covered = 0
    
    while days_covered < k:
        remaining_days = k - days_covered
        
        # Find best ticket for current situation
        best_cost = float('inf')
        best_ticket = None
        
        for cost_per_day, price, duration in heap:
            effective_days = min(duration, remaining_days)
            if effective_days > 0:
                actual_cost = price
                if actual_cost < best_cost:
                    best_cost = actual_cost
                    best_ticket = (price, duration)
        
        if best_ticket:
            price, duration = best_ticket
            total_cost += price
            days_covered += min(duration, remaining_days)
        else:
            break
    
    return total_cost

# Test cases
def test_mincost_tickets():
    # Test case 1
    tickets1 = [[10, 2], [15, 3], [8, 4]]
    k1 = 4
    result1 = mincostTickets(tickets1, k1)
    print(f"Test 1 - Expected: 23, Got: {result1}")
    
    # Test case 2
    tickets2 = [[5, 1], [10, 2], [12, 3]]
    k2 = 2
    result2 = mincostTickets(tickets2, k2)
    print(f"Test 2 - Expected: 10, Got: {result2}")
    
    # Test case 3: Single day
    tickets3 = [[1, 1], [2, 2], [3, 3]]
    k3 = 1
    result3 = mincostTickets(tickets3, k3)
    print(f"Test 3 - Single day, Expected: 1, Got: {result3}")
    
    # Test case 4: Long duration ticket is better
    tickets4 = [[1, 1], [10, 100]]
    k4 = 50
    result4 = mincostTickets(tickets4, k4)
    print(f"Test 4 - Long duration better, Expected: 10, Got: {result4}")

def test_all_solutions():
    tickets = [[10, 2], [15, 3], [8, 4]]
    k = 4
    
    result_dp = mincostTickets(tickets, k)
    result_greedy = mincostTicketsGreedy(tickets, k)
    result_optimized = mincostTicketsOptimized(tickets, k)
    
    print(f"DP solution: {result_dp}")
    print(f"Greedy solution: {result_greedy}")
    print(f"Optimized DP: {result_optimized}")

if __name__ == "__main__":
    test_mincost_tickets()
    test_all_solutions()

"""
Topic Classification: Dynamic Programming, Greedy, Arrays

Key Insights:
1. This is a variation of the minimum cost ticket problem
2. DP approach considers all possible ways to cover k days
3. Greedy approach may not always give optimal solution
4. Need to consider overlapping coverage when buying tickets

Complexity Analysis:
- Time Complexity: O(k * n) for DP approach
- Space Complexity: O(k) for DP array, can be optimized to O(max_duration)
"""
