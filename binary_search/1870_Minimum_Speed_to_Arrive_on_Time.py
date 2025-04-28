"""
LeetCode Problem #1870: Minimum Speed to Arrive on Time

Problem Statement:
You are given a floating-point number `hour`, representing the amount of time you have to reach the office. 
To commute to the office, you must take `n` trains in sequential order. You are also given an integer array `dist` 
of length `n`, where `dist[i]` describes the distance (in kilometers) of the `i-th` train route.

You can choose the speed of each train, but the speed must be an integer. You are required to arrive at the office 
on time (i.e., within `hour` hours), and the speed of the trains must be the same for all the trains.

Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at to reach the 
office on time, or return -1 if it is impossible to be on time.

Note that the time it takes to travel one train route is `dist[i] / speed`. The time spent on the `i-th` train route 
is rounded up to the nearest integer if it is not the last train route, because you arrive at the station and wait 
for the next train.

Example 1:
Input: dist = [1, 3, 2], hour = 6
Output: 1
Explanation: At speed = 1, the total time is 1 + 3 + 2 = 6 hours.

Example 2:
Input: dist = [1, 3, 2], hour = 2.7
Output: -1
Explanation: It is impossible to be on time even at the maximum speed of 10^7 km/h.

Example 3:
Input: dist = [1, 3, 2], hour = 3
Output: 3
Explanation: At speed = 3, the total time is 1 + 1 + 2 = 3 hours.

Constraints:
- `n == dist.length`
- `1 <= n <= 10^5`
- `1 <= dist[i] <= 10^5`
- `1 <= hour <= 10^9`
- The answer will not exceed 10^7.
"""

# Python Solution
from math import ceil

def minSpeedOnTime(dist, hour):
    def can_arrive_on_time(speed):
        total_time = 0
        for i in range(len(dist)):
            if i == len(dist) - 1:
                total_time += dist[i] / speed
            else:
                total_time += ceil(dist[i] / speed)
        return total_time <= hour

    # Binary search for the minimum speed
    left, right = 1, 10**7
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if can_arrive_on_time(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dist1 = [1, 3, 2]
    hour1 = 6
    print(minSpeedOnTime(dist1, hour1))  # Output: 1

    # Test Case 2
    dist2 = [1, 3, 2]
    hour2 = 2.7
    print(minSpeedOnTime(dist2, hour2))  # Output: -1

    # Test Case 3
    dist3 = [1, 3, 2]
    hour3 = 3
    print(minSpeedOnTime(dist3, hour3))  # Output: 3

    # Test Case 4
    dist4 = [5, 5, 5]
    hour4 = 5.5
    print(minSpeedOnTime(dist4, hour4))  # Output: 5

    # Test Case 5
    dist5 = [1]
    hour5 = 1.5
    print(minSpeedOnTime(dist5, hour5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max_speed)), where max_speed = 10^7.
- For each speed checked during binary search, we iterate through the `dist` array to calculate the total time, 
  which takes O(n) time.
- Therefore, the overall time complexity is O(n * log(max_speed)).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables for computation and no additional data structures.

Topic: Binary Search
"""