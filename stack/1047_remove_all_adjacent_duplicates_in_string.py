"""
LeetCode Question #1047: Remove All Adjacent Duplicates In String

Problem Statement:
You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since they are adjacent and equal, and this is the only possible move. The result of this move is that the string is "aaca", of which only "aa" is possible to remove next. After the second removal, the string is "ca", which is the final answer.

Example 2:
Input: s = "azxxzy"
Output: "ay"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

# Solution
def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the last character if it's the same as the current one
        else:
            stack.append(char)  # Add the current character to the stack
    return ''.join(stack)  # Convert the stack back to a string

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abbaca"
    print(removeDuplicates(s1))  # Output: "ca"

    # Test Case 2
    s2 = "azxxzy"
    print(removeDuplicates(s2))  # Output: "ay"

    # Test Case 3
    s3 = "a"
    print(removeDuplicates(s3))  # Output: "a"

    # Test Case 4
    s4 = "aa"
    print(removeDuplicates(s4))  # Output: ""

    # Test Case 5
    s5 = "abccba"
    print(removeDuplicates(s5))  # Output: ""

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity depends on the stack used to store characters. In the worst case, the stack could store all characters of the string (if no duplicates are removed).
- Therefore, the space complexity is O(n), where n is the length of the string.
"""

# Topic: Stack