"""
LeetCode Problem #1318: Minimum Flips to Make a OR b Equal to c

Problem Statement:
Given 3 positive numbers `a`, `b`, and `c`, you can flip the bits of `a` and `b` (change 0 to 1 or 1 to 0) as needed. 
Return the minimum number of flips required in some bits of `a` and `b` to make `(a OR b == c)` true.

Constraints:
- 1 <= a, b, c <= 10^9

Example:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: 
- Initially, a = 010 (binary), b = 110 (binary), c = 101 (binary)
- Flip a[0] to 1, b[2] to 0, and b[1] to 0. Total flips = 3.

Input: a = 4, b = 2, c = 7
Output: 1
Explanation:
- Initially, a = 100 (binary), b = 010 (binary), c = 111 (binary)
- Flip a[1] to 1. Total flips = 1.

Input: a = 1, b = 2, c = 3
Output: 0
Explanation:
- Initially, a = 001 (binary), b = 010 (binary), c = 011 (binary)
- No flips are needed since (a OR b == c).
"""

def minFlips(a: int, b: int, c: int) -> int:
    """
    Calculate the minimum number of bit flips required to make (a OR b == c).
    """
    flips = 0
    while a > 0 or b > 0 or c > 0:
        # Extract the least significant bit (LSB) of a, b, and c
        bit_a = a & 1
        bit_b = b & 1
        bit_c = c & 1

        # If bit_c is 1, at least one of bit_a or bit_b must be 1
        if bit_c == 1:
            if bit_a == 0 and bit_b == 0:
                flips += 1
        # If bit_c is 0, both bit_a and bit_b must be 0
        else:
            flips += bit_a + bit_b

        # Right shift a, b, and c to process the next bit
        a >>= 1
        b >>= 1
        c >>= 1

    return flips

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b, c = 2, 6, 5
    print(f"Test Case 1: a={a}, b={b}, c={c} -> Output: {minFlips(a, b, c)}")  # Expected: 3

    # Test Case 2
    a, b, c = 4, 2, 7
    print(f"Test Case 2: a={a}, b={b}, c={c} -> Output: {minFlips(a, b, c)}")  # Expected: 1

    # Test Case 3
    a, b, c = 1, 2, 3
    print(f"Test Case 3: a={a}, b={b}, c={c} -> Output: {minFlips(a, b, c)}")  # Expected: 0

    # Test Case 4
    a, b, c = 8, 3, 5
    print(f"Test Case 4: a={a}, b={b}, c={c} -> Output: {minFlips(a, b, c)}")  # Expected: 3

    # Test Case 5
    a, b, c = 0, 0, 0
    print(f"Test Case 5: a={a}, b={b}, c={c} -> Output: {minFlips(a, b, c)}")  # Expected: 0

"""
Time Complexity:
- The while loop runs until all bits of `a`, `b`, and `c` are processed. 
  Since the maximum value of `a`, `b`, or `c` is 10^9, the number of bits to process is at most 30 (since 2^30 > 10^9).
- Therefore, the time complexity is O(30), which simplifies to O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Bit Manipulation
"""