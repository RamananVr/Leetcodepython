"""
LeetCode Problem #1404: Number of Steps to Reduce a Number in Binary Representation to One

Problem Statement:
Given a binary string `s` representing a positive integer, return the number of steps to reduce it to 1 under the following rules:
1. If the current number is even, divide it by 2.
2. If the current number is odd, add 1 to it.

It is guaranteed that the input string `s` is a valid binary representation of a positive integer.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" represents the number 13 in decimal.
Step 1) 13 is odd, add 1 -> 14
Step 2) 14 is even, divide by 2 -> 7
Step 3) 7 is odd, add 1 -> 8
Step 4) 8 is even, divide by 2 -> 4
Step 5) 4 is even, divide by 2 -> 2
Step 6) 2 is even, divide by 2 -> 1

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" represents the number 2 in decimal.
Step 1) 2 is even, divide by 2 -> 1

Example 3:
Input: s = "1"
Output: 0
Explanation: "1" is already 1, so no steps are needed.

Constraints:
- 1 <= s.length <= 500
- s consists of only '0' or '1'.
- s[0] == '1'
"""

def numSteps(s: str) -> int:
    """
    Function to calculate the number of steps to reduce a binary number to 1.
    
    Args:
    s (str): A binary string representing a positive integer.
    
    Returns:
    int: The number of steps required to reduce the number to 1.
    """
    steps = 0
    carry = 0  # To handle cases where we need to add 1 to the binary number

    # Traverse the binary string from right to left
    for i in range(len(s) - 1, 0, -1):
        if s[i] == '1':
            if carry == 0:
                # If the current bit is 1 and no carry, we need to add 1 (making it 0 with carry)
                steps += 2
                carry = 1
            else:
                # If the current bit is 1 and there's already a carry, it remains 1
                steps += 1
        else:
            if carry == 0:
                # If the current bit is 0 and no carry, just divide by 2
                steps += 1
            else:
                # If the current bit is 0 and there's a carry, it becomes 1
                steps += 2

    # Handle the most significant bit (leftmost bit)
    if carry == 1:
        steps += 1

    return steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1101"
    print(f"Input: {s1}, Output: {numSteps(s1)}")  # Expected Output: 6

    # Test Case 2
    s2 = "10"
    print(f"Input: {s2}, Output: {numSteps(s2)}")  # Expected Output: 1

    # Test Case 3
    s3 = "1"
    print(f"Input: {s3}, Output: {numSteps(s3)}")  # Expected Output: 0

    # Test Case 4
    s4 = "111"
    print(f"Input: {s4}, Output: {numSteps(s4)}")  # Expected Output: 5

    # Test Case 5
    s5 = "101010"
    print(f"Input: {s5}, Output: {numSteps(s5)}")  # Expected Output: 12

"""
Time Complexity Analysis:
- The algorithm processes each bit of the binary string exactly once, so the time complexity is O(n), 
  where n is the length of the binary string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (only a few variables), so the space complexity is O(1).

Topic: Binary Manipulation
"""