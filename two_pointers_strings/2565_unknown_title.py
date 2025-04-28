"""
LeetCode Problem #2565: Subsequence With the Minimum Score

Problem Statement:
You are given two strings `s` and `t`. You are allowed to remove any number of characters from `s` 
to form a subsequence. The score of a subsequence is defined as the minimum number of characters 
you need to remove from `t` such that the subsequence of `s` is a subsequence of `t`.

Return the minimum score of a subsequence of `s`.

Constraints:
- 1 <= len(s), len(t) <= 10^5
- s and t consist of lowercase English letters.
"""

def minimumScore(s: str, t: str) -> int:
    """
    Function to calculate the minimum score of a subsequence of s.
    """
    n, m = len(s), len(t)
    
    # Step 1: Compute the prefix match of t with s
    prefix = [-1] * n
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            j += 1
        prefix[i] = j

    # Step 2: Compute the suffix match of t with s
    suffix = [m] * n
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            j -= 1
        suffix[i] = j

    # Step 3: Calculate the minimum score
    min_score = m  # Start with the maximum possible score
    for i in range(n - 1):
        min_score = min(min_score, max(0, suffix[i + 1] - prefix[i] - 1))
    
    # Edge cases: Remove all characters from t
    min_score = min(min_score, m - prefix[n - 1])  # All prefix matches
    min_score = min(min_score, suffix[0])         # All suffix matches

    return min_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    t1 = "abcbc"
    print(minimumScore(s1, t1))  # Expected Output: 1

    # Test Case 2
    s2 = "ab"
    t2 = "ba"
    print(minimumScore(s2, t2))  # Expected Output: 2

    # Test Case 3
    s3 = "abc"
    t3 = "def"
    print(minimumScore(s3, t3))  # Expected Output: 3

    # Test Case 4
    s4 = "a"
    t4 = "a"
    print(minimumScore(s4, t4))  # Expected Output: 0

    # Test Case 5
    s5 = "abc"
    t5 = "abcabc"
    print(minimumScore(s5, t5))  # Expected Output: 0

"""
Time Complexity:
- Computing the prefix array takes O(n + m) time, as we iterate through `s` and `t` once.
- Computing the suffix array also takes O(n + m) time.
- Calculating the minimum score involves iterating through `s` once, which takes O(n) time.
- Overall time complexity: O(n + m).

Space Complexity:
- We use two arrays, `prefix` and `suffix`, each of size O(n).
- Overall space complexity: O(n).

Topic: Two Pointers, Strings
"""