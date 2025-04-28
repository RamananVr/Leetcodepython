"""
LeetCode Problem #316: Remove Duplicate Letters

Problem Statement:
Given a string `s`, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Note:
- The input string `s` consists of lowercase English letters.
- The length of `s` is at most 10^4.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""

def removeDuplicateLetters(s: str) -> str:
    """
    Removes duplicate letters from the string `s` such that every letter appears once and only once,
    and the result is the smallest in lexicographical order among all possible results.
    """
    # Dictionary to store the last occurrence of each character
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    # Stack to build the result
    stack = []
    # Set to keep track of characters in the stack
    in_stack = set()

    for i, char in enumerate(s):
        # If the character is already in the stack, skip it
        if char in in_stack:
            continue

        # Remove characters from the stack if:
        # 1. The current character is smaller than the top of the stack (lexicographical order).
        # 2. The top of the stack character appears later in the string (we can add it back later).
        while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
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
    print(f"Input: {s1} -> Output: {removeDuplicateLetters(s1)}")  # Expected: "abc"

    # Test Case 2
    s2 = "cbacdcbc"
    print(f"Input: {s2} -> Output: {removeDuplicateLetters(s2)}")  # Expected: "acdb"

    # Test Case 3
    s3 = "abacb"
    print(f"Input: {s3} -> Output: {removeDuplicateLetters(s3)}")  # Expected: "abc"

    # Test Case 4
    s4 = "bbcaac"
    print(f"Input: {s4} -> Output: {removeDuplicateLetters(s4)}")  # Expected: "bac"

"""
Time Complexity Analysis:
- The algorithm iterates through the string `s` once, making it O(n), where `n` is the length of the string.
- Each character is pushed and popped from the stack at most once, so the stack operations are O(n) in total.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `last_occurrence` dictionary uses O(26) = O(1) space since there are at most 26 lowercase English letters.
- The `stack` and `in_stack` set can grow up to O(26) = O(1) space in the worst case.
- Overall space complexity: O(1).

Topic: Stack
"""