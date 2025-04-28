"""
LeetCode Problem #1839: Longest Substring Of All Vowels in Order

Problem Statement:
A string is considered "beautiful" if it satisfies the following conditions:
- Each of the five English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it and in order (i.e., 'a' before 'e', 'e' before 'i', 'i' before 'o', 'o' before 'u').

Given a string `word`, return the length of the longest beautiful substring of `word`. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

Constraints:
- 1 <= word.length <= 5 * 10^5
- `word` consists of characters 'a', 'e', 'i', 'o', and 'u' only.

Example:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in the word is "aaaaeiiiiouuu" of length 13.
"""

# Python Solution
def longestBeautifulSubstring(word: str) -> int:
    vowels = "aeiou"
    max_length = 0
    current_length = 0
    vowel_index = 0

    for char in word:
        if char == vowels[vowel_index]:  # Current vowel matches expected vowel
            current_length += 1
        elif vowel_index < 4 and char == vowels[vowel_index + 1]:  # Move to next vowel
            vowel_index += 1
            current_length += 1
        else:  # Reset if the sequence breaks
            if char == 'a':  # Start a new sequence if 'a' is encountered
                current_length = 1
                vowel_index = 0
            else:
                current_length = 0
                vowel_index = 0

        # Check if all vowels are included in order
        if vowel_index == 4:  # All vowels are present in order
            max_length = max(max_length, current_length)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    print(longestBeautifulSubstring(word1))  # Output: 13

    # Test Case 2
    word2 = "aeeeiiiioooauuuaeiou"
    print(longestBeautifulSubstring(word2))  # Output: 5

    # Test Case 3
    word3 = "aeiouaeiouaeiou"
    print(longestBeautifulSubstring(word3))  # Output: 15

    # Test Case 4
    word4 = "aaiiou"
    print(longestBeautifulSubstring(word4))  # Output: 0

    # Test Case 5
    word5 = "aeiou"
    print(longestBeautifulSubstring(word5))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the string `word` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a few integer variables to track the current state and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Strings
"""