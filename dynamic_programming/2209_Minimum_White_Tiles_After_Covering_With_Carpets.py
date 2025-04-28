"""
LeetCode Problem #2209: Minimum White Tiles After Covering With Carpets

Problem Statement:
You are given a binary string `floor`, which represents the floor of a room. The character '0' represents a black tile, and the character '1' represents a white tile. You are also given the integers `numCarpets` and `carpetLen`, which represent the number of carpets you have and the length of each carpet.

You can place the carpets on the floor to cover white tiles ('1'). Carpets can overlap, and you can place them anywhere on the floor.

Return the minimum number of white tiles that are not covered by carpets.

Constraints:
- `1 <= floor.length <= 1000`
- `floor[i]` is either '0' or '1'.
- `1 <= numCarpets <= 1000`
- `1 <= carpetLen <= floor.length`
"""

# Solution
def minimumWhiteTiles(floor: str, numCarpets: int, carpetLen: int) -> int:
    n = len(floor)
    # Precompute prefix sums for the number of white tiles
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (1 if floor[i] == '1' else 0)
    
    # DP table: dp[i][j] represents the minimum number of white tiles left uncovered
    # when considering the first i tiles and using j carpets.
    dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(numCarpets + 1):
            # Case 1: Don't use a carpet at position i
            dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
            
            # Case 2: Use a carpet at position i (if we have carpets left)
            if j > 0:
                start = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[start][j - 1])
    
    return dp[n][numCarpets]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    floor = "10110101"
    numCarpets = 2
    carpetLen = 2
    print(minimumWhiteTiles(floor, numCarpets, carpetLen))  # Expected Output: 2

    # Test Case 2
    floor = "11111"
    numCarpets = 1
    carpetLen = 3
    print(minimumWhiteTiles(floor, numCarpets, carpetLen))  # Expected Output: 2

    # Test Case 3
    floor = "00000"
    numCarpets = 2
    carpetLen = 3
    print(minimumWhiteTiles(floor, numCarpets, carpetLen))  # Expected Output: 0

    # Test Case 4
    floor = "111111"
    numCarpets = 3
    carpetLen = 2
    print(minimumWhiteTiles(floor, numCarpets, carpetLen))  # Expected Output: 0

# Time and Space Complexity Analysis
# Time Complexity:
# - The outer loop runs for `n` iterations (length of the floor).
# - The inner loop runs for `numCarpets + 1` iterations.
# - Each iteration involves constant-time operations.
# - Total time complexity: O(n * numCarpets).

# Space Complexity:
# - The DP table requires O(n * numCarpets) space.
# - The prefix_sum array requires O(n) space.
# - Total space complexity: O(n * numCarpets).

# Topic: Dynamic Programming