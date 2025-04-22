"""
LeetCode Question #161: One Edit Distance

Problem Statement:
Given two strings `s` and `t`, return true if they are both one edit distance apart, otherwise return false.

An edit is defined as one of the following operations:
1. Insert a character into one of the strings.
2. Delete a character from one of the strings.
3. Replace a character in one of the strings.

Note:
- The strings are said to be one edit distance apart if you can perform exactly one of the above operations to make the two strings equal.

Constraints:
- 0 <= s.length, t.length <= 10^4
- `s` and `t` consist of lowercase letters, 'a' to 'z'.
"""

def isOneEditDistance(s: str, t: str) -> bool:
    # If the length difference is greater than 1, they can't be one edit apart
    if abs(len(s) - len(t)) > 1:
        return False

    # Ensure s is the shorter string (or equal in length)
    if len(s) > len(t):
        s, t = t, s

    # Check for one edit distance
    for i in range(len(s)):
        if s[i] != t[i]:
            # Case 1: Replace a character
            if len(s) == len(t):
                return s[i + 1:] == t[i + 1:]
            # Case 2: Insert a character into s (or delete from t)
            else:
                return s[i:] == t[i + 1:]

    # Case 3: If no differences found, check if t has one extra character at the end
    return len(s) + 1 == len(t)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Replace a character
    print(isOneEditDistance("abc", "adc"))  # Expected: True

    # Test Case 2: Insert a character
    print(isOneEditDistance("abc", "abdc"))  # Expected: True

    # Test Case 3: Delete a character
    print(isOneEditDistance("abc", "ac"))  # Expected: True

    # Test Case 4: No edits needed (same strings)
    print(isOneEditDistance("abc", "abc"))  # Expected: False

    # Test Case 5: More than one edit distance
    print(isOneEditDistance("abc", "abcdx"))  # Expected: False

    # Test Case 6: Empty string and one character
    print(isOneEditDistance("", "a"))  # Expected: True

    # Test Case 7: Empty string and two characters
    print(isOneEditDistance("", "ab"))  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the shorter string `s` once, so the time complexity is O(min(len(s), len(t))).

Space Complexity:
- The algorithm uses constant space, so the space complexity is O(1).

Topic: Strings
"""