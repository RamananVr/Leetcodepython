"""
LeetCode Problem #1888: Minimum Number of Flips to Make the Binary String Alternating

Problem Statement:
You are given a binary string `s` of length `n`. You can perform two types of operations on the string:
1. Swap any two characters in the string.
2. Flip a character (change '0' to '1' or '1' to '0').

Return the minimum number of operations needed to make the string alternating. A binary string is alternating if no two adjacent characters are equal.

Example:
- "010" and "101" are alternating strings.
- "111" and "000" are not alternating strings.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

# Solution
def minFlips(s: str) -> int:
    """
    Calculate the minimum number of flips required to make the binary string alternating.
    
    :param s: A binary string
    :return: Minimum number of flips
    """
    n = len(s)
    s = s + s  # Concatenate the string to handle circular cases
    alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(len(s))])  # Alternating pattern starting with '0'
    alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])  # Alternating pattern starting with '1'
    
    # Sliding window approach
    diff1, diff2 = 0, 0
    min_flips = float('inf')
    
    for i in range(len(s)):
        if s[i] != alt1[i]:
            diff1 += 1
        if s[i] != alt2[i]:
            diff2 += 1
        
        # Shrink the window when it exceeds the original string length
        if i >= n:
            if s[i - n] != alt1[i - n]:
                diff1 -= 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1
        
        # Update the minimum flips
        if i >= n - 1:
            min_flips = min(min_flips, diff1, diff2)
    
    return min_flips

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "111000"
    print(minFlips(s1))  # Expected Output: 2

    # Test Case 2
    s2 = "010"
    print(minFlips(s2))  # Expected Output: 0

    # Test Case 3
    s3 = "10010100"
    print(minFlips(s3))  # Expected Output: 3

    # Test Case 4
    s4 = "000"
    print(minFlips(s4))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the alternating patterns `alt1` and `alt2` takes O(2n) = O(n).
- The sliding window approach iterates through the concatenated string `s` of length 2n, which takes O(2n) = O(n).
- Overall time complexity: O(n).

Space Complexity:
- The concatenated string `s` takes O(2n) space.
- The alternating patterns `alt1` and `alt2` take O(2n) space.
- Overall space complexity: O(n).

Topic: Sliding Window, Strings
"""