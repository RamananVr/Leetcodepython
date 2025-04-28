"""
LeetCode Problem #720: Longest Word in Dictionary

Problem Statement:
Given an array of strings `words` representing an English dictionary, return the longest word in the dictionary that can be built one character at a time by other words in `words`.

If there is more than one possible answer, return the word that is lexicographically smallest. If no answer exists, return an empty string.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters.
"""

# Solution
def longestWord(words):
    """
    Finds the longest word in the dictionary that can be built one character at a time.

    :param words: List[str] - List of words in the dictionary
    :return: str - The longest word that satisfies the condition
    """
    # Sort words lexicographically
    words.sort()
    # Use a set to store valid words
    valid_words = set([""])
    longest = ""

    for word in words:
        # Check if the prefix (word[:-1]) exists in the valid set
        if word[:-1] in valid_words:
            valid_words.add(word)
            # Update the longest word if the current word is longer
            if len(word) > len(longest):
                longest = word

    return longest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["w", "wo", "wor", "worl", "world"]
    print(longestWord(words1))  # Output: "world"

    # Test Case 2
    words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(longestWord(words2))  # Output: "apple"

    # Test Case 3
    words3 = ["b", "br", "bre", "brea", "break", "breakf", "breakfa", "breakfas", "breakfast"]
    print(longestWord(words3))  # Output: "breakfast"

    # Test Case 4
    words4 = ["a", "b", "ba", "bac", "baca", "bacab"]
    print(longestWord(words4))  # Output: "bacab"

    # Test Case 5
    words5 = ["a", "abc", "ab", "abcd", "abcde"]
    print(longestWord(words5))  # Output: "abcde"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the words takes O(n log n), where n is the number of words.
- Iterating through the words takes O(n).
- Checking if a prefix exists in the set is O(1) on average.
Thus, the overall time complexity is O(n log n).

Space Complexity:
- The space used by the `valid_words` set is O(n), where n is the number of words.
- The space used for sorting is O(n) (depending on the sorting algorithm).
Thus, the overall space complexity is O(n).

Topic: Strings, Sorting, Hash Set
"""