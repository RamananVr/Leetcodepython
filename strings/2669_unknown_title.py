"""
LeetCode Problem #2669: Count the Number of Vowel Strings in Range

Problem Statement:
You are given a 0-indexed array of strings `words` and two integers `left` and `right`.

A string is called a vowel string if it starts with a vowel ('a', 'e', 'i', 'o', 'u') and ends with a vowel.
Return the number of vowel strings `words[i]` where `left <= i <= right`.

Example:
Input: words = ["are", "amy", "u"], left = 0, right = 2
Output: 2
Explanation: 
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
There are 2 vowel strings in the range [0, 2].

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 10
- words[i] consists of only lowercase English letters.
- 0 <= left <= right < words.length
"""

def countVowelStrings(words, left, right):
    """
    Counts the number of vowel strings in the given range [left, right].

    :param words: List[str] - List of strings
    :param left: int - Starting index of the range
    :param right: int - Ending index of the range
    :return: int - Number of vowel strings in the range
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for i in range(left, right + 1):
        word = words[i]
        if word[0] in vowels and word[-1] in vowels:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["are", "amy", "u"]
    left = 0
    right = 2
    print(countVowelStrings(words, left, right))  # Output: 2

    # Test Case 2
    words = ["apple", "banana", "orange", "umbrella"]
    left = 1
    right = 3
    print(countVowelStrings(words, left, right))  # Output: 1

    # Test Case 3
    words = ["a", "e", "i", "o", "u"]
    left = 0
    right = 4
    print(countVowelStrings(words, left, right))  # Output: 5

    # Test Case 4
    words = ["cat", "dog", "elephant", "iguana"]
    left = 0
    right = 3
    print(countVowelStrings(words, left, right))  # Output: 1

    # Test Case 5
    words = ["xyz", "abc", "def"]
    left = 0
    right = 2
    print(countVowelStrings(words, left, right))  # Output: 0

"""
Time Complexity:
- The function iterates through the range [left, right], which has at most (right - left + 1) elements.
- For each word, checking the first and last character is O(1).
- Therefore, the overall time complexity is O(n), where n is the number of elements in the range [left, right].

Space Complexity:
- The function uses a set of vowels, which is a constant space O(1).
- No additional data structures are used, so the space complexity is O(1).

Topic: Strings
"""