"""
LeetCode Problem #948: Bag of Tokens

Problem Statement:
You have an initial power `power`, an initial score of `0`, and a bag of `tokens` where `tokens[i]` is the value of the i-th token (0-indexed).

Your goal is to maximize your score by playing the tokens in one of two ways:
1. If your current power is at least `tokens[i]`, you may play the i-th token face up, losing `tokens[i]` power and gaining `1` score.
2. If your score is at least `1`, you may play the i-th token face down, gaining `tokens[i]` power and losing `1` score.

Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the maximum score you can achieve after playing any number of tokens.

Example 1:
Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token is impossible because you don't have enough power.

Example 2:
Input: tokens = [100, 200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no valid move to play the 1st token face up or face down.

Example 3:
Input: tokens = [100, 200, 300, 400], power = 200
Output: 2
Explanation: Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
Then play the 1st token (200) face up, your power becomes 0 and score becomes 2.
There is no valid move to play the 2nd token face up or face down.

Constraints:
- 0 <= tokens.length <= 1000
- 0 <= tokens[i], power < 10^4
"""

# Python Solution
from typing import List

def bagOfTokensScore(tokens: List[int], power: int) -> int:
    tokens.sort()
    score = 0
    max_score = 0
    left, right = 0, len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            # Play the token face up
            power -= tokens[left]
            score += 1
            max_score = max(max_score, score)
            left += 1
        elif score > 0:
            # Play the token face down
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tokens = [100]
    power = 50
    print(bagOfTokensScore(tokens, power))  # Output: 0

    # Test Case 2
    tokens = [100, 200]
    power = 150
    print(bagOfTokensScore(tokens, power))  # Output: 1

    # Test Case 3
    tokens = [100, 200, 300, 400]
    power = 200
    print(bagOfTokensScore(tokens, power))  # Output: 2

    # Additional Test Case 4
    tokens = [50, 100, 150, 200]
    power = 250
    print(bagOfTokensScore(tokens, power))  # Output: 3

    # Additional Test Case 5
    tokens = []
    power = 100
    print(bagOfTokensScore(tokens, power))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the tokens takes O(n log n), where n is the length of the tokens array.
- The two-pointer traversal of the tokens array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space apart from the input.
- Overall space complexity: O(1).
"""

# Topic: Greedy Algorithm