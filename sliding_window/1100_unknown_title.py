"""
LeetCode Problem #1100: Find K-Length Substrings With No Repeated Characters

Problem Statement:
Given a string `s` and an integer `k`, return the number of substrings of length `k` with no repeated characters.

Example 1:
Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings of length 5 with no repeated characters: 
"havef", "avefu", "vefun", "efuno", "etcod", "tcode".

Example 2:
Input: s = "home", k = 5
Output: 0
Explanation: The string is too short to have substrings of length 5.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
- 1 <= k <= 10^4
"""

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    """
    Returns the number of substrings of length k with no repeated characters.

    :param s: Input string
    :param k: Length of the substring
    :return: Number of valid substrings
    """
    if k > len(s):
        return 0

    char_set = set()
    left = 0
    count = 0

    for right in range(len(s)):
        # Remove characters from the left until there are no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set
        char_set.add(s[right])

        # Check if the current window has exactly k characters
        if right - left + 1 == k:
            count += 1
            # Slide the window forward by removing the leftmost character
            char_set.remove(s[left])
            left += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "havefunonleetcode"
    k1 = 5
    print(numKLenSubstrNoRepeats(s1, k1))  # Output: 6

    # Test Case 2
    s2 = "home"
    k2 = 5
    print(numKLenSubstrNoRepeats(s2, k2))  # Output: 0

    # Test Case 3
    s3 = "abcabc"
    k3 = 3
    print(numKLenSubstrNoRepeats(s3, k3))  # Output: 4

    # Test Case 4
    s4 = "aaaaa"
    k4 = 2
    print(numKLenSubstrNoRepeats(s4, k4))  # Output: 0

    # Test Case 5
    s5 = "abcdefg"
    k5 = 7
    print(numKLenSubstrNoRepeats(s5, k5))  # Output: 1

"""
Time Complexity:
- The algorithm uses a sliding window approach, where each character is added and removed from the set at most once.
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity:
- The space complexity is O(k), as the set can hold at most `k` characters at any given time.

Topic: Sliding Window
"""