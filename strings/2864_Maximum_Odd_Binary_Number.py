"""
LeetCode Problem #2864: Maximum Odd Binary Number

Problem Statement:
You are given a binary string `s` that consists of only '0's and '1's. You need to rearrange the characters of `s` to form the maximum odd binary number.

An odd binary number is a binary number whose last digit is '1'. Among all possible rearrangements of `s` that form an odd binary number, return the one that represents the maximum value in decimal.

If it is impossible to form an odd binary number, return an empty string.

Example 1:
Input: s = "010"
Output: "100"
Explanation: Rearrange the binary string to form the maximum odd binary number. The maximum odd binary number is "100".

Example 2:
Input: s = "000"
Output: ""
Explanation: It is impossible to form an odd binary number since there is no '1' at the end.

Constraints:
- 1 <= s.length <= 100
- s[i] is either '0' or '1'.
"""

# Solution
def maximumOddBinaryNumber(s: str) -> str:
    # Count the number of '1's and '0's in the string
    ones = s.count('1')
    zeros = s.count('0')
    
    # If there are no '1's, it's impossible to form an odd binary number
    if ones == 0:
        return ""
    
    # To form the maximum odd binary number:
    # - Place all '1's except one at the beginning
    # - Place all '0's in the middle
    # - Place the last '1' at the end
    return '1' * (ones - 1) + '0' * zeros + '1'

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "010"
    print(maximumOddBinaryNumber(s1))  # Output: "100"

    # Test Case 2
    s2 = "000"
    print(maximumOddBinaryNumber(s2))  # Output: ""

    # Test Case 3
    s3 = "1110"
    print(maximumOddBinaryNumber(s3))  # Output: "1111"

    # Test Case 4
    s4 = "10101"
    print(maximumOddBinaryNumber(s4))  # Output: "11101"

    # Test Case 5
    s5 = "1"
    print(maximumOddBinaryNumber(s5))  # Output: "1"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the number of '1's and '0's in the string takes O(n), where n is the length of the string.
- Constructing the result string takes O(n) as well.
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses O(1) additional space, as we only store a few integer variables and construct the result string.
- The space complexity is O(1).
"""

# Topic: Strings