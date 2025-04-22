"""
LeetCode Question #320: Generalized Abbreviation

Problem Statement:
Write a function to generate the generalized abbreviations of a word.

A word's generalized abbreviation can be constructed by replacing some (or none) of the characters with their respective counts of consecutive characters. For example:
- The word "word" can be abbreviated as "word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4".

Given a string `word`, return a list of all the possible generalized abbreviations of `word`. Return the answer in any order.

Constraints:
- `1 <= word.length <= 15`
- `word` consists of only lowercase English letters.
"""

from typing import List

def generateAbbreviations(word: str) -> List[str]:
    def backtrack(pos: int, current: str, count: int):
        # If we've reached the end of the word, finalize the abbreviation
        if pos == len(word):
            result.append(current + (str(count) if count > 0 else ""))
            return
        
        # Option 1: Abbreviate the current character (increment count)
        backtrack(pos + 1, current, count + 1)
        
        # Option 2: Keep the current character (reset count)
        backtrack(pos + 1, current + (str(count) if count > 0 else "") + word[pos], 0)
    
    result = []
    backtrack(0, "", 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "word"
    print("Abbreviations for 'word':", generateAbbreviations(word1))
    # Expected Output: ['word', '1ord', 'w1rd', 'wo1d', 'wor1', '2rd', 'w2d', 'wo2', '1o1d', '1or1', 'w1r1', '1o2', '2r1', '3d', 'w3', '4']

    # Test Case 2
    word2 = "a"
    print("Abbreviations for 'a':", generateAbbreviations(word2))
    # Expected Output: ['a', '1']

    # Test Case 3
    word3 = "ab"
    print("Abbreviations for 'ab':", generateAbbreviations(word3))
    # Expected Output: ['ab', '1b', 'a1', '2']

"""
Time Complexity Analysis:
- The total number of abbreviations for a word of length `n` is `2^n` because each character has two choices: to be abbreviated or not.
- The backtracking function explores all these possibilities, so the time complexity is O(2^n).

Space Complexity Analysis:
- The space complexity is O(n) for the recursion stack, where `n` is the length of the word.
- Additionally, the result list will store all `2^n` abbreviations, so the space complexity for the result is O(2^n).

Overall Space Complexity: O(n + 2^n)

Topic: Backtracking
"""