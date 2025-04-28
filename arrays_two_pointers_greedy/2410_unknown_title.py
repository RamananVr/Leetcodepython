"""
LeetCode Problem #2410: Maximum Matching of Players With Trainers

Problem Statement:
You are given two integer arrays, `players` and `trainers`, where:
- `players[i]` is the skill level of the i-th player, and
- `trainers[j]` is the skill level of the j-th trainer.

Each player can be matched with at most one trainer, and each trainer can be matched with at most one player. A player can be matched with a trainer only if the player's skill level is less than or equal to the trainer's skill level.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

Constraints:
- 1 <= players.length, trainers.length <= 10^5
- 1 <= players[i], trainers[j] <= 10^9
"""

# Python Solution
def matchPlayersAndTrainers(players, trainers):
    """
    Finds the maximum number of matchings between players and trainers.

    :param players: List[int] - Skill levels of players
    :param trainers: List[int] - Skill levels of trainers
    :return: int - Maximum number of matchings
    """
    # Sort both players and trainers to facilitate greedy matching
    players.sort()
    trainers.sort()

    i, j = 0, 0
    matches = 0

    # Use two pointers to find the maximum number of matches
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            # Match player i with trainer j
            matches += 1
            i += 1
            j += 1
        else:
            # Trainer j cannot match player i, move to the next trainer
            j += 1

    return matches

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    players = [4, 7, 9]
    trainers = [8, 2, 5, 8]
    print(matchPlayersAndTrainers(players, trainers))  # Output: 2

    # Test Case 2
    players = [1, 1, 1]
    trainers = [10]
    print(matchPlayersAndTrainers(players, trainers))  # Output: 1

    # Test Case 3
    players = [10, 20, 30]
    trainers = [5, 15, 25, 35]
    print(matchPlayersAndTrainers(players, trainers))  # Output: 3

    # Test Case 4
    players = [5, 5, 5]
    trainers = [5, 5, 5]
    print(matchPlayersAndTrainers(players, trainers))  # Output: 3

    # Test Case 5
    players = [1, 2, 3]
    trainers = [4, 5, 6]
    print(matchPlayersAndTrainers(players, trainers))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `players` array takes O(n log n), where n is the length of the `players` array.
- Sorting the `trainers` array takes O(m log m), where m is the length of the `trainers` array.
- The two-pointer traversal takes O(n + m), where n and m are the lengths of the `players` and `trainers` arrays, respectively.
- Overall time complexity: O(n log n + m log m).

Space Complexity:
- Sorting requires O(n) and O(m) space for the `players` and `trainers` arrays, respectively, in the worst case.
- The algorithm uses constant extra space for the two pointers and counters.
- Overall space complexity: O(1) additional space (in-place sorting is assumed).
"""

# Topic: Arrays, Two Pointers, Greedy