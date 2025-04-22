"""
LeetCode Problem #884: Uncommon Words from Two Sentences

Problem Statement:
A sentence is a string of space-separated words. Each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences `s1` and `s2`, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet", "sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:
- 1 <= s1.length, s2.length <= 200
- s1 and s2 consist of lowercase English letters and spaces.
- s1 and s2 do not have leading or trailing spaces.
- All the words in s1 and s2 are separated by a single space.
"""

# Solution
from collections import Counter

def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    # Combine both sentences into one list of words
    words = s1.split() + s2.split()
    # Count the frequency of each word
    word_count = Counter(words)
    # Return words that appear exactly once
    return [word for word, count in word_count.items() if count == 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(uncommonFromSentences(s1, s2))  # Output: ["sweet", "sour"]

    # Test Case 2
    s1 = "apple apple"
    s2 = "banana"
    print(uncommonFromSentences(s1, s2))  # Output: ["banana"]

    # Test Case 3
    s1 = "the quick brown fox"
    s2 = "the lazy dog"
    print(uncommonFromSentences(s1, s2))  # Output: ["quick", "brown", "fox", "lazy", "dog"]

    # Test Case 4
    s1 = "a b c"
    s2 = "a b d"
    print(uncommonFromSentences(s1, s2))  # Output: ["c", "d"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the sentences into words takes O(n + m), where n is the length of s1 and m is the length of s2.
- Counting the frequency of words using Counter takes O(k), where k is the total number of words in s1 and s2.
- Filtering uncommon words takes O(k).
- Overall, the time complexity is O(n + m + k), which simplifies to O(n + m).

Space Complexity:
- The space required for the word list and the Counter dictionary is O(k), where k is the total number of words in s1 and s2.
- The output list of uncommon words will also take O(k) space in the worst case.
- Overall, the space complexity is O(k).
"""

# Topic: Strings, Hash Table