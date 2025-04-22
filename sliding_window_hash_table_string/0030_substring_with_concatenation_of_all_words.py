"""
LeetCode Question #30: Substring with Concatenation of All Words

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

# Python Solution
from collections import Counter

def findSubstring(s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []

    for i in range(word_len):
        left = i
        right = i
        current_count = Counter()

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len

            if word in word_freq:
                current_count[word] += 1

                while current_count[word] > word_freq[word]:
                    current_count[s[left:left + word_len]] -= 1
                    left += word_len

                if right - left == total_len:
                    result.append(left)
            else:
                current_count.clear()
                left = right

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

    # Test Case 5
    s5 = "aaaaaa"
    words5 = ["aa", "aa", "aa"]
    print(findSubstring(s5, words5))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the length of the string `s` and `m` be the number of words in `words`.
- Each word has a fixed length `k`.
- The outer loop runs `k` times (word length).
- The inner loop processes the string `s` in chunks of size `k`, so it runs approximately `n / k` times.
- For each chunk, we perform operations like updating the Counter, which takes O(1) on average.
- Overall time complexity: O(k * (n / k)) = O(n).

Space Complexity:
- We use a Counter to store the frequency of words in `words` and another Counter for the current window.
- The space required for these Counters is proportional to the number of unique words in `words`, which is O(m).
- Overall space complexity: O(m).
"""

# Topic: Sliding Window, Hash Table, String