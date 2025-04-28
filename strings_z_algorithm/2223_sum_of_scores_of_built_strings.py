"""
LeetCode Question #2223: Sum of Scores of Built Strings

Problem Statement:
You are given a string `s` of length `n`. A string `t` is called a built string of `s` if:
- `t` is a prefix of `s`, and
- `t` can be obtained by concatenating one or more copies of `s`.

For example, if `s = "abc"`, then "abc", "abcabc", "abcabcabc", etc., are built strings of `s`.

The score of a built string `t` is the number of characters in `t` that match the corresponding characters in `s`.

Return the sum of scores of all built strings of `s`.

Constraints:
- `1 <= n <= 10^5`
- `s` consists of lowercase English letters.

"""

# Solution
def sumScores(s: str) -> int:
    """
    Calculate the sum of scores of all built strings of the given string `s`.
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    # Compute Z-function
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    # Sum of scores
    return sum(z) + n  # Include the score for the original string `s`

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(sumScores(s1))  # Expected Output: 3

    # Test Case 2
    s2 = "aaa"
    print(sumScores(s2))  # Expected Output: 6

    # Test Case 3
    s3 = "ababab"
    print(sumScores(s3))  # Expected Output: 9

    # Test Case 4
    s4 = "a"
    print(sumScores(s4))  # Expected Output: 1

    # Test Case 5
    s5 = "abcdabcd"
    print(sumScores(s5))  # Expected Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The Z-function computation runs in O(n) time, where `n` is the length of the string `s`.
- Summing the Z-values and adding `n` takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The Z-function array `z` requires O(n) space.
- Other variables use O(1) space.
- Overall space complexity: O(n).

Topic: Strings, Z-Algorithm
"""