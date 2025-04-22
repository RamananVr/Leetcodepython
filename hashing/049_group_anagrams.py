"""
LeetCode Question #49: Group Anagrams

Problem Statement:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

# Solution
from collections import defaultdict

def groupAnagrams(strs):
    """
    Groups anagrams from the input list of strings.

    :param strs: List[str] - List of strings to group
    :return: List[List[str]] - List of grouped anagrams
    """
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the word to create a key that represents its anagram group
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs1))  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # Test Case 2
    strs2 = [""]
    print(groupAnagrams(strs2))  # Output: [[""]]

    # Test Case 3
    strs3 = ["a"]
    print(groupAnagrams(strs3))  # Output: [["a"]]

    # Additional Test Case
    strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz", "def"]
    print(groupAnagrams(strs4))  # Output: [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"], ["def"]]

# Topic: Hashing