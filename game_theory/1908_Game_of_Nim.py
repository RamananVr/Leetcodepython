"""
LeetCode Problem #1908: Game of Nim

Problem Statement:
Alice and Bob take turns playing a game with Alice starting first. In this game, there are n piles of stones. 
Each pile consists of a positive number of stones. The players can remove any number of stones from a single pile 
(but at least one stone must be removed). The player who cannot make a move loses the game.

Given an integer array `piles` where `piles[i]` is the number of stones in the ith pile, return `true` if Alice wins 
the game assuming both players play optimally, otherwise return `false`.

Constraints:
- 1 <= piles.length <= 10^4
- 1 <= piles[i] <= 10^6
"""

def nimGame(piles):
    """
    Determines if Alice wins the game of Nim given the initial piles of stones.

    :param piles: List[int] - List of integers representing the number of stones in each pile.
    :return: bool - True if Alice wins, False otherwise.
    """
    # Calculate the XOR of all pile sizes
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    
    # Alice wins if the XOR sum is non-zero
    return xor_sum != 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Alice wins
    piles1 = [3, 4, 5]
    print(nimGame(piles1))  # Expected output: True

    # Test Case 2: Bob wins
    piles2 = [1, 1, 1]
    print(nimGame(piles2))  # Expected output: False

    # Test Case 3: Alice wins
    piles3 = [7]
    print(nimGame(piles3))  # Expected output: True

    # Test Case 4: Bob wins
    piles4 = [2, 2]
    print(nimGame(piles4))  # Expected output: False

    # Test Case 5: Alice wins
    piles5 = [1, 2, 3]
    print(nimGame(piles5))  # Expected output: True

"""
Time Complexity Analysis:
- Calculating the XOR of all pile sizes takes O(n) time, where n is the number of piles.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (for the `xor_sum` variable).
- Therefore, the space complexity is O(1).

Topic: Game Theory
"""