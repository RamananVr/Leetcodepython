"""
LeetCode Problem #336: Palindrome Pairs

Problem Statement:
Given a list of unique words, return all the pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are:
- "dcbaabcd" from words[1] + words[0]
- "abcddcba" from words[0] + words[1]
- "slls" from words[3] + words[2]
- "llssssll" from words[2] + words[4]

Constraints:
1. 1 <= words.length <= 5000
2. 0 <= words[i].length <= 300
3. words[i] consists of lower-case English letters.
"""

# Solution
def palindromePairs(words):
    def is_palindrome(s):
        return s == s[::-1]

    word_map = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        n = len(word)
        for j in range(n + 1):
            prefix, suffix = word[:j], word[j:]
            
            # Case 1: If prefix is a palindrome, check if reversed suffix exists in the map
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_map and word_map[reversed_suffix] != i:
                    result.append([word_map[reversed_suffix], i])
            
            # Case 2: If suffix is a palindrome, check if reversed prefix exists in the map
            # Avoid duplicates by ensuring j != n (to prevent double-counting empty suffix)
            if j != n and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_map and word_map[reversed_prefix] != i:
                    result.append([i, word_map[reversed_prefix]])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abcd", "dcba", "lls", "s", "sssll"]
    print(palindromePairs(words1))  # Expected Output: [[0, 1], [1, 0], [3, 2], [2, 4]]

    # Test Case 2
    words2 = ["bat", "tab", "cat"]
    print(palindromePairs(words2))  # Expected Output: [[0, 1], [1, 0]]

    # Test Case 3
    words3 = ["a", ""]
    print(palindromePairs(words3))  # Expected Output: [[0, 1], [1, 0]]

    # Test Case 4
    words4 = ["race", "car", "ecar"]
    print(palindromePairs(words4))  # Expected Output: [[0, 2], [2, 0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(words) and k = average length of a word.
- Building the word_map takes O(n).
- For each word, we check all possible splits (n + 1 splits per word), and for each split, we perform:
  - A palindrome check, which takes O(k).
  - A dictionary lookup, which takes O(1).
- Thus, the overall time complexity is O(n * k^2), where k^2 comes from the palindrome check and split operations.

Space Complexity:
- The word_map dictionary takes O(n * k) space to store all words and their indices.
- The result list takes O(n^2) space in the worst case (if all pairs are valid).
- Thus, the overall space complexity is O(n * k + n^2).
"""

# Topic: Strings, Hash Table