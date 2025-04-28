"""
LeetCode Problem #1244: Design A Leaderboard

Problem Statement:
Design a Leaderboard class, which has the following functions:
1. `addScore(playerId: int, score: int) -> None`: Update the leaderboard by adding `score` to the given player's score. If the player does not exist in the leaderboard, add them with the given `score`.
2. `top(K: int) -> int`: Return the sum of the scores of the top `K` players.
3. `reset(playerId: int) -> None`: Reset the score of the player with the given `playerId` to 0. It is guaranteed that the player was added to the leaderboard before calling this function.

Constraints:
- 1 <= playerId, K <= 10000
- It's guaranteed that `K` is less than or equal to the total number of players in the leaderboard.
- The number of calls to `addScore`, `top`, and `reset` functions will not exceed 1000.

"""

from collections import defaultdict
import heapq

class Leaderboard:
    def __init__(self):
        # Dictionary to store player scores
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        """
        Add the given score to the player's total score.
        If the player does not exist, initialize their score.
        """
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        """
        Return the sum of the top K scores.
        """
        # Use a min-heap to efficiently find the top K scores
        return sum(heapq.nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        """
        Reset the score of the given player to 0.
        """
        if playerId in self.scores:
            self.scores[playerId] = 0


# Example Test Cases
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Test Case 1
    leaderboard.addScore(1, 73)  # Player 1's score is now 73
    leaderboard.addScore(2, 56)  # Player 2's score is now 56
    leaderboard.addScore(3, 39)  # Player 3's score is now 39
    leaderboard.addScore(4, 51)  # Player 4's score is now 51
    leaderboard.addScore(5, 4)   # Player 5's score is now 4
    print(leaderboard.top(1))    # Top 1 score: 73 (Player 1) -> Output: 73
    print(leaderboard.top(3))    # Top 3 scores: 73, 56, 51 -> Output: 180
    leaderboard.reset(1)         # Reset Player 1's score to 0
    print(leaderboard.top(3))    # Top 3 scores: 56, 51, 39 -> Output: 146
    leaderboard.addScore(2, 45)  # Player 2's score is now 101
    print(leaderboard.top(2))    # Top 2 scores: 101, 51 -> Output: 152


"""
Time and Space Complexity Analysis:

1. `addScore(playerId, score)`:
   - Time Complexity: O(1), as updating a dictionary value is O(1).
   - Space Complexity: O(1) for each new player added.

2. `top(K)`:
   - Time Complexity: O(N log K), where N is the number of players. The `heapq.nlargest` function maintains a heap of size K while iterating through all scores.
   - Space Complexity: O(K), as the heap stores the top K scores.

3. `reset(playerId)`:
   - Time Complexity: O(1), as resetting a dictionary value is O(1).
   - Space Complexity: O(1).

Overall:
- Time Complexity: O(N log K) for `top(K)` (most expensive operation).
- Space Complexity: O(N), where N is the number of players stored in the dictionary.

Topic: Hash Table, Heap (Priority Queue), Design
"""