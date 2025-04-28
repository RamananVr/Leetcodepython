"""
LeetCode Problem #318: Maximum Product of Word Lengths

Problem Statement:
Given a string array `words`, return the maximum value of `length(word[i]) * length(word[j])` 
where the two words do not share common letters. If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words exist.

Constraints:
- 2 <= words.length <= 1000
- 1 <= words[i].length <= 1000
- words[i] consists only of lowercase English letters.
"""

# Clean, Correct Python Solution
def maxProduct(words):
    """
    Finds the maximum product of lengths of two words in the list `words` such that
    the two words do not share any common letters.

    :param words: List[str] - List of words
    :return: int - Maximum product of lengths of two words without common letters
    """
    # Precompute bit masks for each word
    word_masks = []
    for word in words:
        mask = 0
        for char in word:
            mask |= (1 << (ord(char) - ord('a')))
        word_masks.append(mask)
    
    max_product = 0
    n = len(words)
    
    # Compare each pair of words
    for i in range(n):
        for j in range(i + 1, n):
            if word_masks[i] & word_masks[j] == 0:  # No common letters
                max_product = max(max_product, len(words[i]) * len(words[j]))
    
    return max_product

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(maxProduct(words1))  # Output: 16

    # Test Case 2
    words2 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(maxProduct(words2))  # Output: 4

    # Test Case 3
    words3 = ["a", "aa", "aaa", "aaaa"]
    print(maxProduct(words3))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Precomputing the bit masks for each word takes O(L), where L is the total number of characters across all words.
- Comparing each pair of words takes O(n^2), where n is the number of words.
- Overall time complexity: O(L + n^2).

Space Complexity:
- The space used for storing the bit masks is O(n), where n is the number of words.
- Overall space complexity: O(n).
"""

# Topic: Bit Manipulation