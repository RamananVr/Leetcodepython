"""
LeetCode Question #1593: Split a String Into the Max Number of Unique Substrings

Problem Statement:
Given a string `s`, return the maximum number of unique substrings that the given string can be split into.

You can split string `s` into any list of non-empty substrings where the concatenation of the substrings forms the original string. However, each substring must be unique.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split the string into the maximum number of unique substrings is ["a", "b", "ab", "c", "cc"].

Example 2:
Input: s = "aba"
Output: 2
Explanation: One way to split the string into the maximum number of unique substrings is ["a", "ba"].

Example 3:
Input: s = "aa"
Output: 1
Explanation: The only way to split the string is ["a", "a"], which results in only 1 unique substring.

Constraints:
- `1 <= s.length <= 16`
- `s` consists of only lowercase English letters.
"""

def maxUniqueSplit(s: str) -> int:
    """
    Function to calculate the maximum number of unique substrings
    that the given string can be split into.
    """
    def backtrack(start, seen):
        # If we've reached the end of the string, return 0
        if start == len(s):
            return 0
        
        max_count = 0
        # Try all possible substrings starting from `start`
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                # Add substring to the set and recurse
                seen.add(substring)
                max_count = max(max_count, 1 + backtrack(end, seen))
                # Backtrack: remove the substring from the set
                seen.remove(substring)
        
        return max_count

    # Start backtracking with an empty set of seen substrings
    return backtrack(0, set())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ababccc"
    print(f"Input: {s1} -> Output: {maxUniqueSplit(s1)}")  # Expected: 5

    # Test Case 2
    s2 = "aba"
    print(f"Input: {s2} -> Output: {maxUniqueSplit(s2)}")  # Expected: 2

    # Test Case 3
    s3 = "aa"
    print(f"Input: {s3} -> Output: {maxUniqueSplit(s3)}")  # Expected: 1

    # Test Case 4
    s4 = "abcdef"
    print(f"Input: {s4} -> Output: {maxUniqueSplit(s4)}")  # Expected: 6

    # Test Case 5
    s5 = "aabb"
    print(f"Input: {s5} -> Output: {maxUniqueSplit(s5)}")  # Expected: 4

"""
Time Complexity:
- The time complexity is O(2^n), where n is the length of the string `s`.
  This is because for each character in the string, we have two choices: either include it in the current substring or start a new substring.
  The backtracking explores all possible combinations of substrings.

Space Complexity:
- The space complexity is O(n), where n is the length of the string `s`.
  This is due to the recursion stack and the `seen` set, which can hold at most n substrings.

Topic: Backtracking
"""