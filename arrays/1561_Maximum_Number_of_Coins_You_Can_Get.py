"""
LeetCode Problem #1561: Maximum Number of Coins You Can Get

Problem Statement:
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
- In each step, you will choose any 3 piles of coins (not necessarily consecutive).
- Of your choice, Alice will pick the pile with the maximum number of coins.
- You will pick the next pile with the maximum number of coins.
- Bob will pick the last pile.
- Repeat until there are no more piles of coins.

Given an array of integers `piles` where `piles[i]` is the number of coins in the ith pile, return the maximum number of coins you can get.

Constraints:
- `3 <= piles.length <= 10^5`
- `piles.length % 3 == 0`
- `1 <= piles[i] <= 10^4`
"""

# Solution
def maxCoins(piles):
    """
    Calculate the maximum number of coins you can get.

    :param piles: List[int] - List of integers representing the piles of coins.
    :return: int - Maximum number of coins you can get.
    """
    # Sort the piles in descending order
    piles.sort(reverse=True)
    
    # Initialize the total coins you can collect
    max_coins = 0
    
    # Iterate through the piles, skipping every third pile (Bob's choice)
    # Start from the second pile (your choice) and skip every two piles
    for i in range(1, len(piles), 2):
        max_coins += piles[i]
        # Stop when you've taken n piles (since there are 3n piles total)
        if i // 2 == len(piles) // 3 - 1:
            break
    
    return max_coins

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles1 = [2, 4, 1, 2, 7, 8]
    print(maxCoins(piles1))  # Expected Output: 9

    # Test Case 2
    piles2 = [2, 4, 5]
    print(maxCoins(piles2))  # Expected Output: 4

    # Test Case 3
    piles3 = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    print(maxCoins(piles3))  # Expected Output: 18

    # Test Case 4
    piles4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(maxCoins(piles4))  # Expected Output: 27

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the `piles` array.
- Iterating through the array to calculate the maximum coins takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so no additional space is used apart from the input array.
- Overall space complexity: O(1).
"""

# Topic: Arrays