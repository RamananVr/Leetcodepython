"""
LeetCode Problem #647: Palindromic Substrings

Problem Statement:
Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""

def countSubstrings(s: str) -> int:
    """
    This function counts the number of palindromic substrings in the input string `s`.
    """
    n = len(s)
    count = 0

    # Helper function to expand around the center
    def expandAroundCenter(left: int, right: int) -> int:
        nonlocal count
        local_count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            local_count += 1
            left -= 1
            right += 1
        return local_count

    # Iterate through each possible center
    for i in range(n):
        # Odd-length palindromes (single character center)
        count += expandAroundCenter(i, i)
        # Even-length palindromes (two character center)
        count += expandAroundCenter(i, i + 1)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(f"Input: {s1} -> Output: {countSubstrings(s1)}")  # Expected: 3

    # Test Case 2
    s2 = "aaa"
    print(f"Input: {s2} -> Output: {countSubstrings(s2)}")  # Expected: 6

    # Test Case 3
    s3 = "racecar"
    print(f"Input: {s3} -> Output: {countSubstrings(s3)}")  # Expected: 10

    # Test Case 4
    s4 = "a"
    print(f"Input: {s4} -> Output: {countSubstrings(s4)}")  # Expected: 1

    # Test Case 5
    s5 = "abac"
    print(f"Input: {s5} -> Output: {countSubstrings(s5)}")  # Expected: 5

"""
Time Complexity Analysis:
- The function iterates through each character in the string as a potential center (O(n)).
- For each center, it expands outward to check for palindromes. In the worst case, this expansion takes O(n) time.
- Therefore, the overall time complexity is O(n^2).

Space Complexity Analysis:
- The function uses a constant amount of extra space (O(1)).

Topic: Dynamic Programming / String Manipulation
"""