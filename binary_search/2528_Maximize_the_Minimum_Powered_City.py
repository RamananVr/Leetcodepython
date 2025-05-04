"""
LeetCode Question #2528: Maximize the Minimum Powered City

Problem Statement:
You are given an array `stations` of length `n`, where `stations[i]` represents the number of power stations in the `i-th` city. 
You are also given an integer `r` representing the range of each power station and an integer `k` representing the number of additional power stations you can build.

The power of a city is defined as the sum of power stations in the city itself and all cities within a distance of `r` from it.

Your task is to maximize the minimum power of any city by optimally placing up to `k` additional power stations.

Return the maximum possible minimum power of any city.

Constraints:
- `1 <= n <= 10^5`
- `0 <= stations[i] <= 10^9`
- `0 <= r <= n - 1`
- `0 <= k <= 10^9`

Example:
Input: stations = [1, 2, 4, 5, 0], r = 1, k = 3
Output: 7
Explanation: By adding 3 power stations optimally, the minimum power of any city can be maximized to 7.

"""

# Python Solution
def max_min_power(stations, r, k):
    def is_valid(min_power):
        # Calculate initial power for each city
        n = len(stations)
        power = [0] * n
        current_power = 0
        for i in range(n):
            if i > r:
                current_power -= power[i - r - 1]
            if i + r < n:
                current_power += stations[i]
            power[i] = current_power

        # Add additional power stations to meet the minimum power requirement
        additional_stations = 0
        for i in range(n):
            if power[i] < min_power:
                needed = min_power - power[i]
                additional_stations += needed
                if additional_stations > k:
                    return False
                if i + r < n:
                    power[i + r] += needed
        return True

    # Binary search for the maximum minimum power
    left, right = 0, sum(stations) + k
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stations = [1, 2, 4, 5, 0]
    r = 1
    k = 3
    print(max_min_power(stations, r, k))  # Output: 7

    # Test Case 2
    stations = [0, 0, 0, 0, 0]
    r = 2
    k = 10
    print(max_min_power(stations, r, k))  # Output: 2

    # Test Case 3
    stations = [10, 0, 0, 0, 10]
    r = 1
    k = 5
    print(max_min_power(stations, r, k))  # Output: 10

    # Test Case 4
    stations = [5, 5, 5, 5, 5]
    r = 0
    k = 0
    print(max_min_power(stations, r, k))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the initial power array takes O(n).
- The binary search runs for O(log(max_power)), where max_power is the sum of stations + k.
- For each binary search step, we validate the minimum power in O(n).
- Overall time complexity: O(n * log(max_power)).

Space Complexity:
- The space complexity is O(n) for the power array.

Primary Topic: Binary Search
"""