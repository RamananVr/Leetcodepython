"""
LeetCode Problem #266: Palindrome Permutation

Problem Statement:
Given a string `s`, return `true` if a permutation of the string could form a palindrome, and `false` otherwise.

A string is a palindrome if it reads the same forward and backward. A permutation of a string is a rearrangement of its letters.

Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true

Example 3:
Input: s = "carerac"
Output: true

Constraints:
- 1 <= s.length <= 5000
- s consists of only lowercase English letters.
"""

def canPermutePalindrome(s: str) -> bool:
    """
    Determines if any permutation of the input string can form a palindrome.

    Args:
    s (str): The input string.

    Returns:
    bool: True if a permutation of the string can form a palindrome, False otherwise.
    """
    # Use a set to track characters with odd counts
    odd_chars = set()
    
    for char in s:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    
    # A string can form a palindrome if at most one character has an odd count
    return len(odd_chars) <= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "code"
    print(f"Input: {s1} -> Output: {canPermutePalindrome(s1)}")  # Expected: False

    # Test Case 2
    s2 = "aab"
    print(f"Input: {s2} -> Output: {canPermutePalindrome(s2)}")  # Expected: True

    # Test Case 3
    s3 = "carerac"
    print(f"Input: {s3} -> Output: {canPermutePalindrome(s3)}")  # Expected: True

    # Test Case 4
    s4 = "a"
    print(f"Input: {s4} -> Output: {canPermutePalindrome(s4)}")  # Expected: True

    # Test Case 5
    s5 = "abc"
    print(f"Input: {s5} -> Output: {canPermutePalindrome(s5)}")  # Expected: False

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations (adding/removing from a set) for each character.
- Let n be the length of the string. The time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(1) because the set `odd_chars` can contain at most 26 characters (the lowercase English alphabet).

Topic: Hash Table / String
"""