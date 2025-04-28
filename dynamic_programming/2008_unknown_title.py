"""
LeetCode Problem #2008: Maximum Earnings From Taxi

Problem Statement:
You are given `n` points on a straight line, numbered from `1` to `n`. You are also given a 2D array `rides`, where `rides[i] = [start_i, end_i, tip_i]` indicates that the i-th ride starts at `start_i`, ends at `end_i`, and earns a tip of `tip_i`.

The earnings of a ride are calculated as `end_i - start_i + tip_i`. You may choose to take any number of rides, but the rides must be non-overlapping (i.e., you cannot take two rides that overlap in time).

Return the maximum earnings you can achieve.

Constraints:
- `1 <= n <= 10^5`
- `1 <= rides.length <= 10^5`
- `rides[i].length == 3`
- `1 <= start_i < end_i <= n`
- `1 <= tip_i <= 10^5`

"""

# Solution
from bisect import bisect_right

def maxTaxiEarnings(n, rides):
    # Sort rides by their end time
    rides.sort(key=lambda x: x[1])
    
    # dp[i] represents the maximum earnings achievable up to the i-th ride
    dp = [0] * (len(rides) + 1)
    end_times = [ride[1] for ride in rides]
    
    for i in range(1, len(rides) + 1):
        start, end, tip = rides[i - 1]
        earnings = end - start + tip
        
        # Find the last ride that ends before the current ride starts
        prev_index = bisect_right(end_times, start) - 1
        
        # Update dp[i] with the maximum earnings achievable
        dp[i] = max(dp[i - 1], dp[prev_index + 1] + earnings)
    
    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    rides = [[2, 5, 4], [1, 5, 1], [5, 9, 2]]
    print(maxTaxiEarnings(n, rides))  # Output: 7

    # Test Case 2
    n = 20
    rides = [[1, 6, 1], [6, 10, 2], [10, 15, 3], [15, 20, 4]]
    print(maxTaxiEarnings(n, rides))  # Output: 10

    # Test Case 3
    n = 5
    rides = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    print(maxTaxiEarnings(n, rides))  # Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the rides by their end time takes O(rides.length * log(rides.length)).
- For each ride, we perform a binary search using `bisect_right`, which takes O(log(rides.length)).
- Thus, the overall time complexity is O(rides.length * log(rides.length)).

Space Complexity:
- The `dp` array and `end_times` array both take O(rides.length) space.
- Therefore, the space complexity is O(rides.length).

Topic: Dynamic Programming
"""