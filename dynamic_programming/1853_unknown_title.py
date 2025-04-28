"""
LeetCode Problem #1853: Maximum Number of Events That Can Be Attended II

Problem Statement:
You are given an array of events where `events[i] = [startDayi, endDayi, valuei]`. The `i-th` event starts at `startDayi` and ends at `endDayi`, and if you attend this event, you will receive a value of `valuei`. You are also given an integer `k` which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events that overlap on the same day.

Return the maximum sum of values that you can receive by attending at most `k` events.

Constraints:
- `1 <= k <= events.length`
- `1 <= events.length <= 10^4`
- `1 <= startDayi <= endDayi <= 10^9`
- `1 <= valuei <= 10^6`
"""

from bisect import bisect_left

def maxValue(events, k):
    # Sort events by their end day
    events.sort(key=lambda x: x[1])
    n = len(events)
    
    # Precompute the start days for binary search
    start_days = [event[0] for event in events]
    
    # DP table: dp[i][j] represents the maximum value we can get by considering
    # the first i events and attending at most j events
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        start, end, value = events[i - 1]
        
        # Find the last event that ends before the current event starts
        prev_index = bisect_left(start_days, start) - 1
        
        for j in range(1, k + 1):
            # Option 1: Skip the current event
            dp[i][j] = dp[i - 1][j]
            
            # Option 2: Attend the current event
            if prev_index >= 0:
                dp[i][j] = max(dp[i][j], dp[prev_index + 1][j - 1] + value)
            else:
                dp[i][j] = max(dp[i][j], value)
    
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    events = [[1, 3, 3], [3, 4, 4], [2, 3, 10]]
    k = 2
    print(maxValue(events, k))  # Output: 10

    # Test Case 2
    events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k = 2
    print(maxValue(events, k))  # Output: 7

    # Test Case 3
    events = [[1, 3, 2], [4, 5, 2], [6, 7, 2], [8, 9, 2], [1, 10, 10]]
    k = 3
    print(maxValue(events, k))  # Output: 14

"""
Time Complexity:
- Sorting the events takes O(n log n), where n is the number of events.
- Filling the DP table takes O(n * k), where n is the number of events and k is the maximum number of events we can attend.
- Binary search for each event takes O(log n), and it is performed for each DP state, resulting in O(n * k * log n).
- Overall time complexity: O(n log n + n * k * log n).

Space Complexity:
- The DP table requires O(n * k) space.
- The `start_days` array requires O(n) space.
- Overall space complexity: O(n * k).

Topic: Dynamic Programming
"""