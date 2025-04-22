"""
LeetCode Problem #472: Concatenated Words

Problem Statement:
Given an array of strings `words` (without duplicates), return all the concatenated words in the given list of `words`.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" is concatenated by "cats", "dog" and "cats"; 
             "dogcatsdog" is concatenated by "dog", "cats" and "dog"; 
             "ratcatdogcat" is concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 30
- All the strings of `words` are unique.
- 1 <= sum(words[i].length) <= 10^5
- `words[i]` consists of only lowercase English letters.
"""

from typing import List

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    def canForm(word: str, word_set: set) -> bool:
        if not word:
            return False
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty prefix is always valid

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

    word_set = set(words)
    concatenated_words = []

    for word in words:
        word_set.remove(word)  # Temporarily remove the word to avoid using itself
        if canForm(word, word_set):
            concatenated_words.append(word)
        word_set.add(word)  # Add the word back to the set

    return concatenated_words

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(findAllConcatenatedWordsInADict(words1))  # Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

    # Test Case 2
    words2 = ["cat", "dog", "catdog"]
    print(findAllConcatenatedWordsInADict(words2))  # Output: ["catdog"]

    # Test Case 3
    words3 = ["a", "b", "ab", "abc", "abcd"]
    print(findAllConcatenatedWordsInADict(words3))  # Output: ["ab"]

    # Test Case 4
    words4 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(findAllConcatenatedWordsInADict(words4))  # Output: ["applepen", "pineapple"]

"""
Time Complexity:
- Let `n` be the number of words in the input list and `L` be the average length of the words.
- Checking if a word can be formed using `canForm` takes O(L^2) time due to the nested loop and substring checks.
- For each word, we iterate through the list, so the overall complexity is O(n * L^2).

Space Complexity:
- The `dp` array in `canForm` takes O(L) space for each word.
- The `word_set` takes O(n * L) space to store all the words.
- Overall space complexity is O(n * L).

Topic: Dynamic Programming (DP), String Manipulation, Hash Set
"""