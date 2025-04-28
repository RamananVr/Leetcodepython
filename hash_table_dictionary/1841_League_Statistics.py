"""
LeetCode Problem #1841: League Statistics

Problem Statement:
You are given a list of matches where each match is represented as a tuple (team1, team2, score1, score2). 
- `team1` and `team2` are the names of the two teams that played the match.
- `score1` and `score2` are the scores of `team1` and `team2` respectively.

Your task is to calculate the following statistics for each team:
1. Total matches played.
2. Total wins (a team wins if its score is strictly greater than the opponent's score).
3. Total losses (a team loses if its score is strictly less than the opponent's score).
4. Total draws (a match is a draw if both teams have the same score).
5. Total points (a team earns 3 points for a win, 1 point for a draw, and 0 points for a loss).

Return the statistics as a dictionary where the keys are the team names and the values are dictionaries with the following keys:
- "matches": Total matches played.
- "wins": Total wins.
- "losses": Total losses.
- "draws": Total draws.
- "points": Total points.

Example:
Input: matches = [("A", "B", 3, 1), ("A", "C", 2, 2), ("B", "C", 0, 1)]
Output: {
    "A": {"matches": 2, "wins": 1, "losses": 0, "draws": 1, "points": 4},
    "B": {"matches": 2, "wins": 0, "losses": 2, "draws": 0, "points": 0},
    "C": {"matches": 2, "wins": 1, "losses": 0, "draws": 1, "points": 4}
}

Constraints:
- 1 <= len(matches) <= 10^4
- Each team name is a string of length 1 to 10.
- 0 <= score1, score2 <= 100
"""

from collections import defaultdict

def calculate_league_statistics(matches):
    # Initialize a dictionary to store statistics for each team
    stats = defaultdict(lambda: {"matches": 0, "wins": 0, "losses": 0, "draws": 0, "points": 0})
    
    # Process each match
    for team1, team2, score1, score2 in matches:
        # Update matches played
        stats[team1]["matches"] += 1
        stats[team2]["matches"] += 1
        
        if score1 > score2:  # Team1 wins
            stats[team1]["wins"] += 1
            stats[team2]["losses"] += 1
            stats[team1]["points"] += 3
        elif score1 < score2:  # Team2 wins
            stats[team2]["wins"] += 1
            stats[team1]["losses"] += 1
            stats[team2]["points"] += 3
        else:  # Draw
            stats[team1]["draws"] += 1
            stats[team2]["draws"] += 1
            stats[team1]["points"] += 1
            stats[team2]["points"] += 1
    
    # Convert defaultdict to a regular dictionary for the final output
    return dict(stats)

# Example Test Cases
if __name__ == "__main__":
    matches = [
        ("A", "B", 3, 1),
        ("A", "C", 2, 2),
        ("B", "C", 0, 1)
    ]
    print(calculate_league_statistics(matches))
    # Expected Output:
    # {
    #     "A": {"matches": 2, "wins": 1, "losses": 0, "draws": 1, "points": 4},
    #     "B": {"matches": 2, "wins": 0, "losses": 2, "draws": 0, "points": 0},
    #     "C": {"matches": 2, "wins": 1, "losses": 0, "draws": 1, "points": 4}
    # }

    matches = [
        ("X", "Y", 0, 0),
        ("X", "Z", 1, 2),
        ("Y", "Z", 3, 3)
    ]
    print(calculate_league_statistics(matches))
    # Expected Output:
    # {
    #     "X": {"matches": 2, "wins": 0, "losses": 1, "draws": 1, "points": 1},
    #     "Y": {"matches": 2, "wins": 0, "losses": 0, "draws": 2, "points": 2},
    #     "Z": {"matches": 2, "wins": 1, "losses": 0, "draws": 1, "points": 4}
    # }

# Time Complexity Analysis:
# - Processing each match takes O(1) time.
# - For `n` matches, the total time complexity is O(n).

# Space Complexity Analysis:
# - The space required for the `stats` dictionary depends on the number of unique teams.
# - In the worst case, if all teams are unique, the space complexity is O(t), where `t` is the number of unique teams.

# Topic: Hash Table / Dictionary