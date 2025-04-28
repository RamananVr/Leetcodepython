"""
LeetCode Problem #1297: Maximum Number of Occurrences of a Substring

Problem Statement:
Given a string `s`, return the maximum number of occurrences of any substring under the following rules:
1. The number of unique characters in the substring must be less than or equal to `maxLetters`.
2. The substring size must be between `minSize` and `maxSize` inclusive.

Constraints:
- `1 <= s.length <= 10^5`
- `1 <= maxLetters <= 26`
- `1 <= minSize <= maxSize <= s.length`
- `s` consists of only lowercase English letters.

Example:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: The substring "aab" occurs twice, and it contains 2 unique characters which is less than or equal to maxLetters.

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: The substring "aaa" occurs twice, and it contains 1 unique character which is less than or equal to maxLetters.
"""

from collections import Counter

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    """
    Returns the maximum number of occurrences of any substring of `s` that satisfies the given constraints.
    """
    substring_count = Counter()
    max_occurrences = 0

    for i in range(len(s) - minSize + 1):
        # Extract the substring of length `minSize`
        substring = s[i:i + minSize]
        
        # Check if the substring satisfies the unique character constraint
        if len(set(substring)) <= maxLetters:
            substring_count[substring] += 1
            max_occurrences = max(max_occurrences, substring_count[substring])

    return max_occurrences

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aababcaab"
    maxLetters1 = 2
    minSize1 = 3
    maxSize1 = 4
    print(maxFreq(s1, maxLetters1, minSize1, maxSize1))  # Output: 2

    # Test Case 2
    s2 = "aaaa"
    maxLetters2 = 1
    minSize2 = 3
    maxSize2 = 3
    print(maxFreq(s2, maxLetters2, minSize2, maxSize2))  # Output: 2

    # Test Case 3
    s3 = "abcde"
    maxLetters3 = 2
    minSize3 = 2
    maxSize3 = 3
    print(maxFreq(s3, maxLetters3, minSize3, maxSize3))  # Output: 0

    # Test Case 4
    s4 = "aabbcc"
    maxLetters4 = 2
    minSize4 = 2
    maxSize4 = 3
    print(maxFreq(s4, maxLetters4, minSize4, maxSize4))  # Output: 2

"""
Time Complexity Analysis:
- The outer loop iterates over the string `s` with a sliding window of size `minSize`, which takes O(n) time.
- For each substring, checking the number of unique characters takes O(minSize) time in the worst case.
- Thus, the overall time complexity is O(n * minSize).

Space Complexity Analysis:
- The space complexity is O(n) due to the `Counter` object storing substring frequencies.
- Additionally, the space required for the set of unique characters is O(minSize) in the worst case.

Primary Topic: Sliding Window, Hash Table
"""