"""
LeetCode Problem #1009: Complement of Base 10 Integer

Problem Statement:
Every non-negative integer `n` has a binary representation. For example, `5` can be represented as `"101"` in binary, and its complement is `"010"` which is the number `2`. Given an integer `n`, return its complement.

The complement of a binary representation is obtained by flipping all the bits (changing `1` to `0` and `0` to `1`).

Constraints:
- 0 <= n < 10^9

Example 1:
Input: n = 5
Output: 2
Explanation: The binary representation of 5 is "101", and its complement is "010", which is 2 in decimal.

Example 2:
Input: n = 7
Output: 0
Explanation: The binary representation of 7 is "111", and its complement is "000", which is 0 in decimal.

Example 3:
Input: n = 10
Output: 5
Explanation: The binary representation of 10 is "1010", and its complement is "0101", which is 5 in decimal.

Note:
- The complement operation is applied to the binary representation of the number without leading zeroes.
"""

def bitwiseComplement(n: int) -> int:
    """
    Function to compute the complement of a base-10 integer.
    """
    if n == 0:
        return 1  # Special case: The complement of 0 is 1.
    
    # Find the bit length of n
    bit_length = n.bit_length()
    
    # Create a mask with all bits set to 1 of the same length as n
    mask = (1 << bit_length) - 1
    
    # XOR n with the mask to flip all bits
    return n ^ mask

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    print(f"Input: {n1}, Output: {bitwiseComplement(n1)}")  # Expected Output: 2

    # Test Case 2
    n2 = 7
    print(f"Input: {n2}, Output: {bitwiseComplement(n2)}")  # Expected Output: 0

    # Test Case 3
    n3 = 10
    print(f"Input: {n3}, Output: {bitwiseComplement(n3)}")  # Expected Output: 5

    # Test Case 4 (Edge Case)
    n4 = 0
    print(f"Input: {n4}, Output: {bitwiseComplement(n4)}")  # Expected Output: 1

    # Test Case 5
    n5 = 1
    print(f"Input: {n5}, Output: {bitwiseComplement(n5)}")  # Expected Output: 0

"""
Time Complexity Analysis:
- The time complexity of the solution is O(1) because the operations performed (bit length calculation, bitwise XOR) are constant time for integers within the given constraints (0 <= n < 10^9).

Space Complexity Analysis:
- The space complexity is O(1) as no additional data structures are used, and the space usage is constant.

Topic: Bit Manipulation
"""