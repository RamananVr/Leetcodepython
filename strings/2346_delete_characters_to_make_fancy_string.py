"""
LeetCode Question #2346: Delete Characters to Make Fancy String

Problem Statement:
A fancy string is a string where no three consecutive characters are equal. 
Given a string s, delete the minimum number of characters from s to make it fancy.

Return the final string after the deletion. It will be guaranteed that the answer is unique.

Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation: Remove an 'e' at index 1 to make "leetcode" fancy.

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation: Remove an 'a' at index 2 and at index 5 to make "aabaa" fancy.

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so no need to delete anything.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
"""

# Solution
def makeFancyString(s: str) -> str:
    """
    Function to delete characters from the string to make it fancy.
    A fancy string is a string where no three consecutive characters are equal.
    
    :param s: Input string
    :return: Fancy string after deletion
    """
    result = []
    for char in s:
        # Check if the last two characters in the result are the same as the current character
        if len(result) >= 2 and result[-1] == char and result[-2] == char:
            continue
        result.append(char)
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leeetcode"
    print(makeFancyString(s1))  # Output: "leetcode"

    # Test Case 2
    s2 = "aaabaaaa"
    print(makeFancyString(s2))  # Output: "aabaa"

    # Test Case 3
    s3 = "aab"
    print(makeFancyString(s3))  # Output: "aab"

    # Test Case 4
    s4 = "aaa"
    print(makeFancyString(s4))  # Output: "aa"

    # Test Case 5
    s5 = "a"
    print(makeFancyString(s5))  # Output: "a"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The function uses a list `result` to store the characters of the fancy string.
- In the worst case, the size of `result` is equal to the size of the input string `s`.
- Therefore, the space complexity is O(n).
"""

# Topic: Strings