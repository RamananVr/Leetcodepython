"""
LeetCode Problem #30: Substring with Concatenation of All Words

Problem Statement:
You are given a string `s` and an array of strings `words` of the same length. 
Return all starting indices of substring(s) in `s` that is a concatenation of each word in `words` exactly once, 
in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- `s` and `words[i]` consist of lowercase English letters.
"""

def findSubstring(s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_map = {}

    # Create a frequency map for the words
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1

    result = []

    # Iterate through the string
    for i in range(len(s) - total_len + 1):
        seen = {}
        j = 0
        while j < word_count:
            # Extract a word from the string
            word = s[i + j * word_len:i + (j + 1) * word_len]
            if word in word_map:
                seen[word] = seen.get(word, 0) + 1
                # If the word frequency exceeds the allowed frequency, break
                if seen[word] > word_map[word]:
                    break
            else:
                break
            j += 1
        # If all words are matched
        if j == word_count:
            result.append(i)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    print(findSubstring(s1, words1))  # Output: [0, 9]

    # Test Case 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    print(findSubstring(s2, words2))  # Output: []

    # Test Case 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    print(findSubstring(s3, words3))  # Output: [6, 9, 12]

    # Test Case 4
    s4 = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words4 = ["fooo", "barr", "wing", "ding", "wing"]
    print(findSubstring(s4, words4))  # Output: [13]

# Topic: Strings, Hash Table, Sliding Window