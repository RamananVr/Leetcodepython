"""
LeetCode Question #877: Stone Game

Problem Statement:
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, 
and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to determine if Alice can win. Alice and Bob take turns, with Alice starting first. 
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row. 
This continues until there are no more piles left, and the player with the most stones wins.

Assume both players play optimally.

Return `True` if Alice wins the game, otherwise return `False`.

Constraints:
- 2 <= piles.length <= 500
- piles.length is even.
- 1 <= piles[i] <= 500
- sum(piles) is odd.

"""

# Solution
def stoneGame(piles):
    """
    Determines if Alice can win the stone game given the piles of stones.

    :param piles: List[int] - List of integers representing the piles of stones.
    :return: bool - True if Alice can win, False otherwise.
    """
    # Since the total number of stones is odd and both players play optimally,
    # Alice can always win by choosing the best strategy.
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles1 = [5, 3, 4, 5]
    print(stoneGame(piles1))  # Expected Output: True

    # Test Case 2
    piles2 = [3, 7, 2, 3]
    print(stoneGame(piles2))  # Expected Output: True

    # Test Case 3
    piles3 = [1, 100, 3, 2]
    print(stoneGame(piles3))  # Expected Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution provided here is O(1) because it directly returns `True` without performing any calculations.

Space Complexity:
- The space complexity is O(1) since no additional data structures are used.

Explanation:
The problem guarantees that Alice can always win if both players play optimally. This is because the number of piles is even, 
and Alice can always control the game to ensure she gets the maximum stones. Therefore, the solution is constant time and space.

Topic: Game Theory
"""