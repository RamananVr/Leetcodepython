"""
LeetCode Question #394: Decode String

Problem Statement:
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like `3a` or `2[4]`.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets.
- s is guaranteed to be a valid input.
"""

# Solution
def decodeString(s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            prev_string, num = stack.pop()
            current_string = prev_string + num * current_string
        else:
            current_string += char

    return current_string

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "3[a]2[bc]"
    print(decodeString(s1))  # Output: "aaabcbc"

    # Test Case 2
    s2 = "3[a2[c]]"
    print(decodeString(s2))  # Output: "accaccacc"

    # Test Case 3
    s3 = "2[abc]3[cd]ef"
    print(decodeString(s3))  # Output: "abcabccdcdcdef"

    # Test Case 4
    s4 = "10[a]"
    print(decodeString(s4))  # Output: "aaaaaaaaaa"

    # Test Case 5
    s5 = "3[a2[b4[F]c]]"
    print(decodeString(s5))  # Output: "abFFFFcbFFFFcabFFFFcbFFFFc"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each character in the input string `s` exactly once.
- For each closing bracket `]`, the algorithm performs a string multiplication operation, which takes O(k) time, where `k` is the number of repetitions.
- In the worst case, the total time complexity is O(n * m), where `n` is the length of the string and `m` is the maximum number of repetitions.

Space Complexity:
- The space complexity is O(n), where `n` is the length of the input string. This is due to the stack used to store intermediate results and numbers.

Topic: Stack
"""