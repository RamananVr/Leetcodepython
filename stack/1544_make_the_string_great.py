"""
LeetCode Question #1544: Make The String Great

Problem Statement:
Given a string `s` of lower and upper case English letters, a "good" string is a string where no two adjacent characters are of the same letter but have different cases. For example, "aA" and "Aa" are not good, but "abAB" and "aabAAB" are good.

You are given a string `s`. A good string can be obtained by making zero or more deletions from `s`. Return the smallest good string that can be obtained from `s`.

The resulting string should be returned as a new string.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, remove the character 'E' at index 2, then remove the character 'e' at index 1. Now the string is "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: The entire string is removed since all characters are in conflict.

Example 3:
Input: s = "s"
Output: "s"

Constraints:
- 1 <= s.length <= 100
- s contains only lower and upper case English letters.
"""

# Solution
def makeGood(s: str) -> str:
    stack = []
    for char in s:
        # Check if the stack is not empty and the top of the stack conflicts with the current character
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()  # Remove the conflicting character
        else:
            stack.append(char)  # Add the current character to the stack
    return ''.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leEeetcode"
    print(makeGood(s1))  # Output: "leetcode"

    # Test Case 2
    s2 = "abBAcC"
    print(makeGood(s2))  # Output: ""

    # Test Case 3
    s3 = "s"
    print(makeGood(s3))  # Output: "s"

    # Test Case 4
    s4 = "Pp"
    print(makeGood(s4))  # Output: ""

    # Test Case 5
    s5 = "aAbBcCdD"
    print(makeGood(s5))  # Output: ""

    # Test Case 6
    s6 = "aAabBcC"
    print(makeGood(s6))  # Output: "ab"

"""
Time Complexity Analysis:
- The algorithm iterates through the string `s` once, processing each character exactly once.
- Each operation on the stack (push or pop) takes O(1) time.
- Therefore, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity Analysis:
- The stack is used to store characters from the string. In the worst case, all characters in `s` are added to the stack.
- Therefore, the space complexity is O(n), where `n` is the length of the string `s`.

Topic: Stack
"""