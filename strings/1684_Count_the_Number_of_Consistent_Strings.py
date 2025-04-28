"""
LeetCode Problem #1684: Count the Number of Consistent Strings

Problem Statement:
You are given a string `allowed` consisting of distinct characters and an array of strings `words`.
A string is consistent if all characters in the string appear in the string `allowed`.

Return the number of consistent strings in the array `words`.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:
- 1 <= allowed.length <= 26
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 10
- The characters in `allowed` are distinct.
- `words[i]` and `allowed` contain only lowercase English letters.
"""

def countConsistentStrings(allowed: str, words: list[str]) -> int:
    """
    Counts the number of consistent strings in the array `words` based on the `allowed` string.

    :param allowed: A string of distinct characters that are allowed.
    :param words: A list of strings to check for consistency.
    :return: The number of consistent strings in `words`.
    """
    allowed_set = set(allowed)  # Convert allowed string to a set for O(1) lookups
    consistent_count = 0

    for word in words:
        if all(char in allowed_set for char in word):  # Check if all characters in the word are in allowed_set
            consistent_count += 1

    return consistent_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(countConsistentStrings(allowed, words))  # Output: 2

    # Test Case 2
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(countConsistentStrings(allowed, words))  # Output: 7

    # Test Case 3
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    print(countConsistentStrings(allowed, words))  # Output: 4

    # Test Case 4 (Edge Case: Single allowed character)
    allowed = "a"
    words = ["a", "aa", "aaa", "b", "ab", "ba"]
    print(countConsistentStrings(allowed, words))  # Output: 3

    # Test Case 5 (Edge Case: All words are consistent)
    allowed = "abcdefghijklmnopqrstuvwxyz"
    words = ["hello", "world", "leetcode", "python"]
    print(countConsistentStrings(allowed, words))  # Output: 4

# Time Complexity Analysis:
# - Converting `allowed` to a set takes O(allowed.length), which is O(1) since allowed.length <= 26.
# - For each word in `words`, we check all its characters against the set. 
#   This takes O(words[i].length) for each word, and since the sum of all word lengths is bounded by 10^4, 
#   the total complexity is O(sum of all word lengths) = O(10^4).
# - Overall time complexity: O(10^4).

# Space Complexity Analysis:
# - The `allowed_set` requires O(allowed.length) space, which is O(1) since allowed.length <= 26.
# - No additional significant space is used.
# - Overall space complexity: O(1).

# Topic: Strings