"""
LeetCode Problem #1002: Find Common Characters

Problem Statement:
Given a string array `words`, return an array of all characters that show up in all strings within the `words` array 
(including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""

from collections import Counter
from typing import List

def commonChars(words: List[str]) -> List[str]:
    """
    Finds the common characters that appear in all strings in the input list.
    """
    # Initialize the counter with the first word
    common_count = Counter(words[0])
    
    # Intersect the counter with the counts of each subsequent word
    for word in words[1:]:
        common_count &= Counter(word)
    
    # Expand the characters based on their counts
    result = []
    for char, count in common_count.items():
        result.extend([char] * count)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["bella", "label", "roller"]
    print(commonChars(words1))  # Output: ["e", "l", "l"]

    # Test Case 2
    words2 = ["cool", "lock", "cook"]
    print(commonChars(words2))  # Output: ["c", "o"]

    # Test Case 3
    words3 = ["abc", "bca", "cab"]
    print(commonChars(words3))  # Output: ["a", "b", "c"]

    # Test Case 4
    words4 = ["a", "a", "a"]
    print(commonChars(words4))  # Output: ["a"]

    # Test Case 5
    words5 = ["abc", "def", "ghi"]
    print(commonChars(words5))  # Output: []

"""
Time Complexity Analysis:
- Let `n` be the number of words in the input list and `m` be the average length of the words.
- Creating a Counter for each word takes O(m) time.
- Intersecting the counters for all `n` words takes O(n * m) time in total.
- Constructing the result list from the final counter takes O(m) time.
- Overall time complexity: O(n * m).

Space Complexity Analysis:
- The space required for the Counter is proportional to the number of unique characters in the alphabet, which is constant (26 for lowercase English letters).
- The result list may contain up to O(m) characters.
- Overall space complexity: O(m).

Topic: Arrays, Hash Table
"""