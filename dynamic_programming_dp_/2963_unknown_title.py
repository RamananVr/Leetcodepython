"""
LeetCode Problem #2963: Minimum Total Distance Traveled

Problem Statement:
You are given an array `robot` where `robot[i]` represents the position of the i-th robot on a 1D plane. 
You are also given an array `factory` where each element is a pair `[position, limit]`. 
`position` represents the position of a factory on the 1D plane, and `limit` represents the maximum number of robots that the factory can repair.

Each robot can be assigned to at most one factory, and each factory can repair at most `limit` robots. 
The cost of assigning a robot to a factory is the absolute difference between their positions.

Return the minimum total distance traveled by all robots if they are optimally assigned to factories.

Constraints:
- `1 <= len(robot), len(factory) <= 100`
- `0 <= robot[i], factory[j][0] <= 10^9`
- `1 <= factory[j][1] <= len(robot)`

"""

from typing import List

def minimumTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    """
    Calculate the minimum total distance traveled by all robots to factories.
    """
    # Sort robots and factories by position
    robot.sort()
    factory.sort()

    # Number of robots and factories
    n, m = len(robot), len(factory)

    # Initialize DP table with infinity
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: no robots, no cost

    # Fill the DP table
    for i in range(n + 1):  # Iterate over robots
        for j in range(m):  # Iterate over factories
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])  # Skip the current factory
            total_cost = 0
            for k in range(1, min(factory[j][1], i) + 1):  # Assign up to factory[j][1] robots
                total_cost += abs(robot[i - k] - factory[j][0])
                dp[i][j + 1] = min(dp[i][j + 1], dp[i - k][j] + total_cost)

    return dp[n][m]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    robot = [0, 4, 6]
    factory = [[2, 2], [6, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: 4

    # Test Case 2
    robot = [1, 2, 3]
    factory = [[2, 2], [3, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: 2

    # Test Case 3
    robot = [5, 10, 15]
    factory = [[7, 2], [12, 1]]
    print(minimumTotalDistance(robot, factory))  # Output: 8


"""
Time Complexity:
- Sorting the robots and factories takes O(n log n + m log m), where n is the number of robots and m is the number of factories.
- Filling the DP table involves iterating over all robots and factories, and for each robot-factory pair, we may iterate up to the factory's limit. 
  This results in a complexity of O(n * m * L), where L is the maximum limit among all factories.

Space Complexity:
- The DP table requires O(n * m) space.

Primary Topic: Dynamic Programming (DP)
"""