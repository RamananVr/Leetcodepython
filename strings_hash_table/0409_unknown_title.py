"""
LeetCode Problem #409: Longest Palindrome

Problem Statement:
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome 
that can be built with those letters.

Letters are case-sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Example 3:
Input: s = "bb"
Output: 2
Explanation: The longest palindrome that can be built is "bb", whose length is 2.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.
"""

# Python Solution
from collections import Counter

def longestPalindrome(s: str) -> int:
    """
    Function to calculate the length of the longest palindrome that can be built with the given string `s`.
    """
    char_count = Counter(s)
    length = 0
    odd_found = False

    for count in char_count.values():
        # Add the even part of the count
        length += count // 2 * 2
        # Check if there's an odd count
        if count % 2 == 1:
            odd_found = True

    # If there's at least one odd count, we can add one more character to the palindrome
    if odd_found:
        length += 1

    return length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abccccdd"
    print(f"Input: {s1} -> Output: {longestPalindrome(s1)}")  # Expected Output: 7

    # Test Case 2
    s2 = "a"
    print(f"Input: {s2} -> Output: {longestPalindrome(s2)}")  # Expected Output: 1

    # Test Case 3
    s3 = "bb"
    print(f"Input: {s3} -> Output: {longestPalindrome(s3)}")  # Expected Output: 2

    # Test Case 4
    s4 = "Aa"
    print(f"Input: {s4} -> Output: {longestPalindrome(s4)}")  # Expected Output: 1

    # Test Case 5
    s5 = "abc"
    print(f"Input: {s5} -> Output: {longestPalindrome(s5)}")  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the frequency of characters using `Counter` takes O(n), where n is the length of the string `s`.
- Iterating through the character counts takes O(k), where k is the number of unique characters in `s`.
- In the worst case, k is at most 52 (26 lowercase + 26 uppercase letters), so this is effectively O(1).
- Overall time complexity: O(n).

Space Complexity:
- The `Counter` object stores the frequency of each character, which requires O(k) space.
- In the worst case, k is at most 52, so this is effectively O(1).
- Overall space complexity: O(1).
"""

# Topic: Strings, Hash Table