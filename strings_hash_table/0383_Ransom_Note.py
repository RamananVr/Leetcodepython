"""
LeetCode Problem #383: Ransom Note

Problem Statement:
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

Constraints:
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

Example:
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

# Solution
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.

    Args:
    ransomNote (str): The string representing the ransom note.
    magazine (str): The string representing the magazine.

    Returns:
    bool: True if ransomNote can be constructed, False otherwise.
    """
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)
    
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ransomNote = "a"
    magazine = "b"
    print(canConstruct(ransomNote, magazine))  # Output: False

    # Test Case 2
    ransomNote = "aa"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine))  # Output: False

    # Test Case 3
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))  # Output: True

    # Additional Test Case 4
    ransomNote = "abc"
    magazine = "aabbcc"
    print(canConstruct(ransomNote, magazine))  # Output: True

    # Additional Test Case 5
    ransomNote = "abc"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the Counter for ransomNote and magazine takes O(n + m), where n is the length of ransomNote and m is the length of magazine.
- Iterating through the characters in ransomNote's Counter takes O(k), where k is the number of unique characters in ransomNote.
- Overall, the time complexity is O(n + m).

Space Complexity:
- The space complexity is O(n + m) due to the storage of the Counter objects for ransomNote and magazine.
"""

# Topic: Strings, Hash Table