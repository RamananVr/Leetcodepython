"""
LeetCode Question #819: Most Common Word

Problem Statement:
Given a string `paragraph` and a string array of `banned` words, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in `paragraph` are case-insensitive and the answer should be returned in lowercase.

Constraints:
- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters.

Example:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most common non-banned word in the paragraph.
"""

# Solution
import collections
import re

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    # Normalize the paragraph by converting to lowercase and replacing non-alphanumeric characters with spaces
    normalized_paragraph = re.sub(r'[^\w]', ' ', paragraph).lower()
    # Split the paragraph into words
    words = normalized_paragraph.split()
    # Create a set of banned words for quick lookup
    banned_set = set(banned)
    # Count the frequency of each word that is not banned
    word_count = collections.Counter(word for word in words if word not in banned_set)
    # Return the word with the highest frequency
    return max(word_count, key=word_count.get)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))  # Output: "ball"

    # Test Case 2
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(mostCommonWord(paragraph, banned))  # Output: "b"

    # Test Case 3
    paragraph = "The quick brown fox jumped over the lazy dog."
    banned = ["the", "lazy"]
    print(mostCommonWord(paragraph, banned))  # Output: "quick"

    # Test Case 4
    paragraph = "Hello! Hello? HELLO... hello; world world."
    banned = ["hello"]
    print(mostCommonWord(paragraph, banned))  # Output: "world"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Normalizing the paragraph (re.sub and lower): O(n), where n is the length of the paragraph.
- Splitting the paragraph into words: O(n).
- Counting word frequencies: O(m), where m is the number of words in the paragraph.
- Finding the maximum frequency word: O(m).
Overall: O(n + m), which simplifies to O(n) since m <= n.

Space Complexity:
- Storage for normalized paragraph: O(n).
- Storage for word list: O(m).
- Storage for word count dictionary: O(m).
- Storage for banned set: O(b), where b is the number of banned words.
Overall: O(n + b).
"""

# Topic: Strings, Hash Table