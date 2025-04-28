"""
LeetCode Problem #1147: Longest Chunked Palindrome Decomposition

Problem Statement:
You are given a string text. You should split it into k substrings (sub1, sub2, ..., subk) such that:
- sub1 + sub2 + ... + subk == text
- subi == subk-i+1 for all valid i (1 <= i <= k).

Return the largest possible value of k.

Example:
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string into "ghi", "abcdef", "hello", "adam", "hello", "abcdef", "ghi".

Constraints:
- 1 <= text.length <= 1000
- text consists of only lowercase English letters.
"""

def longestDecomposition(text: str) -> int:
    """
    This function computes the largest possible value of k for the given string text
    such that the string can be split into k substrings satisfying the conditions
    of the problem statement.
    """
    n = len(text)
    if n == 0:
        return 0

    for i in range(1, n // 2 + 1):
        if text[:i] == text[-i:]:
            # If the prefix and suffix match, recursively solve for the middle part
            return 2 + longestDecomposition(text[i:-i])

    # If no prefix-suffix match is found, the entire string is one chunk
    return 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "ghiabcdefhelloadamhelloabcdefghi"
    print(longestDecomposition(text1))  # Output: 7

    # Test Case 2
    text2 = "merchant"
    print(longestDecomposition(text2))  # Output: 1

    # Test Case 3
    text3 = "antaprezatepzapreanta"
    print(longestDecomposition(text3))  # Output: 11

    # Test Case 4
    text4 = "aaa"
    print(longestDecomposition(text4))  # Output: 3

"""
Time Complexity Analysis:
- Let n be the length of the string `text`.
- In the worst case, the function checks prefixes and suffixes of increasing lengths.
- Each prefix-suffix comparison takes O(k) time, where k is the length of the prefix/suffix.
- The total time complexity is O(n^2) in the worst case.

Space Complexity Analysis:
- The function uses recursion, and the maximum depth of recursion is O(n) in the worst case.
- Each recursive call creates a new substring, which takes O(n) space in the worst case.
- Therefore, the space complexity is O(n^2) in the worst case.

Topic: Dynamic Programming (DP), String Matching
"""