"""
LeetCode Problem #288: Unique Word Abbreviation

Problem Statement:
The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is not abbreviated.

For example:
- "dog" --> "d1g"
- "internationalization" --> "i18n"
- "it" --> "it" (no abbreviation)

Implement the `ValidWordAbbr` class:
- `ValidWordAbbr(dictionary: List[str])` Initializes the object with a dictionary of words.
- `bool isUnique(word: str)` Returns true if the abbreviation of `word` is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation, or if the only word with that abbreviation in the dictionary is the word itself.

Constraints:
- 1 <= dictionary.length <= 3 * 10^4
- 1 <= dictionary[i].length <= 20
- dictionary[i] consists of lowercase English letters.
- 1 <= word.length <= 20
- word consists of lowercase English letters.
"""

from typing import List

class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        # Use a dictionary to store abbreviations and their corresponding words
        self.abbr_dict = {}
        # Use a set to avoid duplicate words in the dictionary
        unique_words = set(dictionary)
        
        for word in unique_words:
            abbr = self._get_abbreviation(word)
            if abbr not in self.abbr_dict:
                self.abbr_dict[abbr] = set()
            self.abbr_dict[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbreviation(word)
        # Check if the abbreviation exists in the dictionary
        if abbr not in self.abbr_dict:
            return True
        # If the abbreviation exists, check if it is only associated with the same word
        return self.abbr_dict[abbr] == {word}

    def _get_abbreviation(self, word: str) -> str:
        # Helper function to compute the abbreviation of a word
        if len(word) <= 2:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"

# Example Test Cases
if __name__ == "__main__":
    # Initialize the dictionary
    dictionary = ["deer", "door", "cake", "card"]
    valid_word_abbr = ValidWordAbbr(dictionary)

    # Test cases
    print(valid_word_abbr.isUnique("dear"))  # Output: False (same abbreviation as "deer")
    print(valid_word_abbr.isUnique("cart"))  # Output: True (unique abbreviation "c2t")
    print(valid_word_abbr.isUnique("cane"))  # Output: False (same abbreviation as "cake")
    print(valid_word_abbr.isUnique("make"))  # Output: True (unique abbreviation "m2e")

"""
Time and Space Complexity Analysis:

1. Initialization (`__init__`):
   - Time Complexity: O(n * m), where `n` is the number of words in the dictionary and `m` is the average length of the words. This is because we iterate through each word in the dictionary and compute its abbreviation.
   - Space Complexity: O(n * m), as we store the abbreviations and their corresponding words in a dictionary.

2. `isUnique` Method:
   - Time Complexity: O(m), where `m` is the length of the input word. This is because we compute the abbreviation of the word and perform a dictionary lookup.
   - Space Complexity: O(1), as no additional data structures are used.

3. Overall:
   - Time Complexity: O(n * m) for initialization and O(m) for each `isUnique` call.
   - Space Complexity: O(n * m).

Topic: Hash Table
"""