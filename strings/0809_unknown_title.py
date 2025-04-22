"""
LeetCode Problem #809: Expressive Words

Problem Statement:
Sometimes people repeat letters to represent extra feeling. For example:
- "hello" -> "heeellooo"
Here, the 'e' and 'o' are extended, and the word "hello" becomes "heeellooo".

We will call a string s "stretchy" if it can be turned into another string t by extending some of its letters. Formally, we can say s is stretchy if:
- We can split s into groups of consecutive characters s = s1 + s2 + ... + sk.
- We can split t into groups of consecutive characters t = t1 + t2 + ... + tk.
- For each group, the character is the same and:
  - If the group length in s is 3 or more, the group length in t can be greater than or equal to the group length in s.
  - Otherwise, the group lengths in s and t must be the same.

Given a string s and an array of query strings words, return the number of words in words that are stretchy.

Example:
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
- "hello" can be stretched to "heeellooo".
- "hi" cannot be stretched because it is missing letters.
- "helo" cannot be stretched because the 'o' is not extended enough.

Constraints:
- 1 <= s.length, words.length <= 100
- 1 <= words[i].length <= 100
- s and all words[i] consist only of lowercase English letters.
"""

def expressiveWords(s: str, words: list[str]) -> int:
    def get_groups(word):
        """Helper function to group characters and their counts."""
        groups, counts = [], []
        prev_char, count = word[0], 0
        for char in word:
            if char == prev_char:
                count += 1
            else:
                groups.append(prev_char)
                counts.append(count)
                prev_char, count = char, 1
        groups.append(prev_char)
        counts.append(count)
        return groups, counts

    def is_stretchy(base_groups, base_counts, word_groups, word_counts):
        """Check if a word is stretchy compared to the base string."""
        if base_groups != word_groups:
            return False
        for b_count, w_count in zip(base_counts, word_counts):
            if b_count < w_count or (b_count < 3 and b_count != w_count):
                return False
        return True

    # Get groups and counts for the base string
    base_groups, base_counts = get_groups(s)
    stretchy_count = 0

    # Check each word in the list
    for word in words:
        word_groups, word_counts = get_groups(word)
        if is_stretchy(base_groups, base_counts, word_groups, word_counts):
            stretchy_count += 1

    return stretchy_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(expressiveWords(s, words))  # Output: 1

    # Test Case 2
    s = "zzzzzyyyyy"
    words = ["zzyy", "zy", "zyy"]
    print(expressiveWords(s, words))  # Output: 3

    # Test Case 3
    s = "aaa"
    words = ["aaaa", "aa", "aaa"]
    print(expressiveWords(s, words))  # Output: 1

    # Test Case 4
    s = "heeellooo"
    words = ["heeelloo", "heeellooo", "heeelloooo"]
    print(expressiveWords(s, words))  # Output: 2

"""
Time Complexity Analysis:
- The `get_groups` function processes each string in O(n), where n is the length of the string.
- For each word in `words`, we compare its groups with the base string's groups, which takes O(m), where m is the length of the base string.
- If there are w words in the list, the total complexity is O(w * max(n, m)), where n is the average length of the words and m is the length of the base string.

Space Complexity Analysis:
- The space complexity is O(n + m) for storing the groups and counts of the base string and a single word.

Topic: Strings
"""