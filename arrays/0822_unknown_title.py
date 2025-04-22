"""
LeetCode Problem #822: Card Flipping Game

Problem Statement:
You are given two integer arrays `fronts` and `backs` of length `n`, where the `i-th` card has the integer `fronts[i]` written on the front and `backs[i]` written on the back. Initially, each card is placed with the front side facing up.

We can flip the `i-th` card, so that the back side of the card is now facing up and the front side is facing down.

Return the smallest possible number that is written on the front of a card that is not written on the back of any card. If no such number exists, return `0`.

Constraints:
- `n == fronts.length == backs.length`
- `1 <= n <= 1000`
- `1 <= fronts[i], backs[i] <= 2000`

Example:
Input: fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]
Output: 2
Explanation: If you flip the second card, the front becomes 3 and the back becomes 2. The smallest number that is not on the back of any card is 2.

"""

# Python Solution
def flipgame(fronts, backs):
    """
    Finds the smallest number that is on the front of a card but not on the back of any card.

    :param fronts: List[int] - List of integers on the front of the cards
    :param backs: List[int] - List of integers on the back of the cards
    :return: int - The smallest valid number, or 0 if no such number exists
    """
    # Set of numbers that are the same on both the front and back of a card
    same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
    
    # Combine all numbers from fronts and backs, and filter out the "same" numbers
    candidates = set(fronts + backs) - same
    
    # Return the smallest candidate, or 0 if no candidates exist
    return min(candidates) if candidates else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    fronts = [1, 2, 4, 4, 7]
    backs = [1, 3, 4, 1, 3]
    print(flipgame(fronts, backs))  # Output: 2

    # Test Case 2
    fronts = [1, 1]
    backs = [1, 1]
    print(flipgame(fronts, backs))  # Output: 0

    # Test Case 3
    fronts = [1, 2, 3]
    backs = [4, 5, 6]
    print(flipgame(fronts, backs))  # Output: 1

    # Test Case 4
    fronts = [1, 2, 3]
    backs = [3, 2, 1]
    print(flipgame(fronts, backs))  # Output: 0

    # Test Case 5
    fronts = [5, 6, 7]
    backs = [8, 9, 10]
    print(flipgame(fronts, backs))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `same` set takes O(n), where n is the length of the `fronts` and `backs` arrays.
- Combining `fronts` and `backs` into a set takes O(n).
- Subtracting the `same` set from the combined set and finding the minimum takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The `same` set and the `candidates` set each require O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays