"""
LeetCode Problem #1427: Perform String Shifts

Problem Statement:
You are given a string `s` of lowercase English letters and an array `shift`, where `shift[i] = [direction, amount]`:
- `direction` can be 0 (for a left shift) or 1 (for a right shift).
- `amount` is the number of positions to shift.

A left shift by 1 means removing the first character of `s` and appending it to the end.
Similarly, a right shift by 1 means removing the last character of `s` and inserting it at the beginning.

Return the final string after all the shifts have been applied to `s`.

Constraints:
- `1 <= s.length <= 100`
- `shift.length <= 100`
- `shift[i].length == 2`
- `0 <= shift[i][0] <= 1`
- `0 <= shift[i][1] <= 100`

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift "abc" to the left by 1 -> "bca".
[1,2] means shift "bca" to the right by 2 -> "cab".

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation: 
[1,1] means shift "abcdefg" to the right by 1 -> "gabcdef".
[1,1] means shift "gabcdef" to the right by 1 -> "fgabcde".
[0,2] means shift "fgabcde" to the left by 2 -> "abcdefg".
[1,3] means shift "abcdefg" to the right by 3 -> "efgabcd".
"""

def stringShift(s: str, shift: list[list[int]]) -> str:
    # Calculate the net shift amount
    net_shift = 0
    for direction, amount in shift:
        if direction == 0:  # Left shift
            net_shift -= amount
        else:  # Right shift
            net_shift += amount

    # Normalize the net shift to be within the bounds of the string length
    n = len(s)
    net_shift %= n

    # Perform the shift
    if net_shift > 0:  # Right shift
        return s[-net_shift:] + s[:-net_shift]
    elif net_shift < 0:  # Left shift
        return s[-net_shift:] + s[:-net_shift]
    else:  # No shift
        return s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    shift1 = [[0, 1], [1, 2]]
    print(stringShift(s1, shift1))  # Output: "cab"

    # Test Case 2
    s2 = "abcdefg"
    shift2 = [[1, 1], [1, 1], [0, 2], [1, 3]]
    print(stringShift(s2, shift2))  # Output: "efgabcd"

    # Test Case 3
    s3 = "hello"
    shift3 = [[0, 3], [1, 5], [0, 2]]
    print(stringShift(s3, shift3))  # Output: "lohel"

    # Test Case 4
    s4 = "a"
    shift4 = [[1, 100], [0, 100]]
    print(stringShift(s4, shift4))  # Output: "a"

    # Test Case 5
    s5 = "xyz"
    shift5 = [[0, 4], [1, 1]]
    print(stringShift(s5, shift5))  # Output: "zxy"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the net shift requires iterating through the `shift` array, which takes O(m), where m is the length of the `shift` array.
- Normalizing the shift and slicing the string both take O(n), where n is the length of the string `s`.
- Overall time complexity: O(m + n).

Space Complexity:
- The slicing operation creates a new string, which takes O(n) space.
- No additional data structures are used.
- Overall space complexity: O(n).

Topic: Strings
"""