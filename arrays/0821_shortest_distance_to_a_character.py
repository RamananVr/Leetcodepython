"""
LeetCode Question #821: Shortest Distance to a Character

Problem Statement:
Given a string `s` and a character `c` that occurs in `s`, return an array of integers `answer` where `answer[i]` is the shortest distance from the character `c` in the string.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]

Constraints:
- 1 <= s.length <= 10^4
- s[i] and c are lowercase English letters.
- It is guaranteed that `c` occurs at least once in `s`.
"""

# Clean and Correct Python Solution
def shortestToChar(s: str, c: str) -> list[int]:
    n = len(s)
    answer = [float('inf')] * n

    # First pass: Calculate distances from left to right
    prev_c_index = -float('inf')
    for i in range(n):
        if s[i] == c:
            prev_c_index = i
        answer[i] = i - prev_c_index

    # Second pass: Calculate distances from right to left
    prev_c_index = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev_c_index = i
        answer[i] = min(answer[i], prev_c_index - i)

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "loveleetcode"
    c1 = "e"
    print(shortestToChar(s1, c1))  # Output: [3,2,1,0,1,0,0,1,2,2,1,0]

    # Test Case 2
    s2 = "aaab"
    c2 = "b"
    print(shortestToChar(s2, c2))  # Output: [3,2,1,0]

    # Test Case 3
    s3 = "a"
    c3 = "a"
    print(shortestToChar(s3, c3))  # Output: [0]

    # Test Case 4
    s4 = "abcde"
    c4 = "c"
    print(shortestToChar(s4, c4))  # Output: [2,1,0,1,2]

# Time and Space Complexity Analysis
# Time Complexity:
# - The solution involves two passes over the string `s`, each of which takes O(n) time, where `n` is the length of the string.
# - Therefore, the overall time complexity is O(n).

# Space Complexity:
# - The solution uses an array `answer` of size `n` to store the results.
# - Apart from this, a few variables are used for computation, which take O(1) space.
# - Therefore, the overall space complexity is O(n).

# Topic: Arrays