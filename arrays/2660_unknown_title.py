"""
LeetCode Problem #2660: Determine the Winner of a Bowling Game

Problem Statement:
You are given two integer arrays `player1` and `player2`, where `player1[i]` and `player2[i]` represent the number of pins 
knocked down by Player 1 and Player 2 in the ith round, respectively. The game consists of `n` rounds, and the players 
compete to determine the winner.

The scoring rules are as follows:
1. If a player knocks down 10 pins in a round, they receive a bonus. The bonus is that the number of pins they knock down 
   in the next two rounds is added to their score.
2. If a player knocks down 10 pins in two consecutive rounds, the bonus is applied for both rounds.

The winner is the player with the higher total score after all rounds. If both players have the same score, the result is a tie.

Return:
- 1 if Player 1 wins,
- 2 if Player 2 wins,
- 0 if the game is a tie.

Constraints:
- `n == len(player1) == len(player2)`
- 1 <= n <= 1000
- 0 <= player1[i], player2[i] <= 10
"""

def is_winner(player1, player2):
    """
    Determine the winner of the bowling game based on the scoring rules.

    Args:
    player1 (List[int]): Scores of Player 1 in each round.
    player2 (List[int]): Scores of Player 2 in each round.

    Returns:
    int: 1 if Player 1 wins, 2 if Player 2 wins, 0 if it's a tie.
    """
    def calculate_score(scores):
        n = len(scores)
        total_score = 0
        for i in range(n):
            total_score += scores[i]
            # Check for bonus from the previous round
            if i > 0 and scores[i - 1] == 10:
                total_score += scores[i]
            # Check for bonus from two rounds ago
            if i > 1 and scores[i - 2] == 10:
                total_score += scores[i]
        return total_score

    # Calculate scores for both players
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)

    # Determine the winner
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Player 1 wins
    player1 = [10, 2, 3]
    player2 = [5, 5, 5]
    print(is_winner(player1, player2))  # Output: 1

    # Test Case 2: Player 2 wins
    player1 = [5, 5, 5]
    player2 = [10, 2, 3]
    print(is_winner(player1, player2))  # Output: 2

    # Test Case 3: Tie
    player1 = [10, 2, 3]
    player2 = [10, 2, 3]
    print(is_winner(player1, player2))  # Output: 0

    # Test Case 4: Player 1 wins with consecutive bonuses
    player1 = [10, 10, 5]
    player2 = [5, 5, 5]
    print(is_winner(player1, player2))  # Output: 1

    # Test Case 5: Player 2 wins with consecutive bonuses
    player1 = [5, 5, 5]
    player2 = [10, 10, 5]
    print(is_winner(player1, player2))  # Output: 2

"""
Time Complexity:
- The function `calculate_score` iterates through the scores array once, making it O(n) for each player.
- Since we calculate scores for both players, the overall time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""