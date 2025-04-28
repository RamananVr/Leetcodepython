"""
LeetCode Question #1941: Check if All Characters Have Equal Frequency

Problem Statement:
Given a string `s`, return `true` if all characters in the string have the same frequency, and `false` otherwise.

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters 'a', 'b', and 'c' all appear twice.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters 'a' appear 3 times, while 'b' appears 2 times.

Constraints:
- 1 <= s.length <= 1000
- `s` consists of lowercase English letters.
"""

# Solution
def areOccurrencesEqual(s: str) -> bool:
    """
    Check if all characters in the string have the same frequency.

    :param s: Input string consisting of lowercase English letters.
    :return: True if all characters have the same frequency, False otherwise.
    """
    from collections import Counter

    # Count the frequency of each character in the string
    freq = Counter(s)

    # Get the set of frequencies
    freq_values = set(freq.values())

    # If all frequencies are the same, the set will have only one unique value
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
    s5 = "abcde"
    print(areOccurrencesEqual(s5))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters using `Counter` takes O(n), where n is the length of the string.
- Creating a set of frequencies takes O(k), where k is the number of unique characters in the string.
- Overall, the time complexity is O(n).

Space Complexity:
- The `Counter` object stores up to k key-value pairs, where k is the number of unique characters in the string.
- The set of frequencies also takes O(k) space.
- Overall, the space complexity is O(k).

Topic: Hash Table
"""