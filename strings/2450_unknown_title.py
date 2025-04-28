"""
LeetCode Problem #2450: Number of Distinct Binary Strings After Applying Operations

Problem Statement:
You are given a binary string `s` of length `n`. You can perform the following operation on `s` any number of times:
- Choose any index `i` (0 <= i < n - 1) and swap `s[i]` with `s[i + 1]`.

Return the number of distinct binary strings that can be obtained after performing any number of operations on `s`.

Constraints:
- 1 <= n <= 10^5
- `s` consists of only the characters '0' and '1'.
"""

# Solution
def distinctBinaryStrings(s: str) -> int:
    """
    Returns the number of distinct binary strings that can be obtained
    after performing any number of operations on the input binary string.

    :param s: A binary string consisting of '0' and '1'.
    :return: The number of distinct binary strings possible.
    """
    # The number of distinct binary strings is determined by the number of unique characters in the input string.
    return len(set(s))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "110"
    print(distinctBinaryStrings(s1))  # Output: 2

    # Test Case 2
    s2 = "000"
    print(distinctBinaryStrings(s2))  # Output: 1

    # Test Case 3
    s3 = "10101"
    print(distinctBinaryStrings(s3))  # Output: 2

    # Test Case 4
    s4 = "111111"
    print(distinctBinaryStrings(s4))  # Output: 1

    # Test Case 5
    s5 = "0101010101"
    print(distinctBinaryStrings(s5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses the `set()` function to find unique characters in the string `s`.
- Constructing a set from a string takes O(n), where `n` is the length of the string.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is O(u), where `u` is the number of unique characters in the string.
- Since the input string consists only of '0' and '1', `u` is at most 2.
- Therefore, the space complexity is O(1) (constant space).

Overall:
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Topic: Strings