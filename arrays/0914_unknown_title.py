"""
LeetCode Problem #914: X of a Kind in a Deck of Cards

Problem Statement:
In a deck of cards, each card has an integer written on it. You can divide the deck into one or more groups of cards where:
- Each group has exactly `X` cards.
- All the cards in each group have the same integer.

Return `true` if and only if you can choose such an `X` that is greater than or equal to 2.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1], [2,2], [3,3], [4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1], [2,2,2,2].

Constraints:
- 1 <= deck.length <= 10^4
- 0 <= deck[i] < 10^4
"""

from collections import Counter
from math import gcd
from functools import reduce

def hasGroupsSizeX(deck):
    """
    Determines if the deck can be partitioned into groups of X cards where X >= 2.

    :param deck: List[int] - List of integers representing the deck of cards.
    :return: bool - True if the deck can be partitioned, False otherwise.
    """
    # Count the frequency of each card
    count = Counter(deck)
    
    # Find the greatest common divisor (GCD) of all frequencies
    frequencies = count.values()
    gcd_of_frequencies = reduce(gcd, frequencies)
    
    # If the GCD is greater than or equal to 2, we can partition the deck
    return gcd_of_frequencies >= 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    deck1 = [1, 2, 3, 4, 4, 3, 2, 1]
    print(hasGroupsSizeX(deck1))  # Output: True

    # Test Case 2
    deck2 = [1, 1, 1, 2, 2, 2, 3, 3]
    print(hasGroupsSizeX(deck2))  # Output: False

    # Test Case 3
    deck3 = [1]
    print(hasGroupsSizeX(deck3))  # Output: False

    # Test Case 4
    deck4 = [1, 1]
    print(hasGroupsSizeX(deck4))  # Output: True

    # Test Case 5
    deck5 = [1, 1, 2, 2, 2, 2]
    print(hasGroupsSizeX(deck5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequencies of cards using `Counter` takes O(n), where n is the length of the deck.
- Calculating the GCD of all frequencies using `reduce` and `gcd` takes O(k * log(max_frequency)), where k is the number of unique cards and max_frequency is the maximum frequency of any card.
- Overall, the time complexity is O(n + k * log(max_frequency)).

Space Complexity:
- The `Counter` object stores the frequencies of cards, which takes O(k) space, where k is the number of unique cards.
- The space complexity is O(k).

Topic: Arrays
"""