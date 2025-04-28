"""
LeetCode Problem #2106: Maximum Fruits Harvested After at Most K Steps

Problem Statement:
Fruits are placed at some positions on an infinite 1D line. You are given a 2D integer array `fruits` where `fruits[i] = [position_i, amount_i]` denotes `amount_i` fruits at position `position_i`. `position_i` is sorted in strictly increasing order.

You are also given two integers `startPos` and `k`. Initially, you are at position `startPos`. From any position, you can walk to any other position at a cost of 1 step.

Return the maximum total number of fruits you can collect in at most `k` steps.

Constraints:
- `1 <= fruits.length <= 10^5`
- `fruits[i].length == 2`
- `0 <= position_i <= 10^9`
- `1 <= amount_i <= 10^4`
- `0 <= startPos <= 10^9`
- `1 <= k <= 10^9`
- All the positions in `fruits` are distinct and sorted in strictly increasing order.
"""

# Solution
from typing import List

def maxFruits(fruits: List[List[int]], startPos: int, k: int) -> int:
    # Create a sliding window to calculate the maximum fruits collected
    n = len(fruits)
    left = 0
    max_fruits = 0
    current_fruits = 0

    for right in range(n):
        # Add the fruits at the current position to the window
        current_fruits += fruits[right][1]

        # Calculate the distance to the farthest point in the window
        while left <= right and not is_within_steps(fruits, left, right, startPos, k):
            # Remove the fruits at the leftmost position from the window
            current_fruits -= fruits[left][1]
            left += 1

        # Update the maximum fruits collected
        max_fruits = max(max_fruits, current_fruits)

    return max_fruits

def is_within_steps(fruits: List[List[int]], left: int, right: int, startPos: int, k: int) -> bool:
    """
    Helper function to check if the current window is within the allowed steps.
    """
    left_pos = fruits[left][0]
    right_pos = fruits[right][0]

    # Two possible paths:
    # 1. Go to the leftmost position first, then to the rightmost position
    # 2. Go to the rightmost position first, then to the leftmost position
    return min(abs(startPos - left_pos) + abs(right_pos - left_pos),
               abs(startPos - right_pos) + abs(right_pos - left_pos)) <= k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    fruits = [[2, 4], [4, 5], [6, 3], [8, 2]]
    startPos = 5
    k = 4
    print(maxFruits(fruits, startPos, k))  # Output: 9

    # Test Case 2
    fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
    startPos = 5
    k = 4
    print(maxFruits(fruits, startPos, k))  # Output: 14

    # Test Case 3
    fruits = [[0, 3], [6, 4], [8, 5]]
    startPos = 3
    k = 2
    print(maxFruits(fruits, startPos, k))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach, where each fruit position is processed at most twice (once when expanding the window and once when contracting it).
- Checking if the current window is within the allowed steps takes O(1) time.
- Therefore, the overall time complexity is O(n), where n is the number of fruit positions.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Sliding Window