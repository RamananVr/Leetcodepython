"""
LeetCode Problem #205: Isomorphic Strings

Problem Statement:
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
- 1 <= s.length <= 5 * 10^4
- `s` and `t` consist of any valid ASCII character.
"""

def isIsomorphic(s: str, t: str) -> bool:
    """
    Determines if two strings are isomorphic.

    Args:
    s (str): The first string.
    t (str): The second string.

    Returns:
    bool: True if the strings are isomorphic, False otherwise.
    """
    if len(s) != len(t):
        return False

    # Create two dictionaries to store mappings from s -> t and t -> s
    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        # Check if the mapping exists and is consistent
        if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
           (char_t in t_to_s and t_to_s[char_t] != char_s):
            return False

        # Create the mapping
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, t1 = "egg", "add"
    print(isIsomorphic(s1, t1))  # Output: True

    # Test Case 2
    s2, t2 = "foo", "bar"
    print(isIsomorphic(s2, t2))  # Output: False

    # Test Case 3
    s3, t3 = "paper", "title"
    print(isIsomorphic(s3, t3))  # Output: True

    # Test Case 4
    s4, t4 = "ab", "aa"
    print(isIsomorphic(s4, t4))  # Output: False

    # Test Case 5
    s5, t5 = "a", "a"
    print(isIsomorphic(s5, t5))  # Output: True

"""
Time Complexity:
- The algorithm iterates through the strings `s` and `t` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the strings.

Space Complexity:
- Two dictionaries are used to store the mappings, which can each grow up to the size of the input strings.
- Therefore, the space complexity is O(n), where n is the length of the strings.

Topic: Hash Table
"""