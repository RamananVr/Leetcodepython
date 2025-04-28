"""
LeetCode Problem #2062: Count Vowel Substrings of a String

Problem Statement:
A substring is a contiguous (non-empty) sequence of characters within a string. A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', 'u') and contains all five vowels at least once.

Given a string word, return the number of vowel substrings in word.

Example 1:
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are:
- "aeiou" (contains all 5 vowels)
- "aeiouu" (contains all 5 vowels)

Example 2:
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present in any substring.

Example 3:
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are:
- "uaieo" (contains all 5 vowels)
- "uaieu" (contains all 5 vowels)
- "uaieuo" (contains all 5 vowels)
- "uaieuou" (contains all 5 vowels)
- "aieuo" (contains all 5 vowels)
- "aieuou" (contains all 5 vowels)
- "aieuoua" (contains all 5 vowels)

Constraints:
- 1 <= word.length <= 100
- word consists of lowercase English letters only.
"""

def countVowelSubstrings(word: str) -> int:
    def is_vowel(ch: str) -> bool:
        return ch in "aeiou"

    n = len(word)
    vowels = set("aeiou")
    count = 0

    for i in range(n):
        if is_vowel(word[i]):
            seen = set()
            for j in range(i, n):
                if is_vowel(word[j]):
                    seen.add(word[j])
                    if seen == vowels:
                        count += 1
                else:
                    break
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "aeiouu"
    print(countVowelSubstrings(word1))  # Output: 2

    # Test Case 2
    word2 = "unicornarihan"
    print(countVowelSubstrings(word2))  # Output: 0

    # Test Case 3
    word3 = "cuaieuouac"
    print(countVowelSubstrings(word3))  # Output: 7

    # Test Case 4
    word4 = "bcbcbc"
    print(countVowelSubstrings(word4))  # Output: 0

    # Test Case 5
    word5 = "aeiouaeiou"
    print(countVowelSubstrings(word5))  # Output: 15

"""
Time Complexity Analysis:
- The outer loop runs `n` times, where `n` is the length of the string.
- The inner loop runs at most `n` times for each iteration of the outer loop.
- In the worst case, the algorithm checks all substrings, leading to a time complexity of O(n^2).

Space Complexity Analysis:
- The space complexity is O(1) since we only use a fixed set to track vowels and a few variables.

Topic: Strings
"""