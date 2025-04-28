"""
LeetCode Problem #2506: Count Pairs Of Similar Strings

Problem Statement:
You are given a 0-indexed string array `words`. Two strings are similar if they consist of the same characters.

- For example, "abca" and "cba" are similar since they both consist of characters 'a', 'b', and 'c'.
- However, "ab" and "abc" are not similar since they have different characters.

Return the number of pairs `(i, j)` such that `0 <= i < j < words.length` and `words[i]` is similar to `words[j]`.

Example 1:
Input: words = ["aba", "aabb", "abcd", "bac", "aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- (0, 3): "aba" and "bac"
- (1, 4): "aabb" and "aabc"

Example 2:
Input: words = ["aabb", "ab", "ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- (0, 1): "aabb" and "ab"
- (0, 2): "aabb" and "ba"
- (1, 2): "ab" and "ba"

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.
"""

# Python Solution
from collections import Counter

def similarPairs(words):
    """
    Function to count the number of pairs of similar strings in the given list of words.

    Args:
    words (List[str]): List of strings.

    Returns:
    int: Number of pairs of similar strings.
    """
    # Convert each word into a set of unique characters and count their occurrences
    char_sets = [frozenset(word) for word in words]
    freq = Counter(char_sets)
    
    # Count the number of pairs for each unique set of characters
    count = 0
    for val in freq.values():
        count += (val * (val - 1)) // 2  # nC2 = n * (n - 1) / 2
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["aba", "aabb", "abcd", "bac", "aabc"]
    print(similarPairs(words1))  # Output: 2

    # Test Case 2
    words2 = ["aabb", "ab", "ba"]
    print(similarPairs(words2))  # Output: 3

    # Test Case 3
    words3 = ["abc", "def", "ghi"]
    print(similarPairs(words3))  # Output: 0

    # Test Case 4
    words4 = ["a", "a", "a"]
    print(similarPairs(words4))  # Output: 3

    # Test Case 5
    words5 = ["abcd", "bcda", "dabc", "cdab"]
    print(similarPairs(words5))  # Output: 6

"""
Time Complexity Analysis:
- Converting each word into a frozenset takes O(k), where k is the average length of a word.
- If there are n words, creating the `char_sets` list takes O(n * k).
- Counting frequencies using Counter takes O(n).
- Calculating the number of pairs for each unique set of characters is O(u), where u is the number of unique sets.
  In the worst case, u = n, so this step is O(n).
- Overall time complexity: O(n * k).

Space Complexity Analysis:
- The `char_sets` list stores n frozensets, each of size at most 26 (number of unique lowercase letters).
  This takes O(n * 26) = O(n) space.
- The Counter object stores frequencies of up to n unique sets, taking O(n) space.
- Overall space complexity: O(n).

Topic: Hashing
"""