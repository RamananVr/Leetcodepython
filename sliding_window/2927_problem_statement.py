"""
LeetCode Question #2927: Problem Statement

You are given a string `s` consisting of lowercase English letters. A substring is called a "good substring" if all the characters of the substring are distinct.

Return the number of good substrings of length `k` in the string `s`.

A substring is a contiguous sequence of characters within a string.

Constraints:
- `1 <= k <= 26`
- `k <= len(s) <= 10^5`
- `s` consists of lowercase English letters.

Example:
Input: s = "xyzzaz", k = 3
Output: 1
Explanation: The only good substring of length 3 is "xyz".

Input: s = "aababcabc", k = 3
Output: 4
Explanation: The good substrings of length 3 are "abc", "bca", "cab", and "abc".
"""

# Python Solution
def countGoodSubstrings(s: str, k: int) -> int:
    """
    Counts the number of good substrings of length k in the string s.

    :param s: Input string consisting of lowercase English letters.
    :param k: Length of the substring to check.
    :return: Number of good substrings of length k.
    """
    if k > len(s):
        return 0

    count = 0
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        if len(set(substring)) == k:  # Check if all characters are distinct
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "xyzzaz"
    k1 = 3
    print(countGoodSubstrings(s1, k1))  # Output: 1

    # Test Case 2
    s2 = "aababcabc"
    k2 = 3
    print(countGoodSubstrings(s2, k2))  # Output: 4

    # Test Case 3
    s3 = "abcdef"
    k3 = 2
    print(countGoodSubstrings(s3, k3))  # Output: 5

    # Test Case 4
    s4 = "aaaaa"
    k4 = 2
    print(countGoodSubstrings(s4, k4))  # Output: 0

    # Test Case 5
    s5 = "abcabcabc"
    k5 = 4
    print(countGoodSubstrings(s5, k5))  # Output: 3

"""
Time and Space Complexity Analysis

Time Complexity:
- The function iterates through the string `s` with a sliding window of size `k`.
- For each window, it computes the set of characters in the substring, which takes O(k) time.
- The total time complexity is O((n - k + 1) * k), where `n` is the length of the string `s`.

Space Complexity:
- The space complexity is O(k) due to the set used to store the characters of the substring.

Topic: Sliding Window
"""