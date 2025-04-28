"""
LeetCode Problem #2528: Maximize the Minimum Powered City

Problem Statement:
You are given an array `stations` of length `n` where `stations[i]` represents the number of power stations in the `i-th` city. 
You are also given an integer `r` that represents the range of each power station and an integer `k` that represents the 
number of additional power stations you can build.

The power of a city is defined as the sum of power stations within its range `[i - r, i + r]` (inclusive). If a city is out 
of bounds, the range is adjusted to fit within the array.

Your task is to maximize the minimum power of all cities by optimally placing at most `k` additional power stations.

Return the maximum possible minimum power of all cities.

Constraints:
- `1 <= n <= 10^5`
- `0 <= stations[i] <= 10^5`
- `0 <= r <= n - 1`
- `0 <= k <= 10^9`

"""

from typing import List

def maxPower(stations: List[int], r: int, k: int) -> int:
    def is_possible(min_power: int) -> bool:
        """
        Helper function to check if it's possible to achieve a minimum power of `min_power`
        by adding at most `k` additional power stations.
        """
        additional_stations = 0
        current_power = 0
        needed_stations = [0] * n
        window_sum = sum(stations[:r + 1])

        for i in range(n):
            if i > r:
                window_sum -= stations[i - r - 1]
            if i + r < n:
                window_sum += stations[i + r]

            current_power = window_sum + needed_stations[i]
            if current_power < min_power:
                deficit = min_power - current_power
                if deficit > k:
                    return False
                k-=