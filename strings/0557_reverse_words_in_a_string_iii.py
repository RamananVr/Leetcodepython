"""
LeetCode Question #557: Reverse Words in a String III

Problem Statement:
Given a string `s`, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
- 1 <= s.length <= 5 * 10^4
- `s` contains printable ASCII characters.
- `s` does not contain any leading or trailing spaces.
- There is at least one word in `s`.
- All the words in `s` are separated by a single space.
"""

# Clean and Correct Python Solution
def reverseWords(s: str) -> str:
    # Split the string into words, reverse each word, and join them back with spaces
    return ' '.join(word[::-1] for word in s.split())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "Let's take LeetCode contest"
    print(reverseWords(s1))  # Expected Output: "s'teL ekat edoCteeL tsetnoc"

    # Test Case 2
    s2 = "God Ding"
    print(reverseWords(s2))  # Expected Output: "doG gniD"

    # Test Case 3
    s3 = "Hello World"
    print(reverseWords(s3))  # Expected Output: "olleH dlroW"

    # Test Case 4
    s4 = "a b c"
    print(reverseWords(s4))  # Expected Output: "a b c"

    # Test Case 5
    s5 = "singleword"
    print(reverseWords(s5))  # Expected Output: "drowelgnis"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the string into words takes O(n), where n is the length of the string.
- Reversing each word takes O(k) for each word of length k. Summing over all words, this is O(n).
- Joining the reversed words back into a single string takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- Splitting the string into words creates a list of words, which takes O(n) space.
- Reversing each word creates a new string for each word, which also takes O(n) in total.
- The final joined string takes O(n) space.
- Overall, the space complexity is O(n).
"""

# Topic: Strings