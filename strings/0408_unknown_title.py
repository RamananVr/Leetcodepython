"""
LeetCode Problem #408: Valid Word Abbreviation

Problem Statement:
Given a non-empty string `word` and a string `abbr` that represents an abbreviation of `word`, 
return whether the string `abbr` is a valid abbreviation of `word`.

A string `abbr` is a valid abbreviation of `word` if:
1. It can be formed by replacing some (possibly zero) substrings of `word` with the corresponding counts of characters.
2. The count must be a positive integer and cannot have leading zeros.
3. The remaining characters in `abbr` must match the corresponding characters in `word`.

Example:
- "word" -> "w2d" is a valid abbreviation because "w2d" represents "word".
- "word" -> "3d" is a valid abbreviation because "3d" represents "word".
- "word" -> "w03d" is NOT a valid abbreviation because "03" is not a valid number.

Constraints:
- `word` and `abbr` consist only of lowercase English letters and digits.
- `1 <= len(word) <= 20`
- `1 <= len(abbr) <= 20`
"""

def validWordAbbreviation(word: str, abbr: str) -> bool:
    """
    Determines if `abbr` is a valid abbreviation of `word`.

    :param word: The original word.
    :param abbr: The abbreviation to validate.
    :return: True if `abbr` is a valid abbreviation of `word`, False otherwise.
    """
    i, j = 0, 0  # Pointers for word and abbr
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':  # Leading zeros are not allowed
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num  # Skip `num` characters in `word`
        else:
            if word[i] != abbr[j]:  # Characters must match
                return False
            i += 1
            j += 1

    # Both pointers must reach the end for a valid abbreviation
    return i == len(word) and j == len(abbr)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid abbreviation
    word1 = "internationalization"
    abbr1 = "i12iz4n"
    print(validWordAbbreviation(word1, abbr1))  # Expected: True

    # Test Case 2: Invalid abbreviation (mismatch in characters)
    word2 = "apple"
    abbr2 = "a2e"
    print(validWordAbbreviation(word2, abbr2))  # Expected: False

    # Test Case 3: Invalid abbreviation (leading zero)
    word3 = "substitution"
    abbr3 = "s010n"
    print(validWordAbbreviation(word3, abbr3))  # Expected: False

    # Test Case 4: Valid abbreviation (exact match)
    word4 = "word"
    abbr4 = "w1r1"
    print(validWordAbbreviation(word4, abbr4))  # Expected: True

    # Test Case 5: Valid abbreviation (skipping all characters)
    word5 = "word"
    abbr5 = "4"
    print(validWordAbbreviation(word5, abbr5))  # Expected: True

    # Test Case 6: Invalid abbreviation (too many characters skipped)
    word6 = "word"
    abbr6 = "5"
    print(validWordAbbreviation(word6, abbr6))  # Expected: False

"""
Time Complexity:
- The algorithm processes each character in `abbr` and `word` exactly once.
- Let `n` be the length of `word` and `m` be the length of `abbr`.
- Time complexity: O(max(n, m)).

Space Complexity:
- The algorithm uses a constant amount of extra space.
- Space complexity: O(1).

Topic: Strings
"""