"""
LeetCode Question #1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence

Problem Statement:
Given a sentence that consists of some words separated by a single space, and a searchWord, 
check if searchWord is a prefix of any word in the sentence.

Return the index of the word in the sentence (1-indexed) where searchWord is a prefix of this word. 
If searchWord is a prefix of more than one word, return the index of the first word (minimum index). 
If there is no such word, return -1.

A prefix of a string is any leading contiguous substring of the string.

Example 1:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is a prefix of "burger" which is the 4th word in the sentence.

Example 2:
Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is a prefix of "problem" which is the 2nd word in the sentence.

Example 3:
Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.

Constraints:
- 1 <= sentence.length <= 100
- 1 <= searchWord.length <= 10
- sentence consists of lowercase English letters and spaces.
- searchWord consists of lowercase English letters.
- sentence contains no leading or trailing spaces.
- All the words in sentence are separated by a single space.
"""

# Solution
def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split()  # Split the sentence into words
    for i, word in enumerate(words):
        if word.startswith(searchWord):  # Check if the word starts with searchWord
            return i + 1  # Return the 1-indexed position
    return -1  # Return -1 if no word matches

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "i love eating burger"
    searchWord1 = "burg"
    print(isPrefixOfWord(sentence1, searchWord1))  # Output: 4

    # Test Case 2
    sentence2 = "this problem is an easy problem"
    searchWord2 = "pro"
    print(isPrefixOfWord(sentence2, searchWord2))  # Output: 2

    # Test Case 3
    sentence3 = "i am tired"
    searchWord3 = "you"
    print(isPrefixOfWord(sentence3, searchWord3))  # Output: -1

    # Test Case 4
    sentence4 = "hello world"
    searchWord4 = "wor"
    print(isPrefixOfWord(sentence4, searchWord4))  # Output: 2

    # Test Case 5
    sentence5 = "a quick brown fox jumps over the lazy dog"
    searchWord5 = "qui"
    print(isPrefixOfWord(sentence5, searchWord5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the sentence into words takes O(n), where n is the length of the sentence.
- Iterating through the words and checking the prefix takes O(m * k), where m is the number of words 
  and k is the average length of a word.
- Overall, the time complexity is O(n + m * k), which simplifies to O(n) since m * k is proportional to n.

Space Complexity:
- The space complexity is O(m), where m is the number of words in the sentence, due to the list created by `split()`.
- The function uses constant space for variables, so the overall space complexity is O(m).
"""

# Topic: Strings