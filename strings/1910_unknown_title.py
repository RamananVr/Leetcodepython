"""
LeetCode Problem #1910: Remove All Occurrences of a Substring

Problem Statement:
Given two strings `s` and `part`, perform the following operation repeatedly until `part` no longer exists in `s`:
- Find the first occurrence of the substring `part` in `s` and remove it.

Return `s` after all occurrences of `part` have been removed.

Note:
- The input strings `s` and `part` consist of lowercase English letters.
- It is guaranteed that `part` is not an empty string.

Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"

Explanation:
- The first occurrence of "abc" is removed from "daabcbaabcbc", resulting in "dabaabcbc".
- The next occurrence of "abc" is removed from "dabaabcbc", resulting in "dab".
- Now "abc" no longer exists in "dab", so the final result is "dab".

Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"

Constraints:
- 1 <= s.length <= 1000
- 1 <= part.length <= 100
- `part` is guaranteed to be a substring of `s` at least once.
"""

# Clean and Correct Python Solution
def removeOccurrences(s: str, part: str) -> str:
    while part in s:
        s = s.replace(part, "", 1)  # Replace the first occurrence of `part` with an empty string
    return s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "daabcbaabcbc"
    part1 = "abc"
    print(removeOccurrences(s1, part1))  # Expected Output: "dab"

    # Test Case 2
    s2 = "axxxxyyyyb"
    part2 = "xy"
    print(removeOccurrences(s2, part2))  # Expected Output: "ab"

    # Test Case 3
    s3 = "aabbaabb"
    part3 = "ab"
    print(removeOccurrences(s3, part3))  # Expected Output: ""

    # Test Case 4
    s4 = "hellohellohello"
    part4 = "hello"
    print(removeOccurrences(s4, part4))  # Expected Output: ""

    # Test Case 5
    s5 = "mississippi"
    part5 = "iss"
    print(removeOccurrences(s5, part5))  # Expected Output: "mippi"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(s) and m = len(part).
- In the worst case, we may need to scan the entire string `s` multiple times to remove all occurrences of `part`.
- Each `replace` operation takes O(n) time to find and remove the first occurrence of `part`.
- If there are k occurrences of `part` in `s`, the total time complexity is O(k * n).
- In the worst case, k can be approximately n / m (if `part` is repeated back-to-back in `s`), so the time complexity becomes O((n / m) * n) = O(n^2 / m).

Space Complexity:
- The `replace` method creates a new string each time it is called, so the space complexity is O(n) for the new string.
- The overall space complexity is O(n).

Primary Topic: Strings
"""