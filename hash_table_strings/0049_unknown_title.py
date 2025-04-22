"""
LeetCode Problem #49: Group Anagrams

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

# Clean and Correct Python Solution
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Use a dictionary to group anagrams
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the word to create a key
        sorted_word = ''.join(sorted(word))
        # Append the original word to the corresponding key
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

    # Test Case 4
    strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
    print(groupAnagrams(strs4))  # Output: [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"]]

    # Test Case 5
    strs5 = [""]
    print(groupAnagrams(strs5))  # Output: [[""]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting each word takes O(k log k), where k is the length of the word.
- If there are n words in the input list, the total time complexity is O(n * k log k), 
  where k is the average length of the words.

Space Complexity:
- The space complexity is O(n * k), where n is the number of words and k is the average length of the words.
  This is because we store all the words in the dictionary and the sorted keys.

Overall:
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

# Topic: Hash Table, Strings