"""
LeetCode Problem #1255: Maximum Score Words Formed by Letters

Problem Statement:
Given a list of words, list of single letters `letters` (might contain duplicates), and a list `score` of 26 integers where `score[i]` is the score of the ith letter (a = 0, b = 1, ..., z = 25), return the maximum score of any valid set of words formed by using the given letters (each letter can be used at most once).

A valid set of words is any subset of `words` such that each word can be formed by the given `letters`. The score of a word is the sum of the scores of its letters.

Constraints:
1. 1 <= words.length <= 14
2. 1 <= words[i].length <= 15
3. 1 <= letters.length <= 100
4. letters[i].length == 1
5. score.length == 26
6. 0 <= score[i] <= 10
7. words[i] and letters[i] consist of lowercase English letters.

Example:
Input: words = ["dog", "cat", "dad", "good"], letters = ["a", "a", "c", "d", "d", "g", "o", "o"], score = [1,0,9,5,0,0,3,0,0,2,0,8,0,6,7,0,0,0,0,4,0,0,0,5,0,0]
Output: 23
Explanation: The word "dad" can be formed for a score of 9 + 5 + 5 = 19. The word "good" can be formed for a score of 3 + 7 + 7 + 6 = 23. The maximum score is 23.

"""

from collections import Counter
from typing import List

def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    def calculate_score(word):
        """Calculate the score of a word based on the score array."""
        return sum(score[ord(char) - ord('a')] for char in word)

    def can_form_word(word, available_letters):
        """Check if a word can be formed with the available letters."""
        word_count = Counter(word)
        for char, count in word_count.items():
            if available_letters[char] < count:
                return False
        return True

    def backtrack(index, available_letters):
        """Backtracking function to explore all subsets of words."""
        if index == len(words):
            return 0

        # Skip the current word
        max_score = backtrack(index + 1, available_letters)

        # Try to include the current word if possible
        word = words[index]
        if can_form_word(word, available_letters):
            word_count = Counter(word)
            for char in word_count:
                available_letters[char] -= word_count[char]
            max_score = max(max_score, calculate_score(word) + backtrack(index + 1, available_letters))
            for char in word_count:
                available_letters[char] += word_count[char]

        return max_score

    # Convert letters to a Counter for easier management
    available_letters = Counter(letters)
    return backtrack(0, available_letters)

# Example Test Cases
if __name__ == "__main__":
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 2, 0, 8, 0, 6, 7, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0]
    print(maxScoreWords(words, letters, score))  # Output: 23

    words = ["a", "b", "c", "d"]
    letters = ["a", "b", "c", "d"]
    score = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(maxScoreWords(words, letters, score))  # Output: 10

    words = ["xyz", "xy", "z"]
    letters = ["x", "y", "z", "z"]
    score = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
    print(maxScoreWords(words, letters, score))  # Output: 12

# Time Complexity Analysis:
# Let n = len(words), m = len(letters), and k = average length of a word.
# - The backtracking explores all subsets of words, which is O(2^n).
# - For each subset, we check if a word can be formed and calculate its score, which takes O(k) time.
# - Thus, the overall time complexity is O(2^n * k).
# - Space complexity is O(m + n), where m is for the Counter of letters and n is for the recursion stack.

# Topic: Backtracking