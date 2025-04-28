"""
LeetCode Problem #2390: Removing Stars From a String

Problem Statement:
You are given a string `s`, which contains stars `*`.

In one operation, you can:
- Choose a star in `s`.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters and stars `*`.
- The operation above can always be performed on the string.

Example:
Input: s = "leet**cod*e"
Output: "lecoe"

Input: s = "erase*****"
Output: ""
"""

# Clean and Correct Python Solution
def removeStars(s: str) -> str:
    stack = []
    for char in s:
        if char == '*':
            if stack:
                stack.pop()  # Remove the last non-star character
        else:
            stack.append(char)  # Add the character to the stack
    return ''.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leet**cod*e"
    print(removeStars(s1))  # Output: "lecoe"

    # Test Case 2
    s2 = "erase*****"
    print(removeStars(s2))  # Output: ""

    # Test Case 3
    s3 = "abc*de**f*g*"
    print(removeStars(s3))  # Output: "a"

    # Test Case 4
    s4 = "a*b*c*"
    print(removeStars(s4))  # Output: ""

    # Test Case 5
    s5 = "no*stars*here"
    print(removeStars(s5))  # Output: "nostarshere"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string `s` once, performing O(1) operations (push or pop) for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(n) in the worst case, where all characters in the string are non-star characters and are stored in the stack.
"""

# Topic: Stack