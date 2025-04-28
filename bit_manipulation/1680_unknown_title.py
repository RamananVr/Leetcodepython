"""
LeetCode Problem #1680: Concatenation of Consecutive Binary Numbers

Problem Statement:
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.

Example 2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 are "1", "10", and "11". After concatenating them, we get "11011", which corresponds to the decimal value 27.

Example 3:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of this number modulo 10^9 + 7 is 505379714.

Constraints:
- 1 <= n <= 10^5
"""

# Python Solution
def concatenatedBinary(n: int) -> int:
    MOD = 10**9 + 7
    result = 0
    length = 0  # Tracks the number of bits in the current number

    for i in range(1, n + 1):
        # Update the bit length when we reach a power of 2
        if (i & (i - 1)) == 0:
            length += 1
        # Shift the result left by the current bit length and add the current number
        result = ((result << length) | i) % MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(f"Input: n = {n}, Output: {concatenatedBinary(n)}")  # Expected Output: 1

    # Test Case 2
    n = 3
    print(f"Input: n = {n}, Output: {concatenatedBinary(n)}")  # Expected Output: 27

    # Test Case 3
    n = 12
    print(f"Input: n = {n}, Output: {concatenatedBinary(n)}")  # Expected Output: 505379714

    # Additional Test Case 4
    n = 100
    print(f"Input: n = {n}, Output: {concatenatedBinary(n)}")  # Expected Output: 757631812

    # Additional Test Case 5
    n = 1000
    print(f"Input: n = {n}, Output: {concatenatedBinary(n)}")  # Expected Output: 688653593

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop runs from 1 to n, so it iterates n times.
- For each iteration, the bit length is updated in O(1) time, and the result is updated in O(1) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Bit Manipulation