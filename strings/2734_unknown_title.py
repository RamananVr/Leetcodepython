"""
LeetCode Problem #2734: Lexicographically Smallest String After Substring Operation

Problem Statement:
You are given a string `s` consisting of only lowercase English letters. In one operation, you can do the following:
- Select any non-empty substring of `s` and replace all the characters in it with the previous letter in the alphabet. 
  For example, replace 'b' with 'a', 'c' with 'b', and so on. 'a' cannot be replaced.

Return the lexicographically smallest string you can obtain after performing the above operation exactly once.

Example:
Input: s = "cbabc"
Output: "baabc"

Input: s = "acbbc"
Output: "abaab"

Input: s = "leetcode"
Output: "kddsbncd"

Constraints:
- 1 <= s.length <= 3 * 10^5
- `s` consists of only lowercase English letters.
"""

def smallestString(s: str) -> str:
    """
    Returns the lexicographically smallest string after performing the operation exactly once.
    """
    n = len(s)
    s = list(s)  # Convert string to list for mutability
    started = False  # Flag to track if we started modifying the string

    for i in range(n):
        if s[i] != 'a':  # Replace characters that are not 'a'
            s[i] = chr(ord(s[i]) - 1)  # Replace with the previous letter in the alphabet
            started = True
        elif started:  # Stop modifying once we encounter 'a' after starting
            break

    # If no modification was made (all 'a's), change the last character
    if not started:
        s[-1] = 'z'

    return ''.join(s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cbabc"
    print(smallestString(s1))  # Expected Output: "baabc"

    # Test Case 2
    s2 = "acbbc"
    print(smallestString(s2))  # Expected Output: "abaab"

    # Test Case 3
    s3 = "leetcode"
    print(smallestString(s3))  # Expected Output: "kddsbncd"

    # Test Case 4
    s4 = "aaaaa"
    print(smallestString(s4))  # Expected Output: "aaaaz"

    # Test Case 5
    s5 = "a"
    print(smallestString(s5))  # Expected Output: "z"

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses O(n) space to store the mutable list representation of the string.
- Thus, the space complexity is O(n).

Topic: Strings
"""