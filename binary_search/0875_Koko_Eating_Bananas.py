"""
LeetCode Problem #875: Koko Eating Bananas

Problem Statement:
Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead, and then the hour ends.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

Constraints:
- `1 <= piles.length <= 10^4`
- `piles[i] <= 10^9`
- `1 <= h <= 10^9`
"""

# Clean and Correct Python Solution
def minEatingSpeed(piles, h):
    def canFinish(speed):
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + speed - 1) // speed  # Equivalent to math.ceil(pile / speed)
        return hours_needed <= h

    left, right = 1, max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if canFinish(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

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
    piles = [312884470]
    h = 312884469
    print(minEatingSpeed(piles, h))  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The binary search runs in O(log(max(piles))) iterations, where max(piles) is the largest pile size.
- For each iteration, we calculate the total hours needed using the `canFinish` function, which takes O(n) time, where n is the number of piles.
- Therefore, the overall time complexity is O(n * log(max(piles))).

Space Complexity:
- The algorithm uses O(1) additional space since we are not using any extra data structures.
"""

# Topic: Binary Search