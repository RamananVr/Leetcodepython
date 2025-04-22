"""
LeetCode Problem #395: Longest Substring with At Least K Repeating Characters

Problem Statement:
Given a string `s` and an integer `k`, return the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k`.

If there is no such substring, return 0.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters.
- 1 <= k <= 10^5

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' appears 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' appears 2 times and 'b' appears 3 times.

Example 3:
Input: s = "abcd", k = 2
Output: 0
Explanation: No substring meets the condition.

Follow-up:
Could you solve it in O(n) time complexity?
"""

# Clean and Correct Python Solution
def longestSubstring(s: str, k: int) -> int:
    def helper(start, end):
        if end - start < k:
            return 0
        
        # Count the frequency of each character in the current substring
        freq = {}
        for i in range(start, end):
            freq[s[i]] = freq.get(s[i], 0) + 1
        
        # Find the first character that doesn't meet the frequency requirement
        for mid in range(start, end):
            if freq[s[mid]] < k:
                # Split the string into two parts and solve recursively
                next_mid = mid + 1
                while next_mid < end and freq[s[next_mid]] < k:
                    next_mid += 1
                return max(helper(start, mid), helper(next_mid, end))
        
        # If all characters meet the frequency requirement, return the length of the substring
        return end - start
    
    return helper(0, len(s))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaabb"
    k1 = 3
    print(longestSubstring(s1, k1))  # Output: 3

    # Test Case 2
    s2 = "ababbc"
    k2 = 2
    print(longestSubstring(s2, k2))  # Output: 5

    # Test Case 3
    s3 = "abcd"
    k3 = 2
    print(longestSubstring(s3, k3))  # Output: 0

    # Test Case 4
    s4 = "aaabbbccc"
    k4 = 3
    print(longestSubstring(s4, k4))  # Output: 9

    # Test Case 5
    s5 = "aabbcc"
    k5 = 3
    print(longestSubstring(s5, k5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses a divide-and-conquer approach. In the worst case, the string is split into multiple parts, and each part is processed recursively.
- The time complexity is O(n * unique_characters), where `unique_characters` is the number of distinct characters in the string. In the worst case, this is O(26 * n) = O(n) for lowercase English letters.

Space Complexity:
- The space complexity is O(n) due to the recursive call stack and the frequency dictionary used in each recursive call.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(n)
"""

# Topic: Divide and Conquer, String