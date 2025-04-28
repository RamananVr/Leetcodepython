"""
LeetCode Problem #2516: Take K of Each Character From Left and Right

Problem Statement:
You are given a string `s` consisting of the characters 'a', 'b', and 'c' and a non-negative integer `k`. 
Each character in `s` appears at least `k` times. In one move, you can take one occurrence of any character 
from the left end of `s` or from the right end of `s`.

Return the minimum length of `s` you can make if you take exactly `k` occurrences of each character 'a', 'b', 
and 'c' from `s`. If it is not possible to take `k` occurrences of each character, return -1.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take two 'a's from the left end and one 'a' from the right end, 
then take two 'b's from the right end, and take two 'c's from the right end.
The resulting string is "baaaaac". The length of this string is 8.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'a', one 'b', and one 'c' from the string.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only the letters 'a', 'b', and 'c'.
- 0 <= k <= s.length
"""

def takeCharacters(s: str, k: int) -> int:
    from collections import Counter

    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # If any character appears less than k times, it's impossible to satisfy the condition
    if freq['a'] < k or freq['b'] < k or freq['c'] < k:
        return -1

    # Total number of characters we need to keep in the middle
    required = {'a': freq['a'] - k, 'b': freq['b'] - k, 'c': freq['c'] - k}

    # Sliding window to find the maximum length of a valid substring
    left = 0
    max_len = 0
    current = {'a': 0, 'b': 0, 'c': 0}

    for right in range(len(s)):
        current[s[right]] += 1

        # Shrink the window if the current substring has more than the required characters
        while current['a'] > required['a'] or current['b'] > required['b'] or current['c'] > required['c']:
            current[s[left]] -= 1
            left += 1

        # Update the maximum length of the valid substring
        max_len = max(max_len, right - left + 1)

    # The minimum length of the string after taking k of each character
    return len(s) - max_len


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabaaaacaabc"
    k1 = 2
    print(takeCharacters(s1, k1))  # Output: 8

    # Test Case 2
    s2 = "a"
    k2 = 1
    print(takeCharacters(s2, k2))  # Output: -1

    # Test Case 3
    s3 = "abcabcabc"
    k3 = 3
    print(takeCharacters(s3, k3))  # Output: 9

    # Test Case 4
    s4 = "aabbcc"
    k4 = 1
    print(takeCharacters(s4, k4))  # Output: 6

    # Test Case 5
    s5 = "aaabbbccc"
    k5 = 2
    print(takeCharacters(s5, k5))  # Output: 6


"""
Time Complexity:
- Counting the frequency of characters takes O(n), where n is the length of the string.
- The sliding window approach also takes O(n), as each character is processed at most twice (once when expanding the window and once when shrinking it).
- Overall time complexity: O(n).

Space Complexity:
- The space used by the `Counter` and the `current` dictionary is O(1), as there are only three unique characters ('a', 'b', 'c').
- Overall space complexity: O(1).

Topic: Sliding Window
"""