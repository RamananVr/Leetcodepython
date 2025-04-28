"""
LeetCode Problem #89: Gray Code

Problem Statement:
An n-bit gray code sequence is a sequence of 2^n integers where:
1. Every integer is in the inclusive range [0, 2^n - 1].
2. The first integer is 0.
3. An integer appears no more than once in the sequence.
4. The binary representation of every pair of adjacent integers differs by exactly one bit.
5. The binary representation of the first and last integers also differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.

Example 1:
Input: n = 2
Output: [0, 1, 3, 2]
Explanation:
The binary representation of the gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
- All adjacent pairs of binary representations differ by exactly one bit.
- The first and last binary representations also differ by exactly one bit.

Example 2:
Input: n = 1
Output: [0, 1]

Constraints:
- 1 <= n <= 16
"""

def grayCode(n: int) -> list[int]:
    """
    Generate the n-bit Gray code sequence using a mathematical approach.
    """
    # The i-th Gray code can be generated using the formula: i ^ (i >> 1)
    return [i ^ (i >> 1) for i in range(2 ** n)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(f"Gray Code for n={n1}: {grayCode(n1)}")  # Expected Output: [0, 1, 3, 2]

    # Test Case 2
    n2 = 1
    print(f"Gray Code for n={n2}: {grayCode(n2)}")  # Expected Output: [0, 1]

    # Test Case 3
    n3 = 3
    print(f"Gray Code for n={n3}: {grayCode(n3)}")  # Expected Output: [0, 1, 3, 2, 6, 7, 5, 4]

    # Test Case 4
    n4 = 4
    print(f"Gray Code for n={n4}: {grayCode(n4)}")  # Expected Output: [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]

"""
Time Complexity:
- The function iterates over a range of size 2^n to generate the Gray code sequence.
- Therefore, the time complexity is O(2^n).

Space Complexity:
- The function uses a list to store the Gray code sequence, which has a size of 2^n.
- Therefore, the space complexity is O(2^n).

Topic: Bit Manipulation
"""