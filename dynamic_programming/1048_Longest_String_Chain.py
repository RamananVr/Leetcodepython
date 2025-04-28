"""
LeetCode Problem #1048: Longest String Chain

Problem Statement:
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA 
without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor 
of word2, word2 is a predecessor of word3, and so on.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The chain ["abcd"] is the longest word chain possible, and not ["abcd","dbqca"], 
because "dbqca" is not a valid predecessor of "abcd".

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 16
- words[i] consists only of lowercase English letters.
"""

# Solution
def longestStrChain(words):
    # Sort words by length
    words.sort(key=len)
    
    # Dictionary to store the longest chain ending at each word
    dp = {}
    
    # Iterate through each word
    for word in words:
        dp[word] = 1  # Initialize chain length for the current word
        # Try removing one character at a time to find predecessors
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            if predecessor in dp:
                dp[word] = max(dp[word], dp[predecessor] + 1)
    
    # Return the maximum chain length found
    return max(dp.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestStrChain(words1))  # Output: 4

    # Test Case 2
    words2 = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    print(longestStrChain(words2))  # Output: 5

    # Test Case 3
    words3 = ["abcd", "dbqca"]
    print(longestStrChain(words3))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the words by length takes O(n log n), where n is the number of words.
- For each word, we iterate through its characters (up to 16, since the maximum word length is 16) 
  and check for predecessors in the dictionary. This takes O(n * m), where m is the average word length.
- Overall, the time complexity is O(n log n + n * m), which simplifies to O(n log n) for large n.

Space Complexity:
- The space complexity is O(n), where n is the number of words, due to the dictionary `dp` storing chain lengths.
"""

# Topic: Dynamic Programming