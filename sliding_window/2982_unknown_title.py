"""
LeetCode Problem #2982: Find the Longest Substring Without Repeating Characters

Problem Statement:
Given a string `s`, find the length of the longest substring without repeating characters.

Constraints:
- 0 <= len(s) <= 5 * 10^4
- `s` consists of English letters, digits, symbols, and spaces.

You need to return the length of the longest substring of `s` that does not contain any repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repeating characters.
    """
    # Initialize a set to store characters in the current window
    char_set = set()
    # Initialize two pointers for the sliding window
    left = 0
    # Variable to store the maximum length of substring
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character at the right pointer is already in the set,
        # move the left pointer to the right until the character is removed
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
    # Test Case 1: General case with mixed characters
    s1 = "abcabcbb"
    print(f"Test Case 1: {length_of_longest_substring(s1)}")  # Expected Output: 3

    # Test Case 2: String with all unique characters
    s2 = "abcdef"
    print(f"Test Case 2: {length_of_longest_substring(s2)}")  # Expected Output: 6

    # Test Case 3: String with all identical characters
    s3 = "aaaaaa"
    print(f"Test Case 3: {length_of_longest_substring(s3)}")  # Expected Output: 1

    # Test Case 4: Empty string
    s4 = ""
    print(f"Test Case 4: {length_of_longest_substring(s4)}")  # Expected Output: 0

    # Test Case 5: String with spaces and symbols
    s5 = "a b c!@#"
    print(f"Test Case 5: {length_of_longest_substring(s5)}")  # Expected Output: 7

    # Test Case 6: String with overlapping substrings
    s6 = "pwwkew"
    print(f"Test Case 6: {length_of_longest_substring(s6)}")  # Expected Output: 3

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach with two pointers (left and right).
- Each character is added to or removed from the set at most once.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The space complexity is O(min(n, a)), where n is the length of the string and a is the size of the character set (e.g., 128 for ASCII).

Topic: Sliding Window
"""