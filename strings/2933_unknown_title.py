"""
LeetCode Problem #2933: Check if a String Is an Acronym of Words

Problem Statement:
You are given a list of strings `words` and a string `s`. Determine if `s` is an acronym of the strings in `words`.

An acronym of a list of words is a string formed by concatenating the first character of each word in the list of words.

For example, the acronym of ["apple", "banana", "cherry"] is "abc".

Return `True` if `s` is an acronym of `words`, and `False` otherwise.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= s.length <= 100`
- `words[i]` and `s` consist of lowercase English letters.
"""

# Solution
def isAcronym(words, s):
    """
    Determines if the string `s` is an acronym of the list of strings `words`.

    :param words: List[str] - A list of strings.
    :param s: str - A string to check if it's an acronym of `words`.
    :return: bool - True if `s` is an acronym of `words`, False otherwise.
    """
    # Generate the acronym by concatenating the first character of each word in `words`
    acronym = ''.join(word[0] for word in words)
    # Check if the generated acronym matches `s`
    return acronym == s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    words1 = ["apple", "banana", "cherry"]
    s1 = "abc"
    print(isAcronym(words1, s1))  # Expected output: True

    # Test Case 2: Acronym does not match
    words2 = ["dog", "elephant", "fox"]
    s2 = "defg"
    print(isAcronym(words2, s2))  # Expected output: False

    # Test Case 3: Single word
    words3 = ["hello"]
    s3 = "h"
    print(isAcronym(words3, s3))  # Expected output: True

    # Test Case 4: Empty acronym
    words4 = ["test", "case"]
    s4 = ""
    print(isAcronym(words4, s4))  # Expected output: False

    # Test Case 5: Multiple words with single characters
    words5 = ["a", "b", "c"]
    s5 = "abc"
    print(isAcronym(words5, s5))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the list `words` once to extract the first character of each word.
- Let `n` be the number of words in `words`. The time complexity is O(n).

Space Complexity:
- The solution uses a temporary string to store the acronym, which has a length equal to the number of words in `words`.
- The space complexity is O(n) for the generated acronym string.
"""

# Topic: Strings