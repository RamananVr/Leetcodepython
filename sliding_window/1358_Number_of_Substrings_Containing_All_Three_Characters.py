"""
LeetCode Problem #1358: Number of Substrings Containing All Three Characters

Problem Statement:
Given a string `s` consisting only of characters 'a', 'b', and 'c'. 
Return the number of substrings containing at least one occurrence of all these characters 'a', 'b', and 'c'.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters 'a', 'b', and 'c' are:
"abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc", and "abc" (10 substrings in total).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters 'a', 'b', and 'c' are:
"aaacb", "aacb", and "acb" (3 substrings in total).

Example 3:
Input: s = "abc"
Output: 1

Constraints:
- 3 <= s.length <= 5 * 10^4
- s consists only of characters 'a', 'b', and 'c'.
"""

def numberOfSubstrings(s: str) -> int:
    """
    Returns the number of substrings containing at least one occurrence of 'a', 'b', and 'c'.
    """
    # Sliding window approach
    count = {'a': 0, 'b': 0, 'c': 0}
    left = 0
    result = 0

    for right in range(len(s)):
        # Increment the count of the current character
        count[s[right]] += 1

        # Check if the current window contains all three characters
        while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
            # Add the number of valid substrings ending at `right`
            result += len(s) - right
            # Shrink the window from the left
            count[s[left]] -= 1
            left += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcabc"
    print(f"Input: {s1} -> Output: {numberOfSubstrings(s1)}")  # Expected: 10

    # Test Case 2
    s2 = "aaacb"
    print(f"Input: {s2} -> Output: {numberOfSubstrings(s2)}")  # Expected: 3

    # Test Case 3
    s3 = "abc"
    print(f"Input: {s3} -> Output: {numberOfSubstrings(s3)}")  # Expected: 1

    # Test Case 4
    s4 = "aabbcc"
    print(f"Input: {s4} -> Output: {numberOfSubstrings(s4)}")  # Expected: 15

    # Test Case 5
    s5 = "aaaaa"
    print(f"Input: {s5} -> Output: {numberOfSubstrings(s5)}")  # Expected: 0

"""
Time Complexity:
- The sliding window ensures that each character is processed at most twice (once when expanding the window and once when shrinking it).
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity:
- The space complexity is O(1) since we only use a fixed-size dictionary to store the counts of 'a', 'b', and 'c'.

Topic: Sliding Window
"""