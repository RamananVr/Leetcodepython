"""
LeetCode Problem #1686: Stone Game VI

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones in a pile. On each player's turn, they can choose any stone and remove it from the pile. 
The stone has a value represented by an integer array `aliceValues` for Alice and `bobValues` for Bob. 
- Alice's score is increased by `aliceValues[i]` when she removes the i-th stone.
- Bob's score is increased by `bobValues[i]` when he removes the i-th stone.

The objective of the game is to maximize their respective scores. If both players play optimally, return:
- 1 if Alice's score is greater than Bob's score,
- -1 if Bob's score is greater than Alice's score,
- 0 if their scores are equal.

Constraints:
- `1 <= aliceValues.length == bobValues.length <= 10^5`
- `0 <= aliceValues[i], bobValues[i] <= 100`
"""

# Solution
from typing import List

def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    # Combine the values into a single list of tuples (total_value, alice_value, bob_value)
    combined = [(aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]) for i in range(len(aliceValues))]
    
    # Sort the combined list in descending order based on total_value
    combined.sort(reverse=True, key=lambda x: x[0])
    
    alice_score, bob_score = 0, 0
    
    # Alternate turns between Alice and Bob
    for i, (_, alice_value, bob_value) in enumerate(combined):
        if i % 2 == 0:  # Alice's turn
            alice_score += alice_value
        else:  # Bob's turn
            bob_score += bob_value
    
    # Compare scores and return the result
    if alice_score > bob_score:
        return 1
    elif bob_score > alice_score:
        return -1
    else:
        return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    aliceValues = [1, 3]
    bobValues = [2, 1]
    print(stoneGameVI(aliceValues, bobValues))  # Output: 1

    # Test Case 2
    aliceValues = [1, 2]
    bobValues = [3, 1]
    print(stoneGameVI(aliceValues, bobValues))  # Output: 0

    # Test Case 3
    aliceValues = [2, 4, 3]
    bobValues = [1, 6, 7]
    print(stoneGameVI(aliceValues, bobValues))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Combining the values into a single list takes O(n), where n is the length of aliceValues and bobValues.
- Sorting the combined list takes O(n log n).
- Iterating through the sorted list to calculate scores takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The combined list takes O(n) space.
- Other variables (alice_score, bob_score) use O(1) space.
- Overall space complexity: O(n).

Topic: Greedy
"""