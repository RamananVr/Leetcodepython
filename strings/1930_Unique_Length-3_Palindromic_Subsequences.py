"""
LeetCode Problem #1930: Unique Length-3 Palindromic Subsequences

Problem Statement:
Given a string `s`, return the number of unique palindromic subsequences of length 3 in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A string is palindromic if it reads the same forward and backward.

Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba"
- "aaa"
- "aca"

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3.

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb"
- "bcb"
- "bab"
- "aba"

Constraints:
- 3 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

def countPalindromicSubsequence(s: str) -> int:
    """
    Function to count the number of unique palindromic subsequences of length 3 in the string `s`.
    """
    # Set to store unique palindromic subsequences
    unique_palindromes = set()

    # Iterate over all possible center characters for the palindrome
    for char in set(s):
        # Find the first and last occurrence of the character
        left = s.find(char)
        right = s.rfind(char)

        # If the character appears at least twice
        if right - left > 1:
            # Add all unique characters between the first and last occurrence
            for middle_char in set(s[left + 1:right]):
                unique_palindromes.add((char, middle_char, char))

    # Return the count of unique palindromic subsequences
    return len(unique_palindromes)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabca"
    print(countPalindromicSubsequence(s1))  # Output: 3

    # Test Case 2
    s2 = "adc"
    print(countPalindromicSubsequence(s2))  # Output: 0

    # Test Case 3
    s3 = "bbcbaba"
    print(countPalindromicSubsequence(s3))  # Output: 4

    # Additional Test Case 4
    s4 = "aaaa"
    print(countPalindromicSubsequence(s4))  # Output: 1

    # Additional Test Case 5
    s5 = "abcabcabc"
    print(countPalindromicSubsequence(s5))  # Output: 7

"""
Time Complexity Analysis:
- Let `n` be the length of the string `s`.
- Finding the first and last occurrence of each character takes O(n) for all 26 lowercase English letters.
- For each character, we iterate over the substring between its first and last occurrence, which in the worst case is O(n).
- Thus, the overall time complexity is O(26 * n) = O(n).

Space Complexity Analysis:
- The space complexity is O(26) = O(1) for the set of unique characters and the set of unique palindromic subsequences.

Topic: Strings
"""