"""
LeetCode Problem #461: Hamming Distance

Problem Statement:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
- 0 <= x, y <= 2^31 - 1
"""

def hammingDistance(x: int, y: int) -> int:
    """
    Calculate the Hamming distance between two integers.

    Args:
    x (int): First integer.
    y (int): Second integer.

    Returns:
    int: The Hamming distance between x and y.
    """
    # XOR the two numbers to find differing bits
    xor_result = x ^ y
    
    # Count the number of 1s in the binary representation of the XOR result
    return bin(xor_result).count('1')

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1, y1 = 1, 4
    print(f"Hamming Distance between {x1} and {y1}: {hammingDistance(x1, y1)}")  # Output: 2

    # Test Case 2
    x2, y2 = 3, 1
    print(f"Hamming Distance between {x2} and {y2}: {hammingDistance(x2, y2)}")  # Output: 1

    # Test Case 3
    x3, y3 = 0, 0
    print(f"Hamming Distance between {x3} and {y3}: {hammingDistance(x3, y3)}")  # Output: 0

    # Test Case 4
    x4, y4 = 15, 0
    print(f"Hamming Distance between {x4} and {y4}: {hammingDistance(x4, y4)}")  # Output: 4

    # Test Case 5
    x5, y5 = 8, 7
    print(f"Hamming Distance between {x5} and {y5}: {hammingDistance(x5, y5)}")  # Output: 4

"""
Time Complexity:
- The XOR operation takes O(1) time since it operates on fixed-width integers (32 bits).
- The `bin()` function converts the integer to a binary string, which takes O(k) time, where k is the number of bits in the integer (at most 32 for standard integers).
- The `count('1')` operation iterates over the binary string, which also takes O(k) time.
- Overall, the time complexity is O(k), where k is the number of bits (constant for 32-bit integers).

Space Complexity:
- The space complexity is O(k) due to the binary string representation created by `bin()`.

Topic: Bit Manipulation
"""