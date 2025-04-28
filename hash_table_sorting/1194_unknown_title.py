"""
LeetCode Problem #1194: Tournament Winners

Problem Statement:
In a tournament, there are `n` players numbered from `1` to `n`. Each player competes in a series of matches, and the results are recorded in a list of tuples `matches`. Each tuple `(winner, loser)` indicates that the player `winner` defeated the player `loser` in a match.

A player is considered a "tournament winner" if they have not lost any matches. A player is considered a "runner-up" if they have lost exactly one match.

Write a function `findWinners(matches)` that takes the list of matches and returns two lists:
1. A list of all tournament winners sorted in ascending order.
2. A list of all runners-up sorted in ascending order.

Constraints:
- `1 <= matches.length <= 10^5`
- `1 <= winner, loser <= 10^5`
- All matches are unique.

Example:
Input: matches = [[1, 2], [2, 3], [4, 5], [6, 4], [2, 6]]
Output: [[1, 5], [4, 6]]

Explanation:
- Player 1 has not lost any matches, so they are a tournament winner.
- Player 5 has not lost any matches, so they are a tournament winner.
- Player 4 has lost exactly one match, so they are a runner-up.
- Player 6 has lost exactly one match, so they are a runner-up.
"""

from collections import defaultdict

def findWinners(matches):
    """
    Function to find tournament winners and runners-up.
    
    :param matches: List[List[int]] - List of matches where each match is [winner, loser].
    :return: List[List[int]] - Two lists: [winners, runners_up].
    """
    # Dictionary to count losses for each player
    loss_count = defaultdict(int)
    
    # Set to track all players who have participated
    players = set()
    
    # Process each match
    for winner, loser in matches:
        players.add(winner)
        players.add(loser)
        loss_count[loser] += 1
    
    # Winners: Players with 0 losses
    winners = [player for player in players if loss_count[player] == 0]
    
    # Runners-up: Players with exactly 1 loss
    runners_up = [player for player in players if loss_count[player] == 1]
    
    # Sort the results
    winners.sort()
    runners_up.sort()
    
    return [winners, runners_up]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matches = [[1, 2], [2, 3], [4, 5], [6, 4], [2, 6]]
    print(findWinners(matches))  # Output: [[1, 5], [4, 6]]
    
    # Test Case 2
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5]]
    print(findWinners(matches))  # Output: [[1, 2, 4], [7]]
    
    # Test Case 3
    matches = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(findWinners(matches))  # Output: [[1], [2]]

# Time Complexity Analysis:
# - Processing the matches takes O(m), where m is the number of matches.
# - Constructing the winners and runners-up lists takes O(n), where n is the number of unique players.
# - Sorting the winners and runners-up lists takes O(n log n).
# Overall time complexity: O(m + n log n).

# Space Complexity Analysis:
# - The `loss_count` dictionary stores at most n entries, where n is the number of unique players.
# - The `players` set stores at most n entries.
# Overall space complexity: O(n).

# Topic: Hash Table, Sorting