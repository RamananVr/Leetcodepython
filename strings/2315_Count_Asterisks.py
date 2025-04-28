"""
LeetCode Problem #2315: Count Asterisks

Problem Statement:
You are given a string `s`, where every two consecutive vertical bars '|' separate a group of characters. 
For example, the string "ab|cd|ef" has three groups: "ab", "cd", and "ef".

Asterisks '*' can appear anywhere in the string. Asterisks between each pair of consecutive vertical bars 
are considered "excluded" from the count. Note that each pair of vertical bars must contain at least one 
character.

Return the number of asterisks in the string that are not between pairs of vertical bars.

Example 1:
Input: s = "l|*e*et|c**o|*de|"
Output: 2
Explanation: The asterisks outside the pairs of '|' are the 2nd and 3rd asterisks.

Example 2:
Input: s = "iamprogrammer"
Output: 0
Explanation: There are no asterisks in the string.

Example 3:
Input: s = "yo|uar|e**|b|e***au|tifu|l"
Output: 5
Explanation: The asterisks outside the pairs of '|' are the 1st, 2nd, 3rd, 4th, and 5th asterisks.

Constraints:
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters, vertical bars '|', and asterisks '*'.
- `s` contains at least one vertical bar '|'.
"""

def countAsterisks(s: str) -> int:
    """
    Counts the number of asterisks '*' in the string `s` that are not between pairs of vertical bars '|'.
    
    :param s: Input string containing lowercase letters, '|', and '*'.
    :return: Number of asterisks outside pairs of vertical bars.
    """
    count = 0
    in_bar_section = False

    for char in s:
        if char == '|':
            in_bar_section = not in_bar_section  # Toggle the in_bar_section flag
        elif char == '*' and not in_bar_section:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "l|*e*et|c**o|*de|"
    print(countAsterisks(s1))  # Output: 2

    # Test Case 2
    s2 = "iamprogrammer"
    print(countAsterisks(s2))  # Output: 0

    # Test Case 3
    s3 = "yo|uar|e**|b|e***au|tifu|l"
    print(countAsterisks(s3))  # Output: 5

    # Additional Test Case 4
    s4 = "*|*|*|*|*"
    print(countAsterisks(s4))  # Output: 0

    # Additional Test Case 5
    s5 = "a*b|c*d|e*f"
    print(countAsterisks(s5))  # Output: 2

"""
Time Complexity Analysis:
- The solution iterates through the string `s` once, making it O(n), where `n` is the length of the string.

Space Complexity Analysis:
- The solution uses a constant amount of extra space (only a few variables), making it O(1).

Topic: Strings
"""