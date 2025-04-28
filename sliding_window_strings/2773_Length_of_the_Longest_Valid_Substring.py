"""
LeetCode Problem #2773: Length of the Longest Valid Substring

Problem Statement:
You are given a string `word` and a list of strings `forbidden`. A substring of `word` is called valid if it does not contain any string from `forbidden` as a substring.

Return the length of the longest valid substring of `word`.

Constraints:
- 1 <= len(word) <= 10^5
- 1 <= len(forbidden[i]) <= 10
- 1 <= len(forbidden) <= 10^3
- `word` consists only of lowercase English letters.
- `forbidden` consists of distinct strings of lowercase English letters.

Example:
Input: word = "cbaaaabc", forbidden = ["aaa", "cb"]
Output: 4
Explanation: The valid substrings are "cbaa", "baaa", "aaab", "aabc", etc. The longest valid substring is "cbaa" with length 4.
"""

def longestValidSubstring(word: str, forbidden: list[str]) -> int:
    """
    Finds the length of the longest valid substring of `word` that does not contain
    any string from `forbidden` as a substring.
    """
    n = len(word)
    forbidden_set = set(forbidden)
    max_length = 0
    left = 0

    for right in range(n):
        # Check substrings ending at `right` and adjust `left` pointer
        for length in range(1, 11):  # Forbidden strings are at most length 10
            if right - length + 1 < left:
                break
            if word[right - length + 1:right + 1] in forbidden_set:
                left = right - length + 2
                break

        # Update the maximum valid substring length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "cbaaaabc"
    forbidden1 = ["aaa", "cb"]
    print(longestValidSubstring(word1, forbidden1))  # Output: 4

    # Test Case 2
    word2 = "abcdef"
    forbidden2 = ["gh", "ij"]
    print(longestValidSubstring(word2, forbidden2))  # Output: 6

    # Test Case 3
    word3 = "aaaaa"
    forbidden3 = ["aa"]
    print(longestValidSubstring(word3, forbidden3))  # Output: 1

    # Test Case 4
    word4 = "abcde"
    forbidden4 = ["abc", "de"]
    print(longestValidSubstring(word4, forbidden4))  # Output: 2

    # Test Case 5
    word5 = "xyzxyzxyz"
    forbidden5 = ["xyz"]
    print(longestValidSubstring(word5, forbidden5))  # Output: 2

"""
Time Complexity Analysis:
- Let `n` be the length of the string `word` and `m` be the maximum length of strings in `forbidden`.
- For each character in `word`, we check up to `m` substrings (at most 10 due to constraints).
- Thus, the time complexity is O(n * m), where m <= 10, so effectively O(n).

Space Complexity Analysis:
- The space complexity is O(f), where `f` is the number of forbidden strings, as we store them in a set.
- Additionally, we use a few variables for pointers and counters, so the overall space complexity is O(f).

Topic: Sliding Window, Strings
"""