"""
LeetCode Problem #1065: Index Pairs of a String

Problem Statement:
Given a string `text` and an array of strings `words`, return all index pairs `[i, j]` so that the substring `text[i...j]` is in the array `words`.

Return the pairs `[i, j]` in sorted order (i.e., sort them by their first coordinate, and in case of ties, by their second coordinate).

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story", "fleet", "leetcode"]
Output: [[3, 7], [9, 13], [10, 17]]

Example 2:
Input: text = "ababa", words = ["aba", "ab"]
Output: [[0, 1], [0, 2], [1, 3], [2, 3]]

Constraints:
- 1 <= text.length <= 100
- 1 <= words.length <= 20
- 1 <= words[i].length <= 50
- text and words[i] consist of lowercase English letters.
"""

def indexPairs(text: str, words: list[str]) -> list[list[int]]:
    """
    Finds all index pairs [i, j] such that the substring text[i...j] is in the array words.
    """
    result = []
    for word in words:
        start = text.find(word)
        while start != -1:
            result.append([start, start + len(word) - 1])
            start = text.find(word, start + 1)
    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "thestoryofleetcodeandme"
    words1 = ["story", "fleet", "leetcode"]
    print(indexPairs(text1, words1))  # Expected Output: [[3, 7], [9, 13], [10, 17]]

    # Test Case 2
    text2 = "ababa"
    words2 = ["aba", "ab"]
    print(indexPairs(text2, words2))  # Expected Output: [[0, 1], [0, 2], [1, 3], [2, 3]]

    # Test Case 3
    text3 = "mississippi"
    words3 = ["is", "sip", "hi"]
    print(indexPairs(text3, words3))  # Expected Output: [[1, 2], [4, 5], [6, 8]]

    # Test Case 4
    text4 = "aaaaa"
    words4 = ["aa", "aaa"]
    print(indexPairs(text4, words4))  # Expected Output: [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]

# Time Complexity Analysis:
# Let n = length of the text and m = total number of characters in all words combined.
# For each word in `words`, we search for all occurrences in `text` using `str.find()`.
# In the worst case, this takes O(n) time per word. If there are w words, the total time complexity is O(w * n).
# Sorting the result takes O(k * log(k)), where k is the number of index pairs found.
# Overall time complexity: O(w * n + k * log(k)).

# Space Complexity Analysis:
# The space complexity is O(k), where k is the number of index pairs stored in the result.
# No additional data structures are used, so the space complexity is linear in terms of the output size.

# Topic: Strings