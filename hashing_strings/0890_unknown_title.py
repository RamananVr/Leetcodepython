"""
LeetCode Problem #890: Find and Replace Pattern

Problem Statement:
You are given a list of strings `words` and a string `pattern`. You want to find all strings in `words` that match the `pattern`.

A string matches the `pattern` if there exists a bijection (one-to-one mapping) between characters in the string and characters in the `pattern`. For example, given `pattern = "abb"`, strings like "mee" and "egg" match the pattern because there is a one-to-one mapping from characters in the pattern to characters in the string.

Return a list of the strings in `words` that match the `pattern`.

Example:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

Constraints:
- 1 <= words.length <= 50
- 1 <= pattern.length <= 20
- All strings in `words` and `pattern` consist of lowercase English letters.
"""

# Solution
def findAndReplacePattern(words, pattern):
    def encode(s):
        """
        Encodes a string into a pattern based on the order of first occurrences of characters.
        Example: "abb" -> [0, 1, 1], "mee" -> [0, 1, 1]
        """
        mapping = {}
        encoded = []
        for i, char in enumerate(s):
            if char not in mapping:
                mapping[char] = len(mapping)
            encoded.append(mapping[char])
        return tuple(encoded)

    # Encode the pattern
    pattern_encoded = encode(pattern)

    # Filter words that match the encoded pattern
    return [word for word in words if encode(word) == pattern_encoded]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(findAndReplacePattern(words, pattern))  # Output: ["mee", "aqq"]

    # Test Case 2
    words = ["xyz", "xyy", "xzz", "aaa", "bbb"]
    pattern = "foo"
    print(findAndReplacePattern(words, pattern))  # Output: ["xyy", "xzz"]

    # Test Case 3
    words = ["abc", "def", "ghi"]
    pattern = "xyz"
    print(findAndReplacePattern(words, pattern))  # Output: ["abc", "def", "ghi"]

    # Test Case 4
    words = ["a", "b", "c"]
    pattern = "a"
    print(findAndReplacePattern(words, pattern))  # Output: ["a", "b", "c"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Encoding a single word or the pattern takes O(L), where L is the length of the word/pattern.
- Encoding all words in the list takes O(N * L), where N is the number of words and L is the average length of the words.
- Filtering the words based on the encoded pattern takes O(N).
- Overall time complexity: O(N * L).

Space Complexity:
- The space used for the mapping dictionary during encoding is O(L) for each word/pattern.
- The space used for the result list is O(N) in the worst case (if all words match the pattern).
- Overall space complexity: O(N + L).
"""

# Topic: Hashing, Strings