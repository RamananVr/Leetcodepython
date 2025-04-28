"""
LeetCode Problem #1960: Maximum Product of the Length of Two Palindromic Substrings

Problem Statement:
You are given a string `s` of length `n`. Find the maximum product of the lengths of two palindromic substrings 
that do not overlap. The two substrings must be non-empty, and the product of their lengths should be maximized.

Formally, you need to find two indices `i` and `j` such that:
- 0 <= i < j < n
- The substring `s[0:i+1]` is a palindrome.
- The substring `s[j:n]` is a palindrome.
- The product of the lengths of these two substrings, `(i+1) * (n-j)`, is maximized.

Return the maximum product of the lengths of two palindromic substrings.

Constraints:
- 2 <= s.length <= 10^5
- `s` consists of lowercase English letters only.
"""

def maxProduct(s: str) -> int:
    """
    Function to calculate the maximum product of the lengths of two non-overlapping palindromic substrings.
    """
    n = len(s)
    
    # Step 1: Compute the maximum palindromic length ending at each index (left-to-right)
    left = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(left[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1
        left[i] = k - 1
        if i + left[i] > r:
            l, r = i - left[i], i + left[i]
    
    # Convert `left` to store the maximum palindromic length ending at each index
    max_left = [0] * n
    max_left[0] = 1
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], 2 * left[i] + 1)
    
    # Step 2: Compute the maximum palindromic length starting at each index (right-to-left)
    right = [0] * n
    l, r = 0, -1
    for i in range(n - 1, -1, -1):
        k = 1 if i > r else min(right[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1
        right[i] = k - 1
        if i + right[i] > r:
            l, r = i - right[i], i + right[i]
    
    # Convert `right` to store the maximum palindromic length starting at each index
    max_right = [0] * n
    max_right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], 2 * right[i] + 1)
    
    # Step 3: Calculate the maximum product of lengths
    max_product = 0
    for i in range(n - 1):
        max_product = max(max_product, max_left[i] * max_right[i + 1])
    
    return max_product

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ababbb"
    print(maxProduct(s1))  # Expected Output: 9 (palindromes: "aba" and "bbb")

    # Test Case 2
    s2 = "zaaaxbbby"
    print(maxProduct(s2))  # Expected Output: 9 (palindromes: "aaa" and "bbb")

    # Test Case 3
    s3 = "acdapmpomp"
    print(maxProduct(s3))  # Expected Output: 15 (palindromes: "aca" and "mpomp")

    # Test Case 4
    s4 = "aaaa"
    print(maxProduct(s4))  # Expected Output: 4 (palindromes: "aa" and "aa")

"""
Time Complexity:
- Computing the maximum palindromic lengths (left and right arrays) takes O(n) using a modified Manacher's algorithm.
- Calculating the maximum product takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use O(n) space for the `left`, `right`, `max_left`, and `max_right` arrays.
- Overall space complexity: O(n).

Topic: Strings, Palindromes, Dynamic Programming
"""