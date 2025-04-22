"""
LeetCode Problem #916: Word Subsets

Problem Statement:
You are given two string arrays `words1` and `words2`.

A string `b` is a subset of string `a` if every letter in `b` occurs in `a` with at least the same frequency.
For example, "worr" is a subset of "world", but "world" is not a subset of "worr".

A string `a` from `words1` is universal if for every string `b` in `words2`, `b` is a subset of `a`.

Return a list of all the universal strings in `words1`. You may return the answer in any order.

Constraints:
- `1 <= words1.length, words2.length <= 10^4`
- `1 <= words1[i].length, words2[i].length <= 10^4`
- `words1[i]` and `words2[i]` consist only of lowercase English letters.

Example:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""

from collections import Counter
from typing import List

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    # Combine the frequency requirements of all words in words2
    combined_freq = Counter()
    for word in words2:
        word_freq = Counter(word)
        for char, freq in word_freq.items():
            combined_freq[char] = max(combined_freq[char], freq)
    
    # Check each word in words1 against the combined frequency requirements
    result = []
    for word in words1:
        word_freq = Counter(word)
        if all(word_freq[char] >= freq for char, freq in combined_freq.items()):
            result.append(word)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    print(wordSubsets(words1, words2))  # Output: ["facebook", "google", "leetcode"]

    # Test Case 2
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["l", "e"]
    print(wordSubsets(words1, words2))  # Output: ["apple", "google", "leetcode"]

    # Test Case 3
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["a", "z"]
    print(wordSubsets(words1, words2))  # Output: ["amazon"]

    # Test Case 4
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["x"]
    print(wordSubsets(words1, words2))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the length of `words1` and `m` be the length of `words2`.
- Let `L1` be the average length of strings in `words1` and `L2` be the average length of strings in `words2`.
- Constructing the `combined_freq` from `words2` takes O(m * L2).
- For each word in `words1`, checking against `combined_freq` takes O(n * L1).
- Overall time complexity: O(m * L2 + n * L1).

Space Complexity:
- The space required for `combined_freq` is O(26) (constant space for English lowercase letters).
- The space required for the frequency counter of each word in `words1` is O(26) (constant space).
- Overall space complexity: O(26) = O(1) (constant space).

Topic: Arrays, Hash Table
"""