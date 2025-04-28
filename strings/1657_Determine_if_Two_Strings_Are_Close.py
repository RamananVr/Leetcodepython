"""
LeetCode Problem #1657: Determine if Two Strings Are Close

Problem Statement:
Two strings are considered "close" if you can attain one string from the other using the following operations:
1. Swap any two existing characters. For example, "abcde" -> "acbde".
2. Transform every occurrence of one existing character into another existing character, and do the same with the other character. 
   For example, "aacabb" -> "bbcbaa" (all 'a's are transformed to 'b's, and all 'b's are transformed to 'a's).

You can use the operations above any number of times.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are close, and `false` otherwise.

Constraints:
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` consist of lowercase English letters.
"""

from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    """
    Determine if two strings are close based on the given operations.
    """
    # If the lengths of the strings are different, they cannot be close
    if len(word1) != len(word2):
        return False

    # Count the frequency of characters in both strings
    freq1 = Counter(word1)
    freq2 = Counter(word2)

    # Check if both strings have the same set of unique characters
    if set(freq1.keys()) != set(freq2.keys()):
        return False

    # Check if the frequency counts (ignoring which character they belong to) are the same
    if sorted(freq1.values()) != sorted(freq2.values()):
        return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Strings are close
    word1 = "abc"
    word2 = "bca"
    print(closeStrings(word1, word2))  # Output: True

    # Test Case 2: Strings are not close (different unique characters)
    word1 = "a"
    word2 = "aa"
    print(closeStrings(word1, word2))  # Output: False

    # Test Case 3: Strings are not close (different frequency distributions)
    word1 = "cabbba"
    word2 = "aabbss"
    print(closeStrings(word1, word2))  # Output: False

    # Test Case 4: Strings are close (same unique characters and frequency distributions)
    word1 = "cabbba"
    word2 = "abbccc"
    print(closeStrings(word1, word2))  # Output: True

    # Test Case 5: Strings are not close (different lengths)
    word1 = "abc"
    word2 = "abcd"
    print(closeStrings(word1, word2))  # Output: False

"""
Time Complexity:
- Counting the frequency of characters in both strings takes O(n), where n is the length of the strings.
- Checking if the sets of unique characters are the same takes O(26) = O(1) (since there are at most 26 lowercase English letters).
- Sorting the frequency counts takes O(26 log 26) = O(1) (since there are at most 26 unique characters).
- Overall, the time complexity is O(n).

Space Complexity:
- The space required to store the frequency counts is O(26) = O(1) (since there are at most 26 unique characters).
- Overall, the space complexity is O(1).

Topic: Strings
"""