"""
LeetCode Problem #2370: Longest Ideal Subsequence

Problem Statement:
You are given a string `s` consisting of lowercase letters and an integer `k`. 
We call a string `t` ideal if the following conditions are satisfied:
- `t` is a subsequence of the string `s`.
- The absolute difference between the ASCII values of any two adjacent characters in `t` is at most `k`.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters 
without changing the order of the remaining characters.

Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal subsequence is "acbd". The absolute difference between the ASCII values 
of each adjacent character is at most 2.

Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal subsequence is "abcd". The absolute difference between the ASCII values 
of each adjacent character is at most 3.

Constraints:
- 1 <= s.length <= 10^5
- 0 <= k <= 25
- `s` consists of lowercase English letters.
"""

# Python Solution
def longestIdealString(s: str, k: int) -> int:
    # Initialize a DP array to store the maximum length of ideal subsequence ending at each character
    dp = [0] * 26  # 26 lowercase English letters
    
    for char in s:
        char_index = ord(char) - ord('a')  # Convert character to index (0 for 'a', 1 for 'b', ..., 25 for 'z')
        max_length = 0
        
        # Check all characters within the range of ASCII difference `k`
        for i in range(max(0, char_index - k), min(25, char_index + k) + 1):
            max_length = max(max_length, dp[i])
        
        # Update the DP array for the current character
        dp[char_index] = max_length + 1
    
    # The result is the maximum value in the DP array
    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "acfgbd"
    k1 = 2
    print(longestIdealString(s1, k1))  # Output: 4

    # Test Case 2
    s2 = "abcd"
    k2 = 3
    print(longestIdealString(s2, k2))  # Output: 4

    # Test Case 3
    s3 = "xyz"
    k3 = 1
    print(longestIdealString(s3, k3))  # Output: 3

    # Test Case 4
    s4 = "a"
    k4 = 0
    print(longestIdealString(s4, k4))  # Output: 1

    # Test Case 5
    s5 = "zxy"
    k5 = 25
    print(longestIdealString(s5, k5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each character in the string `s`, which has a length of `n`.
- For each character, it checks a range of at most `2k + 1` indices in the DP array (bounded by 26).
- Therefore, the time complexity is O(n * min(26, 2k + 1)).
- Since `k` is at most 25, the complexity simplifies to O(n).

Space Complexity:
- The algorithm uses a DP array of size 26 to store the maximum length of ideal subsequences for each character.
- Therefore, the space complexity is O(26), which simplifies to O(1).

Topic: Dynamic Programming (DP)
"""