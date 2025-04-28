"""
LeetCode Problem #1794: Count Pairs of Equal Substrings With Minimum Difference

Problem Statement:
You are given two strings s1 and s2 of equal length consisting of lowercase English letters. 
A substring is a contiguous sequence of characters within a string. 
A pair of substrings (x, y) is called equal if x is a substring of s1, y is a substring of s2, and x == y.

The difference between a pair of substrings (x, y) is defined as the absolute difference 
between the starting indices of x in s1 and y in s2.

Return the minimum difference among all pairs of equal substrings. If no such pair exists, return -1.

Example:
Input: s1 = "abcd", s2 = "bcdf"
Output: 1
Explanation: The substrings "b" in s1 and "b" in s2 are equal, and their starting indices are 1 and 0, respectively. 
The absolute difference is |1 - 0| = 1.

Constraints:
- 1 <= s1.length == s2.length <= 100
- s1 and s2 consist of lowercase English letters.
"""

# Solution
def minimumDifference(s1: str, s2: str) -> int:
    n = len(s1)
    min_diff = float('inf')
    found = False

    # Iterate over all possible substring lengths
    for length in range(1, n + 1):
        # Use sets to store substrings of the current length
        substrings_s1 = {}
        substrings_s2 = {}

        # Collect substrings of s1 and s2 of the current length
        for i in range(n - length + 1):
            substrings_s1[s1[i:i + length]] = i
            substrings_s2[s2[i:i + length]] = i

        # Check for common substrings
        for substring in substrings_s1:
            if substring in substrings_s2:
                found = True
                diff = abs(substrings_s1[substring] - substrings_s2[substring])
                min_diff = min(min_diff, diff)

    return min_diff if found else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcd"
    s2 = "bcdf"
    print(minimumDifference(s1, s2))  # Output: 1

    # Test Case 2
    s1 = "abc"
    s2 = "def"
    print(minimumDifference(s1, s2))  # Output: -1

    # Test Case 3
    s1 = "aabbcc"
    s2 = "bbccaa"
    print(minimumDifference(s1, s2))  # Output: 0

    # Test Case 4
    s1 = "xyzxyz"
    s2 = "xyzxyz"
    print(minimumDifference(s1, s2))  # Output: 0

    # Test Case 5
    s1 = "abcde"
    s2 = "edcba"
    print(minimumDifference(s1, s2))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all possible substring lengths (1 to n), which is O(n).
- For each substring length, we iterate over all possible starting indices in s1 and s2, which is O(n) each.
- Checking for common substrings involves iterating over the keys of substrings_s1, which is O(n) in the worst case.
- Overall, the time complexity is O(n^3).

Space Complexity:
- We use two dictionaries to store substrings of s1 and s2 for each substring length. 
  In the worst case, each dictionary can store up to O(n) substrings.
- The space complexity is O(n) for the dictionaries, and O(1) for other variables.
- Overall, the space complexity is O(n).

Topic: Strings
"""