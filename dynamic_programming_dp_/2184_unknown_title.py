"""
LeetCode Problem #2184: Number of Ways to Build Sturdy Brick Wall

Problem Statement:
You are building a wall of bricks of width `width` and height `height`. Each brick has a fixed width, and you can use bricks of widths `brickTypes` to build the wall. The wall is considered sturdy if no vertical line can pass through the entire height of the wall without hitting a brick.

Given the integers `width`, `height`, and the list `brickTypes`, return the number of ways to build a sturdy wall modulo 10^9 + 7.

Constraints:
- 1 <= width, height <= 100
- 1 <= len(brickTypes) <= 10
- 1 <= brickTypes[i] <= width
"""

# Solution
from functools import lru_cache

def buildWall(width, height, brickTypes):
    MOD = 10**9 + 7

    # Generate all possible row configurations
    def generateRowConfigs(currentWidth, currentRow):
        if currentWidth == width:
            rowConfigs.append(tuple(currentRow))
            return
        if currentWidth > width:
            return
        for brick in brickTypes:
            generateRowConfigs(currentWidth + brick, currentRow + [currentWidth + brick])

    rowConfigs = []
    generateRowConfigs(0, [])

    # Precompute valid transitions between rows
    def isValidTransition(row1, row2):
        for cut in row1:
            if cut in row2:
                return False
        return True

    validTransitions = {row: [] for row in rowConfigs}
    for row1 in rowConfigs:
        for row2 in rowConfigs:
            if isValidTransition(row1, row2):
                validTransitions[row1].append(row2)

    # Use DP to count the number of ways to build the wall
    @lru_cache(None)
    def dp(currentHeight, previousRow):
        if currentHeight == height:
            return 1
        totalWays = 0
        for nextRow in validTransitions[previousRow]:
            totalWays += dp(currentHeight + 1, nextRow)
            totalWays %= MOD
        return totalWays

    # Start the DP process
    totalWays = 0
    for row in rowConfigs:
        totalWays += dp(1, row)
        totalWays %= MOD

    return totalWays

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    width = 5
    height = 2
    brickTypes = [1, 2, 3]
    print(buildWall(width, height, brickTypes))  # Expected Output: 4

    # Test Case 2
    width = 3
    height = 2
    brickTypes = [1, 2]
    print(buildWall(width, height, brickTypes))  # Expected Output: 2

    # Test Case 3
    width = 7
    height = 3
    brickTypes = [2, 3]
    print(buildWall(width, height, brickTypes))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Generating row configurations: O(2^width), as we recursively explore all possible combinations of bricks to fill the width.
   - Valid transitions computation: O(n^2), where n is the number of row configurations.
   - DP computation: O(height * n * m), where n is the number of row configurations and m is the average number of valid transitions per row.
   Overall: The complexity is dominated by the row configuration generation, making it approximately O(2^width).

2. Space Complexity:
   - Row configurations storage: O(n), where n is the number of row configurations.
   - DP cache: O(height * n).
   Overall: Space complexity is approximately O(height * n).

Topic: Dynamic Programming (DP)
"""