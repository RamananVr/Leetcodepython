"""
LeetCode Problem #1316: Distinct Echo Substrings

Problem Statement:
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e., it is an "echo substring"). 

Formally, a substring s of text is an echo substring if s can be written as t + t (the concatenation of t with itself for some string t).

Example 1:
Input: text = "abcabcabc"
Output: 3
Explanation: The 3 echo substrings are "abcabc", "bcabca", "cabcab".

Example 2:
Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 echo substrings are "leetcode", "eetcode".

Constraints:
- 1 <= text.length <= 10^4
- text consists of lowercase English characters only.
"""

# Solution
def distinctEchoSubstrings(text: str) -> int:
    n = len(text)
    seen = set()
    
    for length in range(1, n // 2 + 1):  # Length of the repeating substring t
        for i in range(n - 2 * length + 1):  # Start index of the substring
            t1 = text[i:i + length]
            t2 = text[i + length:i + 2 * length]
            if t1 == t2:
                seen.add(text[i:i + 2 * length])
    
    return len(seen)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "abcabcabc"
    print(distinctEchoSubstrings(text1))  # Output: 3

    # Test Case 2
    text2 = "leetcodeleetcode"
    print(distinctEchoSubstrings(text2))  # Output: 2

    # Test Case 3
    text3 = "aaaa"
    print(distinctEchoSubstrings(text3))  # Output: 3

    # Test Case 4
    text4 = "abcd"
    print(distinctEchoSubstrings(text4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over possible lengths of the repeating substring t, up to n // 2.
- The inner loop iterates over all possible starting indices for substrings of length 2 * length.
- For each pair of substrings, we perform a comparison operation.
- In the worst case, this results in O(n^2) comparisons.

Space Complexity:
- We use a set to store distinct echo substrings, which in the worst case could contain O(n^2) substrings.
- The space complexity is O(n^2) in the worst case.

Topic: Strings
"""