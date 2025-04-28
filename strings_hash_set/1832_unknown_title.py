"""
LeetCode Problem #1832: Check if the Sentence Is Pangram

Problem Statement:
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Constraints:
- 1 <= sentence.length <= 1000
- sentence consists of lowercase English letters.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: The sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
Explanation: The sentence does not contain every letter of the English alphabet.
"""

def checkIfPangram(sentence: str) -> bool:
    """
    Function to check if a given sentence is a pangram.

    Args:
    sentence (str): A string containing only lowercase English letters.

    Returns:
    bool: True if the sentence is a pangram, False otherwise.
    """
    # A pangram must contain all 26 letters of the English alphabet
    return len(set(sentence)) == 26

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: A valid pangram
    sentence1 = "thequickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence1))  # Output: True

    # Test Case 2: Not a pangram
    sentence2 = "leetcode"
    print(checkIfPangram(sentence2))  # Output: False

    # Test Case 3: A pangram with repeated letters
    sentence3 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    print(checkIfPangram(sentence3))  # Output: True

    # Test Case 4: A short string that cannot be a pangram
    sentence4 = "abc"
    print(checkIfPangram(sentence4))  # Output: False

    # Test Case 5: A pangram with all letters in random order
    sentence5 = "zxcvbnmasdfghjklqwertyuiop"
    print(checkIfPangram(sentence5))  # Output: True

"""
Time Complexity Analysis:
- The function uses the `set` data structure to store unique characters from the input string.
- Constructing a set from the input string takes O(n) time, where n is the length of the string.
- Checking the size of the set is an O(1) operation.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The set used to store unique characters can contain at most 26 elements (the letters of the English alphabet).
- Thus, the space complexity is O(1) because the size of the set is bounded by a constant.

Topic: Strings, Hash Set
"""