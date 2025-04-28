"""
LeetCode Problem #1662: Check If Two String Arrays are Equivalent

Problem Statement:
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order form the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "abc" which is the same as word2.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
- 1 <= word1.length, word2.length <= 10^3
- 1 <= word1[i].length, word2[i].length <= 10^3
- 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^6
- word1[i] and word2[i] consist of lowercase letters.
"""

# Solution
def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    """
    Check if two string arrays are equivalent by comparing their concatenated strings.

    :param word1: List of strings representing the first string array.
    :param word2: List of strings representing the second string array.
    :return: True if the concatenated strings are equal, False otherwise.
    """
    return "".join(word1) == "".join(word2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))  # Output: True

    # Test Case 2
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(arrayStringsAreEqual(word1, word2))  # Output: False

    # Test Case 3
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1, word2))  # Output: True

    # Test Case 4
    word1 = ["hello", "world"]
    word2 = ["helloworld"]
    print(arrayStringsAreEqual(word1, word2))  # Output: True

    # Test Case 5
    word1 = ["a", "b", "c"]
    word2 = ["abc"]
    print(arrayStringsAreEqual(word1, word2))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `join` operation for both `word1` and `word2` takes O(n1) and O(n2) respectively, where n1 and n2 are the total lengths of the strings in word1 and word2.
- The comparison operation takes O(min(n1, n2)).
- Overall time complexity: O(n1 + n2).

Space Complexity:
- The `join` operation creates new strings for word1 and word2, which take O(n1) and O(n2) space respectively.
- Overall space complexity: O(n1 + n2).
"""

# Topic: Strings