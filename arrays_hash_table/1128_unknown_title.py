"""
LeetCode Problem #1128: Number of Equivalent Domino Pairs

Problem Statement:
Given a list of dominoes, `dominoes[i] = [a, b]` is equivalent to `dominoes[j] = [c, d]` if and only if 
either (a == c and b == d) or (a == d and b == c) — that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,2]]
Output: 3

Constraints:
- 1 <= dominoes.length <= 4 * 10^4
- 1 <= dominoes[i][j] <= 9
"""

# Solution
from collections import defaultdict

def numEquivDominoPairs(dominoes):
    """
    Function to calculate the number of equivalent domino pairs.

    :param dominoes: List[List[int]] - List of domino pairs
    :return: int - Number of equivalent domino pairs
    """
    count = defaultdict(int)
    result = 0

    for a, b in dominoes:
        # Normalize the domino pair to ensure (a, b) and (b, a) are treated the same
        key = tuple(sorted((a, b)))
        result += count[key]
        count[key] += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dominoes1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
    print(numEquivDominoPairs(dominoes1))  # Output: 1

    # Test Case 2
    dominoes2 = [[1, 2], [1, 2], [1, 2]]
    print(numEquivDominoPairs(dominoes2))  # Output: 3

    # Test Case 3
    dominoes3 = [[1, 2], [2, 1], [1, 2], [2, 1]]
    print(numEquivDominoPairs(dominoes3))  # Output: 6

    # Test Case 4
    dominoes4 = [[1, 1], [1, 1], [1, 1], [1, 1]]
    print(numEquivDominoPairs(dominoes4))  # Output: 6

    # Test Case 5
    dominoes5 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(numEquivDominoPairs(dominoes5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Iterating through the dominoes list takes O(n), where n is the length of the dominoes list.
- Sorting each domino pair (constant size of 2) takes O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The `count` dictionary stores at most 45 keys (since there are 9 * 10 / 2 = 45 unique domino pairs).
- Thus, the space complexity is O(1) (constant space usage).
"""

# Topic: Arrays, Hash Table