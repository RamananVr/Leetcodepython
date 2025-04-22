"""
LeetCode Question #425: Word Squares

Problem Statement:
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball", "area", "lead", "lady"] forms a word square because:
    b a l l
    a r e a
    l e a d
    l a d y

Note:
1. There are at least 1 and at most 1000 words.
2. All words will have the same length.
3. Words consist of only lowercase English letters.

You need to return all possible word squares.

Example:
Input: ["area","lead","wall","lady","ball"]
Output: [
    ["wall","area","lead","lady"],
    ["ball","area","lead","lady"]
]

Constraints:
- The input list of words will not contain duplicates.
- All words will have the same length.
"""

from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def build_prefix_map(words):
            """Build a prefix map where the key is a prefix and the value is a list of words with that prefix."""
            prefix_map = defaultdict(list)
            for word in words:
                for i in range(len(word) + 1):
                    prefix_map[word[:i]].append(word)
            return prefix_map

        def backtrack(step, square):
            """Backtracking function to build word squares."""
            if step == n:
                results.append(square[:])
                return
            
            # Build the prefix for the current column
            prefix = ''.join(square[i][step] for i in range(step))
            for candidate in prefix_map[prefix]:
                square.append(candidate)
                backtrack(step + 1, square)
                square.pop()

        # Initialize variables
        n = len(words[0])  # All words have the same length
        prefix_map = build_prefix_map(words)
        results = []

        # Start backtracking for each word
        for word in words:
            backtrack(1, [word])
        
        return results

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    words1 = ["area", "lead", "wall", "lady", "ball"]
    print("Test Case 1 Output:", solution.wordSquares(words1))
    # Expected Output:
    # [
    #     ["wall", "area", "lead", "lady"],
    #     ["ball", "area", "lead", "lady"]
    # ]

    # Test Case 2
    words2 = ["abat", "baba", "atan", "atal"]
    print("Test Case 2 Output:", solution.wordSquares(words2))
    # Expected Output:
    # [
    #     ["abat", "baba", "atan", "atal"]
    # ]

    # Test Case 3
    words3 = ["abcd", "bnrt", "crmy", "dtye"]
    print("Test Case 3 Output:", solution.wordSquares(words3))
    # Expected Output:
    # [
    #     ["abcd", "bnrt", "crmy", "dtye"]
    # ]

"""
Time Complexity:
- Let n be the length of each word and k be the number of words.
- Building the prefix map takes O(k * n) time.
- The backtracking process explores all possible word squares. In the worst case, there are k^n possible word squares, and for each square, we spend O(n^2) time to construct prefixes.
- Overall time complexity: O(k * n + k^n * n^2).

Space Complexity:
- The prefix map requires O(k * n) space.
- The recursion stack can go as deep as n, and each stack frame uses O(n) space for the current square.
- Overall space complexity: O(k * n + n^2).

Topic: Backtracking, Trie
"""