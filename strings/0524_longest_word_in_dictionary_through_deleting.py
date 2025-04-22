"""
LeetCode Question #524: Longest Word in Dictionary through Deleting

Problem Statement:
Given a string `s` and a list of strings `dictionary`, find the longest string in the dictionary that can be formed by deleting some characters of the given string `s` such that the resulting string is a subsequence of `s`. If there are multiple possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return an empty string.

Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"

Example 2:
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"

Constraints:
- `1 <= s.length <= 1000`
- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 1000`
- All the strings in `dictionary` are unique.
- `dictionary[i]` and `s` consist of only lowercase English letters.
"""

# Solution
def findLongestWord(s: str, dictionary: list[str]) -> str:
    def is_subsequence(x: str, y: str) -> bool:
        """Check if x is a subsequence of y."""
        it = iter(y)
        return all(char in it for char in x)

    # Sort dictionary by length (descending) and lexicographical order (ascending)
    dictionary.sort(key=lambda word: (-len(word), word))

    for word in dictionary:
        if is_subsequence(word, s):
            return word
    return ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abpcplea"
    dictionary1 = ["ale", "apple", "monkey", "plea"]
    print(findLongestWord(s1, dictionary1))  # Output: "apple"

    # Test Case 2
    s2 = "abpcplea"
    dictionary2 = ["a", "b", "c"]
    print(findLongestWord(s2, dictionary2))  # Output: "a"

    # Test Case 3
    s3 = "abc"
    dictionary3 = ["abcd", "ab", "bc"]
    print(findLongestWord(s3, dictionary3))  # Output: "ab"

    # Test Case 4
    s4 = "xyz"
    dictionary4 = ["a", "b", "c"]
    print(findLongestWord(s4, dictionary4))  # Output: ""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the dictionary: O(n * log(n)), where n is the number of words in the dictionary.
- Checking subsequences: For each word in the dictionary, we check if it is a subsequence of `s`. This takes O(m * k), where m is the length of `s` and k is the average length of words in the dictionary.
- Overall complexity: O(n * log(n) + n * m * k).

Space Complexity:
- Sorting the dictionary requires O(n) space.
- The subsequence check uses an iterator, which is O(1) space.
- Overall space complexity: O(n).

Topic: Strings
"""