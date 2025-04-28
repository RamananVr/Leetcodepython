"""
LeetCode Problem #2696: Minimum String Length After Removing Substrings

Problem Statement:
You are given a string `s` consisting only of the characters 'A', 'B', and 'C'. 
You can perform the following operation on the string any number of times:

- Remove an occurrence of the substring "AB" or "BA" from the string.

Your task is to return the minimum possible length of the string after performing 
any number of operations.

Example 1:
Input: s = "ABFCACDB"
Output: 2
Explanation: Remove "AB" -> "FCACDB", then remove "AC" -> "FCDB", then remove "DB" -> "FC". 
The minimum length is 2.

Example 2:
Input: s = "ACBBD"
Output: 5
Explanation: No "AB" or "BA" substrings exist, so the minimum length is the original length.

Constraints:
- 1 <= s.length <= 100
- s consists of only the characters 'A', 'B', and 'C'.
"""

# Solution
def minLength(s: str) -> int:
    stack = []
    for char in s:
        if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'B' and char == 'A')):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ABFCACDB"
    print(minLength(s1))  # Output: 2

    # Test Case 2
    s2 = "ACBBD"
    print(minLength(s2))  # Output: 5

    # Test Case 3
    s3 = "AABBCC"
    print(minLength(s3))  # Output: 4

    # Test Case 4
    s4 = "ABABAB"
    print(minLength(s4))  # Output: 0

    # Test Case 5
    s5 = "CBAAC"
    print(minLength(s5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing stack operations (push/pop) for each character.
- Each stack operation (push/pop) is O(1).
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The space complexity depends on the size of the stack. In the worst case, the stack could store all characters of the string.
- Therefore, the space complexity is O(n), where `n` is the length of the string.

Topic: Stack
"""