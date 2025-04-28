"""
LeetCode Problem #806: Number of Lines To Write String

Problem Statement:
You are given a string `s` of lowercase English letters and an array `widths`, where `widths[0]` is the width of the letter 'a', `widths[1]` is the width of the letter 'b', and so on.

You want to write the string `s` on a series of lines. Each line can have a maximum width of 100 units. The string is written sequentially, starting from the first character of `s`.

Return an array `result` of length 2:
- `result[0]` is the total number of lines required.
- `result[1]` is the width of the last line used in writing the string.

Example:
Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation:
All letters have the same width of 10. To write all 26 letters:
- The first 10 letters take up 100 units (1 line).
- The next 10 letters take up 100 units (2nd line).
- The last 6 letters take up 60 units (3rd line).

Constraints:
- `widths.length == 26`
- `2 <= widths[i] <= 10`
- `1 <= s.length <= 1000`
- `s` contains only lowercase English letters.
"""

def numberOfLines(widths, s):
    """
    Calculate the number of lines and the width of the last line required to write the string `s`.

    :param widths: List[int] - An array of 26 integers representing the widths of each letter.
    :param s: str - The string to be written.
    :return: List[int] - A list containing the number of lines and the width of the last line.
    """
    max_width = 100
    lines = 1
    current_width = 0

    for char in s:
        char_width = widths[ord(char) - ord('a')]
        if current_width + char_width > max_width:
            lines += 1
            current_width = char_width
        else:
            current_width += char_width

    return [lines, current_width]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "abcdefghijklmnopqrstuvwxyz"
    print(numberOfLines(widths, s))  # Output: [3, 60]

    # Test Case 2
    widths = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    s = "bbbcccdddaaa"
    print(numberOfLines(widths, s))  # Output: [2, 16]

    # Test Case 3
    widths = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    s = "hello"
    print(numberOfLines(widths, s))  # Output: [1, 25]

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the length of the string `s`. We iterate through each character in the string once.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.

# Topic: Arrays