"""
LeetCode Problem #2068: Check Whether Two Strings are Almost Equivalent

Problem Statement:
Two strings `word1` and `word2` are considered "almost equivalent" if the differences in the frequencies of each character between the two strings are at most 3. In other words, for every character `c`, the absolute difference between the frequency of `c` in `word1` and the frequency of `c` in `word2` is at most 3.

Given two strings `word1` and `word2`, return `True` if `word1` and `word2` are almost equivalent, or `False` otherwise.

Constraints:
- `word1` and `word2` have the same length, and their lengths are between 1 and 100.
- `word1` and `word2` consist only of lowercase English letters.

Example:
Input: word1 = "aaaa", word2 = "bccb"
Output: False
Explanation: The character 'a' appears 4 times in `word1` but 0 times in `word2`. The absolute difference is 4, which is greater than 3.

Input: word1 = "abcdeef", word2 = "abaaacc"
Output: True
Explanation: The absolute differences for all characters are within the allowed range.

Input: word1 = "cccddabba", word2 = "babababab"
Output: True
Explanation: The absolute differences for all characters are within the allowed range.
"""

# Python Solution
from collections import Counter

def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    # Count the frequency of characters in both strings
    freq1 = Counter(word1)
    freq2 = Counter(word2)
    
    # Combine all unique characters from both strings
    all_chars = set(freq1.keys()).union(set(freq2.keys()))
    
    # Check the absolute difference in frequencies for each character
    for char in all_chars:
        if abs(freq1[char] - freq2[char]) > 3:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "aaaa"
    word2 = "bccb"
    print(checkAlmostEquivalent(word1, word2))  # Output: False

    # Test Case 2
    word1 = "abcdeef"
    word2 = "abaaacc"
    print(checkAlmostEquivalent(word1, word2))  # Output: True

    # Test Case 3
    word1 = "cccddabba"
    word2 = "babababab"
    print(checkAlmostEquivalent(word1, word2))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequencies of characters in `word1` and `word2` takes O(n), where n is the length of the strings.
- Combining the unique characters from both strings takes O(1) since there are at most 26 lowercase English letters.
- Iterating over the set of unique characters and checking the frequency differences takes O(1) (constant time for at most 26 characters).
- Overall, the time complexity is O(n).

Space Complexity:
- The space required to store the frequency counts for `word1` and `word2` is O(1) since there are at most 26 unique characters.
- The space required for the set of unique characters is also O(1).
- Overall, the space complexity is O(1).
"""

# Topic: Strings, Hash Table