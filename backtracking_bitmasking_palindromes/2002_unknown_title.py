"""
LeetCode Problem #2002: Maximum Product of the Length of Two Palindromic Subsequences

Problem Statement:
Given a string `s`, split it into two disjoint subsequences such that the product of the lengths of the two subsequences is maximized. 
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. 
A string is palindromic if it reads the same forward and backward.

Return the maximum possible product of the lengths of the two palindromic subsequences.

Constraints:
- 2 <= s.length <= 12
- s consists of lowercase English letters only.
"""

from itertools import combinations

def is_palindrome(subsequence: str) -> bool:
    """Helper function to check if a string is a palindrome."""
    return subsequence == subsequence[::-1]

def maxProduct(s: str) -> int:
    """
    Function to calculate the maximum product of the lengths of two palindromic subsequences.
    """
    n = len(s)
    max_product = 0

    # Iterate over all possible subsets of indices
    for mask1 in range(1, 1 << n):  # mask1 represents the first subsequence
        subseq1 = ''.join(s[i] for i in range(n) if mask1 & (1 << i))
        if not is_palindrome(subseq1):
            continue

        for mask2 in range(1, 1 << n):  # mask2 represents the second subsequence
            if mask1 & mask2:  # Ensure the two subsequences are disjoint
                continue
            subseq2 = ''.join(s[i] for i in range(n) if mask2 & (1 << i))
            if is_palindrome(subseq2):
                max_product = max(max_product, len(subseq1) * len(subseq2))

    return max_product

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcodecom"
    print(maxProduct(s1))  # Expected Output: 9

    # Test Case 2
    s2 = "bb"
    print(maxProduct(s2))  # Expected Output: 1

    # Test Case 3
    s3 = "accbcaxxcxx"
    print(maxProduct(s3))  # Expected Output: 25

"""
Time Complexity Analysis:
- There are 2^n subsets of indices for a string of length n.
- For each subset, we check if the subsequence is a palindrome, which takes O(n) time.
- Thus, the total time complexity is O(2^n * n).

Space Complexity Analysis:
- The space complexity is O(n) for storing the subsequences during the computation.

Topic: Backtracking, Bitmasking, Palindromes
"""