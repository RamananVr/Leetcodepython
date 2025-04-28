"""
LeetCode Problem #1178: Number of Valid Words for Each Puzzle

Problem Statement:
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
1. Word contains the first letter of the puzzle.
2. For each letter in the word, that letter is in the puzzle.

For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while
invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list that are valid with respect to the puzzle puzzles[i].

Constraints:
- 1 <= words.length <= 10^5
- 4 <= words[i].length <= 50
- 1 <= puzzles.length <= 10^4
- puzzles[i].length == 7
- words[i] and puzzles[i] consist of lowercase English letters.
- Each puzzle[i] doesn't contain repeated characters.

Example:
Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]

Explanation:
- For "aboveyz", only "aaaa" is valid.
- For "abrodyz", only "aaaa" is valid.
- For "abslute", "aaaa", "asas", and "able" are valid.
- For "absoryz", "aaaa" and "asas" are valid.
- For "actresz", "aaaa", "asas", "actt", and "access" are valid.
- For "gaswxyz", no words are valid.

Topic: Bit Manipulation
"""

from collections import Counter

def findNumOfValidWords(words, puzzles):
    def word_to_bitmask(word):
        """Convert a word into a bitmask representation."""
        bitmask = 0
        for char in word:
            bitmask |= (1 << (ord(char) - ord('a')))
        return bitmask

    # Preprocess words into bitmasks and count their frequencies
    word_count = Counter(word_to_bitmask(word) for word in words)

    result = []
    for puzzle in puzzles:
        # Convert the puzzle into a bitmask
        puzzle_bitmask = word_to_bitmask(puzzle)
        # The first letter of the puzzle must be present
        first_letter_bit = 1 << (ord(puzzle[0]) - ord('a'))

        # Generate all subsets of the puzzle's bitmask
        subset = puzzle_bitmask
        count = 0
        while subset:
            # Check if the subset includes the first letter
            if subset & first_letter_bit:
                count += word_count[subset]
            # Generate the next subset
            subset = (subset - 1) & puzzle_bitmask

        # Check the empty subset (only if it includes the first letter)
        if first_letter_bit & puzzle_bitmask:
            count += word_count[first_letter_bit]

        result.append(count)

    return result

# Example Test Cases
if __name__ == "__main__":
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print(findNumOfValidWords(words, puzzles))  # Output: [1, 1, 3, 2, 4, 0]

    # Additional test cases
    words = ["apple", "pleas", "please"]
    puzzles = ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy"]
    print(findNumOfValidWords(words, puzzles))  # Output: [0, 1, 3, 2]

"""
Time Complexity:
- Preprocessing words into bitmasks: O(W * L), where W is the number of words and L is the average length of a word.
- For each puzzle, generating subsets: O(P * 2^7), where P is the number of puzzles (2^7 because puzzles have at most 7 unique letters).
- Overall: O(W * L + P * 2^7).

Space Complexity:
- Storing word bitmasks in a Counter: O(W).
- Result array: O(P).
- Total: O(W + P).

Topic: Bit Manipulation
"""