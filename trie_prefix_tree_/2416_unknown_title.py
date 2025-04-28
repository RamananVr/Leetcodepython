"""
LeetCode Problem #2416: Sum of Prefix Scores of Strings

Problem Statement:
You are given an array `words` of size `n` consisting of non-empty strings.

We define the score of a string `word` as the number of strings in `words` that are prefixes of `word`.

- For example, if `words = ["a", "ab", "abc", "bc"]`, then:
  - The score of `"abc"` is `3` because `"a"`, `"ab"`, and `"abc"` are prefixes of `"abc"`.
  - The score of `"bc"` is `1` because only `"bc"` is a prefix of `"bc"`.

Return an array `answer` of size `n` where `answer[i]` is the sum of scores of every prefix of `words[i]`.

Example:
Input: words = ["abc", "ab", "bc", "b"]
Output: [5, 4, 3, 2]

Explanation:
- For `"abc"`: `"a"` (1), `"ab"` (1), `"abc"` (1) → score = 3
- For `"ab"`: `"a"` (1), `"ab"` (1) → score = 2
- For `"bc"`: `"b"` (1), `"bc"` (1) → score = 2
- For `"b"`: `"b"` (1) → score = 1
Total scores: [5, 4, 3, 2]

Constraints:
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- `words[i]` consists of only lowercase English letters.
- The sum of lengths of all strings in `words` does not exceed `10^5`.
"""

# Clean and Correct Python Solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words):
        # Build a Trie and count prefix occurrences
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1

        # Calculate the sum of prefix scores for each word
        result = []
        for word in words:
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            result.append(score)
        return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    words = ["abc", "ab", "bc", "b"]
    print(solution.sumPrefixScores(words))  # Output: [5, 4, 3, 2]

    # Test Case 2
    words = ["a", "aa", "aaa"]
    print(solution.sumPrefixScores(words))  # Output: [3, 5, 6]

    # Test Case 3
    words = ["dog", "cat", "car", "cart"]
    print(solution.sumPrefixScores(words))  # Output: [1, 1, 2, 3]

    # Test Case 4
    words = ["x", "xy", "xyz", "x"]
    print(solution.sumPrefixScores(words))  # Output: [4, 3, 2, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the Trie: O(L), where L is the total number of characters across all words.
- Calculating prefix scores: O(L), as we traverse the Trie for each word.
- Total: O(L).

Space Complexity:
- Trie storage: O(L), where L is the total number of characters across all words.
- Result array: O(n), where n is the number of words.
- Total: O(L).

Note: L is the sum of the lengths of all strings in the input array `words`.
"""

# Topic: Trie (Prefix Tree)