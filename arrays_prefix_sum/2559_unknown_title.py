"""
LeetCode Problem #2559: Count Vowel Strings in Ranges

Problem Statement:
You are given a 0-indexed array of strings `words` and a 2D array of integers `queries`.

Each string in `words` consists of lowercase English letters, and each query in `queries` is an array of two integers `[l, r]` where `l <= r`.

A string is considered a vowel string if both the first and the last characters of the string are vowels (i.e., 'a', 'e', 'i', 'o', 'u').

For each query `[l, r]`, count the number of vowel strings in the range `words[l]` to `words[r]` (inclusive) and return an array of the counts.

Example:
Input: words = ["apple", "orange", "banana", "umbrella"], queries = [[0, 1], [1, 3]]
Output: [1, 2]

Constraints:
- 1 <= words.length <= 10^5
- 1 <= queries.length <= 10^5
- 1 <= words[i].length <= 10
- `words[i]` consists of only lowercase English letters.
- 0 <= l <= r < words.length
"""

# Solution
def countVowelStrings(words, queries):
    def is_vowel_string(word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return word[0] in vowels and word[-1] in vowels

    # Precompute a prefix sum array for vowel strings
    n = len(words)
    prefix_vowel_count = [0] * (n + 1)
    for i in range(n):
        prefix_vowel_count[i + 1] = prefix_vowel_count[i] + (1 if is_vowel_string(words[i]) else 0)

    # Process each query using the prefix sum array
    result = []
    for l, r in queries:
        result.append(prefix_vowel_count[r + 1] - prefix_vowel_count[l])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["apple", "orange", "banana", "umbrella"]
    queries = [[0, 1], [1, 3]]
    print(countVowelStrings(words, queries))  # Output: [1, 2]

    # Test Case 2
    words = ["a", "e", "i", "o", "u"]
    queries = [[0, 4], [1, 3], [2, 2]]
    print(countVowelStrings(words, queries))  # Output: [5, 3, 1]

    # Test Case 3
    words = ["cat", "dog", "elephant", "iguana", "owl"]
    queries = [[0, 2], [3, 4], [0, 4]]
    print(countVowelStrings(words, queries))  # Output: [1, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Precomputing the prefix sum array takes O(n), where n is the length of `words`.
- Each query is processed in O(1) using the prefix sum array.
- For q queries, the total time complexity is O(n + q).

Space Complexity:
- The prefix sum array requires O(n) space.
- The result array requires O(q) space.
- Total space complexity is O(n + q).

Topic: Arrays, Prefix Sum
"""