"""
LeetCode Problem #2796: "Repeat String Match"

Problem Statement:
Given two strings `a` and `b`, return the minimum number of times you need to repeat string `a` such that string `b` is a substring of the repeated string. If it is impossible for `b` to be a substring of the repeated string, return -1.

Note:
- `a` and `b` consist of lowercase English letters.
- 1 <= len(a), len(b) <= 10^4

Example:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We repeat "abcd" three times to get "abcdabcdabcd", which contains "cdabcdab" as a substring.

Constraints:
- The length of `b` will always be greater than or equal to the length of `a`.
"""

# Solution
def repeatedStringMatch(a: str, b: str) -> int:
    """
    Returns the minimum number of times string `a` needs to be repeated
    such that `b` is a substring of the repeated string. If not possible, returns -1.
    """
    # Minimum number of repetitions needed
    min_repeats = -(-len(b) // len(a))  # Equivalent to math.ceil(len(b) / len(a))

    # Check if `b` is a substring of `a` repeated `min_repeats` or `min_repeats + 1` times
    for i in range(2):
        repeated_a = a * (min_repeats + i)
        if b in repeated_a:
            return min_repeats + i

    # If `b` is not a substring in any of the cases, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = "abcd"
    b = "cdabcdab"
    print(repeatedStringMatch(a, b))  # Output: 3

    # Test Case 2
    a = "a"
    b = "aa"
    print(repeatedStringMatch(a, b))  # Output: 2

    # Test Case 3
    a = "abc"
    b = "wxyz"
    print(repeatedStringMatch(a, b))  # Output: -1

    # Test Case 4
    a = "abc"
    b = "cabcabca"
    print(repeatedStringMatch(a, b))  # Output: 4

    # Test Case 5
    a = "xyz"
    b = "xyzxyzxyz"
    print(repeatedStringMatch(a, b))  # Output: 3

"""
Time Complexity Analysis:
- Let `n` be the length of `a` and `m` be the length of `b`.
- Constructing the repeated string `a * (min_repeats + i)` takes O(n * (min_repeats + i)) time.
- Checking if `b` is a substring of the repeated string takes O(n * (min_repeats + i)) time in the worst case.
- Since we check for two cases (`min_repeats` and `min_repeats + 1`), the total time complexity is O(n * (m / n + 1)) = O(m + n).

Space Complexity Analysis:
- The space complexity is O(n * (min_repeats + i)) for storing the repeated string, which is proportional to the size of the repeated string.
- Thus, the space complexity is O(m + n).

Topic: Strings
"""