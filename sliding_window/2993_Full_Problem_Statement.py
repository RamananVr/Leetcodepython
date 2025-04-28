"""
LeetCode Problem #2993: Full Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode does not have a problem numbered 2993. 
If this problem exists, its details are unavailable to me. Instead, I will create a hypothetical 
problem statement for demonstration purposes.)

Problem Statement:
You are given a string `s` consisting of lowercase English letters. Your task is to find the 
length of the longest substring of `s` that contains at most two distinct characters.

Write a function `length_of_longest_substring_two_distinct(s: str) -> int` that returns the 
length of the longest substring with at most two distinct characters.

Constraints:
- 1 <= len(s) <= 10^5
- `s` consists of lowercase English letters.

Example:
Input: s = "eceba"
Output: 3
Explanation: The substring "ece" contains 2 distinct characters and is the longest such substring.

Input: s = "ccaabbb"
Output: 5
Explanation: The substring "aabbb" contains 2 distinct characters and is the longest such substring.
"""

# Solution
def length_of_longest_substring_two_distinct(s: str) -> int:
    """
    Finds the length of the longest substring with at most two distinct characters.
    
    Args:
    s (str): Input string consisting of lowercase English letters.
    
    Returns:
    int: Length of the longest substring with at most two distinct characters.
    """
    from collections import defaultdict

    # Sliding window approach
    left = 0
    char_count = defaultdict(int)
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

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
    s4 = "abc"
    print(length_of_longest_substring_two_distinct(s4))  # Output: 2

    # Test Case 5
    s5 = "aaaa"
    print(length_of_longest_substring_two_distinct(s5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the string once.
- The `left` pointer adjusts as needed, but each character is processed at most twice (once when added and once when removed).
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(1) for the `char_count` dictionary, as it stores at most 2 distinct characters at any time.
- Thus, the space complexity is O(1).

Topic: Sliding Window
"""