"""
LeetCode Problem #2135: Count Words Obtained After Adding a Letter

Problem Statement:
You are given two arrays of strings `startWords` and `targetWords`. Each string in `targetWords` can be obtained by adding exactly one letter to some string in `startWords`, and then rearranging the resulting string.

For example, `startWords = ["ant", "act", "tack"]` and `targetWords = ["tack", "act", "acti"]`:
- "tack" can be obtained from "act" by adding 'k' and rearranging.
- "act" cannot be obtained from "ant" since rearranging "ant" after adding a letter does not produce "act".
- "acti" can be obtained from "act" by adding 'i' and rearranging.

Return the number of strings in `targetWords` that can be obtained from strings in `startWords` by adding a letter and rearranging.

Constraints:
- `1 <= startWords.length, targetWords.length <= 10^5`
- `1 <= startWords[i].length, targetWords[j].length <= 26`
- All the strings consist of lowercase English letters only.
- No string in `startWords` or `targetWords` has duplicate letters.

"""

# Solution
def wordCount(startWords, targetWords):
    def to_bitmask(word):
        """Convert a word into a bitmask representation."""
        bitmask = 0
        for char in word:
            bitmask |= (1 << (ord(char) - ord('a')))
        return bitmask

    # Convert all startWords into bitmask representations
    start_bitmasks = set(to_bitmask(word) for word in startWords)
    count = 0

    for target in targetWords:
        target_mask = to_bitmask(target)
        # Check if removing one letter from target_mask results in a start_bitmask
        for char in target:
            # Remove the current character from the bitmask
            reduced_mask = target_mask & ~(1 << (ord(char) - ord('a')))
            if reduced_mask in start_bitmasks:
                count += 1
                break

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startWords = ["ant", "act", "tack"]
    targetWords = ["tack", "act", "acti"]
    print(wordCount(startWords, targetWords))  # Output: 2

    # Test Case 2
    startWords = ["ab", "bc", "cd"]
    targetWords = ["abc", "bcd", "cde"]
    print(wordCount(startWords, targetWords))  # Output: 2

    # Test Case 3
    startWords = ["a", "b", "c"]
    targetWords = ["ab", "bc", "cd", "de"]
    print(wordCount(startWords, targetWords))  # Output: 3

    # Test Case 4
    startWords = ["xyz", "abc"]
    targetWords = ["xyza", "abcd", "xyzab"]
    print(wordCount(startWords, targetWords))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting each word in `startWords` and `targetWords` to a bitmask takes O(L), where L is the average length of the words.
- Converting all `startWords` to bitmasks takes O(S * L), where S is the number of words in `startWords`.
- Iterating through `targetWords` and checking for valid transformations takes O(T * L), where T is the number of words in `targetWords`.
- Overall time complexity: O((S + T) * L).

Space Complexity:
- The space required to store the bitmask representations of `startWords` is O(S).
- Overall space complexity: O(S).
"""

# Topic: Hashing, Bit Manipulation