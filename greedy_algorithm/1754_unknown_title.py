"""
LeetCode Problem #1754: Largest Merge Of Two Strings

Problem Statement:
You are given two strings `word1` and `word2`. You want to construct a string `merge` in the following way:
- While either `word1` or `word2` are non-empty, choose one of the following options:
  - If `word1` is non-empty, append the first character in `word1` to `merge` and delete it from `word1`.
  - If `word2` is non-empty, append the first character in `word2` to `merge` and delete it from `word2`.
- Return the lexicographically largest `merge` you can construct.

Example 1:
Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"

Example 2:
Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"

Constraints:
- 1 <= word1.length, word2.length <= 3000
- word1 and word2 consist only of lowercase English letters.
"""

def largestMerge(word1: str, word2: str) -> str:
    """
    Constructs the lexicographically largest merge of two strings.
    
    Args:
    word1 (str): The first input string.
    word2 (str): The second input string.
    
    Returns:
    str: The lexicographically largest merge of the two strings.
    """
    merge = []
    i, j = 0, 0

    # Use two pointers to construct the merge
    while i < len(word1) and j < len(word2):
        # Compare the remaining substrings of word1 and word2
        if word1[i:] > word2[j:]:
            merge.append(word1[i])
            i += 1
        else:
            merge.append(word2[j])
            j += 1

    # Append the remaining characters from word1 or word2
    merge.append(word1[i:])
    merge.append(word2[j:])

    return ''.join(merge)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "cabaa"
    word2 = "bcaaa"
    print("Test Case 1 Output:", largestMerge(word1, word2))  # Expected: "cbcabaaaaa"

    # Test Case 2
    word1 = "abcabc"
    word2 = "abdcaba"
    print("Test Case 2 Output:", largestMerge(word1, word2))  # Expected: "abdcabcabcaba"

    # Test Case 3
    word1 = "aaa"
    word2 = "aaa"
    print("Test Case 3 Output:", largestMerge(word1, word2))  # Expected: "aaaaaa"

    # Test Case 4
    word1 = "z"
    word2 = "a"
    print("Test Case 4 Output:", largestMerge(word1, word2))  # Expected: "za"

# Time Complexity Analysis:
# - Comparing substrings word1[i:] and word2[j:] takes O(n + m) in the worst case, where n and m are the lengths of word1 and word2.
# - Since we perform this comparison for each character in word1 and word2, the overall time complexity is O((n + m)^2).
# - Appending characters to the merge list is O(1) per operation, so it does not dominate the complexity.

# Space Complexity Analysis:
# - The space complexity is O(n + m) for the merge list, where n and m are the lengths of word1 and word2.
# - No additional space is used apart from the output.

# Topic: Greedy Algorithm