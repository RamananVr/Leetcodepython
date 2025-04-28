"""
LeetCode Problem #2531: Make Number of Distinct Characters Equal

Problem Statement:
You are given two strings `word1` and `word2`. You want to make the number of distinct characters in `word1` and `word2` equal. You can achieve this by performing the following operation any number of times:

- Choose any character from `word1` and any character from `word2`, and swap them.

Return `true` if it is possible to make the number of distinct characters in `word1` and `word2` equal, and `false` otherwise.

Constraints:
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` consist of only lowercase English letters.
"""

def isItPossible(word1: str, word2: str) -> bool:
    from collections import Counter

    # Count the frequency of characters in both words
    count1 = Counter(word1)
    count2 = Counter(word2)

    # Get the number of distinct characters in both words
    distinct1 = len(count1)
    distinct2 = len(count2)

    # Iterate over all possible swaps
    for char1 in count1:
        for char2 in count2:
            # Simulate the swap
            new_distinct1 = distinct1
            new_distinct2 = distinct2

            # Adjust distinct counts for word1
            if count1[char1] == 1:
                new_distinct1 -= 1
            if char2 not in count1:
                new_distinct1 += 1

            # Adjust distinct counts for word2
            if count2[char2] == 1:
                new_distinct2 -= 1
            if char1 not in count2:
                new_distinct2 += 1

            # Check if the distinct counts are equal after the swap
            if new_distinct1 == new_distinct2:
                return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "ac"
    word2 = "b"
    print(isItPossible(word1, word2))  # Output: False

    # Test Case 2
    word1 = "abcc"
    word2 = "aab"
    print(isItPossible(word1, word2))  # Output: True

    # Test Case 3
    word1 = "abcde"
    word2 = "fghij"
    print(isItPossible(word1, word2))  # Output: True

    # Test Case 4
    word1 = "a"
    word2 = "a"
    print(isItPossible(word1, word2))  # Output: True

    # Test Case 5
    word1 = "abc"
    word2 = "def"
    print(isItPossible(word1, word2))  # Output: True

"""
Time Complexity Analysis:
- Let `m` be the length of `word1` and `n` be the length of `word2`.
- Counting the frequency of characters in both words takes O(m + n).
- The nested loop iterates over all distinct characters in `word1` and `word2`, which is at most 26 * 26 = 676 iterations (since there are only 26 lowercase English letters).
- Therefore, the overall time complexity is O(m + n + 1), which simplifies to O(m + n).

Space Complexity Analysis:
- The space complexity is O(1) for the distinct character counts and O(26) = O(1) for the frequency counters (since there are only 26 lowercase English letters).
- Thus, the space complexity is O(1).

Topic: Hash Table
"""