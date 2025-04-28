"""
LeetCode Question #2865: Count the Number of Vowel Strings in Range

Problem Statement:
You are given a 0-indexed array of strings `words` and two integers `left` and `right`.

A string is called a vowel string if it starts with a vowel ('a', 'e', 'i', 'o', 'u') and ends with a vowel ('a', 'e', 'i', 'o', 'u').

Return the number of vowel strings `words[i]` where `left <= i <= right`.

Example:
Input: words = ["apple", "banana", "orange", "umbrella"], left = 0, right = 2
Output: 2
Explanation: "apple" and "orange" are vowel strings.

Constraints:
- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.
- 0 <= left <= right < words.length
"""

# Solution
def countVowelStrings(words, left, right):
    """
    Counts the number of vowel strings in the range [left, right].

    :param words: List[str] - List of strings.
    :param left: int - Left index of the range.
    :param right: int - Right index of the range.
    :return: int - Number of vowel strings in the range.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for i in range(left, right + 1):
        if words[i][0] in vowels and words[i][-1] in vowels:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words = ["apple", "banana", "orange", "umbrella"]
    left = 0
    right = 2
    print(countVowelStrings(words, left, right))  # Output: 2

    # Test Case 2
    words = ["egg", "ice", "owl", "up"]
    left = 1
    right = 3
    print(countVowelStrings(words, left, right))  # Output: 3

    # Test Case 3
    words = ["cat", "dog", "elephant", "iguana"]
    left = 0
    right = 3
    print(countVowelStrings(words, left, right))  # Output: 1

    # Test Case 4
    words = ["a", "e", "i", "o", "u"]
    left = 0
    right = 4
    print(countVowelStrings(words, left, right))  # Output: 5

    # Test Case 5
    words = ["xyz", "abc", "def"]
    left = 0
    right = 2
    print(countVowelStrings(words, left, right))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the range [left, right], which has at most (right - left + 1) elements.
- For each string, checking the first and last character takes O(1) time.
- Therefore, the overall time complexity is O(right - left + 1), which is linear in the size of the range.

Space Complexity:
- The function uses a set of vowels, which is a constant space requirement: O(1).
- No additional data structures are used, so the space complexity is O(1).

Overall:
Time Complexity: O(right - left + 1)
Space Complexity: O(1)
"""

# Topic: Arrays