"""
LeetCode Problem #1688: Count of Matches in Tournament

Problem Statement:
You are given an integer `n`, the number of teams in a tournament that has the following rules:
1. If the number of teams is even, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.
2. If the number of teams is odd, one team randomly advances to the next round, and the rest are paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round.

Return the total number of matches played in the tournament until a winner is decided.

Constraints:
- `1 <= n <= 200`

Example:
Input: n = 7
Output: 6
Explanation:
- Round 1: Teams = 7, Matches = 3, Teams Remaining = 4
- Round 2: Teams = 4, Matches = 2, Teams Remaining = 2
- Round 3: Teams = 2, Matches = 1, Teams Remaining = 1
- Total Matches = 3 + 2 + 1 = 6
"""

def numberOfMatches(n: int) -> int:
    """
    Calculate the total number of matches played in a tournament.

    :param n: int - The number of teams in the tournament.
    :return: int - The total number of matches played.
    """
    matches = 0
    while n > 1:
        if n % 2 == 0:
            matches += n // 2
            n //= 2
        else:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
    return matches

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 7
    print(f"Input: n = {n1}, Output: {numberOfMatches(n1)}")  # Expected Output: 6

    # Test Case 2
    n2 = 14
    print(f"Input: n = {n2}, Output: {numberOfMatches(n2)}")  # Expected Output: 13

    # Test Case 3
    n3 = 1
    print(f"Input: n = {n3}, Output: {numberOfMatches(n3)}")  # Expected Output: 0

    # Test Case 4
    n4 = 8
    print(f"Input: n = {n4}, Output: {numberOfMatches(n4)}")  # Expected Output: 7

    # Test Case 5
    n5 = 3
    print(f"Input: n = {n5}, Output: {numberOfMatches(n5)}")  # Expected Output: 2

"""
Time Complexity Analysis:
- The number of iterations in the while loop is proportional to the number of rounds in the tournament.
- In each round, the number of teams is approximately halved.
- Therefore, the time complexity is O(log n), where n is the initial number of teams.

Space Complexity Analysis:
- The algorithm uses a constant amount of space, as no additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Simulation
"""