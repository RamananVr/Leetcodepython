"""
LeetCode Question #159: Longest Substring with At Most Two Distinct Characters

Problem Statement:
Given a string `s`, find the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters.
"""

def length_of_longest_substring_two_distinct(s: str) -> int:
    """
    Finds the length of the longest substring with at most two distinct characters.

    :param s: Input string
    :return: Length of the longest substring with at most two distinct characters
    """
    # Edge case: if the string is empty, return 0
    if not s:
        return 0

    # Sliding window approach
    left = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):
        # Add the current character to the dictionary
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # If there are more than 2 distinct characters, shrink the window
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "eceba"
    print(length_of_longest_substring_two_distinct(s1))  # Output: 3

    # Test Case 2
    s2 = "ccaabbb"
    print(length_of_longest_substring_two_distinct(s2))  # Output: 5

    # Test Case 3
    s3 = "a"
    print(length_of_longest_substring_two_distinct(s3))  # Output: 1

    # Test Case 4
    s4 = "abaccc"
    print(length_of_longest_substring_two_distinct(s4))  # Output: 4

    # Test Case 5
    s5 = "abcabcabc"
    print(length_of_longest_substring_two_distinct(s5))  # Output: 2

"""
Time Complexity:
- The algorithm uses a sliding window approach, where each character is processed at most twice (once when expanding the window and once when shrinking it).
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(1) because the `char_count` dictionary will store at most 2 distinct characters at any given time.

Topic: Sliding Window
"""