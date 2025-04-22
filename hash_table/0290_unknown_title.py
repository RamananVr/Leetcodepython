"""
LeetCode Problem #290: Word Pattern

Problem Statement:
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false

Constraints:
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces.
"""

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    # Create two mappings: pattern -> word and word -> pattern
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pattern = "abba"
    s = "dog cat cat dog"
    print(wordPattern(pattern, s))  # Output: True

    # Test Case 2
    pattern = "abba"
    s = "dog cat cat fish"
    print(wordPattern(pattern, s))  # Output: False

    # Test Case 3
    pattern = "aaaa"
    s = "dog cat cat dog"
    print(wordPattern(pattern, s))  # Output: False

    # Test Case 4
    pattern = "abba"
    s = "dog dog dog dog"
    print(wordPattern(pattern, s))  # Output: False

    # Test Case 5
    pattern = "abc"
    s = "dog cat fish"
    print(wordPattern(pattern, s))  # Output: True

"""
Time Complexity:
- Splitting the string `s` into words takes O(n), where n is the length of the string `s`.
- Iterating through the pattern and words takes O(m), where m is the length of the pattern (or the number of words in `s`).
- Dictionary operations (insertion and lookup) are O(1) on average.
- Overall, the time complexity is O(n + m).

Space Complexity:
- The space complexity is O(m + k), where m is the length of the pattern and k is the number of unique words in `s`.
- This is because we store mappings in two dictionaries.

Topic: Hash Table
"""