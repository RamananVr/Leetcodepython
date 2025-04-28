"""
LeetCode Problem #1668: Maximum Repeating Substring

Problem Statement:
Given a string `sequence` and a string `word`, return the maximum number of times `word` can be repeated as a substring in `sequence`. 
The `word`'s repetitions must be contiguous and non-overlapping.

Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc", but "baba" is not.

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".

Constraints:
- `1 <= sequence.length <= 100`
- `1 <= word.length <= 100`
- `sequence` and `word` contain only lowercase English letters.
"""

def maxRepeating(sequence: str, word: str) -> int:
    """
    Returns the maximum number of times `word` can be repeated as a substring in `sequence`.
    """
    max_count = 0
    repeated_word = word

    # Keep appending `word` to itself and check if it's a substring of `sequence`
    while repeated_word in sequence:
        max_count += 1
        repeated_word += word

    return max_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sequence = "ababc"
    word = "ab"
    print(maxRepeating(sequence, word))  # Output: 2

    # Test Case 2
    sequence = "ababc"
    word = "ba"
    print(maxRepeating(sequence, word))  # Output: 1

    # Test Case 3
    sequence = "ababc"
    word = "ac"
    print(maxRepeating(sequence, word))  # Output: 0

    # Additional Test Case 4
    sequence = "aaaaa"
    word = "a"
    print(maxRepeating(sequence, word))  # Output: 5

    # Additional Test Case 5
    sequence = "abcabcabc"
    word = "abc"
    print(maxRepeating(sequence, word))  # Output: 3

"""
Time Complexity Analysis:
- Let `n` be the length of `sequence` and `m` be the length of `word`.
- In the worst case, we repeatedly append `word` to itself and check if the resulting string is a substring of `sequence`.
- The substring check (`in` operator) takes O(n) time, and we perform this check at most `n // m` times (since the maximum number of repetitions is limited by the length of `sequence` divided by the length of `word`).
- Therefore, the overall time complexity is O((n // m) * n), which simplifies to O(n^2 / m).

Space Complexity Analysis:
- The space complexity is O(k * m), where `k` is the number of repetitions of `word` (at most `n // m`), because we construct the `repeated_word` string incrementally.

Topic: Strings
"""