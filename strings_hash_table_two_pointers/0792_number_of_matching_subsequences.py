"""
LeetCode Question #792: Number of Matching Subsequences

Problem Statement:
Given a string `s` and an array of strings `words`, return the number of words[i] that are subsequences of `s`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: "a", "acd", "ace" are subsequences of "abcde".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
Output: 2

Constraints:
- 1 <= s.length <= 5 * 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 50
- `s` and `words[i]` consist of only lowercase English letters.
"""

# Clean, Correct Python Solution
from collections import defaultdict

def numMatchingSubseq(s: str, words: list[str]) -> int:
    # Create a dictionary to store lists of words waiting for each character
    waiting = defaultdict(list)
    
    # Initialize the waiting dictionary with the first character of each word
    for word in words:
        waiting[word[0]].append(iter(word[1:]))
    
    # Count of matching subsequences
    count = 0
    
    # Iterate through each character in the string `s`
    for char in s:
        # Get the list of iterators waiting for the current character
        current_waiting = waiting[char]
        waiting[char] = []  # Clear the list for the current character
        
        for it in current_waiting:
            next_char = next(it, None)  # Move to the next character in the word
            if next_char is None:
                # If the iterator is exhausted, the word is a subsequence
                count += 1
            else:
                # Otherwise, add the iterator back to the waiting list for the next character
                waiting[next_char].append(it)
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcde"
    words1 = ["a", "bb", "acd", "ace"]
    print(numMatchingSubseq(s1, words1))  # Output: 3

    # Test Case 2
    s2 = "dsahjpjauf"
    words2 = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    print(numMatchingSubseq(s2, words2))  # Output: 2

    # Test Case 3
    s3 = "aaaaa"
    words3 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]
    print(numMatchingSubseq(s3, words3))  # Output: 5

    # Test Case 4
    s4 = "xyz"
    words4 = ["x", "y", "z", "xy", "xz", "yz", "xyz"]
    print(numMatchingSubseq(s4, words4))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the length of `s` and `m` be the total number of characters across all words in `words`.
- Each character in `s` is processed once, and for each character, we iterate over the list of iterators waiting for that character.
- The total number of operations is proportional to the total number of characters in all words, i.e., O(n + m).

Space Complexity:
- The space used by the `waiting` dictionary is proportional to the number of unique characters in `words` and the number of iterators, i.e., O(m).
- Additional space is used for the iterators, but this is negligible compared to the input size.

Overall:
Time Complexity: O(n + m)
Space Complexity: O(m)
"""

# Topic: Strings, Hash Table, Two Pointers