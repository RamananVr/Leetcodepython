"""
LeetCode Problem #2976: Maximize the Profit as the Salesman

Problem Statement:
You are a traveling salesman, and you have `n` cities to visit. Each city has a profit associated with it, 
and you can only visit a subset of these cities. However, there are constraints: 
- You can only visit cities in a non-decreasing order of their indices.
- You can skip cities, but you cannot revisit a city once skipped.

You are given an integer `n` representing the number of cities and a list of tuples `offers` where each tuple 
is of the form `(start, end, profit)`. Here:
- `start` and `end` are the indices of the cities (0-indexed) that define the range of the offer.
- `profit` is the profit you earn if you accept the offer.

Your task is to determine the maximum profit you can achieve by selecting a subset of non-overlapping offers.

Return the maximum profit.

Constraints:
- 1 <= n <= 10^5
- 1 <= len(offers) <= 10^5
- 0 <= start <= end < n
- 1 <= profit <= 10^4
"""

from typing import List
import bisect

def maximizeTheProfit(n: int, offers: List[List[int]]) -> int:
    # Sort offers by their ending city
    offers.sort(key=lambda x: x[1])
    
    # dp[i] will store the maximum profit we can achieve considering the first i offers
    dp = [0] * (len(offers) + 1)
    
    # Extract the end points of the offers for binary search
    end_points = [offer[1] for offer in offers]
    
    for i in range(1, len(offers) + 1):
        start, end, profit = offers[i - 1]
        
        # Find the last offer that ends before the current offer starts
        idx = bisect.bisect_right(end_points, start - 1)
        
        # Option 1: Skip the current offer
        skip_profit = dp[i - 1]
        
        # Option 2: Take the current offer
        take_profit = profit + dp[idx]
        
        # Take the maximum of the two options
        dp[i] = max(skip_profit, take_profit)
    
    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    offers = [[0, 2, 4], [1, 3, 2], [0, 4, 3]]
    print(maximizeTheProfit(n, offers))  # Output: 6

    # Test Case 2
    n = 4
    offers = [[0, 1, 2], [1, 2, 4], [2, 3, 6]]
    print(maximizeTheProfit(n, offers))  # Output: 6

    # Test Case 3
    n = 6
    offers = [[0, 1, 5], [1, 2, 6], [2, 5, 10], [0, 5, 15]]
    print(maximizeTheProfit(n, offers))  # Output: 15

"""
Time Complexity:
- Sorting the offers takes O(len(offers) * log(len(offers))).
- For each offer, we perform a binary search, which takes O(log(len(offers))).
- Thus, the overall time complexity is O(len(offers) * log(len(offers))).

Space Complexity:
- The space complexity is O(len(offers)) due to the dp array and the end_points list.

Topic: Dynamic Programming, Binary Search
"""