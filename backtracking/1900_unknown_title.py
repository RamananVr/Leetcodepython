"""
LeetCode Problem #1900: The Earliest and Latest Rounds Where Players Compete

Problem Statement:
There are n players numbered from 1 to n, and they are competing in a tournament. Every round, the players are paired up, and each pair competes such that one player wins and the other loses. If the number of players is odd, one player randomly advances to the next round without competing. This continues until there is only one player remaining.

A player seeded x and a player seeded y are said to compete in a round if they are paired up in that round. The earliest round in which they compete is the smallest round number where this happens, and the latest round is the largest round number where this happens.

Given the integers n, firstPlayer, and secondPlayer, return a list of two integers [earliest, latest] representing the earliest and latest rounds in which players firstPlayer and secondPlayer compete.

Constraints:
- 2 <= n <= 29
- 1 <= firstPlayer < secondPlayer <= n
"""

from typing import List

def earliestAndLatest(n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
    def dfs(players, round_num):
        # If firstPlayer and secondPlayer are in the same pair, return the round number
        if firstPlayer in players and secondPlayer in players:
            idx1, idx2 = players.index(firstPlayer), players.index(secondPlayer)
            if abs(idx1 - idx2) == 1 and min(idx1, idx2) % 2 == 0:
                return round_num, round_num

        # Generate all possible outcomes for the next round
        next_rounds = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                next_rounds.append((players[i], players[i + 1]))
            else:
                next_rounds.append((players[i],))

        # Simulate all combinations of winners
        min_earliest, max_latest = float('inf'), float('-inf')
        for winners in product(*next_rounds):
            winners = sorted(winners)
            earliest, latest = dfs(winners, round_num + 1)
            min_earliest = min(min_earliest, earliest)
            max_latest = max(max_latest, latest)

        return min_earliest, max_latest

    from itertools import product
    players = list(range(1, n + 1))
    return list(dfs(players, 1))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 11
    firstPlayer = 2
    secondPlayer = 4
    print(earliestAndLatest(n, firstPlayer, secondPlayer))  # Output: [3, 4]

    # Test Case 2
    n = 5
    firstPlayer = 1
    secondPlayer = 5
    print(earliestAndLatest(n, firstPlayer, secondPlayer))  # Output: [1, 1]

    # Test Case 3
    n = 8
    firstPlayer = 4
    secondPlayer = 7
    print(earliestAndLatest(n, firstPlayer, secondPlayer))  # Output: [2, 3]


"""
Time Complexity:
- The time complexity is O(2^n) in the worst case due to the recursive exploration of all possible outcomes for each round.

Space Complexity:
- The space complexity is O(n) due to the recursion stack and the storage of players in each round.

Topic: Backtracking
"""