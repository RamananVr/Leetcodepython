"""
LeetCode Problem #868: Binary Gap

Problem Statement:
Given a positive integer n, find and return the maximum distance between two consecutive 1's in the binary representation of n. 
If there are fewer than two 1's in the binary representation of n, return 0.

The binary representation of a number is a string that consists only of '0's and '1's. For example, the binary representation of 22 is "10110".

Example 1:
Input: n = 22
Output: 2
Explanation: The binary representation of 22 is "10110". In the binary representation, there are three 1's, and two consecutive pairs of 1's have distances of 2 and 1. The maximum distance is 2.

Example 2:
Input: n = 8
Output: 0
Explanation: The binary representation of 8 is "1000". There is only one '1' in the binary representation, so there are no consecutive pairs of 1's.

Example 3:
Input: n = 5
Output: 2
Explanation: The binary representation of 5 is "101". The distance between the two 1's is 2.

Constraints:
- 1 <= n <= 10^9
"""

def binary_gap(n: int) -> int:
    """
    Finds the maximum distance between two consecutive 1's in the binary representation of n.
    
    :param n: A positive integer
    :return: Maximum distance between consecutive 1's in the binary representation of n
    """
    # Convert the number to its binary representation
    binary = bin(n)[2:]
    
    # Initialize variables
    max_gap = 0
    prev_index = -1
    
    # Iterate through the binary representation
    for i, char in enumerate(binary):
        if char == '1':
            if prev_index != -1:
                max_gap = max(max_gap, i - prev_index)
            prev_index = i
    
    return max_gap

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 22
    print(f"Input: {n1}, Output: {binary_gap(n1)}")  # Expected Output: 2

    # Test Case 2
    n2 = 8
    print(f"Input: {n2}, Output: {binary_gap(n2)}")  # Expected Output: 0

    # Test Case 3
    n3 = 5
    print(f"Input: {n3}, Output: {binary_gap(n3)}")  # Expected Output: 2

    # Additional Test Case
    n4 = 6
    print(f"Input: {n4}, Output: {binary_gap(n4)}")  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the number to its binary representation using `bin(n)` takes O(log(n)) time, where n is the input number.
- Iterating through the binary string takes O(log(n)) time, as the length of the binary representation is proportional to log(n).
- Overall, the time complexity is O(log(n)).

Space Complexity:
- The binary representation of the number is stored as a string, which takes O(log(n)) space.
- Other variables (max_gap, prev_index) use O(1) space.
- Overall, the space complexity is O(log(n)).

Topic: Bit Manipulation
"""