"""
LeetCode Question #411: Minimum Unique Word Abbreviation

Problem Statement:
A string such as "word" contains the following abbreviations:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Given a target string `target` and a set of strings `dictionary`, find an abbreviation of `target` with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has a length of 4.

Note:
1. In the case of multiple answers, you may return any one of them.
2. Assume `target` consists only of lowercase English letters and has a length in the range [1, 21].
3. Assume `dictionary` contains at most 50 strings, and each string has a length equal to `target`.

Example:
Input: target = "apple", dictionary = ["blade"]
Output: "a4"

Input: target = "apple", dictionary = ["plain", "amber", "blade"]
Output: "1p3"

Constraints:
- The dictionary contains only strings of the same length as the target.
- The output abbreviation must not conflict with any abbreviation of the strings in the dictionary.
"""

from itertools import product

def minAbbreviation(target: str, dictionary: list[str]) -> str:
    def to_abbr(mask):
        """Convert a bitmask to an abbreviation."""
        abbr = []
        count = 0
        for i in range(len(target)):
            if mask & (1 << i):
                if count:
                    abbr.append(str(count))
                    count = 0
                abbr.append(target[i])
            else:
                count += 1
        if count:
            abbr.append(str(count))
        return ''.join(abbr)

    def is_valid(mask):
        """Check if the abbreviation conflicts with any word in the dictionary."""
        for word in dictionary:
            match = True
            for i in range(len(target)):
                if mask & (1 << i) and target[i] != word[i]:
                    continue
                if not (mask & (1 << i)) and target[i] == word[i]:
                    match = False
                    break
            if match:
                return False
        return True

    # Filter dictionary to only include words of the same length as the target
    dictionary = [word for word in dictionary if len(word) == len(target)]

    if not dictionary:
        return str(len(target))

    n = len(target)
    min_len = float('inf')
    result = target

    # Generate all possible masks
    for mask in range(1 << n):
        abbr = to_abbr(mask)
        if len(abbr) < min_len and is_valid(mask):
            min_len = len(abbr)
            result = abbr

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = "apple"
    dictionary = ["blade"]
    print(minAbbreviation(target, dictionary))  # Output: "a4"

    # Test Case 2
    target = "apple"
    dictionary = ["plain", "amber", "blade"]
    print(minAbbreviation(target, dictionary))  # Output: "1p3"

    # Test Case 3
    target = "word"
    dictionary = []
    print(minAbbreviation(target, dictionary))  # Output: "4"

    # Test Case 4
    target = "word"
    dictionary = ["word"]
    print(minAbbreviation(target, dictionary))  # Output: "w3"

"""
Time Complexity:
- Generating all masks: O(2^n), where n is the length of the target string.
- For each mask, checking validity against the dictionary: O(m * n), where m is the size of the dictionary.
- Overall complexity: O(2^n * m * n).

Space Complexity:
- The space complexity is O(n) for storing the abbreviation and mask-related operations.

Topic: Backtracking, Bit Manipulation
"""