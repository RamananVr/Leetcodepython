"""
LeetCode Problem #1160: Find Words That Can Be Formed by Characters

Problem Statement:
You are given an array of strings `words` and a string `chars`.

A string is good if it can be formed by characters from `chars` (each character can only be used once). 
Return the sum of lengths of all good strings in `words`.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" (length 3) and "hat" (length 3).
The sum of their lengths is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" (length 5) and "world" (length 5).
The sum of their lengths is 5 + 5 = 10.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length, chars.length <= 100
- words[i] and chars consist of lowercase English letters.
"""

from collections import Counter

def countCharacters(words, chars):
    """
    Function to calculate the sum of lengths of all good strings in the words list.
    
    :param words: List[str] - List of words to check
    :param chars: str - String of characters available to form words
    :return: int - Sum of lengths of all good strings
    """
    # Count the frequency of each character in chars
    chars_count = Counter(chars)
    total_length = 0

    # Iterate through each word in the words list
    for word in words:
        word_count = Counter(word)
        # Check if the word can be formed using chars
        if all(word_count[char] <= chars_count[char] for char in word_count):
            total_length += len(word)
    
    return total_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["cat", "bt", "hat", "tree"]
    chars1 = "atach"
    print(countCharacters(words1, chars1))  # Output: 6

    # Test Case 2
    words2 = ["hello", "world", "leetcode"]
    chars2 = "welldonehoneyr"
    print(countCharacters(words2, chars2))  # Output: 10

    # Test Case 3
    words3 = ["a", "b", "c"]
    chars3 = "abc"
    print(countCharacters(words3, chars3))  # Output: 3

    # Test Case 4
    words4 = ["abc", "def", "ghi"]
    chars4 = "xyz"
    print(countCharacters(words4, chars4))  # Output: 0

"""
Time Complexity Analysis:
- Let `n` be the number of words in the `words` list and `m` be the average length of the words.
- Counting the frequency of characters in `chars` takes O(c), where `c` is the length of `chars`.
- For each word in `words`, we count its frequency (O(m)) and compare it with `chars_count` (O(m)).
- Thus, the total time complexity is O(c + n * m).

Space Complexity Analysis:
- The space complexity is O(c + m), where `c` is the size of the `chars_count` dictionary and `m` is the size of the `word_count` dictionary for the largest word.

Topic: Hash Table
"""