"""
LeetCode Problem #340: Longest Substring with At Most K Distinct Characters

Problem Statement:
Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

If `k` is 0, return 0.

Constraints:
- 0 <= k <= s.length
- `s` consists of English letters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Example 3:
Input: s = "a", k = 0
Output: 0
Explanation: Since k is 0, no substring is valid.

Follow-up:
Could you solve it in O(n) time complexity?
"""

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Finds the length of the longest substring with at most k distinct characters.

    :param s: Input string
    :param k: Maximum number of distinct characters allowed
    :return: Length of the longest substring with at most k distinct characters
    """
    if k == 0:
        return 0

    # Dictionary to store the frequency of characters in the current window
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Add the current character to the window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # If the number of distinct characters exceeds k, shrink the window
        while len(char_count) > k:
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
    k1 = 2
    print(length_of_longest_substring_k_distinct(s1, k1))  # Output: 3

    # Test Case 2
    s2 = "aa"
    k2 = 1
    print(length_of_longest_substring_k_distinct(s2, k2))  # Output: 2

    # Test Case 3
    s3 = "a"
    k3 = 0
    print(length_of_longest_substring_k_distinct(s3, k3))  # Output: 0

    # Test Case 4
    s4 = "abcadcacacaca"
    k4 = 3
    print(length_of_longest_substring_k_distinct(s4, k4))  # Output: 10

    # Test Case 5
    s5 = "aabbcc"
    k5 = 2
    print(length_of_longest_substring_k_distinct(s5, k5))  # Output: 4

"""
Time Complexity:
- The algorithm processes each character in the string exactly once, as the `right` pointer iterates through the string.
- The `left` pointer also moves at most `n` times, where `n` is the length of the string.
- Thus, the time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where `k` is the maximum number of distinct characters allowed in the substring.
- This is because the `char_count` dictionary can store at most `k` keys.

Topic: Sliding Window
"""