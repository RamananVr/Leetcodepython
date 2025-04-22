"""
LeetCode Problem #846: Hand of Straights

Problem Statement:
Alice has a hand of cards, given as an array of integers `hand`. Each integer represents a card in her hand. 
Alice wants to rearrange the cards into groups where each group has exactly `groupSize` consecutive cards.

Return `True` if Alice can rearrange the cards into such groups, or `False` otherwise.

Constraints:
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: True
Explanation: Alice's hand can be rearranged as [1,2,3], [2,3,4], [6,7,8].

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: False
Explanation: Alice's hand cannot be rearranged into groups of 4.

Follow-up:
- What if the input array is sorted? How would your solution change?
"""

from collections import Counter

def isNStraightHand(hand, groupSize):
    """
    Determines if the cards in `hand` can be rearranged into groups of `groupSize` consecutive cards.

    :param hand: List[int] - The cards in Alice's hand.
    :param groupSize: int - The size of each group.
    :return: bool - True if the cards can be rearranged into groups, False otherwise.
    """
    if len(hand) % groupSize != 0:
        return False

    card_count = Counter(hand)
    for card in sorted(card_count):
        if card_count[card] > 0:
            for i in range(groupSize):
                if card_count[card + i] < card_count[card]:
                    return False
                card_count[card + i] -= card_count[card]
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(isNStraightHand(hand, groupSize))  # Output: True

    # Test Case 2
    hand = [1, 2, 3, 4, 5]
    groupSize = 4
    print(isNStraightHand(hand, groupSize))  # Output: False

    # Test Case 3
    hand = [1, 2, 3, 4, 5, 6]
    groupSize = 2
    print(isNStraightHand(hand, groupSize))  # Output: True

    # Test Case 4
    hand = [8, 10, 12]
    groupSize = 3
    print(isNStraightHand(hand, groupSize))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `hand` takes O(n log n), where n is the length of the hand.
- Iterating through the sorted cards and processing each group takes O(n * groupSize) in the worst case.
- Overall time complexity: O(n log n + n * groupSize). Since groupSize is typically small, this simplifies to O(n log n).

Space Complexity:
- The `Counter` object stores the frequency of each card, which takes O(u) space, where u is the number of unique cards.
- Overall space complexity: O(u).

Topic: Hash Table, Sorting
"""