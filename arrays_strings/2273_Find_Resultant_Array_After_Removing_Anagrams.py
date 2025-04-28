"""
LeetCode Problem #2273: Find Resultant Array After Removing Anagrams

Problem Statement:
You are given a 0-indexed string array `words`, where `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that `0 < i < words.length` and `words[i - 1]` and `words[i]` are anagrams, and delete `words[i]` from `words`. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return `words` after performing all operations. It can be shown that selecting the indices for deletion in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "ab" and "ba" are anagrams of each other.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 10
- `words[i]` consists of lowercase English letters.

Example:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
"""

# Python Solution
def removeAnagrams(words):
    """
    Removes consecutive anagrams from the list of words.

    :param words: List[str] - A list of lowercase English words.
    :return: List[str] - The resultant list after removing consecutive anagrams.
    """
    result = [words[0]]  # Initialize the result with the first word
    for i in range(1, len(words)):
        # Check if the current word is an anagram of the last word in the result
        if sorted(words[i]) != sorted(result[-1]):
            result.append(words[i])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abba", "baba", "bbaa", "cd", "cd"]
    print(removeAnagrams(words1))  # Output: ["abba", "cd"]

    # Test Case 2
    words2 = ["a", "b", "c", "d", "e"]
    print(removeAnagrams(words2))  # Output: ["a", "b", "c", "d", "e"]

    # Test Case 3
    words3 = ["listen", "silent", "enlist", "google", "gogole"]
    print(removeAnagrams(words3))  # Output: ["listen", "google"]

    # Test Case 4
    words4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz", "pqr"]
    print(removeAnagrams(words4))  # Output: ["abc", "xyz", "pqr"]

    # Test Case 5
    words5 = ["a"]
    print(removeAnagrams(words5))  # Output: ["a"]

# Time Complexity Analysis:
# - Sorting each word takes O(k log k), where k is the length of the word.
# - For n words, the total time complexity is O(n * k log k), where n is the number of words.
# - In the worst case, k = 10 (maximum word length), so the complexity simplifies to O(n * log k).

# Space Complexity Analysis:
# - Sorting each word requires O(k) space for the sorted version of the word.
# - The result list requires O(n) space in the worst case.
# - Thus, the total space complexity is O(n + k).

# Topic: Arrays, Strings