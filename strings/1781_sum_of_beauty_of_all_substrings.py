"""
LeetCode Question #1781: Sum of Beauty of All Substrings

Problem Statement:
The beauty of a string is defined as the difference in frequencies between the most frequent and least frequent characters.
Given a string `s`, return the sum of the beauty of all of its substrings.

The beauty of a substring is defined as the difference between the frequency of the most frequent character and the frequency of the least frequent character in the substring.

Example:
Input: s = "aabcb"
Output: 5
Explanation: 
- The substrings with non-zero beauty are ["aab", "ab", "bcb"].
- "aab" has beauty 1 (frequency difference between 'a' and 'b').
- "ab" has beauty 1 (frequency difference between 'a' and 'b').
- "bcb" has beauty 1 (frequency difference between 'b' and 'c').
- Total beauty = 1 + 1 + 1 = 5.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters.
"""

# Solution
from collections import Counter

def beautySum(s: str) -> int:
    total_beauty = 0
    n = len(s)
    
    # Iterate over all possible substrings
    for i in range(n):
        freq = Counter()
        for j in range(i, n):
            # Update frequency of the current character
            freq[s[j]] += 1
            
            # Calculate beauty for the current substring
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total_beauty += max_freq - min_freq
    
    return total_beauty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabcb"
    print(beautySum(s1))  # Expected Output: 5

    # Test Case 2
    s2 = "aabcbaa"
    print(beautySum(s2))  # Expected Output: 17

    # Test Case 3
    s3 = "abc"
    print(beautySum(s3))  # Expected Output: 3

    # Test Case 4
    s4 = "aaaa"
    print(beautySum(s4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs `n` times, where `n` is the length of the string.
- The inner loop runs up to `n` times for each iteration of the outer loop.
- For each substring, we calculate the max and min frequency, which takes O(26) time (since there are at most 26 lowercase English letters).
- Overall time complexity: O(n^2 * 26) = O(n^2).

Space Complexity:
- We use a Counter to store character frequencies, which takes O(26) space (constant space for lowercase English letters).
- Overall space complexity: O(1) (constant space).

Topic: Strings
"""