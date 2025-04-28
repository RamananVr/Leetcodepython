"""
LeetCode Problem #1858: Longest Word With All Prefixes

Problem Statement:
------------------
You are given an array of strings `words`. A string is considered a "valid word" if every prefix of the string is also present in the array.

- For example, "abc" is a valid word because "a", "ab", and "abc" are all present in the array.

Return the longest valid word in `words`. If there are multiple valid words of the same length, return the lexicographically smallest one.

Example 1:
Input: words = ["k", "ki", "kir", "kira", "kiran"]
Output: "kiran"
Explanation: "kiran" is a valid word because all of its prefixes ("k", "ki", "kir", "kira", "kiran") are in the array.

Example 2:
Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: "apple" is a valid word because all of its prefixes ("a", "ap", "app", "appl", "apple") are in the array.

Example 3:
Input: words = ["abc", "bc", "ab", "qwe"]
Output: ""

Constraints:
------------
- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 10^5
- 1 <= sum(words[i].length) <= 10^5
- `words[i]` consists of lowercase English letters.

"""

# Solution
from typing import List

def longestWord(words: List[str]) -> str:
    # Sort words by length first, then lexicographically
    words.sort(key=lambda x: (len(x), x))
    
    # Use a set to store valid prefixes
    valid_prefixes = set()
    valid_prefixes.add("")  # Empty string is a valid prefix
    
    # Variable to store the result
    result = ""
    
    for word in words:
        # Check if the prefix (word[:-1]) is valid
        if word[:-1] in valid_prefixes:
            valid_prefixes.add(word)
            # Update result if the current word is longer or lexicographically smaller
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["k", "ki", "kir", "kira", "kiran"]
    print(longestWord(words1))  # Output: "kiran"

    # Test Case 2
    words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(longestWord(words2))  # Output: "apple"

    # Test Case 3
    words3 = ["abc", "bc", "ab", "qwe"]
    print(longestWord(words3))  # Output: ""

    # Test Case 4
    words4 = ["a", "b", "ba", "bac", "bad", "bada"]
    print(longestWord(words4))  # Output: "bada"

    # Test Case 5
    words5 = ["a", "ab", "abc", "abcd", "abcde", "abcdef"]
    print(longestWord(words5))  # Output: "abcdef"

"""
Time and Space Complexity Analysis:
-----------------------------------
Time Complexity:
- Sorting the words takes O(n * log(n)), where n is the number of words.
- Iterating through the words and checking prefixes takes O(sum(len(word))) = O(L), where L is the total length of all words.
- Overall time complexity: O(n * log(n) + L).

Space Complexity:
- The `valid_prefixes` set stores at most n words, so it takes O(n) space.
- The sorting operation may require additional space depending on the sorting algorithm, but this is typically O(n).
- Overall space complexity: O(n).

Topic: Strings, Sorting, Hash Set
"""