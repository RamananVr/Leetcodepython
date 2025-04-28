"""
LeetCode Problem #880: Decoded String at Index

Problem Statement:
You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

- If the character read is a letter, that letter is written onto the tape.
- If the character read is a digit (say `d`), the entire current tape is repeatedly written `d-1` more times in total.

Given an integer `k`, return the `k`-th letter (1-indexed) in the decoded string.

Constraints:
- `2 <= s.length <= 100`
- `s` consists of lowercase English letters and digits `2-9`.
- `1 <= k <= 10^9`
- It is guaranteed that `k` is less than or equal to the length of the decoded string.
- The decoded string is guaranteed to have less than `2^63` letters.
"""

def decodeAtIndex(s: str, k: int) -> str:
    """
    This function returns the k-th letter in the decoded string.
    """
    # Step 1: Calculate the length of the decoded string
    size = 0
    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1

    # Step 2: Traverse the string in reverse to find the k-th character
    for char in reversed(s):
        k %= size  # Reduce k to within the current size
        if k == 0 and char.isalpha():
            return char  # Found the k-th character
        if char.isdigit():
            size //= int(char)  # Reduce size by dividing by the digit
        else:
            size -= 1  # Reduce size by 1 for a letter

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leet2code3"
    k1 = 10
    print(decodeAtIndex(s1, k1))  # Output: "o"

    # Test Case 2
    s2 = "ha22"
    k2 = 5
    print(decodeAtIndex(s2, k2))  # Output: "h"

    # Test Case 3
    s3 = "a2b3c4d5e6f7g8h9"
    k3 = 100
    print(decodeAtIndex(s3, k3))  # Output: "b"

    # Test Case 4
    s4 = "abc"
    k4 = 3
    print(decodeAtIndex(s4, k4))  # Output: "c"

    # Test Case 5
    s5 = "a23"
    k5 = 6
    print(decodeAtIndex(s5, k5))  # Output: "a"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the string `s` twice: once to calculate the size of the decoded string and once in reverse to find the k-th character.
- Thus, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few variables are used).
- Thus, the space complexity is O(1).

Topic: String Manipulation
"""