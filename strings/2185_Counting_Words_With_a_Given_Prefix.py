"""
LeetCode Problem #2185: Counting Words With a Given Prefix

Problem Statement:
You are given an array of strings `words` and a string `pref`.
Return the number of strings in `words` that contain `pref` as a prefix.
A prefix of a string `s` is any leading contiguous substring of `s`.

Example 1:
Input: words = ["pay", "attention", "practice", "attend"], pref = "at"
Output: 2
Explanation: The strings that contain "at" as a prefix are "attention" and "attend".

Example 2:
Input: words = ["leetcode", "win", "loops", "success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length, pref.length <= 100
- `words[i]` and `pref` consist of lowercase English letters.
"""

# Solution
def prefix_count(words, pref):
    """
    Counts the number of strings in the list `words` that start with the prefix `pref`.

    :param words: List[str] - List of words to check.
    :param pref: str - The prefix to look for.
    :return: int - Number of words that start with the prefix `pref`.
    """
    return sum(word.startswith(pref) for word in words)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["pay", "attention", "practice", "attend"]
    pref1 = "at"
    print(prefix_count(words1, pref1))  # Output: 2

    # Test Case 2
    words2 = ["leetcode", "win", "loops", "success"]
    pref2 = "code"
    print(prefix_count(words2, pref2))  # Output: 0

    # Test Case 3
    words3 = ["apple", "application", "app", "banana", "apply"]
    pref3 = "app"
    print(prefix_count(words3, pref3))  # Output: 4

    # Test Case 4
    words4 = ["hello", "world", "help", "hero", "her"]
    pref4 = "he"
    print(prefix_count(words4, pref4))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `words` once, checking if each word starts with the prefix `pref`.
- The `startswith` method runs in O(k), where k is the length of the prefix `pref`.
- If there are n words in the list, the total time complexity is O(n * k).

Space Complexity:
- The function uses constant space, as it does not create any additional data structures.
- The space complexity is O(1).
"""

# Topic: Strings