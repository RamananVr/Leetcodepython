"""
LeetCode Problem #1957: Delete Characters to Make Fancy String

Problem Statement:
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It will be guaranteed that the answer is unique.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
"""

def makeFancyString(s: str) -> str:
    """
    Function to delete characters from the input string to make it a fancy string.
    A fancy string is defined as a string where no three consecutive characters are equal.

    Args:
    s (str): The input string.

    Returns:
    str: The resulting fancy string.
    """
    result = []
    for char in s:
        # Only add the character if the last two characters in the result are not the same as the current character
        if len(result) < 2 or not (result[-1] == char and result[-2] == char):
            result.append(char)
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: No three consecutive characters
    s1 = "leeetcode"
    print(makeFancyString(s1))  # Expected Output: "leetcode"

    # Test Case 2: All characters are the same
    s2 = "aaa"
    print(makeFancyString(s2))  # Expected Output: "aa"

    # Test Case 3: Mixed characters with three consecutive ones
    s3 = "aabaaaa"
    print(makeFancyString(s3))  # Expected Output: "aabaa"

    # Test Case 4: Long string with multiple consecutive characters
    s4 = "aaabaaaaccaaa"
    print(makeFancyString(s4))  # Expected Output: "aabaaaccaa"

    # Test Case 5: Single character string
    s5 = "a"
    print(makeFancyString(s5))  # Expected Output: "a"

    # Test Case 6: Two-character string
    s6 = "aa"
    print(makeFancyString(s6))  # Expected Output: "aa"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the input string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The function uses a list `result` to store the characters of the fancy string.
- In the worst case, the size of `result` is equal to the size of the input string `s`.
- Therefore, the space complexity is O(n).

Topic: Strings
"""