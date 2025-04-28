"""
LeetCode Problem #1768: Merge Strings Alternately

Problem Statement:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The letters from word1 and word2 are merged alternately. Since both strings are the same length, 
all their letters are merged alternately.

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end of the merged string.

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end of the merged string.

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""

# Clean and Correct Python Solution
def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    # Append remaining characters from the longer string
    if i < len(word1):
        merged.extend(word1[i:])
    if j < len(word2):
        merged.extend(word2[j:])
    return ''.join(merged)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "abc"
    word2 = "pqr"
    print(mergeAlternately(word1, word2))  # Output: "apbqcr"

    # Test Case 2
    word1 = "ab"
    word2 = "pqrs"
    print(mergeAlternately(word1, word2))  # Output: "apbqrs"

    # Test Case 3
    word1 = "abcd"
    word2 = "pq"
    print(mergeAlternately(word1, word2))  # Output: "apbqcd"

    # Test Case 4 (Edge Case: Single character strings)
    word1 = "a"
    word2 = "b"
    print(mergeAlternately(word1, word2))  # Output: "ab"

    # Test Case 5 (Edge Case: One string is empty)
    word1 = ""
    word2 = "xyz"
    print(mergeAlternately(word1, word2))  # Output: "xyz"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The while loop iterates through the shorter of the two strings, which takes O(min(len(word1), len(word2))).
- The remaining characters from the longer string are appended, which takes O(max(len(word1), len(word2))).
- Overall, the time complexity is O(len(word1) + len(word2)).

Space Complexity:
- The merged list stores all characters from both strings, so its space complexity is O(len(word1) + len(word2)).
- The final string is constructed using ''.join(), which also takes O(len(word1) + len(word2)).
- Overall, the space complexity is O(len(word1) + len(word2)).
"""

# Topic: Strings