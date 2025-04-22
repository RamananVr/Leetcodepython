"""
LeetCode Question #3: Longest Substring Without Repeating Characters

Problem Statement:
Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols, and spaces.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    # Initialize a set to store characters in the current window
    char_set = set()
    # Initialize pointers and the result variable
    left = 0
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcabcbb"
    print(f"Input: {s1} -> Output: {length_of_longest_substring(s1)}")  # Expected: 3

    # Test Case 2
    s2 = "bbbbb"
    print(f"Input: {s2} -> Output: {length_of_longest_substring(s2)}")  # Expected: 1

    # Test Case 3
    s3 = "pwwkew"
    print(f"Input: {s3} -> Output: {length_of_longest_substring(s3)}")  # Expected: 3

    # Test Case 4
    s4 = ""
    print(f"Input: {s4} -> Output: {length_of_longest_substring(s4)}")  # Expected: 0

    # Test Case 5
    s5 = "dvdf"
    print(f"Input: {s5} -> Output: {length_of_longest_substring(s5)}")  # Expected: 3

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach with two pointers (left and right).
- Each character is added to and removed from the set at most once.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The space complexity is O(min(n, a)), where n is the length of the string and a is the size of the character set (e.g., 26 for lowercase English letters).
- In the worst case, the set can contain all unique characters in the string.

Topic: Sliding Window
"""