"""
LeetCode Question #191: Number of 1 Bits

Problem Statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has 
(also known as the Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty-one '1' bits.

Constraints:
- The input must be a binary string of length 32.
- You must treat the input as an unsigned integer.

Follow-up:
If this function is called many times, how would you optimize it?
"""

# Clean, Correct Python Solution
def hammingWeight(n: int) -> int:
    """
    Function to count the number of '1' bits in the binary representation of an unsigned integer.

    :param n: Unsigned integer
    :return: Number of '1' bits in the binary representation of n
    """
    count = 0
    while n:
        count += n & 1  # Check if the least significant bit is 1
        n >>= 1         # Right shift n by 1 to process the next bit
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 0b00000000000000000000000000001011
    print(hammingWeight(n1))  # Output: 3

    # Test Case 2
    n2 = 0b00000000000000000000000010000000
    print(hammingWeight(n2))  # Output: 1

    # Test Case 3
    n3 = 0b11111111111111111111111111111101
    print(hammingWeight(n3))  # Output: 31

# Time and Space Complexity Analysis
"""
Time Complexity:
- The while loop runs until n becomes 0. Since n is a 32-bit integer, the loop will run at most 32 iterations.
- Each iteration performs constant-time operations (bitwise AND, addition, and right shift).
- Therefore, the time complexity is O(1), as the number of iterations is fixed and does not depend on the input size.

Space Complexity:
- The function uses a constant amount of extra space (for the `count` variable).
- Therefore, the space complexity is O(1).
"""

# Topic: Bit Manipulation