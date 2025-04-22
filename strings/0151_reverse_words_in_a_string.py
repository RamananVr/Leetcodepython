"""
LeetCode Question #151: Reverse Words in a String

Problem Statement:
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note:
- Input string `s` may contain leading or trailing spaces or multiple spaces between two words.
- The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
- 1 <= s.length <= 10^4
- `s` contains English letters (upper-case and lower-case), digits, and spaces.
- There is at least one word in `s`.

Follow-up:
Could you solve it in-place with O(1) extra space?
"""

# Solution
def reverseWords(s: str) -> str:
    """
    Reverse the words in the input string `s`.

    :param s: Input string containing words separated by spaces.
    :return: A string with words reversed and separated by a single space.
    """
    # Split the string into words, ignoring extra spaces
    words = s.split()
    # Reverse the list of words and join them with a single space
    return " ".join(reversed(words))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "the sky is blue"
    print(reverseWords(s1))  # Output: "blue is sky the"

    # Test Case 2
    s2 = "  hello world  "
    print(reverseWords(s2))  # Output: "world hello"

    # Test Case 3
    s3 = "a good   example"
    print(reverseWords(s3))  # Output: "example good a"

    # Test Case 4
    s4 = "  LeetCode   is   awesome  "
    print(reverseWords(s4))  # Output: "awesome is LeetCode"

    # Test Case 5
    s5 = "singleword"
    print(reverseWords(s5))  # Output: "singleword"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the string into words using `split()` takes O(n), where n is the length of the string.
- Reversing the list of words using `reversed()` takes O(k), where k is the number of words.
- Joining the reversed words into a single string using `join()` takes O(n), where n is the total length of the words.
- Overall, the time complexity is O(n).

Space Complexity:
- The `split()` method creates a list of words, which takes O(n) space in the worst case.
- The `reversed()` function creates an iterator, which is O(1) in terms of space.
- The final string created by `join()` also takes O(n) space.
- Overall, the space complexity is O(n).

Topic: Strings
"""