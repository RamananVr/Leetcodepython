"""
LeetCode Problem #2998: <Problem Title>

Problem Statement:
(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2998 does not exist. 
For the purpose of this exercise, I will create a fictional problem statement.)

Problem:
You are given a string `s` consisting of lowercase English letters and an integer `k`. 
Your task is to find the length of the longest substring of `s` that contains at most `k` distinct characters.

Example:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Constraints:
1. 1 <= s.length <= 10^5
2. 1 <= k <= 26
3. `s` consists of only lowercase English letters.
"""

# Solution
def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    # Dictionary to store the count of characters in the current window
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
    s3 = "aabbcc"
    k3 = 2
    print(length_of_longest_substring_k_distinct(s3, k3))  # Output: 4

    # Test Case 4
    s4 = "abcde"
    k4 = 3
    print(length_of_longest_substring_k_distinct(s4, k4))  # Output: 3

    # Test Case 5
    s5 = "aaaa"
    k5 = 1
    print(length_of_longest_substring_k_distinct(s5, k5))  # Output: 4

"""
Time Complexity Analysis:
- The outer loop iterates through the string `s` once, so it runs in O(n) time.
- The inner while loop ensures that the window is adjusted, but each character is added and removed from the dictionary at most once. 
  Thus, the total time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k), where `k` is the maximum number of distinct characters allowed in the substring. 
  This is because the dictionary `char_count` can store at most `k` keys.

Topic: Sliding Window
"""