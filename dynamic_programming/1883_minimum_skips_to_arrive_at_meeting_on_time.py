"""
LeetCode Question #1883: Minimum Skips to Arrive at Meeting On Time

Problem Statement:
You are given an integer `n` representing the number of roads between your home and the meeting point, and an array `dist` of length `n` where `dist[i]` is the length of the ith road. You are also given an integer `speed` representing your speed (in distance per unit time), and an integer `hoursBefore` representing the maximum time you have to reach the meeting point.

You want to minimize the number of skips you need to arrive at the meeting point on time. A skip allows you to travel through a road without rounding up the travel time to the nearest integer. For example, if you travel a road of length 5 at a speed of 2, it normally takes `ceil(5 / 2) = 3` units of time. However, if you skip, it takes exactly `5 / 2 = 2.5` units of time.

Return the minimum number of skips required to arrive at the meeting point on time, or -1 if it is impossible.

Constraints:
- `1 <= n <= 1000`
- `1 <= dist[i] <= 10^5`
- `1 <= speed <= 10^5`
- `1 <= hoursBefore <= 10^7`
"""

# Python Solution
from math import ceil

def minSkips(dist, speed, hoursBefore):
    n = len(dist)
    # dp[i][j]: Minimum time to travel the first i roads with j skips
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: 0 roads, 0 skips => 0 time

    for i in range(1, n + 1):
        for j in range(i + 1):  # j skips cannot exceed i roads
            # Without skipping
            dp[i][j] = ceil(dp[i - 1][j] + dist[i - 1] / speed)
            # With skipping (if skips are available)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i - 1] / speed)

    # Find the minimum skips required to meet the time constraint
    for skips in range(n + 1):
        if dp[n][skips] <= hoursBefore:
            return skips

    return -1  # Impossible to arrive on time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dist = [1, 3, 2]
    speed = 4
    hoursBefore = 2
    print(minSkips(dist, speed, hoursBefore))  # Output: 1

    # Test Case 2
    dist = [7, 3, 5, 5]
    speed = 2
    hoursBefore = 10
    print(minSkips(dist, speed, hoursBefore))  # Output: 2

    # Test Case 3
    dist = [5, 5, 5, 5]
    speed = 1
    hoursBefore = 10
    print(minSkips(dist, speed, hoursBefore))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a 2D table of size `n x n`.
- For each road `i` (1 to n), we iterate over the possible number of skips `j` (0 to i).
- Thus, the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n^2) due to the 2D DP table.

Topic: Dynamic Programming
"""