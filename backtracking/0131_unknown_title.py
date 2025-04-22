"""
LeetCode Problem #131: Palindrome Partitioning

Problem Statement:
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of `s`.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.
"""

# Solution
def partition(s: str) -> list[list[str]]:
    def is_palindrome(sub: str) -> bool:
        """Helper function to check if a string is a palindrome."""
        return sub == sub[::-1]

    def backtrack(start: int, path: list[str]):
        """Backtracking function to find all palindrome partitions."""
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aab"
    print(f"Input: {s1}")
    print(f"Output: {partition(s1)}")
    # Expected Output: [["a","a","b"],["aa","b"]]

    # Test Case 2
    s2 = "a"
    print(f"Input: {s2}")
    print(f"Output: {partition(s2)}")
    # Expected Output: [["a"]]

    # Test Case 3
    s3 = "racecar"
    print(f"Input: {s3}")
    print(f"Output: {partition(s3)}")
    # Expected Output: [["r","a","c","e","c","a","r"], ["r","aceca","r"], ["racecar"]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The backtracking algorithm explores all possible partitions of the string.
- For a string of length `n`, there are 2^(n-1) possible partitions (each character can either be split or not).
- For each partition, we check if the substrings are palindromes, which takes O(n) time in the worst case.
- Therefore, the overall time complexity is O(n * 2^(n-1)).

Space Complexity:
- The space complexity is dominated by the recursion stack and the space used to store the result.
- The recursion stack can go as deep as `n` (the length of the string).
- The result can contain up to 2^(n-1) partitions, each of which can have up to `n` substrings.
- Therefore, the space complexity is O(n * 2^(n-1)).
"""

# Topic: Backtracking