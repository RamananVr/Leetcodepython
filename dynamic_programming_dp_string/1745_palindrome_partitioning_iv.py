"""
LeetCode Question #1745: Palindrome Partitioning IV

Problem Statement:
Given a string `s`, return `true` if it is possible to split the string `s` into three non-empty palindromic substrings. Otherwise, return `false`.

A string is a palindrome if it reads the same forward and backward.

Constraints:
- `3 <= s.length <= 2000`
- `s` consists only of lowercase English letters.
"""

def checkPartitioning(s: str) -> bool:
    """
    Determines if the string `s` can be split into three non-empty palindromic substrings.
    """
    n = len(s)

    # Step 1: Precompute a 2D DP table to check if s[i:j+1] is a palindrome
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True  # Single character is always a palindrome
    for length in range(2, n + 1):  # Check substrings of length 2 and above
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    is_palindrome[i][j] = True  # Two-character palindrome
                else:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1]  # Check inner substring

    # Step 2: Try all possible partitions into three parts
    for i in range(1, n - 1):  # First cut
        if is_palindrome[0][i - 1]:  # First part is a palindrome
            for j in range(i + 1, n):  # Second cut
                if is_palindrome[i][j - 1] and is_palindrome[j][n - 1]:  # Second and third parts are palindromes
                    return True

    return False


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Example from the problem statement
    s1 = "abcbdd"
    print(checkPartitioning(s1))  # Expected output: True

    # Test Case 2: Another valid partition
    s2 = "bcbddxy"
    print(checkPartitioning(s2))  # Expected output: False

    # Test Case 3: Edge case with minimum length
    s3 = "aaa"
    print(checkPartitioning(s3))  # Expected output: True

    # Test Case 4: No valid partition
    s4 = "abcdef"
    print(checkPartitioning(s4))  # Expected output: False

    # Test Case 5: All characters are the same
    s5 = "aaaaaa"
    print(checkPartitioning(s5))  # Expected output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing the `is_palindrome` table takes O(n^2) time, where `n` is the length of the string.
- The nested loops for trying all possible partitions take O(n^2) time in the worst case.
- Overall time complexity: O(n^2).

Space Complexity:
- The `is_palindrome` table requires O(n^2) space.
- Other variables use O(1) additional space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming (DP), String
"""