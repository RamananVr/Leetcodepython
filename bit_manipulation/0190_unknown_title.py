"""
LeetCode Problem #190: Reverse Bits

Problem Statement:
Reverse bits of a given 32 bits unsigned integer.

Note:
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3, and the output represents the signed integer -1073741825.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
- The input must be a binary string of length 32.

Follow up:
If this function is called many times, how would you optimize it?
"""

def reverseBits(n: int) -> int:
    """
    Reverse the bits of a 32-bit unsigned integer.

    Args:
    n (int): A 32-bit unsigned integer.

    Returns:
    int: The reversed 32-bit unsigned integer.
    """
    result = 0
    for i in range(32):
        # Extract the least significant bit of n
        bit = n & 1
        # Shift the result to the left and add the extracted bit
        result = (result << 1) | bit
        # Shift n to the right to process the next bit
        n >>= 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = int('00000010100101000001111010011100', 2)
    print(reverseBits(n1))  # Expected Output: 964176192

    # Test Case 2
    n2 = int('11111111111111111111111111111101', 2)
    print(reverseBits(n2))  # Expected Output: 3221225471

    # Test Case 3
    n3 = int('00000000000000000000000000000000', 2)
    print(reverseBits(n3))  # Expected Output: 0

    # Test Case 4
    n4 = int('11111111111111111111111111111111', 2)
    print(reverseBits(n4))  # Expected Output: 4294967295

"""
Time Complexity Analysis:
- The function iterates over all 32 bits of the input integer. Each iteration involves a constant amount of work (bitwise operations and shifts).
- Therefore, the time complexity is O(32), which simplifies to O(1) since the number of bits is fixed.

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables like `result` and `bit`.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""