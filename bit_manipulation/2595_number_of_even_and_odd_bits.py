"""
LeetCode Question #2595: Number of Even and Odd Bits

Problem Statement:
You are given a positive integer `n`. Let `bin(n)` represent the binary representation of `n`. 
In the binary representation, the least significant bit is at position 0, the second least significant bit is at position 1, and so on.

Return an array `ans` of size 2 where:
- `ans[0]` is the number of 1's in the even positions of `bin(n)` (0-indexed).
- `ans[1]` is the number of 1's in the odd positions of `bin(n)` (0-indexed).

Example:
Input: n = 17
Output: [2, 0]
Explanation: The binary representation of 17 is "10001".
- The 1's at even positions are at indices 0 and 4. Hence, ans[0] = 2.
- There are no 1's at odd positions. Hence, ans[1] = 0.

Constraints:
- 1 <= n <= 10^9
"""

def evenOddBit(n: int) -> list:
    """
    Function to calculate the number of 1's in even and odd positions of the binary representation of n.
    
    Args:
    n (int): A positive integer.

    Returns:
    list: A list of two integers [even_count, odd_count].
    """
    binary = bin(n)[2:]  # Get binary representation of n as a string (excluding the '0b' prefix)
    even_count = 0
    odd_count = 0

    # Iterate through the binary string in reverse (to handle 0-indexed positions)
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            if i % 2 == 0:  # Even position
                even_count += 1
            else:  # Odd position
                odd_count += 1

    return [even_count, odd_count]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 17
    print(f"Input: {n1}, Output: {evenOddBit(n1)}")  # Expected: [2, 0]

    # Test Case 2
    n2 = 2
    print(f"Input: {n2}, Output: {evenOddBit(n2)}")  # Expected: [0, 1]

    # Test Case 3
    n3 = 21
    print(f"Input: {n3}, Output: {evenOddBit(n3)}")  # Expected: [2, 1]

    # Test Case 4
    n4 = 1
    print(f"Input: {n4}, Output: {evenOddBit(n4)}")  # Expected: [1, 0]

    # Test Case 5
    n5 = 1023
    print(f"Input: {n5}, Output: {evenOddBit(n5)}")  # Expected: [5, 5]

"""
Time Complexity Analysis:
- The binary representation of a number `n` has at most O(log(n)) bits.
- Iterating through the binary string takes O(log(n)) time.
- Thus, the time complexity is O(log(n)).

Space Complexity Analysis:
- The space required to store the binary representation is O(log(n)).
- No additional data structures are used, so the space complexity is O(log(n)).

Topic: Bit Manipulation
"""