"""
LeetCode Problem #1737: Change Minimum Characters to Satisfy One of Three Conditions

Problem Statement:
You are given two strings `a` and `b` that consist of lowercase English letters. In one operation, you can change any character in `a` or `b` to any lowercase English letter.

Your goal is to satisfy one of the following three conditions with the minimum number of operations:
1. Every character in `a` is strictly less than every character in `b` in the alphabet.
2. Every character in `b` is strictly less than every character in `a` in the alphabet.
3. Both `a` and `b` consist of only one distinct character.

Return the minimum number of operations required to achieve any of these conditions.

Constraints:
- 1 <= len(a), len(b) <= 10^5
- `a` and `b` consist only of lowercase English letters.
"""

# Solution
from collections import Counter

def minCharacters(a: str, b: str) -> int:
    # Helper function to calculate prefix sums for character frequencies
    def get_prefix_sums(freq):
        prefix = [0] * 26
        prefix[0] = freq[0]
        for i in range(1, 26):
            prefix[i] = prefix[i - 1] + freq[i]
        return prefix

    # Count character frequencies for both strings
    freq_a = [0] * 26
    freq_b = [0] * 26
    for char in a:
        freq_a[ord(char) - ord('a')] += 1
    for char in b:
        freq_b[ord(char) - ord('a')] += 1

    # Calculate prefix sums
    prefix_a = get_prefix_sums(freq_a)
    prefix_b = get_prefix_sums(freq_b)

    # Total lengths of a and b
    len_a, len_b = len(a), len(b)

    # Condition 1 and 2: Make all characters in a < b or all characters in b < a
    min_operations = float('inf')
    for i in range(25):  # Only go up to 25 because we compare i and i+1
        # Make all characters in a < b
        ops_a_less_b = (len_a - prefix_a[i]) + prefix_b[i]
        # Make all characters in b < a
        ops_b_less_a = (len_b - prefix_b[i]) + prefix_a[i]
        min_operations = min(min_operations, ops_a_less_b, ops_b_less_a)

    # Condition 3: Make both strings consist of only one distinct character
    for i in range(26):
        ops_same_char = (len_a - freq_a[i]) + (len_b - freq_b[i])
        min_operations = min(min_operations, ops_same_char)

    return min_operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = "aba"
    b = "caa"
    print(minCharacters(a, b))  # Expected Output: 2

    # Test Case 2
    a = "dabadd"
    b = "cda"
    print(minCharacters(a, b))  # Expected Output: 3

    # Test Case 3
    a = "a"
    b = "z"
    print(minCharacters(a, b))  # Expected Output: 0

    # Test Case 4
    a = "abc"
    b = "xyz"
    print(minCharacters(a, b))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting character frequencies for `a` and `b` takes O(len(a) + len(b)).
- Calculating prefix sums takes O(26) (constant time).
- Iterating over 25 possible split points for conditions 1 and 2 takes O(25) (constant time).
- Iterating over 26 possible characters for condition 3 takes O(26) (constant time).
- Overall, the time complexity is O(len(a) + len(b)).

Space Complexity:
- We use arrays of size 26 for `freq_a`, `freq_b`, `prefix_a`, and `prefix_b`, which is O(26) (constant space).
- Overall, the space complexity is O(1) (constant space).

Topic: Strings
"""