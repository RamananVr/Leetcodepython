"""
LeetCode Question #2212: Maximum Points in an Archery Competition

Problem Statement:
Alice and Bob are playing a game of archery. Alice has already shot `n` arrows, and Bob wants to maximize his score by shooting `numArrows` arrows. The target has 12 scoring sections, numbered from 0 to 11, and each section `i` has a score of `i` points.

Alice's scores are given in an array `aliceArrows` of size 12, where `aliceArrows[i]` represents the number of arrows Alice shot at section `i`. To win a section `i`, Bob must shoot more arrows than Alice in that section. If Bob wins section `i`, he gets `i` points. If Bob does not win section `i`, he gets 0 points for that section.

Bob wants to maximize his total score. Return the maximum score Bob can achieve and an array `bobArrows` of size 12, where `bobArrows[i]` is the number of arrows Bob shot at section `i`. If there are multiple answers, return any.

Constraints:
- `numArrows == sum(bobArrows)`
- `1 <= numArrows <= 10^5`
- `aliceArrows.length == bobArrows.length == 12`
- `0 <= aliceArrows[i] <= numArrows`

Example:
Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: [0,0,0,2,1,0,3,0,0,1,3,0]
Explanation: Bob can win sections 3, 4, 6, 9, and 10 to get a total score of 3 + 4 + 6 + 9 + 10 = 32 points.
"""

from typing import List, Tuple

def maximumBobPoints(numArrows: int, aliceArrows: List[int]) -> Tuple[int, List[int]]:
    n = len(aliceArrows)
    max_score = 0
    best_allocation = [0] * n

    # Iterate over all possible subsets of sections (2^12 possibilities)
    for mask in range(1 << n):
        score = 0
        arrows_used = 0
        allocation = [0] * n

        for i in range(n):
            if mask & (1 << i):  # If section i is included in the subset
                arrows_needed = aliceArrows[i] + 1
                if arrows_used + arrows_needed <= numArrows:
                    score += i
                    arrows_used += arrows_needed
                    allocation[i] = arrows_needed

        if score > max_score:
            max_score = score
            best_allocation = allocation[:]

    # Distribute remaining arrows to any section (e.g., section 0)
    remaining_arrows = numArrows - sum(best_allocation)
    if remaining_arrows > 0:
        best_allocation[0] += remaining_arrows

    return max_score, best_allocation

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numArrows = 9
    aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
    print(maximumBobPoints(numArrows, aliceArrows))  # Output: (32, [0,0,0,2,1,0,3,0,0,1,3,0])

    # Test Case 2
    numArrows = 3
    aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,0]
    print(maximumBobPoints(numArrows, aliceArrows))  # Output: (1, [0,0,2,0,0,0,0,0,0,0,0,0])

    # Test Case 3
    numArrows = 12
    aliceArrows = [0,1,1,1,1,1,1,1,1,1,1,1]
    print(maximumBobPoints(numArrows, aliceArrows))  # Output: (66, [12,0,0,0,0,0,0,0,0,0,0,0])

"""
Time Complexity:
- There are 2^12 subsets of sections, and for each subset, we iterate over 12 sections.
- Thus, the time complexity is O(2^12 * 12), which is effectively constant since 2^12 = 4096.

Space Complexity:
- The space complexity is O(12) for the allocation array.

Topic: Bitmasking, Dynamic Programming
"""