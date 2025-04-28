"""
LeetCode Question #1880: Check if Word Equals Summation of Two Words

Problem Statement:
The letter value of a letter is its position in the alphabet starting from 0 (i.e., 'a' -> 0, 'b' -> 1, ..., 'z' -> 25).
The numerical value of some string of lowercase English letters `word` is the concatenation of the letter values of each letter in `word`, which is then converted into an integer.

For example, if `word = "acb"`:
- The letter values are ['a' -> 0, 'c' -> 2, 'b' -> 1].
- The numerical value is "021" -> 21.

Given three strings `firstWord`, `secondWord`, and `targetWord`, return `true` if the summation of the numerical values of `firstWord` and `secondWord` equals the numerical value of `targetWord`, or `false` otherwise.

Constraints:
- `1 <= firstWord.length, secondWord.length, targetWord.length <= 8`
- `firstWord`, `secondWord`, and `targetWord` consist of lowercase English letters only.
"""

# Python Solution
def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def word_to_value(word: str) -> int:
        # Convert each character to its letter value and concatenate to form the numerical value
        return int("".join(str(ord(char) - ord('a')) for char in word))
    
    # Calculate numerical values for each word
    first_value = word_to_value(firstWord)
    second_value = word_to_value(secondWord)
    target_value = word_to_value(targetWord)
    
    # Check if the sum of firstWord and secondWord equals targetWord
    return first_value + second_value == target_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    firstWord = "acb"
    secondWord = "cba"
    targetWord = "cdb"
    print(isSumEqual(firstWord, secondWord, targetWord))  # Expected: True

    # Test Case 2
    firstWord = "aaa"
    secondWord = "a"
    targetWord = "aaaa"
    print(isSumEqual(firstWord, secondWord, targetWord))  # Expected: True

    # Test Case 3
    firstWord = "abc"
    secondWord = "def"
    targetWord = "ghij"
    print(isSumEqual(firstWord, secondWord, targetWord))  # Expected: False

    # Test Case 4
    firstWord = "zzz"
    secondWord = "zzz"
    targetWord = "zzzz"
    print(isSumEqual(firstWord, secondWord, targetWord))  # Expected: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function `word_to_value` processes each word by iterating through its characters.
- For a word of length `n`, the conversion takes O(n) time.
- Since we call `word_to_value` three times (once for each word), the total time complexity is O(n), where `n` is the maximum length of the three words.

Space Complexity:
- The function uses a list comprehension to construct the numerical value string, which takes O(n) space for a word of length `n`.
- The space complexity for the entire function is O(n), where `n` is the maximum length of the three words.
"""

# Topic: Strings