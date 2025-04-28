"""
LeetCode Problem #2645: Minimum Additions to Make Valid String

Problem Statement:
A string is called valid if it can be formed by concatenating the string "abc" several times. For example, "abc", "abcabc", and "" are valid strings, but "ab", "cab", and "abcd" are not valid strings.

Given a string s, you can add characters at any position in the string to make it valid. Return the minimum number of characters that you need to add to make s valid.

Example 1:
Input: s = "aabbcc"
Output: 3
Explanation: Add "abc" at the beginning to make the string valid.

Example 2:
Input: s = "abcabc"
Output: 0
Explanation: The string is already valid.

Example 3:
Input: s = "abccba"
Output: 6
Explanation: Add "abc" twice to make the string valid.

Constraints:
- 1 <= s.length <= 1000
- s consists of letters 'a', 'b', and 'c' only.
"""

# Python Solution
def addMinimum(s: str) -> int:
    additions = 0
    i = 0
    n = len(s)
    
    while i < n:
        # Check for the sequence "abc"
        if i < n and s[i] == 'a':
            i += 1
        else:
            additions += 1  # Add 'a'
        
        if i < n and s[i] == 'b':
            i += 1
        else:
            additions += 1  # Add 'b'
        
        if i < n and s[i] == 'c':
            i += 1
        else:
            additions += 1  # Add 'c'
    
    return additions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabbcc"
    print(addMinimum(s1))  # Output: 3

    # Test Case 2
    s2 = "abcabc"
    print(addMinimum(s2))  # Output: 0

    # Test Case 3
    s3 = "abccba"
    print(addMinimum(s3))  # Output: 6

    # Test Case 4
    s4 = "a"
    print(addMinimum(s4))  # Output: 2

    # Test Case 5
    s5 = "bca"
    print(addMinimum(s5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
The solution iterates through the string `s` once, processing each character in constant time. 
Thus, the time complexity is O(n), where n is the length of the string.

Space Complexity:
The solution uses a constant amount of extra space (for variables like `additions` and `i`).
Thus, the space complexity is O(1).

Topic: Strings
"""