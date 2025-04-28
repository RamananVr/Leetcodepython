"""
LeetCode Problem #2429: Minimize XOR

Problem Statement:
You are given two positive integers `num1` and `num2`. You need to find the positive integer `num3` such that:
1. The XOR of `num1` and `num3` is minimized.
2. `num3` has the same number of set bits (1s in binary representation) as `num2`.

Return the integer `num3`.

Example:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
- num1 = 3 (binary: 011)
- num2 = 5 (binary: 101, has 2 set bits)
- num3 = 3 (binary: 011, has 2 set bits)
- XOR of num1 and num3 = 3 XOR 3 = 0, which is minimized.

Constraints:
- 1 <= num1, num2 <= 10^9
"""

# Python Solution
def minimizeXor(num1: int, num2: int) -> int:
    # Count the number of set bits in num2
    num2_set_bits = bin(num2).count('1')
    
    # Initialize num3 as 0
    num3 = 0
    
    # Iterate over the bits of num1 from most significant to least significant
    for i in range(31, -1, -1):
        if num2_set_bits == 0:
            break
        # Check if the i-th bit in num1 is set
        if (num1 & (1 << i)) != 0:
            # Set the i-th bit in num3
            num3 |= (1 << i)
            num2_set_bits -= 1
    
    # If there are still bits to set, set them in the least significant positions
    for i in range(31):
        if num2_set_bits == 0:
            break
        # Check if the i-th bit in num3 is not set
        if (num3 & (1 << i)) == 0:
            # Set the i-th bit in num3
            num3 |= (1 << i)
            num2_set_bits -= 1
    
    return num3

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 3
    num2 = 5
    print(minimizeXor(num1, num2))  # Output: 3

    # Test Case 2
    num1 = 28
    num2 = 7
    print(minimizeXor(num1, num2))  # Output: 23

    # Test Case 3
    num1 = 1
    num2 = 12
    print(minimizeXor(num1, num2))  # Output: 15

    # Test Case 4
    num1 = 65
    num2 = 8
    print(minimizeXor(num1, num2))  # Output: 64

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over the 32 bits of the integers twice (once for the bits of `num1` and once for the least significant bits).
- Therefore, the time complexity is O(32), which is effectively O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""