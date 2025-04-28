"""
LeetCode Problem #1573: Number of Ways to Split a String

Problem Statement:
You are given a binary string s (a string consisting only of '0's and '1's). You can split s into 3 non-empty parts 
s1, s2, s3 (s1 + s2 + s3 = s). Return the number of ways s can be split such that the number of 1's in s1, s2, and s3 
are all the same. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: s = "10101"
Output: 4
Explanation: There are four ways to split s into three parts with equal numbers of 1's:
"1 | 01 | 01", "1 | 010 | 1", "10 | 1 | 01", "10 | 10 | 1"

Example 2:
Input: s = "1001"
Output: 0
Explanation: It is impossible to split s into three parts with equal numbers of 1's.

Example 3:
Input: s = "0000"
Output: 3
Explanation: There are three ways to split s into three parts with equal numbers of 1's:
"0 | 0 | 00", "0 | 00 | 0", "00 | 0 | 0"

Constraints:
- 3 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

# Python Solution
def numWays(s: str) -> int:
    MOD = 10**9 + 7
    total_ones = s.count('1')
    
    # If the total number of 1's is not divisible by 3, return 0
    if total_ones % 3 != 0:
        return 0
    
    # If there are no 1's, we can split the string in (n-1)*(n-2)/2 ways
    if total_ones == 0:
        n = len(s)
        return ((n - 1) * (n - 2) // 2) % MOD
    
    # Find the number of 1's in each part
    ones_per_part = total_ones // 3
    first_cut_ways = 0
    second_cut_ways = 0
    
    # Count the number of ways to make the first and second cuts
    ones_count = 0
    for char in s:
        if char == '1':
            ones_count += 1
        if ones_count == ones_per_part:
            first_cut_ways += 1
        elif ones_count == 2 * ones_per_part:
            second_cut_ways += 1
    
    # The total number of ways is the product of the two counts
    return (first_cut_ways * second_cut_ways) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "10101"
    print(numWays(s1))  # Output: 4

    # Test Case 2
    s2 = "1001"
    print(numWays(s2))  # Output: 0

    # Test Case 3
    s3 = "0000"
    print(numWays(s3))  # Output: 3

    # Test Case 4
    s4 = "111111"
    print(numWays(s4))  # Output: 9

    # Test Case 5
    s5 = "000000"
    print(numWays(s5))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the total number of 1's in the string takes O(n), where n is the length of the string.
- Iterating through the string to count the ways to make the cuts also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Strings
"""