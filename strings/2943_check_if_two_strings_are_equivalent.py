"""
LeetCode Question #2943: Check if Two Strings are Equivalent

Problem Statement:
Given two strings `word1` and `word2`, return `True` if the two strings are equivalent, and `False` otherwise.

Two strings are considered equivalent if they represent the same sequence of characters when concatenated.

Example:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: True
Explanation: word1 represents "abc" and word2 represents "abc". Therefore, they are equivalent.

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: False
Explanation: word1 represents "acb" and word2 represents "abc". Therefore, they are not equivalent.

Input: word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: True
Explanation: word1 represents "abcddefg" and word2 represents "abcddefg". Therefore, they are equivalent.

Constraints:
- 1 <= len(word1), len(word2) <= 10^3
- 1 <= len(word1[i]), len(word2[i]) <= 10^3
- 1 <= sum(len(word1[i])) <= 10^6
- 1 <= sum(len(word2[i])) <= 10^6
- word1[i] and word2[i] consist of lowercase English letters.
"""

# Solution
def arrayStringsAreEqual(word1, word2):
    """
    Check if two lists of strings are equivalent when concatenated.

    :param word1: List[str] - First list of strings
    :param word2: List[str] - Second list of strings
    :return: bool - True if the concatenated strings are equivalent, False otherwise
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
- The `join` operation for each list takes O(n), where n is the total number of characters in the list.
- Comparing two strings takes O(n), where n is the length of the strings.
- Therefore, the overall time complexity is O(n), where n is the total number of characters in both lists.

Space Complexity:
- The `join` operation creates a new string, which takes O(n) space, where n is the total number of characters in the list.
- Therefore, the space complexity is O(n).

In summary:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Strings