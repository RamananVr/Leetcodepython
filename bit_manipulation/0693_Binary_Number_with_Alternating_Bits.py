"""
LeetCode Problem #693: Binary Number with Alternating Bits

Problem Statement:
Given a positive integer n, return true if the number has alternating bits, 
i.e., if two adjacent bits in the binary representation of the number are 
different. Otherwise, return false.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is "101", which has alternating bits.

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is "111", which does not have alternating bits.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is "1011", which does not have alternating bits.

Constraints:
- 1 <= n <= 2^31 - 1
"""

def hasAlternatingBits(n: int) -> bool:
    """
    Determines if a number has alternating bits in its binary representation.

    Args:
    n (int): A positive integer.

    Returns:
    bool: True if the number has alternating bits, False otherwise.
    """
    # Perform XOR between n and n >> 1
    xor_result = n ^ (n >> 1)
    
    # Check if xor_result is a sequence of all 1s
    return (xor_result & (xor_result + 1)) == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    print(hasAlternatingBits(n1))  # Output: True

    # Test Case 2
    n2 = 7
    print(hasAlternatingBits(n2))  # Output: False

    # Test Case 3
    n3 = 11
    print(hasAlternatingBits(n3))  # Output: False

    # Test Case 4
    n4 = 10
    print(hasAlternatingBits(n4))  # Output: True

    # Test Case 5
    n5 = 1
    print(hasAlternatingBits(n5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves bitwise operations, which are O(1) in terms of computational complexity.
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space for variables and does not require any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""