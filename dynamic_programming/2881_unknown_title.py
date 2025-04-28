"""
LeetCode Problem #2881: Maximize the Profit as the Salesman

Problem Statement:
You are a traveling salesman tasked with selling products in different cities. You are given an integer `n` representing the number of cities, and a list of intervals `offers` where each offer is represented as `[start, end, profit]`. 
- `start` and `end` are the indices of the cities where the offer is valid (inclusive).
- `profit` is the amount of money you earn if you accept the offer.

You can only accept non-overlapping offers. Your goal is to maximize the total profit by selecting a subset of offers.

Return the maximum profit you can achieve.

Constraints:
- `1 <= n <= 10^5`
- `1 <= offers.length <= 10^5`
- `offers[i].length == 3`
- `0 <= start <= end < n`
- `1 <= profit <= 10^4`
"""

# Solution
from bisect import bisect_right

def maximizeTheProfit(n, offers):
    # Sort offers by their ending city
    offers.sort(key=lambda x: x[1])
    
    # DP array to store the maximum profit up to each city
    dp = [0] * (n + 1)
    
    # List of ending cities for binary search
    end_cities = [offer[1] for offer in offers]
    
    for i in range(len(offers)):
        start, end, profit = offers[i]
        
        # Find the last non-overlapping offer using binary search
        idx = bisect_right(end_cities, start - 1)
        
        # Update the DP value for the current offer
        dp[end + 1] = max(dp[end + 1], dp[end_cities[idx - 1] + 1] + profit)
    
    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    offers = [[0, 1, 5], [1, 2, 6], [0, 2, 8]]
    print(maximizeTheProfit(n, offers))  # Expected Output: 11

    # Test Case 2
    n = 10
    offers = [[0, 3, 10], [4, 6, 15], [7, 9, 20]]
    print(maximizeTheProfit(n, offers))  # Expected Output: 45

    # Test Case 3
    n = 3
    offers = [[0, 0, 5], [1, 1, 6], [2, 2, 8]]
    print(maximizeTheProfit(n, offers))  # Expected Output: 19

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the offers: O(m log m), where m is the number of offers.
- Iterating through the offers: O(m).
- Binary search for each offer: O(log m).
Overall: O(m log m), where m is the number of offers.

Space Complexity:
- DP array: O(n).
- End cities list: O(m).
Overall: O(n + m).
"""

# Topic: Dynamic Programming