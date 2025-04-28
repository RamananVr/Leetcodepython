"""
LeetCode Problem #1347: Minimum Number of Steps to Make Two Strings Anagram

Problem Statement:
Given two strings s and t of the same length, return the minimum number of steps to make t an anagram of s.

In one step, you can choose any character of t and replace it with another character.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with 'b' to make t anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i', 'c' in t to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: t is already an anagram of s.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- s and t consist of lowercase English letters only.
"""

from collections import Counter

def minSteps(s: str, t: str) -> int:
    """
    Calculate the minimum number of steps to make t an anagram of s.

    Args:
    s (str): The first string.
    t (str): The second string.

    Returns:
    int: The minimum number of steps required.
    """
    # Count the frequency of characters in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Calculate the excess characters in t that need to be replaced
    steps = 0
    for char in count_s:
        if char in count_t:
            steps += max(0, count_s[char] - count_t[char])
        else:
            steps += count_s[char]
    
    return steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, t1 = "bab", "aba"
    print(f"Test Case 1: {minSteps(s1, t1)}")  # Expected Output: 1

    # Test Case 2
    s2, t2 = "leetcode", "practice"
    print(f"Test Case 2: {minSteps(s2, t2)}")  # Expected Output: 5

    # Test Case 3
    s3, t3 = "anagram", "mangaar"
    print(f"Test Case 3: {minSteps(s3, t3)}")  # Expected Output: 0

    # Test Case 4
    s4, t4 = "xxyyzz", "zzxxyy"
    print(f"Test Case 4: {minSteps(s4, t4)}")  # Expected Output: 0

    # Test Case 5
    s5, t5 = "aabbcc", "xyzxyz"
    print(f"Test Case 5: {minSteps(s5, t5)}")  # Expected Output: 6

"""
Time Complexity:
- Counting the characters in both strings takes O(n), where n is the length of the strings.
- Iterating through the character counts of `s` takes O(26) (constant time, as there are at most 26 lowercase English letters).
- Overall, the time complexity is O(n).

Space Complexity:
- The space required for the Counter objects is O(26) (constant space for the 26 lowercase English letters).
- Overall, the space complexity is O(1) (constant space).

Topic: Strings, Hash Table
"""