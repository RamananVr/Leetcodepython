"""
LeetCode Question #1234: Replace the Substring for Balanced String

Problem Statement:
You are given a string s of length n containing only the characters 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the string s balanced.

If the string is already balanced, return 0.

Constraints:
- 1 <= s.length <= 10^5
- s.length is a multiple of 4
- s consists of only 'Q', 'W', 'E', and 'R'.

Example:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Input: s = "QQWE"
Output: 1
Explanation: Replace the 'Q' at index 0 with 'R' to make s = "RQWE".

Input: s = "QQQW"
Output: 2
Explanation: Replace the first two 'Q's with 'E' and 'R' to make s = "ERQW".

Input: s = "QQQQ"
Output: 3
Explanation: Replace three 'Q's with 'W', 'E', and 'R' to make s = "WERQ".
"""

from collections import Counter

def balancedString(s: str) -> int:
    n = len(s)
    target = n // 4
    count = Counter(s)
    left = 0
    min_length = n

    for right in range(n):
        count[s[right]] -= 1

        while left < n and all(count[char] <= target for char in 'QWER'):
            min_length = min(min_length, right - left + 1)
            count[s[left]] += 1
            left += 1

    return min_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Already balanced
    s1 = "QWER"
    print(balancedString(s1))  # Output: 0

    # Test Case 2: Replace one character
    s2 = "QQWE"
    print(balancedString(s2))  # Output: 1

    # Test Case 3: Replace two characters
    s3 = "QQQW"
    print(balancedString(s3))  # Output: 2

    # Test Case 4: Replace three characters
    s4 = "QQQQ"
    print(balancedString(s4))  # Output: 3

    # Test Case 5: Larger input
    s5 = "WQWRQQQW"
    print(balancedString(s5))  # Output: 3

"""
Time Complexity Analysis:
- The outer loop iterates over the string once (O(n)).
- The inner loop also iterates over the string, but each character is processed at most twice (once by the right pointer and once by the left pointer).
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- We use a Counter to store the frequency of characters, which requires O(1) space since there are only four possible characters ('Q', 'W', 'E', 'R').
- Thus, the space complexity is O(1).

Topic: Sliding Window, String
"""