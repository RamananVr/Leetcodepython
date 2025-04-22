"""
LeetCode Problem #140: Word Break II

Problem Statement:
Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume that the dictionary does not contain duplicate words.

Example 1:
Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
Output: ["cats and dog", "cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: []

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings in `wordDict` are unique.
"""

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    # Convert wordDict to a set for O(1) lookups
    word_set = set(wordDict)
    # Memoization dictionary to store results for substrings
    memo = {}

    def backtrack(start: int) -> List[str]:
        # If we have already computed the result for this start index, return it
        if start in memo:
            return memo[start]
        
        # If we reach the end of the string, return an empty list (base case)
        if start == len(s):
            return [""]

        # List to store all valid sentences starting from this index
        sentences = []

        # Try every possible end index for the current substring
        for end in range(start + 1, len(s) + 1):
            # Extract the substring
            word = s[start:end]
            # If the substring is in the dictionary
            if word in word_set:
                # Recursively solve for the remaining substring
                rest_sentences = backtrack(end)
                # Combine the current word with the results of the recursive call
                for sentence in rest_sentences:
                    if sentence:
                        sentences.append(word + " " + sentence)
                    else:
                        sentences.append(word)

        # Store the result in the memo dictionary
        memo[start] = sentences
        return sentences

    # Start the backtracking from index 0
    return backtrack(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    print("Test Case 1 Output:", wordBreak(s1, wordDict1))  # Expected: ["cats and dog", "cat sand dog"]

    # Test Case 2
    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print("Test Case 2 Output:", wordBreak(s2, wordDict2))  # Expected: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print("Test Case 3 Output:", wordBreak(s3, wordDict3))  # Expected: []

"""
Time Complexity:
- Let n = len(s) and m = the average length of words in wordDict.
- The backtracking function explores all possible partitions of the string. In the worst case, there are 2^n partitions.
- For each partition, we check if the substring is in the dictionary, which takes O(m) time on average.
- Memoization helps reduce redundant computations, but the worst-case complexity is still exponential: O(2^n * m).

Space Complexity:
- The memo dictionary stores results for up to n substrings, each of which can have multiple sentences. In the worst case, this requires O(2^n) space.
- The recursion stack can go up to O(n) depth.
- Total space complexity: O(2^n).

Topic: Dynamic Programming (DP) + Backtracking
"""