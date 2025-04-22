"""
LeetCode Problem #242: Valid Anagram

Problem Statement:
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

Follow-up:
What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def isAnagram(s: str, t: str) -> bool:
    """
    Determines if string t is an anagram of string s.

    Args:
    s (str): The first string.
    t (str): The second string.

    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Use a Counter to count the frequency of characters in both strings
    from collections import Counter
    return Counter(s) == Counter(t)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Anagram strings
    s1 = "anagram"
    t1 = "nagaram"
    print(isAnagram(s1, t1))  # Expected output: True

    # Test Case 2: Non-anagram strings
    s2 = "rat"
    t2 = "car"
    print(isAnagram(s2, t2))  # Expected output: False

    # Test Case 3: Empty strings
    s3 = ""
    t3 = ""
    print(isAnagram(s3, t3))  # Expected output: True

    # Test Case 4: Strings with different lengths
    s4 = "hello"
    t4 = "helloo"
    print(isAnagram(s4, t4))  # Expected output: False

    # Test Case 5: Strings with repeated characters
    s5 = "aabbcc"
    t5 = "ccbbaa"
    print(isAnagram(s5, t5))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `Counter` function iterates through each string once, which takes O(n) time for both `s` and `t`.
- Comparing two Counter objects takes O(k), where k is the number of unique characters in the strings.
- Overall, the time complexity is O(n + m), where n is the length of `s` and m is the length of `t`.

Space Complexity:
- The `Counter` function creates a dictionary-like object to store character frequencies, which takes O(k) space, 
  where k is the number of unique characters in the strings.
- Overall, the space complexity is O(k).

Topic: Strings
"""