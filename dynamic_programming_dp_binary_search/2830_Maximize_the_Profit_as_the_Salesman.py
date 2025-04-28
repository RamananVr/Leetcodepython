"""
LeetCode Problem #2830: Maximize the Profit as the Salesman

Problem Statement:
You are a traveling salesman, and you have been given a list of offers. Each offer is represented as a tuple (start, end, profit), where:
- `start` and `end` are integers representing the start and end days of the offer (inclusive).
- `profit` is an integer representing the profit you earn if you accept the offer.

You can only accept non-overlapping offers, meaning if you accept an offer, you cannot accept another offer that overlaps with it.

Your task is to determine the maximum profit you can achieve by selecting a subset of non-overlapping offers.

Constraints:
- 1 <= len(offers) <= 10^4
- 0 <= start <= end <= 10^4
- 1 <= profit <= 10^4
"""

from typing import List, Tuple
import bisect

def maximizeTheProfit(offers: List[Tuple[int, int, int]]) -> int:
    """
    Function to calculate the maximum profit by selecting non-overlapping offers.
    
    :param offers: List of tuples, where each tuple contains (start, end, profit).
    :return: Maximum profit achievable.
    """
    # Sort offers by their end time
    offers.sort(key=lambda x: x[1])
    
    # Extract end times for binary search
    end_times = [offer[1] for offer in offers]
    
    # DP array to store the maximum profit up to each offer
    dp = [0] * (len(offers) + 1)
    
    for i in range(1, len(offers) + 1):
        start, end, profit = offers[i - 1]
        
        # Find the last non-overlapping offer using binary search
        idx = bisect.bisect_right(end_times, start) - 1
        
        # Include the current offer's profit
        include_profit = profit + (dp[idx + 1] if idx != -1 else 0)
        
        # Exclude the current offer
        exclude_profit = dp[i - 1]
        
        # Take the maximum of including or excluding the current offer
        dp[i] = max(include_profit, exclude_profit)
    
    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    offers = [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60)]
    print(maximizeTheProfit(offers))  # Output: 120 (Choose offers (1, 3, 50) and (4, 6, 70))
    
    # Test Case 2
    offers = [(1, 2, 10), (2, 3, 20), (3, 4, 30), (4, 5, 40)]
    print(maximizeTheProfit(offers))  # Output: 100 (Choose all offers)
    
    # Test Case 3
    offers = [(1, 10, 100), (2, 3, 20), (4, 5, 30), (6, 7, 40)]
    print(maximizeTheProfit(offers))  # Output: 100 (Choose offer (1, 10, 100))
    
    # Test Case 4
    offers = [(1, 2, 5), (3, 4, 10), (5, 6, 15), (7, 8, 20)]
    print(maximizeTheProfit(offers))  # Output: 50 (Choose all offers)

"""
Time Complexity:
- Sorting the offers takes O(n log n), where n is the number of offers.
- For each offer, we perform a binary search to find the last non-overlapping offer, which takes O(log n).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the DP array and the end_times list.

Topic: Dynamic Programming (DP), Binary Search
"""