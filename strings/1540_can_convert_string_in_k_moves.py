"""
LeetCode Question #1540: Can Convert String in K Moves

Problem Statement:
Given two strings s and t, your goal is to convert s into t by applying a series of shift operations to the characters in s. 
A shift operation means taking a character from s and shifting it forward in the alphabet by 1 to 25 times. 
For example, shifting 'a' by 1 results in 'b', and shifting 'z' by 1 results in 'a'.

You can apply at most k shift operations to each character in s. 
Return true if you can convert s into t using at most k shift operations per character, otherwise return false.

Constraints:
- 1 <= s.length, t.length <= 10^5
- 0 <= k <= 10^9
- s and t contain only lowercase English letters.
"""

def canConvertString(s: str, t: str, k: int) -> bool:
    """
    Determines if string s can be converted to string t using at most k shift operations per character.
    """
    # If the lengths of s and t are not the same, conversion is impossible
    if len(s) != len(t):
        return False

    # Frequency array to track the number of shifts needed for each difference
    shift_count = [0] * 26

    for i in range(len(s)):
        # Calculate the shift needed to convert s[i] to t[i]
        shift = (ord(t[i]) - ord(s[i])) % 26
        if shift > 0:
            # Calculate the total number of moves required for this shift
            # shift + 26 * (shift_count[shift]) ensures we account for repeated shifts
            if shift + 26 * shift_count[shift] > k:
                return False
            shift_count[shift] += 1

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case where conversion is possible
    s1, t1, k1 = "input", "ouput", 9
    print(canConvertString(s1, t1, k1))  # Expected: True

    # Test Case 2: Conversion is not possible due to insufficient k
    s2, t2, k2 = "abc", "bcd", 1
    print(canConvertString(s2, t2, k2))  # Expected: False

    # Test Case 3: Strings are already equal
    s3, t3, k3 = "abc", "abc", 0
    print(canConvertString(s3, t3, k3))  # Expected: True

    # Test Case 4: Different lengths
    s4, t4, k4 = "abc", "abcd", 10
    print(canConvertString(s4, t4, k4))  # Expected: False

    # Test Case 5: Large k allows for conversion
    s5, t5, k5 = "a", "z", 25
    print(canConvertString(s5, t5, k5))  # Expected: True

"""
Time Complexity:
- O(n), where n is the length of the strings s and t. We iterate through the strings once to calculate the shifts.

Space Complexity:
- O(1), as the shift_count array has a fixed size of 26, regardless of the input size.

Topic: Strings
"""