"""
LeetCode Question #727: Minimum Window Subsequence

Problem Statement:
Given strings `S` and `T`, find the minimum window in `S` which will contain all the characters in `T` in the same order as they appear in `T`.

If there is no such window in `S` that covers all characters in `T`, return the empty string `""`. If there are multiple such minimum-length windows, return the one that appears first.

Example 1:
Input: S = "abcdebdde", T = "bde"
Output: "bcde"

Example 2:
Input: S = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", T = "u"
Output: ""

Constraints:
- `S` and `T` consist of lowercase English letters.
- The length of `S` and `T` will not exceed 1000.

"""

# Solution
def minWindow(S: str, T: str) -> str:
    m, n = len(S), len(T)
    start, min_len = -1, float('inf')
    
    # Two pointers approach
    i, j = 0, 0
    while i < m:
        # Move j to match T[j] with S[i]
        if S[i] == T[j]:
            j += 1
            # If we matched the entire T
            if j == n:
                end = i + 1
                j -= 1
                # Move i backward to find the minimum window
                while j >= 0:
                    if S[i] == T[j]:
                        j -= 1
                    i -= 1
                i += 1
                j += 1
                # Update the minimum window
                if end - i < min_len:
                    start, min_len = i, end - i
        i += 1
    
    return "" if start == -1 else S[start:start + min_len]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    S1 = "abcdebdde"
    T1 = "bde"
    print(minWindow(S1, T1))  # Output: "bcde"

    # Test Case 2
    S2 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
    T2 = "u"
    print(minWindow(S2, T2))  # Output: ""

    # Test Case 3
    S3 = "abcde"
    T3 = "ace"
    print(minWindow(S3, T3))  # Output: "abcde"

    # Test Case 4
    S4 = "abcdebdde"
    T4 = "bd"
    print(minWindow(S4, T4))  # Output: "bd"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a two-pointer approach to traverse the string `S` while matching characters of `T`.
- In the worst case, we traverse `S` multiple times (once forward and once backward for each match of `T`).
- Therefore, the time complexity is O(m * n), where `m` is the length of `S` and `n` is the length of `T`.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

"""

# Topic: Two Pointers, String Matching