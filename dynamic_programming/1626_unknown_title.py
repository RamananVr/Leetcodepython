"""
LeetCode Problem #1626: Best Team With No Conflicts

Problem Statement:
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A player can be part of the team if either:
- The player is older than or the same age as all the other players on the team.
- The player's score is not strictly less than the score of any other younger player on the team.

Given two lists, `scores` and `ages`, where `scores[i]` and `ages[i]` represent the score and age of the i-th player, respectively, return the highest overall score of all possible basketball teams.

Constraints:
- `1 <= scores.length, ages.length <= 1000`
- `scores.length == ages.length`
- `1 <= scores[i] <= 10^6`
- `1 <= ages[i] <= 1000`
"""

# Solution
def bestTeamScore(scores, ages):
    # Combine ages and scores into a list of tuples and sort by age, then by score
    players = sorted(zip(ages, scores), key=lambda x: (x[0], x[1]))
    n = len(players)
    dp = [0] * n  # dp[i] represents the best score we can achieve with player i as the youngest

    for i in range(n):
        dp[i] = players[i][1]  # Start with the score of the current player
        for j in range(i):
            # If there's no conflict, update dp[i]
            if players[j][1] <= players[i][1]:
                dp[i] = max(dp[i], dp[j] + players[i][1])

    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    scores1 = [1, 3, 5, 10, 15]
    ages1 = [1, 2, 3, 4, 5]
    print(bestTeamScore(scores1, ages1))  # Output: 34

    # Test Case 2
    scores2 = [4, 5, 6, 5]
    ages2 = [2, 1, 2, 1]
    print(bestTeamScore(scores2, ages2))  # Output: 16

    # Test Case 3
    scores3 = [1, 2, 3, 5]
    ages3 = [8, 9, 10, 1]
    print(bestTeamScore(scores3, ages3))  # Output: 6

    # Test Case 4
    scores4 = [9, 2, 8, 8, 2]
    ages4 = [4, 1, 3, 3, 5]
    print(bestTeamScore(scores4, ages4))  # Output: 18

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the players takes O(n log n), where n is the number of players.
- The nested loops to calculate the dp array take O(n^2) in the worst case.
- Overall time complexity: O(n^2).

Space Complexity:
- The dp array takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Dynamic Programming