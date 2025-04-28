"""
LeetCode Problem #2225: Find Players With Zero or One Losses

Problem Statement:
You are given an integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return a list `answer` of size 2 where:
- `answer[0]` is a list of all players who have not lost any matches.
- `answer[1]` is a list of all players who have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:
- You should only consider players that have played at least one match.
- The test cases are generated such that no two matches have the same outcome.

Constraints:
- 1 <= matches.length <= 10^5
- matches[i].length == 2
- 1 <= winner_i, loser_i <= 10^5
- winner_i != loser_i
"""

from collections import defaultdict

def findWinners(matches):
    """
    Function to find players with zero or one losses.

    Args:
    matches (List[List[int]]): A list of matches where each match is represented as [winner, loser].

    Returns:
    List[List[int]]: A list containing two lists:
                     - Players with zero losses.
                     - Players with exactly one loss.
    """
    # Dictionary to count losses for each player
    loss_count = defaultdict(int)

    # Process each match
    for winner, loser in matches:
        # Increment loss count for the loser
        loss_count[loser] += 1
        # Ensure the winner is in the dictionary with 0 losses
        if winner not in loss_count:
            loss_count[winner] = 0

    # Separate players based on their loss counts
    zero_losses = [player for player, losses in loss_count.items() if losses == 0]
    one_loss = [player for player, losses in loss_count.items() if losses == 1]

    # Return the results sorted in increasing order
    return [sorted(zero_losses), sorted(one_loss)]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matches1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    print(findWinners(matches1))
    # Expected Output: [[1, 2, 10], [4, 5, 7, 8]]

    # Test Case 2
    matches2 = [[2, 3], [1, 3], [5, 4], [6, 4]]
    print(findWinners(matches2))
    # Expected Output: [[1, 2, 5, 6], []]

    # Test Case 3
    matches3 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    print(findWinners(matches3))
    # Expected Output: [[1], [2]]

    # Test Case 4
    matches4 = [[1, 2], [2, 1]]
    print(findWinners(matches4))
    # Expected Output: [[], []]


"""
Time and Space Complexity Analysis:

Time Complexity:
- Processing each match takes O(1) time, and there are `n` matches, so processing all matches takes O(n).
- Sorting the players with zero and one losses takes O(k log k) and O(m log m), where `k` and `m` are the sizes of the respective lists.
- In the worst case, `k + m` is at most the number of unique players, which is bounded by `2n` (since each match involves two players).
- Thus, the overall time complexity is O(n + k log k + m log m), which simplifies to O(n log n) in the worst case.

Space Complexity:
- The `loss_count` dictionary stores at most `2n` entries (one for each unique player), so the space complexity is O(n).
- The output lists also require O(k + m) space, which is bounded by O(n).
- Thus, the overall space complexity is O(n).

Topic: Hash Table
"""