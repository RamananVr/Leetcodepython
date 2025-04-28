"""
LeetCode Problem #1156: Swap For Longest Repeated Character Substring

Problem Statement:
Given a string `text`, we are allowed to swap two of the characters in the string. 
Find the length of the longest substring with repeated characters that can be achieved 
after performing at most one swap.

Example 1:
Input: text = "ababa"
Output: 3
Explanation: After swapping the first 'b' and the last 'a', the string becomes "aaaab", 
which has a substring "aaa" of length 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' and the last 'a' to get "aaaaaaa".

Example 3:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, the string already has a substring "aaaaa" of length 5.

Example 4:
Input: text = "abcdef"
Output: 1
Explanation: No matter how you swap, the longest substring with repeated characters is 1.

Constraints:
- 1 <= text.length <= 2 * 10^4
- text consists of lowercase English characters only.
"""

def maxRepOpt1(text: str) -> int:
    from collections import Counter

    # Count the frequency of each character in the string
    char_count = Counter(text)
    n = len(text)
    max_length = 0

    # Two pointers to find groups of consecutive characters
    i = 0
    while i < n:
        # Find the length of the current group of the same character
        j = i
        while j < n and text[j] == text[i]:
            j += 1
        group_length = j - i

        # Check if we can extend this group by swapping
        max_length = max(max_length, group_length)
        if char_count[text[i]] > group_length:
            max_length = max(max_length, group_length + 1)

        # Check if we can merge two groups of the same character separated by one different character
        if j < n - 1 and text[j + 1] == text[i]:
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            merged_length = (j - i) + (k - j - 1)
            if char_count[text[i]] > merged_length:
                merged_length += 1
            max_length = max(max_length, merged_length)

        # Move to the next group
        i = j

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "ababa"
    print(maxRepOpt1(text1))  # Output: 3

    # Test Case 2
    text2 = "aaabaaa"
    print(maxRepOpt1(text2))  # Output: 6

    # Test Case 3
    text3 = "aaaaa"
    print(maxRepOpt1(text3))  # Output: 5

    # Test Case 4
    text4 = "abcdef"
    print(maxRepOpt1(text4))  # Output: 1

    # Test Case 5
    text5 = "aabba"
    print(maxRepOpt1(text5))  # Output: 4

"""
Time Complexity:
- The algorithm iterates through the string once, and for each group of characters, it performs constant-time operations.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a Counter to store the frequency of each character, which requires O(26) space (constant space for lowercase English letters).
- Thus, the space complexity is O(1) in terms of asymptotic analysis.

Topic: Sliding Window, String
"""