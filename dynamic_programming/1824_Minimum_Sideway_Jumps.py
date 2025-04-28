"""
LeetCode Problem #1824: Minimum Sideway Jumps

Problem Statement:
There is a three-lane road of length `n` that consists of `n + 1` points labeled from `0` to `n`. A frog starts at point `0` in the second lane and wants to jump to point `n` in any lane. However, there could be obstacles along the way.

You are given an array `obstacles` of length `n + 1` where each `obstacles[i]` (0-indexed) describes an obstacle on the lane at point `i`. If `obstacles[i] == 0`, there are no obstacles at point `i`. If `obstacles[i] == 1`, there is an obstacle on lane 1. Similarly, if `obstacles[i] == 2`, there is an obstacle on lane 2, and if `obstacles[i] == 3`, there is an obstacle on lane 3.

- The frog can only travel from point `i` to point `i + 1` on the same lane if there is no obstacle on the lane at point `i + 1`.
- To avoid obstacles, the frog can also perform a side jump to move to another lane (even if there is no obstacle on the current lane).

The side jump is described as:
- The frog can jump from lane `1` to lane `2` or lane `3`.
- The frog can jump from lane `2` to lane `1` or lane `3`.
- The frog can jump from lane `3` to lane `1` or lane `2`.

Return the minimum number of side jumps the frog needs to reach point `n` starting from lane `2` at point `0`.

Constraints:
- `obstacles.length == n + 1`
- `1 <= n <= 5 * 10^5`
- `0 <= obstacles[i] <= 3`
- `obstacles[0] == obstacles[n] == 0`
"""

def minSideJumps(obstacles):
    """
    Dynamic Programming solution to find the minimum number of side jumps.
    """
    n = len(obstacles) - 1
    # Initialize the dp array with large values
    dp = [1, 0, 1]  # dp[0] -> lane 1, dp[1] -> lane 2, dp[2] -> lane 3

    for i in range(1, n + 1):
        # Update dp for the current position
        for lane in range(3):
            if obstacles[i] == lane + 1:
                dp[lane] = float('inf')  # Cannot stay on a lane with an obstacle

        # Check for side jumps
        for lane in range(3):
            if obstacles[i] != lane + 1:
                dp[lane] = min(dp[lane], dp[(lane + 1) % 3] + 1, dp[(lane + 2) % 3] + 1)

    return min(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    obstacles = [0, 1, 2, 3, 0]
    print(minSideJumps(obstacles))  # Output: 2

    # Test Case 2
    obstacles = [0, 1, 1, 3, 3, 0]
    print(minSideJumps(obstacles))  # Output: 0

    # Test Case 3
    obstacles = [0, 2, 1, 0, 3, 0]
    print(minSideJumps(obstacles))  # Output: 2

"""
Time Complexity:
- The algorithm iterates through the `obstacles` array once, and for each position, it performs constant-time operations to update the `dp` array.
- Therefore, the time complexity is O(n), where `n` is the length of the `obstacles` array.

Space Complexity:
- The algorithm uses a fixed-size `dp` array of size 3 to store the minimum side jumps for each lane.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""