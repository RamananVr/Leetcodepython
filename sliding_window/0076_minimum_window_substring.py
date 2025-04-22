"""
LeetCode Question #76: Minimum Window Substring

Problem Statement:
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The test cases are guaranteed such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""

Constraints:
- `m == len(s)`
- `n == len(t)`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

Follow up:
Could you find an algorithm that runs in `O(m + n)` time?
"""

# Solution
from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    # Count the frequency of characters in t
    t_count = Counter(t)
    required = len(t_count)
    
    # Sliding window pointers
    left, right = 0, 0
    formed = 0
    window_counts = {}
    
    # Result tuple: (window length, left, right)
    result = float("inf"), None, None
    
    while right < len(s):
        # Add the current character to the window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if the current character satisfies the frequency requirement
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        # Try to shrink the window
        while left <= right and formed == required:
            char = s[left]
            
            # Update the result if the current window is smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove the leftmost character from the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            # Move the left pointer forward
            left += 1
        
        # Expand the window by moving the right pointer forward
        right += 1
    
    # Return the smallest window substring
    return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(minWindow(s1, t1))  # Output: "BANC"

    # Test Case 2
    s2 = "a"
    t2 = "a"
    print(minWindow(s2, t2))  # Output: "a"

    # Test Case 3
    s3 = "a"
    t3 = "aa"
    print(minWindow(s3, t3))  # Output: ""

    # Test Case 4
    s4 = "AA"
    t4 = "AA"
    print(minWindow(s4, t4))  # Output: "AA"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each character in `s` at most twice: once when expanding the window and once when contracting it.
- Therefore, the time complexity is O(m + n), where `m` is the length of `s` and `n` is the length of `t`.

Space Complexity:
- The space complexity is O(n + m), where `n` is the number of unique characters in `t` (for the `t_count` dictionary) and `m` is the number of unique characters in `s` (for the `window_counts` dictionary).

Topic: Sliding Window
"""