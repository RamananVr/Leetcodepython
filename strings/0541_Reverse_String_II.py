"""
LeetCode Problem #541: Reverse String II

Problem Statement:
Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

- If there are fewer than `k` characters left, reverse all of them.
- If there are between `k` and `2k` characters, then reverse the first `k` characters and leave the others as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters.
- 1 <= k <= 10^4
"""

# Python Solution
def reverseStr(s: str, k: int) -> str:
    """
    Reverse the first k characters for every 2k characters in the string s.
    """
    s = list(s)  # Convert string to list for in-place modification
    for i in range(0, len(s), 2 * k):
        # Reverse the first k characters in the current 2k block
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcdefg"
    k1 = 2
    print(reverseStr(s1, k1))  # Output: "bacdfeg"

    # Test Case 2
    s2 = "abcd"
    k2 = 2
    print(reverseStr(s2, k2))  # Output: "bacd"

    # Test Case 3
    s3 = "a"
    k3 = 2
    print(reverseStr(s3, k3))  # Output: "a"

    # Test Case 4
    s4 = "abcdefghij"
    k4 = 3
    print(reverseStr(s4, k4))  # Output: "cbadefihgj"

    # Test Case 5
    s5 = "abcdef"
    k5 = 4
    print(reverseStr(s5, k5))  # Output: "dcbaef"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop iterates over the string in chunks of size 2k. For each chunk, we reverse at most k characters.
- In the worst case, we process the entire string of length n.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses O(n) space to store the list representation of the string.
- The in-place reversal does not require additional space.
- Thus, the space complexity is O(n).
"""

# Topic: Strings