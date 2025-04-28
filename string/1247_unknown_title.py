"""
LeetCode Problem #1247: Minimum Swaps to Make Strings Equal

Problem Statement:
You are given two strings `s1` and `s2` of equal length consisting of characters 'x' and 'y' only. 
Your task is to make these two strings equal using the minimum number of swaps. 

A swap consists of choosing two indices (i, j) such that `s1[i] != s2[i]` and swapping `s1[i]` with `s2[j]`.

Return the minimum number of swaps required to make `s1` and `s2` equal, or return -1 if it is impossible.

Constraints:
- `1 <= s1.length == s2.length <= 1000`
- `s1`, `s2` contain only 'x' or 'y'.

Example:
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] with s2[1] to make s1 = "yy" and s2 = "yy".

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] with s2[0], then swap s1[1] with s2[1] to make s1 = "yy" and s2 = "yy".

Input: s1 = "xx", s2 = "xy"
Output: -1
Explanation: It is impossible to make the strings equal.
"""

def minimumSwap(s1: str, s2: str) -> int:
    # Count mismatched pairs
    xy_count = 0  # Count of 'x' in s1 and 'y' in s2
    yx_count = 0  # Count of 'y' in s1 and 'x' in s2

    for a, b in zip(s1, s2):
        if a == 'x' and b == 'y':
            xy_count += 1
        elif a == 'y' and b == 'x':
            yx_count += 1

    # If the total mismatched pairs are odd, it's impossible to make the strings equal
    if (xy_count + yx_count) % 2 != 0:
        return -1

    # Each pair of 'xy' and 'yx' mismatches can be resolved in 2 swaps
    # If there is one extra mismatch of each type, it takes 2 additional swaps
    return xy_count // 2 + yx_count // 2 + 2 * (xy_count % 2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "xx"
    s2 = "yy"
    print(minimumSwap(s1, s2))  # Output: 1

    # Test Case 2
    s1 = "xy"
    s2 = "yx"
    print(minimumSwap(s1, s2))  # Output: 2

    # Test Case 3
    s1 = "xx"
    s2 = "xy"
    print(minimumSwap(s1, s2))  # Output: -1

    # Test Case 4
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    print(minimumSwap(s1, s2))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the strings `s1` and `s2` once to count mismatched pairs.
- This takes O(n) time, where n is the length of the strings.

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few integer variables).
- Thus, the space complexity is O(1).

Topic: String
"""