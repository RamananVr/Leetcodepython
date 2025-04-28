"""
LeetCode Problem #1989: Maximum Number of People That Can Be Caught in Tag

Problem Statement:
You are playing a game of tag with some people. The game is played on a straight line, and each person has a position on the line. 
You are given two arrays `players` and `catchers` where:
- `players[i]` is the position of the i-th player.
- `catchers[j]` is the position of the j-th catcher.

Each catcher can catch at most one player, and a player can only be caught if the distance between the player and the catcher is less than or equal to `max_distance`.

Return the maximum number of players that can be caught.

Constraints:
- 1 <= len(players), len(catchers) <= 10^4
- 0 <= players[i], catchers[j] <= 10^9
- 0 <= max_distance <= 10^9
"""

# Python Solution
def maxNumberOfPeopleCaught(players, catchers, max_distance):
    """
    Finds the maximum number of players that can be caught by catchers.

    :param players: List[int] - Positions of players.
    :param catchers: List[int] - Positions of catchers.
    :param max_distance: int - Maximum distance within which a player can be caught.
    :return: int - Maximum number of players that can be caught.
    """
    # Sort both players and catchers by their positions
    players.sort()
    catchers.sort()

    # Initialize pointers and count
    player_pointer = 0
    catcher_pointer = 0
    caught_count = 0

    # Use two pointers to match players and catchers
    while player_pointer < len(players) and catcher_pointer < len(catchers):
        if abs(players[player_pointer] - catchers[catcher_pointer]) <= max_distance:
            # Catcher catches the player
            caught_count += 1
            player_pointer += 1
            catcher_pointer += 1
        elif players[player_pointer] < catchers[catcher_pointer]:
            # Player is too far left, move to the next player
            player_pointer += 1
        else:
            # Catcher is too far left, move to the next catcher
            catcher_pointer += 1

    return caught_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    players = [1, 3, 5]
    catchers = [2, 6]
    max_distance = 2
    print(maxNumberOfPeopleCaught(players, catchers, max_distance))  # Output: 2

    # Test Case 2
    players = [1, 2, 3]
    catchers = [10, 11, 12]
    max_distance = 5
    print(maxNumberOfPeopleCaught(players, catchers, max_distance))  # Output: 0

    # Test Case 3
    players = [1, 4, 6, 8]
    catchers = [2, 5, 7]
    max_distance = 1
    print(maxNumberOfPeopleCaught(players, catchers, max_distance))  # Output: 3

    # Test Case 4
    players = [1, 2, 3, 4]
    catchers = [1, 2, 3, 4]
    max_distance = 0
    print(maxNumberOfPeopleCaught(players, catchers, max_distance))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `players` and `catchers` arrays takes O(n log n) and O(m log m), where n is the length of `players` and m is the length of `catchers`.
- The two-pointer traversal takes O(n + m).
- Overall time complexity: O(n log n + m log m).

Space Complexity:
- Sorting is done in-place, and the two-pointer approach uses constant extra space.
- Overall space complexity: O(1).
"""

# Topic: Two Pointers, Sorting