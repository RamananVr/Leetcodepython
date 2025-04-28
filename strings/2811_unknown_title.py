"""
LeetCode Problem #2811: Check if a String Is an Acronym of Words

Problem Statement:
You are given a list of strings `words` and a string `s`.

An acronym of `words` is a string made by concatenating the first character of each string in `words` in order. 
For example, the acronym of `["alice", "bob", "charlie"]` is `"abc"`.

Return `true` if `s` is the acronym of `words`, and `false` otherwise.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= s.length <= 100`
- `s` and `words[i]` consist of lowercase English letters.
"""

def isAcronym(words, s):
    """
    Determines if the string `s` is the acronym of the list of strings `words`.

    :param words: List[str] - A list of strings.
    :param s: str - A string to check if it is the acronym of `words`.
    :return: bool - True if `s` is the acronym of `words`, False otherwise.
    """
    # Generate the acronym by concatenating the first character of each word in `words`
    acronym = ''.join(word[0] for word in words)
    # Check if the generated acronym matches `s`
    return acronym == s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    words1 = ["alice", "bob", "charlie"]
    s1 = "abc"
    print(isAcronym(words1, s1))  # Expected: True

    # Test Case 2: Acronym does not match
    words2 = ["apple", "banana", "cherry"]
    s2 = "abx"
    print(isAcronym(words2, s2))  # Expected: False

    # Test Case 3: Single word
    words3 = ["hello"]
    s3 = "h"
    print(isAcronym(words3, s3))  # Expected: True

    # Test Case 4: Empty acronym
    words4 = ["dog", "elephant", "frog"]
    s4 = ""
    print(isAcronym(words4, s4))  # Expected: False

    # Test Case 5: Multiple words with same first letter
    words5 = ["cat", "car", "candle"]
    s5 = "ccc"
    print(isAcronym(words5, s5))  # Expected: True

    # Test Case 6: Length mismatch
    words6 = ["zebra", "yak", "xylophone"]
    s6 = "zy"
    print(isAcronym(words6, s6))  # Expected: False

"""
Time Complexity Analysis:
- The solution iterates through the list `words` once to extract the first character of each word.
- Let `n` be the number of words in `words` and `m` be the average length of each word.
- The time complexity is O(n), as we only process the first character of each word.

Space Complexity Analysis:
- The space complexity is O(n) for the generated acronym string, where `n` is the number of words in `words`.

Topic: Strings
"""