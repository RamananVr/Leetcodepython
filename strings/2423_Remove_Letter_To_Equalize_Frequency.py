"""
LeetCode Problem #2423: Remove Letter To Equalize Frequency

Problem Statement:
You are given a string `word` consisting of lowercase English letters. You need to determine if you can remove exactly one letter from the string such that the frequency of all remaining letters is the same.

Return `True` if it is possible to achieve this, otherwise return `False`.

Example 1:
Input: word = "abcc"
Output: True
Explanation: Remove 'a' or 'b' to make the frequency of all remaining letters equal.

Example 2:
Input: word = "aazz"
Output: False
Explanation: It is impossible to make the frequency of all remaining letters equal by removing one letter.

Constraints:
- 2 <= word.length <= 1000
- `word` consists of lowercase English letters.
"""

# Solution
from collections import Counter

def equalFrequency(word: str) -> bool:
    # Count the frequency of each character in the word
    freq = Counter(word)
    
    # Iterate through each character in the word
    for char in freq:
        # Create a copy of the frequency dictionary
        temp_freq = freq.copy()
        # Remove one occurrence of the current character
        temp_freq[char] -= 1
        # If the frequency becomes zero, remove the character from the dictionary
        if temp_freq[char] == 0:
            del temp_freq[char]
        # Check if all remaining frequencies are the same
        if len(set(temp_freq.values())) == 1:
            return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "abcc"
    print(equalFrequency(word1))  # Output: True

    # Test Case 2
    word2 = "aazz"
    print(equalFrequency(word2))  # Output: False

    # Test Case 3
    word3 = "aaa"
    print(equalFrequency(word3))  # Output: True

    # Test Case 4
    word4 = "abc"
    print(equalFrequency(word4))  # Output: True

    # Test Case 5
    word5 = "aabbcc"
    print(equalFrequency(word5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters using `Counter` takes O(n), where n is the length of the string.
- Iterating through each unique character in the frequency dictionary takes O(k), where k is the number of unique characters (k <= 26 for lowercase English letters).
- For each character, creating a copy of the frequency dictionary and checking if all frequencies are equal takes O(k).
- Overall, the time complexity is O(n + k^2), which simplifies to O(n) for practical purposes since k is bounded by 26.

Space Complexity:
- The space complexity is O(k) for storing the frequency dictionary, where k is the number of unique characters.
- The temporary frequency dictionary also takes O(k) space.
- Overall, the space complexity is O(k), which is O(1) in practical terms since k is bounded by 26.

Topic: Strings
"""