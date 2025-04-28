"""
LeetCode Problem #2041: Check if All Characters Have Equal Number of Occurrences

Problem Statement:
Given a string `s`, return `true` if all characters in the string have the same frequency, and `false` otherwise.

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters 'a', 'b', and 'c' all occur 2 times.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters 'a' occur 3 times, while 'b' occurs 2 times.

Constraints:
- 1 <= s.length <= 1000
- `s` consists of lowercase English letters.
"""

# Solution
from collections import Counter

def areOccurrencesEqual(s: str) -> bool:
    """
    Function to check if all characters in the string have the same frequency.

    Args:
    s (str): Input string consisting of lowercase English letters.

    Returns:
    bool: True if all characters have the same frequency, False otherwise.
    """
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Get the set of all frequency values
    freq_values = set(freq.values())
    
    # If all characters have the same frequency, the set will have only one unique value
    return len(freq_values) == 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abacbc"
    print(areOccurrencesEqual(s1))  # Output: True

    # Test Case 2
    s2 = "aaabb"
    print(areOccurrencesEqual(s2))  # Output: False

    # Test Case 3
    s3 = "zzzz"
    print(areOccurrencesEqual(s3))  # Output: True

    # Test Case 4
    s4 = "aabbcc"
    print(areOccurrencesEqual(s4))  # Output: True

    # Test Case 5
    s5 = "aabbccc"
    print(areOccurrencesEqual(s5))  # Output: False

"""
Time Complexity Analysis:
- Counting the frequency of characters using `Counter` takes O(n), where n is the length of the string.
- Creating a set of frequency values takes O(k), where k is the number of unique characters in the string.
- Overall, the time complexity is O(n), as k <= n.

Space Complexity Analysis:
- The `Counter` object stores the frequency of each character, which requires O(k) space, where k is the number of unique characters.
- The set of frequency values also requires O(k) space.
- Overall, the space complexity is O(k).

Topic: Hash Table
"""