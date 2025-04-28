"""
LeetCode Problem #1408: String Matching in an Array

Problem Statement:
Given an array of string `words`, return all strings in `words` that are substrings of another word in any order. 
A string `words[i]` is a substring of `words[j]`, if `words[i]` can be obtained by removing some characters 
(possibly none) from the start and some characters (possibly none) from the end of `words[j]`.

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of "superhero".

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et" and "code" are substrings of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string in `words` is a substring of another string.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] contains only lowercase English letters.
- All the strings in `words` are unique.
"""

# Python Solution
def stringMatching(words):
    """
    Finds all strings in the input list that are substrings of another string in the list.

    :param words: List[str] - List of unique strings
    :return: List[str] - List of strings that are substrings of another string
    """
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["mass", "as", "hero", "superhero"]
    print(stringMatching(words1))  # Output: ["as", "hero"]

    # Test Case 2
    words2 = ["leetcode", "et", "code"]
    print(stringMatching(words2))  # Output: ["et", "code"]

    # Test Case 3
    words3 = ["blue", "green", "bu"]
    print(stringMatching(words3))  # Output: []

    # Test Case 4
    words4 = ["a", "b", "c", "abc"]
    print(stringMatching(words4))  # Output: ["a", "b", "c"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over each word in the list (O(n)).
- The inner loop iterates over each word in the list again (O(n)).
- Checking if one string is a substring of another takes O(m), where m is the length of the longer string.
- Therefore, the overall time complexity is O(n^2 * m), where n is the number of words and m is the average length of the strings.

Space Complexity:
- The space complexity is O(k), where k is the number of substrings added to the result list.
- No additional data structures are used, so the space complexity is dominated by the output list.

Topic: Strings
"""