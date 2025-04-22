"""
LeetCode Question #424: Longest Repeating Character Replacement

Problem Statement:
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""

def characterReplacement(s: str, k: int) -> int:
    """
    Finds the length of the longest substring containing the same letter
    after performing at most k character replacements.

    :param s: Input string consisting of uppercase English letters.
    :param k: Maximum number of character replacements allowed.
    :return: Length of the longest substring with the same letter.
    """
    # Sliding window approach
    left = 0
    max_count = 0
    char_count = {}
    max_length = 0

    for right in range(len(s)):
        # Update the count of the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # Track the count of the most frequent character in the current window
        max_count = max(max_count, char_count[s[right]])

        # Check if the window is valid (i.e., replacements needed <= k)
        while (right - left + 1) - max_count > k:
            # Shrink the window from the left
            char_count[s[left]] -= 1
            left += 1

        # Update the maximum length of the valid window
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ABAB"
    k1 = 2
    print(characterReplacement(s1, k1))  # Expected Output: 4

    # Test Case 2
    s2 = "AABABBA"
    k2 = 1
    print(characterReplacement(s2, k2))  # Expected Output: 4

    # Test Case 3
    s3 = "AAAA"
    k3 = 2
    print(characterReplacement(s3, k3))  # Expected Output: 4

    # Test Case 4
    s4 = "ABCDE"
    k4 = 2
    print(characterReplacement(s4, k4))  # Expected Output: 3

    # Test Case 5
    s5 = "AAABBC"
    k5 = 2
    print(characterReplacement(s5, k5))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once using the sliding window approach.
- Each character is processed at most twice (once when expanding the window and once when shrinking it).
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a dictionary to store the frequency of characters in the current window.
- The dictionary can contain at most 26 keys (since there are 26 uppercase English letters).
- Therefore, the space complexity is O(1) (constant space).

Topic: Sliding Window
"""