"""
LeetCode Problem #2220: Minimum Bit Flips to Convert Number

Problem Statement:
You are given two integers `start` and `goal`. An integer `bit flip` changes the value of a single bit 
from 0 to 1 or from 1 to 0. Return the minimum number of bit flips to convert `start` to `goal`.

Example 1:
Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 is 1010, and the binary representation of 7 is 0111. 
We need to flip the first, third, and fourth bits in 1010 to make it 0111. Hence, the answer is 3.

Example 2:
Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 is 0011, and the binary representation of 4 is 0100. 
We need to flip all three bits to convert 3 to 4. Hence, the answer is 3.

Constraints:
- 0 <= start, goal <= 10^9
"""

def minBitFlips(start: int, goal: int) -> int:
    """
    Calculate the minimum number of bit flips required to convert `start` to `goal`.

    Args:
    start (int): The starting integer.
    goal (int): The target integer.

    Returns:
    int: The minimum number of bit flips.
    """
    # XOR the two numbers to find differing bits
    xor_result = start ^ goal
    
    # Count the number of 1s in the XOR result (Hamming weight)
    return bin(xor_result).count('1')

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    start = 10
    goal = 7
    print(f"Test Case 1: minBitFlips({start}, {goal}) = {minBitFlips(start, goal)}")  # Expected Output: 3

    # Test Case 2
    start = 3
    goal = 4
    print(f"Test Case 2: minBitFlips({start}, {goal}) = {minBitFlips(start, goal)}")  # Expected Output: 3

    # Test Case 3
    start = 0
    goal = 0
    print(f"Test Case 3: minBitFlips({start}, {goal}) = {minBitFlips(start, goal)}")  # Expected Output: 0

    # Test Case 4
    start = 8
    goal = 15
    print(f"Test Case 4: minBitFlips({start}, {goal}) = {minBitFlips(start, goal)}")  # Expected Output: 4

    # Test Case 5
    start = 123456
    goal = 654321
    print(f"Test Case 5: minBitFlips({start}, {goal}) = {minBitFlips(start, goal)}")  # Expected Output: 11

"""
Time Complexity:
- The time complexity is O(n), where n is the number of bits in the binary representation of the larger of `start` or `goal`.
  This is because the XOR operation and counting the number of 1s in the binary representation both depend on the number of bits.

Space Complexity:
- The space complexity is O(1), as we are using a constant amount of extra space.

Topic: Bit Manipulation
"""