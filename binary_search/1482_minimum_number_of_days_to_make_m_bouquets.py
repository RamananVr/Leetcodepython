"""
LeetCode Question #1482: Minimum Number of Days to Make m Bouquets

Problem Statement:
You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. The garden consists of `n` flowers, the `i-th` flower will bloom in the `bloomDay[i]` and cannot be used before that day.

Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return `-1`.

Constraints:
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`
"""

from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    def canMakeBouquets(days: int) -> bool:
        """Helper function to check if we can make m bouquets in the given number of days."""
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
            if bouquets >= m:
                return True
        return False

    # If it's impossible to make m bouquets, return -1
    if m * k > len(bloomDay):
        return -1

    # Binary search to find the minimum number of days
    left, right = min(bloomDay), max(bloomDay)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if canMakeBouquets(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    print(minDays(bloomDay, m, k))  # Output: 3

    # Test Case 2
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 2
    print(minDays(bloomDay, m, k))  # Output: -1

    # Test Case 3
    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    print(minDays(bloomDay, m, k))  # Output: 12

    # Test Case 4
    bloomDay = [1000000000, 1000000000]
    m = 1
    k = 1
    print(minDays(bloomDay, m, k))  # Output: 1000000000

    # Test Case 5
    bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    m = 4
    k = 2
    print(minDays(bloomDay, m, k))  # Output: 9

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The binary search runs in O(log(max(bloomDay) - min(bloomDay))).
   - The `canMakeBouquets` function iterates through the `bloomDay` array, which takes O(n) time.
   - Therefore, the overall time complexity is O(n * log(max(bloomDay) - min(bloomDay))).

2. Space Complexity:
   - The algorithm uses O(1) additional space since we are not using any extra data structures.

Topic: Binary Search
"""