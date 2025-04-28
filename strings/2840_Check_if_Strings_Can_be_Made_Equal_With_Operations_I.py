"""
LeetCode Problem #2840: Check if Strings Can be Made Equal With Operations I

Problem Statement:
You are given two strings `s1` and `s2`, both of length `n`. You can perform the following operation on `s1` any number of times:

- Choose two indices `i` and `j` (0 <= i, j < n) and swap the characters at `s1[i]` and `s1[j]`.

Return `true` if you can make `s1` equal to `s2`, and `false` otherwise.

Constraints:
- `n == s1.length == s2.length`
- `1 <= n <= 100`
- `s1` and `s2` consist of lowercase English letters.
"""

def canBeEqual(s1: str, s2: str) -> bool:
    """
    Determines if s1 can be made equal to s2 by performing any number of swaps.

    Args:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    bool: True if s1 can be made equal to s2, False otherwise.
    """
    # If the sorted characters of both strings are the same, they can be made equal
    return sorted(s1) == sorted(s2)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Identical strings
    s1 = "abc"
    s2 = "abc"
    print(canBeEqual(s1, s2))  # Expected: True

    # Test Case 2: Strings that can be made equal
    s1 = "bca"
    s2 = "abc"
    print(canBeEqual(s1, s2))  # Expected: True

    # Test Case 3: Strings that cannot be made equal
    s1 = "abc"
    s2 = "def"
    print(canBeEqual(s1, s2))  # Expected: False

    # Test Case 4: Single character strings
    s1 = "a"
    s2 = "a"
    print(canBeEqual(s1, s2))  # Expected: True

    # Test Case 5: Strings with different frequencies of characters
    s1 = "aabbcc"
    s2 = "abcabc"
    print(canBeEqual(s1, s2))  # Expected: True

    # Test Case 6: Strings with different lengths (invalid input per constraints)
    # This case is not valid as per the constraints, but we can still test it.
    # s1 = "abc"
    # s2 = "abcd"
    # print(canBeEqual(s1, s2))  # Expected: False (if allowed to test invalid inputs)


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting both strings takes O(n log n), where n is the length of the strings.
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- Sorting requires additional space proportional to the size of the input, i.e., O(n).
- Thus, the space complexity is O(n).

Topic: Strings
"""