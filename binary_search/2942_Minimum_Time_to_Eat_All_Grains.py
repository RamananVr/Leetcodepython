"""
LeetCode Problem #2942: Minimum Time to Eat All Grains

Problem Statement:
You are given an array `piles` where `piles[i]` represents the number of grains in the i-th pile. You are also given an integer `h` which represents the maximum number of hours you have to eat all the grains. You can eat grains at a constant speed `k` grains per hour. If you eat from a pile, you must finish eating from that pile before moving to the next one. You cannot eat from multiple piles simultaneously.

Return the minimum integer `k` such that you can eat all the grains within `h` hours.

Constraints:
- `1 <= piles.length <= 10^4`
- `1 <= piles[i] <= 10^9`
- `1 <= h <= 10^9`
"""

# Solution
from math import ceil

def minEatingSpeed(piles, h):
    def canEatAllGrains(speed):
        # Check if we can eat all grains at the given speed within h hours
        total_hours = sum(ceil(pile / speed) for pile in piles)
        return total_hours <= h

    # Binary search for the minimum speed
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if canEatAllGrains(mid):
            right = mid  # Try a smaller speed
        else:
            left = mid + 1  # Increase the speed
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))  # Expected Output: 4

    # Test Case 2
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(minEatingSpeed(piles, h))  # Expected Output: 30

    # Test Case 3
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(minEatingSpeed(piles, h))  # Expected Output: 23

    # Test Case 4
    piles = [1, 1, 1, 1]
    h = 4
    print(minEatingSpeed(piles, h))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The binary search runs in O(log(max(piles))) iterations, where max(piles) is the largest pile size.
- For each iteration, we calculate the total hours required using the `canEatAllGrains` function, which takes O(n) time, where n is the number of piles.
- Therefore, the overall time complexity is O(n * log(max(piles))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""