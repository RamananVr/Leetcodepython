"""
LeetCode Question #1935: Maximum Number of Words You Can Type

Problem Statement:
A keyboard consists of alphabetic keys and a space bar. You are typing a text, and you want to know how many words you can type using the keyboard. Sometimes, certain keys are broken, and you cannot use them.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all broken keys, return the number of words in `text` that you can fully type using the keyboard.

Constraints:
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.

Example:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: The word "hello" can be typed since none of its letters are broken, but the word "world" cannot be typed because the letter "d" is broken.

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: The word "leet" cannot be typed because the letters "l" and "t" are broken. The word "code" can be typed.

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: Neither of the words can be typed because the letter "e" is broken.
"""

# Clean, Correct Python Solution
def canBeTypedWords(text: str, brokenLetters: str) -> int:
    # Convert broken letters into a set for quick lookup
    broken_set = set(brokenLetters)
    # Split the text into words
    words = text.split()
    # Count words that can be typed
    count = 0
    for word in words:
        # Check if any letter in the word is broken
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
    brokenLetters4 = "q"
    print(canBeTypedWords(text4, brokenLetters4))  # Output: 3

    # Test Case 5
    text5 = "keyboard"
    brokenLetters5 = ""
    print(canBeTypedWords(text5, brokenLetters5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the text into words takes O(n), where n is the length of the text.
- For each word, we check if any of its characters are in the broken set. This takes O(m * k), where m is the average length of a word and k is the number of words in the text.
- Overall, the complexity is O(n + m * k), which simplifies to O(n) since m * k is proportional to n.

Space Complexity:
- The space complexity is O(b), where b is the length of the brokenLetters string, due to the set used for storing broken letters.
- The split operation creates a list of words, which takes O(k), where k is the number of words in the text.
- Overall, the space complexity is O(b + k).
"""

# Topic: Strings