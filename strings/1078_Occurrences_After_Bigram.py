"""
LeetCode Problem #1078: Occurrences After Bigram

Problem Statement:
Given two strings `first` and `second`, consider occurrences in some text of the form "first second third", 
where `second` comes immediately after `first`, and `third` comes immediately after `second`.

For each such occurrence, you must output the word `third`.

Implement a function `findOcurrences(text: str, first: str, second: str) -> List[str]` that takes a string `text` 
and two strings `first` and `second`, and returns a list of all words `third` that appear in the described pattern.

Constraints:
- `text` consists of lowercase English letters and spaces.
- `text` has at least one word.
- `first` and `second` are lowercase English letters.
- 1 <= len(text) <= 1000
- 1 <= len(first), len(second) <= 10

Example:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl", "student"]

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we", "rock"]
"""

from typing import List

def findOcurrences(text: str, first: str, second: str) -> List[str]:
    """
    Finds all occurrences of the word 'third' that follow the pattern 'first second third' in the given text.
    """
    words = text.split()  # Split the text into individual words
    result = []
    
    # Iterate through the words list and check for the pattern
    for i in range(len(words) - 2):
        if words[i] == first and words[i + 1] == second:
            result.append(words[i + 2])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "alice is a good girl she is a good student"
    first1 = "a"
    second1 = "good"
    print(findOcurrences(text1, first1, second1))  # Output: ["girl", "student"]

    # Test Case 2
    text2 = "we will we will rock you"
    first2 = "we"
    second2 = "will"
    print(findOcurrences(text2, first2, second2))  # Output: ["we", "rock"]

    # Test Case 3
    text3 = "hello world hello world hello"
    first3 = "hello"
    second3 = "world"
    print(findOcurrences(text3, first3, second3))  # Output: ["hello", "hello"]

    # Test Case 4
    text4 = "a b c d e f g"
    first4 = "c"
    second4 = "d"
    print(findOcurrences(text4, first4, second4))  # Output: ["e"]

    # Test Case 5
    text5 = "one two three four five"
    first5 = "three"
    second5 = "four"
    print(findOcurrences(text5, first5, second5))  # Output: ["five"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the text into words takes O(n), where n is the length of the text.
- Iterating through the words list takes O(m), where m is the number of words in the text.
- Overall, the time complexity is O(n), as splitting the text dominates the iteration.

Space Complexity:
- The space complexity is O(m), where m is the number of words in the text, due to the storage of the `words` list.
- The `result` list also takes space proportional to the number of matches, but this is negligible compared to the `words` list.
- Overall, the space complexity is O(m).

Topic: Strings
"""