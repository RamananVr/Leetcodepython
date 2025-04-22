"""
LeetCode Problem #686: Repeated String Match

Problem Statement:
Given two strings `a` and `b`, return the minimum number of times you must repeat string `a` such that string `b` is a substring of the repeated string. If it is impossible for `b` to be a substring of the repeated string, return -1.

Note:
- `a` and `b` consist of lowercase English letters.
- The length of `a` and `b` will not exceed 1000.

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: "abcd" repeated 3 times is "abcdabcdabcd", and "cdabcdab" is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
Explanation: "a" repeated 2 times is "aa", and "aa" is a substring of it.

Example 3:
Input: a = "abc", b = "wxyz"
Output: -1
Explanation: "wxyz" is not a substring of any repetition of "abc".

Constraints:
- 1 <= a.length, b.length <= 1000
"""

def repeatedStringMatch(a: str, b: str) -> int:
    """
    Returns the minimum number of times string `a` must be repeated such that `b` is a substring
    of the repeated string. If impossible, returns -1.
    """
    # Calculate the minimum number of repetitions needed
    min_repeats = -(-len(b) // len(a))  # Equivalent to math.ceil(len(b) / len(a))
    
    # Check if `b` is a substring of `a` repeated `min_repeats` or `min_repeats + 1` times
    for i in range(min_repeats, min_repeats + 2):
        if b in a * i:
            return i
    
    # If `b` is not a substring in any case, return -1
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

    # Additional Test Case 4
    a = "abc"
    b = "cabcabca"
    print(repeatedStringMatch(a, b))  # Output: 4

    # Additional Test Case 5
    a = "xyz"
    b = "xyzxyzxyzxyz"
    print(repeatedStringMatch(a, b))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The main operation is checking if `b` is a substring of `a * i`, which takes O(len(a) * i) time.
- The loop runs at most 2 iterations (min_repeats and min_repeats + 1).
- In the worst case, `i` is proportional to len(b) / len(a), so the overall complexity is O(len(a) * len(b) / len(a)) = O(len(b)).

Space Complexity:
- The space complexity is O(len(a) * i) for the repeated string `a * i`.
- In the worst case, this is proportional to O(len(b)).
- Therefore, the space complexity is O(len(b)).

Topic: Strings
"""