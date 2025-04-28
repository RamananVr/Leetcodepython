"""
LeetCode Problem #1939: Maximum Number of Words You Can Type

Problem Statement:
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all distinct letters that are broken, return the number of words in the text you can fully type using this keyboard.

A word is fully typable if it does not contain any broken letters.

Constraints:
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each broken letter is a lowercase English letter.
- `0 <= text.split().length <= 10^4`

Example:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: The only word you can fully type is "world".

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: The only word you can fully type is "code".

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: There are no words you can fully type.
"""

# Python Solution
def canBeTypedWords(text: str, brokenLetters: str) -> int:
    # Convert brokenLetters into a set for O(1) lookup
    broken_set = set(brokenLetters)
    # Split the text into words
    words = text.split()
    # Count the number of words that do not contain any broken letters
    count = 0
    for word in words:
        if not any(char in broken_set for char in word):
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "hello world"
    brokenLetters1 = "ad"
    print(canBeTypedWords(text1, brokenLetters1))  # Output: 1

    # Test Case 2
    text2 = "leet code"
    brokenLetters2 = "lt"
    print(canBeTypedWords(text2, brokenLetters2))  # Output: 1

    # Test Case 3
    text3 = "leet code"
    brokenLetters3 = "e"
    print(canBeTypedWords(text3, brokenLetters3))  # Output: 0

    # Test Case 4
    text4 = "a quick brown fox"
    brokenLetters4 = "z"
    print(canBeTypedWords(text4, brokenLetters4))  # Output: 4

    # Test Case 5
    text5 = "a quick brown fox"
    brokenLetters5 = "o"
    print(canBeTypedWords(text5, brokenLetters5))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the text into words takes O(n), where n is the length of the text.
- For each word, we check if any character is in the broken set. This takes O(m * k), where m is the average length of a word and k is the number of words in the text.
- Overall, the time complexity is O(n + m * k). Since m * k is approximately equal to n, the time complexity simplifies to O(n).

Space Complexity:
- The space complexity is O(b), where b is the length of the brokenLetters string, as we store the broken letters in a set.
- The space used for splitting the text into words is also O(n), but this is temporary and depends on the input size.

Overall Space Complexity: O(n + b)
"""

# Topic: Strings