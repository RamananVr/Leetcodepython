"""
LeetCode Problem #920: Number of Music Playlists

Problem Statement:
Your music player contains `n` different songs. You want to listen to `goal` songs (not necessarily different) during your trip. 
To avoid boredom, you will create a playlist so that:
1. Every song is played at least once.
2. A song can only be played again only if `k` other songs have been played.

Given `n`, `goal`, and `k`, return the number of possible playlists that you can create. 
Since the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 0 <= k < n <= goal <= 100
- The input values are integers.
"""

# Solution
def numMusicPlaylists(n: int, goal: int, k: int) -> int:
    MOD = 10**9 + 7

    # dp[i][j] represents the number of playlists of length i with exactly j unique songs
    dp = [[0] * (n + 1) for _ in range(goal + 1)]
    dp[0][0] = 1  # Base case: 0 songs in the playlist with 0 unique songs

    for i in range(1, goal + 1):
        for j in range(1, n + 1):
            # Case 1: Add a new unique song
            dp[i][j] += dp[i - 1][j - 1] * (n - (j - 1))
            dp[i][j] %= MOD

            # Case 2: Replay an existing song (only if there are at least k other songs)
            if j > k:
                dp[i][j] += dp[i - 1][j] * (j - k)
                dp[i][j] %= MOD

    return dp[goal][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, goal1, k1 = 3, 3, 1
    print(numMusicPlaylists(n1, goal1, k1))  # Expected Output: 6

    # Test Case 2
    n2, goal2, k2 = 2, 3, 0
    print(numMusicPlaylists(n2, goal2, k2))  # Expected Output: 6

    # Test Case 3
    n3, goal3, k3 = 2, 3, 1
    print(numMusicPlaylists(n3, goal3, k3))  # Expected Output: 2

    # Test Case 4
    n4, goal4, k4 = 4, 4, 2
    print(numMusicPlaylists(n4, goal4, k4))  # Expected Output: 24

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a nested loop to fill a DP table of size (goal + 1) x (n + 1).
- Therefore, the time complexity is O(goal * n).

Space Complexity:
- The space complexity is O(goal * n) due to the DP table.

Topic: Dynamic Programming (DP)
"""