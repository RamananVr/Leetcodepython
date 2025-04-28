"""
LeetCode Problem #1456: Maximum Number of Vowels in a Substring of Given Length

Problem Statement:
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length
"""

def maxVowels(s: str, k: int) -> int:
    """
    Finds the maximum number of vowels in any substring of length k in the given string s.

    :param s: The input string consisting of lowercase English letters.
    :param k: The length of the substring to consider.
    :return: The maximum number of vowels in any substring of length k.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    current_vowels = 0

    # Initialize the first window of size k
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
    max_vowels = current_vowels

    # Slide the window across the string
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        if s[i - k] in vowels:
            current_vowels -= 1
        max_vowels = max(max_vowels, current_vowels)

    return max_vowels

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abciiidef"
    k1 = 3
    print(maxVowels(s1, k1))  # Output: 3

    # Test Case 2
    s2 = "aeiou"
    k2 = 2
    print(maxVowels(s2, k2))  # Output: 2

    # Test Case 3
    s3 = "leetcode"
    k3 = 3
    print(maxVowels(s3, k3))  # Output: 2

    # Test Case 4
    s4 = "rhythms"
    k4 = 4
    print(maxVowels(s4, k4))  # Output: 0

    # Test Case 5
    s5 = "tryhard"
    k5 = 4
    print(maxVowels(s5, k5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where we iterate through the string once.
- Initializing the first window takes O(k) time.
- Sliding the window across the rest of the string takes O(n - k) time, where n is the length of the string.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a set to store the vowels, which takes O(1) space.
- No additional space is used apart from a few variables.
- Overall space complexity: O(1).

Topic: Sliding Window
"""