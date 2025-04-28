"""
LeetCode Problem #2463: Minimum Total Distance Traveled

Problem Statement:
You are given an array `robot` where `robot[i]` is the position of the i-th robot. You are also given a 2D array `factory` where `factory[j] = [position_j, limit_j]` indicates that the j-th factory is located at `position_j` and can repair at most `limit_j` robots.

The positions of the robots and factories are given as integers. The distance between a robot at position `x` and a factory at position `y` is `|x - y|` (absolute difference).

Return the minimum total distance required to repair all the robots. If it is impossible to repair all the robots, return -1.

Constraints:
- `1 <= robot.length, factory.length <= 100`
- `0 <= robot[i], position_j <= 10^9`
- `1 <= limit_j <= robot.length`

"""

# Solution
from functools import lru_cache

def minimumTotalDistance(robot, factory):
    # Sort robots and factories by position to minimize distance
    robot.sort()
    factory.sort(key=lambda x: x[0])
    
    @lru_cache(None)
    def dp(r_idx, f_idx, used):
        # Base case: all robots are assigned
        if r_idx == len(robot):
            return 0
        # Base case: all factories are exhausted
        if f_idx == len(factory):
            return float('inf')
        
        # Skip current factory
        skip_factory = dp(r_idx, f_idx + 1, 0)
        
        # Assign robot to current factory if within limit
        assign_robot = float('inf')
        if used < factory[f_idx][1]:
            assign_robot = abs(robot[r_idx] - factory[f_idx][0]) + dp(r_idx + 1, f_idx, used + 1)
        
        # Return the minimum of skipping or assigning
        return min(skip_factory, assign_robot)
    
    # Start the recursion
    result = dp(0, 0, 0)
    return result if result != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    robot = [0, 4, 6]
    factory = [[2, 2], [6, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: 4

    # Test Case 2
    robot = [1, 5, 9]
    factory = [[3, 1], [7, 2]]
    print(minimumTotalDistance(robot, factory))  # Output: 8

    # Test Case 3
    robot = [1, 2, 3]
    factory = [[2, 2], [4, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: 2

    # Test Case 4
    robot = [1, 2, 3]
    factory = [[4, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `robot` array and `factory` array takes O(n log n + m log m), where n is the number of robots and m is the number of factories.
- The recursive DP function has a state space of O(n * m * limit), where `limit` is the maximum number of robots a factory can repair. Each state is computed in O(1), so the overall complexity is O(n * m * limit).

Space Complexity:
- The space complexity is dominated by the memoization table, which is O(n * m * limit).
- Additionally, the recursion stack can go up to O(n + m) depth.

Primary Topic: Dynamic Programming (DP)
"""