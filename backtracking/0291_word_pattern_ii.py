"""
LeetCode Question #291: Word Pattern II

Problem Statement:
Given a pattern and a string s, return true if s matches the pattern. A string s matches a pattern if there is a bijective mapping between a letter in pattern and a non-empty substring in s. Bijective means that no two letters in pattern map to the same substring and no substring maps to two different letters.

Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: "a" -> "red", "b" -> "blue"

Example 2:
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: "a" -> "asd"

Example 3:
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false

Constraints:
- 1 <= pattern.length, s.length <= 20
- pattern and s consist of only lowercase English letters.
"""

def wordPatternMatch(pattern: str, s: str) -> bool:
    def backtrack(p_idx, s_idx, p_to_s, s_to_p):
        # If both pattern and string are fully matched
        if p_idx == len(pattern) and s_idx == len(s):
            return True
        # If either pattern or string is exhausted
        if p_idx == len(pattern) or s_idx == len(s):
            return False

        # Current character in the pattern
        char = pattern[p_idx]

        # Try all possible substrings of s starting from s_idx
        for end in range(s_idx + 1, len(s) + 1):
            substring = s[s_idx:end]

            # Check if the current mapping is valid
            if char in p_to_s and p_to_s[char] != substring:
                continue
            if substring in s_to_p and s_to_p[substring] != char:
                continue

            # Add the mapping and proceed
            p_to_s[char] = substring
            s_to_p[substring] = char

            if backtrack(p_idx + 1, end, p_to_s, s_to_p):
                return True

            # Backtrack: remove the mapping
            del p_to_s[char]
            del s_to_p[substring]

        return False

    # Dictionaries to store the bijective mappings
    return backtrack(0, 0, {}, {})

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pattern1 = "abab"
    s1 = "redblueredblue"
    print(wordPatternMatch(pattern1, s1))  # Output: True

    # Test Case 2
    pattern2 = "aaaa"
    s2 = "asdasdasdasd"
    print(wordPatternMatch(pattern2, s2))  # Output: True

    # Test Case 3
    pattern3 = "aabb"
    s3 = "xyzabcxzyabc"
    print(wordPatternMatch(pattern3, s3))  # Output: False

"""
Time Complexity:
- The time complexity is O(n^m), where n is the length of the string `s` and m is the length of the pattern. 
  This is because for each character in the pattern, we try all possible substrings of `s`.

Space Complexity:
- The space complexity is O(m + n), where m is the length of the pattern and n is the length of the string `s`.
  This is due to the space used by the dictionaries `p_to_s` and `s_to_p` and the recursion stack.

Topic: Backtracking
"""