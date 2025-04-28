"""
LeetCode Problem #2452: Words Within Two Edits of Dictionary

Problem Statement:
You are given two string arrays, `queries` and `dictionary`. All words in each array comprise lowercase English letters and have the same length.

A string word1 is within two edits of word2 if you can transform word1 into word2 by changing at most two characters in word1.

Return a list of all words in `queries` that are within two edits of at least one word in `dictionary`.

Example:
Input: queries = ["word","note","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","wood"]

Constraints:
1. 1 <= queries.length, dictionary.length <= 100
2. 1 <= queries[i].length, dictionary[j].length <= 100
3. queries[i].length == dictionary[j].length
4. queries[i] and dictionary[j] consist of only lowercase English letters.
"""

# Solution
from typing import List

def twoEditWords(queries: List[str], dictionary: List[str]) -> List[str]:
    def within_two_edits(word1: str, word2: str) -> bool:
        # Check if word1 and word2 differ by at most 2 characters
        diff_count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
                if diff_count > 2:
                    return False
        return True

    result = []
    for query in queries:
        for dict_word in dictionary:
            if within_two_edits(query, dict_word):
                result.append(query)
                break
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    queries = ["word", "note", "wood"]
    dictionary = ["wood", "joke", "moat"]
    print(twoEditWords(queries, dictionary))  # Output: ["word", "wood"]

    # Test Case 2
    queries = ["yes", "bat", "cat"]
    dictionary = ["bat", "rat", "mat"]
    print(twoEditWords(queries, dictionary))  # Output: ["bat", "cat"]

    # Test Case 3
    queries = ["abc", "def", "ghi"]
    dictionary = ["xyz", "uvw", "abc"]
    print(twoEditWords(queries, dictionary))  # Output: ["abc"]

    # Test Case 4
    queries = ["aaaa", "bbbb", "cccc"]
    dictionary = ["aaaa", "bbbb", "cccc"]
    print(twoEditWords(queries, dictionary))  # Output: ["aaaa", "bbbb", "cccc"]

    # Test Case 5
    queries = ["abcd", "efgh", "ijkl"]
    dictionary = ["mnop", "qrst", "uvwx"]
    print(twoEditWords(queries, dictionary))  # Output: []

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Let `n` be the length of `queries` and `m` be the length of `dictionary`.
   - Let `k` be the length of each word (since all words have the same length).
   - For each query word, we compare it with every word in the dictionary, and each comparison takes O(k) time.
   - Total time complexity: O(n * m * k).

2. Space Complexity:
   - The space complexity is O(1) for the helper function since it uses a constant amount of space.
   - The result list will take O(n) space in the worst case (if all query words are added to the result).
   - Total space complexity: O(n).

Topic: Strings
"""