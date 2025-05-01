"""
LeetCode Problem #2175: "Smallest K-Length Subsequence With Occurrences of a Letter"

Problem Statement:
You are given a string `s`, an integer `k`, a character `letter`, and an integer `repetition`. 
Return the lexicographically smallest subsequence of `s` of length `k` that has at least `repetition` occurrences of the character `letter`.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Constraints:
- `1 <= repetition <= k <= s.length <= 5 * 10^4`
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter and appears in `s`.

Example:
Input: s = "leet", k = 3, letter = "e", repetition = 1
Output: "eet"

Input: s = "leetcode", k = 4, letter = "e", repetition = 2
Output: "ecde"

Input: s = "bb", k = 2, letter = "b", repetition = 2
Output: "bb"
"""

from collections import Counter

def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
    stack = []
    count_letter = s.count(letter)  # Total occurrences of `letter` in `s`
    used_letter = 0  # Count of `letter` used in the stack

    for i, char in enumerate(s):
        # While the stack is not empty, the current character is smaller than the top of the stack,
        # and removing the top of the stack still allows us to form a valid subsequence:
        while (stack and 
               char < stack[-1] and 
               len(stack) - 1 + len(s) - i >= k and 
               (stack[-1] != letter or used_letter + count_letter > repetition)):
            removed = stack.pop()
            if removed == letter:
                used_letter -= 1

        # Add the current character to the stack if it doesn't exceed the required length
        if len(stack) < k:
            if char == letter:
                stack.append(char)
                used_letter += 1
                count_letter -= 1
            elif k - len(stack) > repetition - used_letter:
                stack.append(char)
        else:
            if char == letter:
                count_letter -= 1

    return ''.join(stack)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1, letter1, repetition1 = "leet", 3, "e", 1
    print(smallestSubsequence(s1, k1, letter1, repetition1))  # Output: "eet"

    # Test Case 2
    s2, k2, letter2, repetition2 = "leetcode", 4, "e", 2
    print(smallestSubsequence(s2, k2, letter2, repetition2))  # Output: "ecde"

    # Test Case 3
    s3, k3, letter3, repetition3 = "bb", 2, "b", 2
    print(smallestSubsequence(s3, k3, letter3, repetition3))  # Output: "bb"

    # Test Case 4
    s4, k4, letter4, repetition4 = "abcde", 3, "c", 1
    print(smallestSubsequence(s4, k4, letter4, repetition4))  # Output: "abc"

    # Test Case 5
    s5, k5, letter5, repetition5 = "aaabbbccc", 5, "b", 2
    print(smallestSubsequence(s5, k5, letter5, repetition5))  # Output: "abbcc"


"""
Time Complexity:
- The algorithm iterates through the string `s` once, and each character is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity:
- The space complexity is O(k) for the stack, where `k` is the length of the desired subsequence.

Topic: Greedy, Stack
"""