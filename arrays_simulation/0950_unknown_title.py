"""
LeetCode Problem #950: Reveal Cards In Increasing Order

Problem Statement:
You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. 
The integer on the card represents its value. You can order the deck in any order you want. Initially, 
all the cards are face down (unrevealed) in a pile.

You will do the following steps repeatedly until all cards are revealed:
1. Take the top card of the deck, reveal it, and remove it from the pile.
2. If there are still cards in the pile, put the next top card of the deck at the bottom of the deck.

If you order the deck optimally, the sequence of revealed cards will be in increasing order.

Return an ordering of the deck that would reveal the cards in increasing order.

Note:
- The order of the deck is unique.
- The input deck is guaranteed to have unique integers.

Example 1:
Input: deck = [17, 13, 11, 2, 3, 5, 7]
Output: [2, 13, 3, 11, 5, 17, 7]
Explanation: 
We get the deck in the order [2, 13, 3, 11, 5, 17, 7] and reveal the cards in this order:
1. Reveal 2, put 13 at the bottom.
2. Reveal 3, put 11 at the bottom.
3. Reveal 5, put 17 at the bottom.
4. Reveal 7.

Example 2:
Input: deck = [1, 1000]
Output: [1, 1000]

Constraints:
- 1 <= deck.length <= 1000
- 1 <= deck[i] <= 10^6
- All the values of deck are unique.
"""

# Solution
from collections import deque

def deckRevealedIncreasing(deck):
    """
    Returns the ordering of the deck that reveals cards in increasing order.

    :param deck: List[int] - List of unique integers representing the deck of cards.
    :return: List[int] - Ordered deck to reveal cards in increasing order.
    """
    # Sort the deck in ascending order
    deck.sort()
    
    # Create a deque to simulate the process
    index_queue = deque(range(len(deck)))
    result = [0] * len(deck)
    
    for card in deck:
        # Place the smallest card in the correct position
        result[index_queue.popleft()] = card
        # Move the next index to the bottom of the queue
        if index_queue:
            index_queue.append(index_queue.popleft())
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    deck1 = [17, 13, 11, 2, 3, 5, 7]
    print(deckRevealedIncreasing(deck1))  # Output: [2, 13, 3, 11, 5, 17, 7]

    # Test Case 2
    deck2 = [1, 1000]
    print(deckRevealedIncreasing(deck2))  # Output: [1, 1000]

    # Test Case 3
    deck3 = [10, 20, 30, 40, 50]
    print(deckRevealedIncreasing(deck3))  # Output: [10, 40, 20, 50, 30]

    # Test Case 4
    deck4 = [5]
    print(deckRevealedIncreasing(deck4))  # Output: [5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the deck takes O(n log n), where n is the length of the deck.
- Simulating the process with the deque takes O(n), as each card is processed once.
- Overall time complexity: O(n log n).

Space Complexity:
- The deque used for indices takes O(n) space.
- The result array also takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Simulation
"""