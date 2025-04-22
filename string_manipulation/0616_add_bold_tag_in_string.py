"""
LeetCode Question #616: Add Bold Tag in String

Problem Statement:
You are given a string `s` and an array of strings `words`. You need to add a bold tag `<b>` and `</b>` to substrings in `s` that match any string in the `words` array. If two such substrings overlap, you should wrap them together in a single pair of bold tags. If two substrings are consecutive, you should also wrap them together in a single pair of bold tags.

Return the resulting string after adding the bold tags.

Constraints:
- `1 <= s.length <= 10^4`
- `0 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `s` and `words[i]` consist of lowercase English letters.

Example 1:
Input: s = "abcxyz123", words = ["abc", "123"]
Output: "<b>abc</b>xyz<b>123</b>"

Example 2:
Input: s = "aaabbcc", words = ["aaa", "aab", "bc"]
Output: "<b>aaabbc</b>c"

Note:
- The returned string should use the least number of tags possible.
"""

def addBoldTag(s: str, words: list[str]) -> str:
    """
    Adds bold tags around substrings in `s` that match any string in `words`.
    """
    n = len(s)
    bold = [False] * n  # Array to mark bold regions

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
    s1 = "abcxyz123"
    words1 = ["abc", "123"]
    print(addBoldTag(s1, words1))  # Output: "<b>abc</b>xyz<b>123</b>"

    # Test Case 2
    s2 = "aaabbcc"
    words2 = ["aaa", "aab", "bc"]
    print(addBoldTag(s2, words2))  # Output: "<b>aaabbc</b>c"

    # Test Case 3
    s3 = "abcdef"
    words3 = ["gh", "ij"]
    print(addBoldTag(s3, words3))  # Output: "abcdef" (no bold tags)

    # Test Case 4
    s4 = "aabbcc"
    words4 = ["a", "b", "c"]
    print(addBoldTag(s4, words4))  # Output: "<b>aabbcc</b>"

    # Test Case 5
    s5 = "xyz"
    words5 = []
    print(addBoldTag(s5, words5))  # Output: "xyz" (no bold tags)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the length of the string `s` and `m` be the total number of characters across all words in `words`.
- For each word in `words`, we search for all occurrences in `s` using `s.find()`. In the worst case, this takes O(n) time per word.
- If there are `k` words in `words`, the total time complexity is O(k * n).

Space Complexity:
- The `bold` array requires O(n) space.
- The result list also requires O(n) space.
- Overall, the space complexity is O(n).

Topic: String Manipulation
"""