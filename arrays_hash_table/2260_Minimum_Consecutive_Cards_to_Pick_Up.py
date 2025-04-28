"""
LeetCode Problem #2260: Minimum Consecutive Cards to Pick Up

Problem Statement:
You are given an integer array `cards` where `cards[i]` represents the value of the ith card. A pair of cards are considered matching if they have the same value. 
Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
If it is impossible to have matching cards, return -1.

Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the subarray [3,4,2,3] (4 cards) to have a pair of matching cards.

Example 2:
Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a subarray with matching cards.

Constraints:
- 1 <= cards.length <= 10^5
- 0 <= cards[i] <= 10^6
"""

# Python Solution
def minimumCardPickup(cards):
    """
    Finds the minimum number of consecutive cards to pick up to have a pair of matching cards.

    :param cards: List[int] - List of integers representing card values.
    :return: int - Minimum number of consecutive cards to pick up, or -1 if no matching cards exist.
    """
    last_seen = {}
    min_length = float('inf')

    for i, card in enumerate(cards):
        if card in last_seen:
            min_length = min(min_length, i - last_seen[card] + 1)
        last_seen[card] = i

    return min_length if min_length != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cards1 = [3, 4, 2, 3, 4, 7]
    print(minimumCardPickup(cards1))  # Output: 4

    # Test Case 2
    cards2 = [1, 0, 5, 3]
    print(minimumCardPickup(cards2))  # Output: -1

    # Test Case 3
    cards3 = [1, 2, 3, 4, 5, 6, 1]
    print(minimumCardPickup(cards3))  # Output: 7

    # Test Case 4
    cards4 = [1, 1]
    print(minimumCardPickup(cards4))  # Output: 2

    # Test Case 5
    cards5 = [1]
    print(minimumCardPickup(cards5))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `cards` array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `cards` array.

Space Complexity:
- The algorithm uses a dictionary (`last_seen`) to store the last seen index of each card value.
- In the worst case, the dictionary could store up to n unique card values, where n is the length of the `cards` array.
- Therefore, the space complexity is O(n).

Topic: Arrays, Hash Table
"""