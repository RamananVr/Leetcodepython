"""
LeetCode Problem #2083: Substrings That Begin and End With the Same Letter

Problem Statement:
Given a string `s`, return the number of substrings that begin and end with the same character.

A substring is a contiguous sequence of characters within a string.

Example:
Input: s = "abcab"
Output: 7
Explanation:
The substrings that begin and end with the same character are:
- "a" (index 0)
- "b" (index 1)
- "c" (index 2)
- "a" (index 3)
- "b" (index 4)
- "aba" (index 0 to 2)
- "bab" (index 1 to 4)

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

# Solution
def countSubstrings(s: str) -> int:
    """
    Counts the number of substrings that begin and end with the same character.

    :param s: Input string consisting of lowercase English letters.
    :return: Number of substrings that begin and end with the same character.
    """
    # Frequency map to count occurrences of each character
    freq = {}
    
    # Count the frequency of each character in the string
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Calculate the number of substrings for each character
    # If a character appears `n` times, the number of substrings is n + (n * (n - 1)) // 2
    # Explanation:
    # - Single character substrings: n
    # - Substrings of length > 1: Combination of pairs (n choose 2) = n * (n - 1) // 2
    result = 0
    for count in freq.values():
        result += count + (count * (count - 1)) // 2
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcab"
    print(countSubstrings(s1))  # Output: 7

    # Test Case 2
    s2 = "aaaa"
    print(countSubstrings(s2))  # Output: 10

    # Test Case 3
    s3 = "abcd"
    print(countSubstrings(s3))  # Output: 4

    # Test Case 4
    s4 = "a"
    print(countSubstrings(s4))  # Output: 1

    # Test Case 5
    s5 = "abacaba"
    print(countSubstrings(s5))  # Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the frequency map takes O(n), where n is the length of the string `s`.
- Calculating the result involves iterating over the frequency map, which has at most 26 entries (for lowercase English letters). This is O(1) in practice.
- Overall time complexity: O(n).

Space Complexity:
- The frequency map requires O(26) space in the worst case (for all lowercase English letters).
- Overall space complexity: O(1) in practice, as the frequency map size is constant.

Topic: Strings
"""