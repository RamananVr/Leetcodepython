"""
LeetCode Problem #2186: Minimum Number of Steps to Make Two Strings Anagram II

Problem Statement:
You are given two strings `s` and `t`. In one step, you can remove one character from either string.

Return the minimum number of steps to make `s` and `t` anagrams of each other.

An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Constraints:
- 1 <= s.length, t.length <= 10^5
- `s` and `t` consist of lowercase English letters.
"""

from collections import Counter

def minSteps(s: str, t: str) -> int:
    """
    Calculate the minimum number of steps to make two strings anagrams of each other.
    
    Args:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    int: The minimum number of steps required.
    """
    # Count the frequency of characters in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Calculate the total number of characters to remove
    steps = 0
    for char in set(count_s.keys()).union(count_t.keys()):
        steps += abs(count_s[char] - count_t[char])
    
    return steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcode"
    t1 = "coats"
    print(minSteps(s1, t1))  # Output: 7

    # Test Case 2
    s2 = "night"
    t2 = "thing"
    print(minSteps(s2, t2))  # Output: 0

    # Test Case 3
    s3 = "aabbcc"
    t3 = "xxyyzz"
    print(minSteps(s3, t3))  # Output: 12

    # Test Case 4
    s4 = "abc"
    t4 = "def"
    print(minSteps(s4, t4))  # Output: 6

"""
Time Complexity Analysis:
- Counting the frequency of characters in `s` and `t` takes O(n + m), where `n` is the length of `s` and `m` is the length of `t`.
- Iterating over the union of keys from both counters takes O(26) (constant time) since there are at most 26 lowercase English letters.
- Therefore, the overall time complexity is O(n + m).

Space Complexity Analysis:
- The space required for the counters is O(26) (constant space) since there are at most 26 lowercase English letters.
- Therefore, the overall space complexity is O(1) (constant space).

Topic: Strings, Hash Table
"""