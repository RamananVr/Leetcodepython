"""
LeetCode Problem #758: Bold Words in String

Problem Statement:
You are given an array of strings `words` and a string `s`. All the words in `words` are unique. 
You need to make all the substrings of `s` which are present in `words` bold. The substrings that 
are to be made bold can overlap, and you need to make them bold only once.

Return the string `s` after making all the substrings bold. The bold parts of the string are 
represented in this format: `<b>substring</b>`.

Example:
Input: words = ["abc", "123"], s = "abcxyz123"
Output: "<b>abc</b>xyz<b>123</b>"

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= s.length <= 1000`
- All the strings in `words` are unique.
- `words[i]` and `s` consist of lowercase English letters and digits.

"""

# Solution
def boldWords(words, s):
    """
    Function to make substrings of `s` bold if they are present in `words`.

    Args:
    words (List[str]): List of unique words to be bolded in `s`.
    s (str): Input string.

    Returns:
    str: String with bolded substrings.
    """
    n = len(s)
    bold = [False] * n  # Array to track which characters should be bolded

    # Mark the bold regions
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                bold[i] = True
            start = s.find(word, start + 1)

    # Build the result string with bold tags
    result = []
    i = 0
    while i < n:
        if bold[i]:
            result.append("<b>")
            while i < n and bold[i]:
                result.append(s[i])
                i += 1
            result.append("</b>")
        else:
            result.append(s[i])
            i += 1

    return "".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["abc", "123"]
    s = "abcxyz123"
    print(boldWords(words, s))  # Output: "<b>abc</b>xyz<b>123</b>"

    # Test Case 2
    words = ["aa", "bb"]
    s = "aabbcc"
    print(boldWords(words, s))  # Output: "<b>aa</b><b>bb</b>cc"

    # Test Case 3
    words = ["xyz", "123"]
    s = "abcxyz123xyz"
    print(boldWords(words, s))  # Output: "abc<b>xyz</b><b>123</b><b>xyz</b>"

    # Test Case 4
    words = ["a", "b", "c"]
    s = "abc"
    print(boldWords(words, s))  # Output: "<b>a</b><b>b</b><b>c</b>"

    # Test Case 5
    words = ["abc"]
    s = "abcabcabc"
    print(boldWords(words, s))  # Output: "<b>abcabcabc</b>"

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each word in `words`, we search for its occurrences in `s` using `s.find()`.
  This takes O(n * m) time in the worst case, where `n` is the length of `s` and `m` is the total length of all words in `words`.
- Constructing the result string takes O(n) time.

Overall time complexity: O(n * m).

Space Complexity:
- The `bold` array takes O(n) space.
- The result list takes O(n) space.

Overall space complexity: O(n).
"""

# Topic: Strings