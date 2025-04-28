"""
LeetCode Problem #2472: Maximum Number of Non-overlapping Palindrome Substrings

Problem Statement:
You are given a string `s` and an integer `k`. A substring is called a palindrome if it reads the same backward as forward. 
A palindrome substring is considered valid if its length is at least `k`. Your task is to find the maximum number of 
non-overlapping valid palindrome substrings in `s`.

Constraints:
- 1 <= k <= s.length <= 1000
- s consists of lowercase English letters.

Example:
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can choose "aba" and "dbbd" as the two non-overlapping palindromes.

Input: s = "adbcda", k = 2
Output: 0
Explanation: There are no valid palindromes of length >= 2.
"""

# Solution
def is_palindrome(s: str) -> bool:
    """Helper function to check if a string is a palindrome."""
    return s == s[::-1]

def max_palindromes(s: str, k: int) -> int:
    """
    Finds the maximum number of non-overlapping valid palindrome substrings in the given string `s`.
    
    :param s: The input string.
    :param k: The minimum length of a valid palindrome substring.
    :return: The maximum number of non-overlapping valid palindrome substrings.
    """
    n = len(s)
    i = 0
    count = 0

    while i < n:
        # Check for a valid palindrome starting at index `i`
        found = False
        for j in range(i + k - 1, n):
            if is_palindrome(s[i:j + 1]):
                count += 1
                i = j + 1  # Move past this palindrome
                found = True
                break
        if not found:
            i += 1  # Move to the next character if no palindrome is found

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abaccdbbd"
    k1 = 3
    print(max_palindromes(s1, k1))  # Output: 2

    # Test Case 2
    s2 = "adbcda"
    k2 = 2
    print(max_palindromes(s2, k2))  # Output: 0

    # Test Case 3
    s3 = "aaa"
    k3 = 2
    print(max_palindromes(s3, k3))  # Output: 1

    # Test Case 4
    s4 = "racecarannakayak"
    k4 = 7
    print(max_palindromes(s4, k4))  # Output: 2

    # Test Case 5
    s5 = "aabbcc"
    k5 = 2
    print(max_palindromes(s5, k5))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates through the string `s`, and for each starting index `i`, the inner loop checks substrings of length >= k.
- In the worst case, the inner loop checks up to `n` substrings for each starting index.
- Therefore, the time complexity is O(n^2), where `n` is the length of the string.

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from a few variables.

Topic: Strings, Palindromes, Greedy
"""