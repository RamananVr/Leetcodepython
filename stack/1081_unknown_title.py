"""
LeetCode Problem #1081: Smallest Subsequence of Distinct Characters

Problem Statement:
Given a string s, return the smallest subsequence of s that contains all the distinct characters of s exactly once.
The result must be in lexicographical order.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

Example:
Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
"""

# Solution
def smallestSubsequence(s: str) -> str:
    """
    Returns the smallest subsequence of s that contains all distinct characters exactly once
    in lexicographical order.
    """
    # Dictionary to store the last occurrence of each character
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    
    # Stack to build the result
    stack = []
    
    # Set to track characters already in the stack
    in_stack = set()
    
    for idx, char in enumerate(s):
        # If the character is already in the stack, skip it
        if char in in_stack:
            continue
        
        # Remove characters from the stack that are lexicographically larger than the current character
        # and can still appear later in the string
        while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
            removed_char = stack.pop()
            in_stack.remove(removed_char)
        
        # Add the current character to the stack and mark it as in the stack
        stack.append(char)
        in_stack.add(char)
    
    # Join the stack to form the result string
    return ''.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bcabc"
    print(smallestSubsequence(s1))  # Output: "abc"

    # Test Case 2
    s2 = "cbacdcbc"
    print(smallestSubsequence(s2))  # Output: "acdb"

    # Test Case 3
    s3 = "abacb"
    print(smallestSubsequence(s3))  # Output: "abc"

    # Test Case 4
    s4 = "aaaaa"
    print(smallestSubsequence(s4))  # Output: "a"

    # Test Case 5
    s5 = "edcbaedcba"
    print(smallestSubsequence(s5))  # Output: "abcde"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, which takes O(n) time.
- The operations on the stack (push, pop, and membership checks) are O(1) on average.
- Therefore, the overall time complexity is O(n), where n is the length of the string.

Space Complexity:
- The `last_occurrence` dictionary stores the last index of each character, which requires O(26) space (constant for lowercase English letters).
- The `stack` and `in_stack` set can each store up to O(26) characters (constant for lowercase English letters).
- Therefore, the overall space complexity is O(n) for the input string and O(1) for auxiliary data structures.

Topic: Stack
"""