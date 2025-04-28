"""
LeetCode Problem #1552: Magnetic Force Between Two Balls

Problem Statement:
In a row of `n` houses, each house is located at some position on the x-axis. You are given an array `position` where `position[i]` is the position of the `i-th` house. You want to place `m` balls in these houses such that the minimum magnetic force between any two balls is maximized.

The magnetic force between two balls at positions `x` and `y` is defined as `|x - y|`.

Return the maximum possible minimum magnetic force between any two balls.

Constraints:
- `2 <= n <= 10^5`
- `2 <= m <= n`
- `1 <= position[i] <= 10^9`
- All integers in `position` are distinct.
"""

# Solution
def maxDistance(position, m):
    """
    Function to find the maximum possible minimum magnetic force between any two balls.

    :param position: List[int] - Positions of the houses
    :param m: int - Number of balls to place
    :return: int - Maximum possible minimum magnetic force
    """
    # Sort the positions to enable binary search
    position.sort()

    # Helper function to check if we can place `m` balls with at least `min_force` distance
    def canPlaceBalls(min_force):
        count = 1  # Place the first ball at the first position
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= min_force:
                count += 1
                last_position = position[i]
                if count == m:  # Successfully placed all balls
                    return True
        return False

    # Binary search for the maximum minimum force
    left, right = 1, position[-1] - position[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if canPlaceBalls(mid):
            result = mid  # Update result and try for a larger minimum force
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    position1 = [1, 2, 3, 4, 7]
    m1 = 3
    print(maxDistance(position1, m1))  # Expected Output: 3

    # Test Case 2
    position2 = [5, 4, 3, 2, 1, 1000000000]
    m2 = 2
    print(maxDistance(position2, m2))  # Expected Output: 999999999

    # Test Case 3
    position3 = [1, 2, 8, 4, 9]
    m3 = 3
    print(maxDistance(position3, m3))  # Expected Output: 3

"""
Time Complexity:
- Sorting the `position` array takes O(n log n).
- The binary search runs for O(log(max_distance)), where `max_distance` is the difference between the largest and smallest positions.
- For each binary search iteration, the `canPlaceBalls` function is called, which takes O(n) time.
- Overall time complexity: O(n log n + n log(max_distance)), where `max_distance` is the range of positions.

Space Complexity:
- The algorithm uses O(1) additional space apart from the input array.
- Overall space complexity: O(1).

Topic: Binary Search
"""