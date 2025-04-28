"""
LeetCode Question #2828: Check if a String is an Acronym of Words

Problem Statement:
You are given an array of strings `words` and a string `s`.

`words` consists of lowercase English letters, and `s` is a string of lowercase English letters.

Determine if `s` is an acronym of `words`. An acronym of `words` is formed by concatenating the first character of each string in `words` in order. For example, the acronym of `["alice", "bob", "charlie"]` is `"abc"`.

Return `true` if `s` is an acronym of `words`, and `false` otherwise.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= s.length <= 100`
- `words[i]` and `s` consist of lowercase English letters.
"""

# Solution
def isAcronym(words: list[str], s: str) -> bool:
    """
    Determines if the string `s` is an acronym of the list of strings `words`.

    Args:
    words (list[str]): A list of strings consisting of lowercase English letters.
    s (str): A string consisting of lowercase English letters.

    Returns:
    bool: True if `s` is an acronym of `words`, False otherwise.
    """
    # Generate the acronym by concatenating the first character of each word in `words`
    acronym = ''.join(word[0] for word in words)
    # Check if the generated acronym matches `s`
    return acronym == s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    words = ["alice", "bob", "charlie"]
    s = "abc"
    print(isAcronym(words, s))  # Expected output: True

    # Test Case 2: Acronym does not match
    words = ["apple", "banana", "cherry"]
    s = "xyz"
    print(isAcronym(words, s))  # Expected output: False

    # Test Case 3: Single word
    words = ["hello"]
    s = "h"
    print(isAcronym(words, s))  # Expected output: True

    # Test Case 4: Empty acronym
    words = ["dog", "elephant", "fish"]
    s = ""
    print(isAcronym(words, s))  # Expected output: False

    # Test Case 5: Multiple words with single characters
    words = ["a", "b", "c"]
    s = "abc"
    print(isAcronym(words, s))  # Expected output: True

    # Test Case 6: Mismatched length
    words = ["cat", "dog", "elephant"]
    s = "cd"
    print(isAcronym(words, s))  # Expected output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the list `words` once to extract the first character of each word.
- Let `n` be the number of words in `words`. The time complexity is O(n).

Space Complexity:
- The space complexity is O(n) for the generated acronym string, where `n` is the number of words in `words`.
- No additional data structures are used, so the space complexity is dominated by the size of the acronym string.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Strings