"""
LeetCode Question #1934: Minimum Number of Flips to Make the Binary String Alternating

Problem Statement:
You are given a binary string `s` of length `n`. You can perform two types of operations on the string:
1. Choose any index `i` and flip the character at index `i` (i.e., change '0' to '1' or '1' to '0').
2. Choose any index `i` and move the character at index `i` to the end of the string.

Return the minimum number of flips required to make the binary string alternating. A binary string is alternating if no two adjacent characters are the same.

Example:
- "010" and "101" are alternating strings.
- "111" and "000" are not alternating strings.

Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either '0' or '1'.
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
    
    # Generate the two possible alternating patterns
    alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(len(s))])
    alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])
    
    # Sliding window approach
    diff1, diff2 = 0, 0
    min_flips = float('inf')
    
    for i in range(len(s)):
        # Count mismatches for both patterns
        if s[i] != alt1[i]:
            diff1 += 1
        if s[i] != alt2[i]:
            diff2 += 1
        
        # When the window size exceeds n, slide the window
        if i >= n:
            if s[i - n] != alt1[i - n]:
                diff1 -= 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1
        
        # Update the minimum flips for valid windows
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
- Generating the alternating patterns `alt1` and `alt2` takes O(2n) = O(n).
- The sliding window approach iterates through the concatenated string `s` of length 2n, which takes O(2n) = O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The concatenated string `s` takes O(2n) space.
- The alternating patterns `alt1` and `alt2` also take O(2n) space.
- Overall, the space complexity is O(n).

Topic: Sliding Window
"""