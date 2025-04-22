"""
LeetCode Problem #567: Permutation in String

Problem Statement:
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise.

In other words, return true if one of `s1`'s permutations is the substring of `s2`.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""

from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    """
    Check if s2 contains a permutation of s1.

    Args:
    s1 (str): The string whose permutations we are checking for.
    s2 (str): The string in which we are searching for permutations.

    Returns:
    bool: True if s2 contains a permutation of s1, False otherwise.
    """
    # Edge case: If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
    if len(s1) > len(s2):
        return False

    # Count the frequency of characters in s1
    s1_count = Counter(s1)
    # Initialize a sliding window of size len(s1) in s2
    window_count = Counter(s2[:len(s1)])

    # Check if the initial window matches s1_count
    if s1_count == window_count:
        return True

    # Slide the window across s2
    for i in range(len(s1), len(s2)):
        # Add the new character to the window
        window_count[s2[i]] += 1
        # Remove the character that is sliding out of the window
        window_count[s2[i - len(s1)]] -= 1

        # Clean up the counter to remove zero-count entries
        if window_count[s2[i - len(s1)]] == 0:
            del window_count[s2[i - len(s1)]]

        # Check if the current window matches s1_count
        if s1_count == window_count:
            return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))  # Output: True

    # Test Case 2
    s1 = "ab"
    s2 = "eidboaoo"
    print(checkInclusion(s1, s2))  # Output: False

    # Test Case 3
    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2))  # Output: True

    # Test Case 4
    s1 = "hello"
    s2 = "ooolleoooleh"
    print(checkInclusion(s1, s2))  # Output: False

    # Test Case 5
    s1 = "a"
    s2 = "a"
    print(checkInclusion(s1, s2))  # Output: True

"""
Time Complexity:
- The time complexity is O(n), where n is the length of s2.
  - We iterate through s2 once with a sliding window of size len(s1).
  - Each update to the Counter object (adding/removing a character) is O(1) on average.

Space Complexity:
- The space complexity is O(1), as the Counter object will store at most 26 keys (one for each lowercase English letter).

Topic: Sliding Window, Hash Table
"""