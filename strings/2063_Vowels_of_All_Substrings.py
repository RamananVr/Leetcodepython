"""
LeetCode Problem #2063: Vowels of All Substrings

Problem Statement:
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', 'u') in every substring of word.

A substring is a contiguous sequence of characters within a string.

Example:
Input: word = "aba"
Output: 6
Explanation: 
- The substrings of "aba" are: "a", "b", "a", "ab", "ba", "aba".
- "a" occurs in 4 of these substrings. "a" contributes 4 to the total.
- "b" is not a vowel and contributes 0.
- "a" occurs in 2 of these substrings. "a" contributes 2 to the total.
- Total = 4 + 0 + 2 = 6.

Constraints:
- 1 <= word.length <= 10^5
- word consists of lowercase English letters.
"""

# Solution
def countVowels(word: str) -> int:
    """
    Calculate the sum of the number of vowels in every substring of the given word.

    :param word: A string consisting of lowercase English letters.
    :return: The sum of the number of vowels in all substrings.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(word)
    total_vowels = 0

    for i, char in enumerate(word):
        if char in vowels:
            # Each character contributes to substrings starting from index i
            # and ending at index j (where j >= i). The total number of such substrings
            # is (i + 1) * (n - i).
            total_vowels += (i + 1) * (n - i)

    return total_vowels

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word = "aba"
    print(countVowels(word))  # Output: 6

    # Test Case 2
    word = "abc"
    print(countVowels(word))  # Output: 2

    # Test Case 3
    word = "aeiou"
    print(countVowels(word))  # Output: 35

    # Test Case 4
    word = "leetcode"
    print(countVowels(word))  # Output: 49

    # Test Case 5
    word = "xyz"
    print(countVowels(word))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The solution uses a set to store the vowels, which is a constant size (5 elements).
- No additional space is used proportional to the input size.
- Therefore, the space complexity is O(1).

Topic: Strings
"""