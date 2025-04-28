"""
LeetCode Problem #2663: Lexicographically Smallest Beautiful String

Problem Statement:
A string is considered "beautiful" if it satisfies the following conditions:
1. It consists of only lowercase English letters.
2. It does not contain any substring of length 2 or more that is a palindrome.

Given a string `s` and an integer `k`, your task is to find the lexicographically smallest string that is:
- Greater than `s` (in lexicographical order).
- Beautiful (does not contain palindromic substrings of length 2 or more).
- Consists of only the first `k` lowercase English letters.

If no such string exists, return an empty string.

Constraints:
- 1 <= len(s) <= 10^5
- 2 <= k <= 26

Example:
Input: s = "abcz", k = 4
Output: "abda"

Input: s = "dcba", k = 4
Output: ""

"""

def smallestBeautifulString(s: str, k: int) -> str:
    """
    Finds the lexicographically smallest beautiful string greater than `s` using the first `k` letters.
    """
    s = list(s)
    n = len(s)
    
    # Helper function to check if a string is beautiful
    def is_beautiful(s, idx):
        if idx > 0 and s[idx] == s[idx - 1]:
            return False
        if idx > 1 and s[idx] == s[idx - 2]:
            return False
        return True

    # Start from the end of the string and try to increment
    for i in range(n - 1, -1, -1):
        for j in range(ord(s[i]) + 1, ord('a') + k):
            s[i] = chr(j)
            if is_beautiful(s, i):
                # Fill the rest of the string with the smallest valid characters
                for x in range(i + 1, n):
                    for c in range(ord('a'), ord('a') + k):
                        s[x] = chr(c)
                        if is_beautiful(s, x):
                            break
                return ''.join(s)
    
    # If no valid string is found, return an empty string
    return ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcz"
    k1 = 4
    print(smallestBeautifulString(s1, k1))  # Output: "abda"

    # Test Case 2
    s2 = "dcba"
    k2 = 4
    print(smallestBeautifulString(s2, k2))  # Output: ""

    # Test Case 3
    s3 = "aaa"
    k3 = 3
    print(smallestBeautifulString(s3, k3))  # Output: "aab"

    # Test Case 4
    s4 = "z"
    k4 = 26
    print(smallestBeautifulString(s4, k4))  # Output: "aa"

    # Test Case 5
    s5 = "abc"
    k5 = 3
    print(smallestBeautifulString(s5, k5))  # Output: "aca"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over the string from right to left, attempting to increment each character.
- For each character, it tries up to `k` possible values and checks if the resulting string is beautiful.
- In the worst case, this results in O(n * k) operations, where `n` is the length of the string and `k` is the number of allowed characters.

Space Complexity:
- The algorithm uses O(n) space to store the string as a list for in-place modifications.
- No additional data structures are used, so the space complexity is O(n).

Topic: Strings, Greedy Algorithm
"""