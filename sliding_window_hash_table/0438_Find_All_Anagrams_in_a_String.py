"""
LeetCode Problem #438: Find All Anagrams in a String

Problem Statement:
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- `s` and `p` consist of lowercase English letters.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Follow-up:
Could you do it in O(n) time complexity?
"""

from collections import Counter
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    """
    Finds all start indices of p's anagrams in s.
    """
    # Initialize variables
    p_count = Counter(p)  # Frequency count of characters in p
    s_count = Counter()   # Sliding window frequency count for s
    result = []
    p_length = len(p)

    # Iterate through the string s
    for i in range(len(s)):
        # Add the current character to the sliding window
        s_count[s[i]] += 1

        # Remove the character that is out of the sliding window
        if i >= p_length:
            if s_count[s[i - p_length]] == 1:
                del s_count[s[i - p_length]]
            else:
                s_count[s[i - p_length]] -= 1

        # Compare the sliding window with p's frequency count
        if s_count == p_count:
            result.append(i - p_length + 1)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cbaebabacd"
    p1 = "abc"
    print(findAnagrams(s1, p1))  # Output: [0, 6]

    # Test Case 2
    s2 = "abab"
    p2 = "ab"
    print(findAnagrams(s2, p2))  # Output: [0, 1, 2]

    # Test Case 3
    s3 = "a"
    p3 = "a"
    print(findAnagrams(s3, p3))  # Output: [0]

    # Test Case 4
    s4 = "abcdefg"
    p4 = "hij"
    print(findAnagrams(s4, p4))  # Output: []

"""
Time Complexity:
- The algorithm iterates through the string `s` once, performing O(1) operations for each character.
- The sliding window comparison (using Counter) is efficient because the size of the alphabet (26 lowercase English letters) is constant.
- Overall time complexity: O(n), where n is the length of `s`.

Space Complexity:
- The space used by the `Counter` objects is proportional to the size of the alphabet, which is constant (26).
- Additional space is used for the result list, which in the worst case can store up to O(n) indices.
- Overall space complexity: O(1) for the sliding window and O(k) for the result list, where k is the number of anagrams found.

Topic: Sliding Window, Hash Table
"""