"""
LeetCode Problem #2749: Minimum Operations to Make the Integer Zero

Problem Statement:
You are given two integers `num1` and `num2`.

In one operation, you can do the following:
- Choose any non-negative integer `x` and subtract `num2 * 2^x` from `num1`.

Return the minimum number of operations required to make `num1` equal to 0. 
If it is impossible to make `num1` equal to 0, return -1.

Constraints:
- 0 <= num1 <= 10^9
- 1 <= num2 <= 10^9
"""

def minOperations(num1: int, num2: int) -> int:
    """
    Calculate the minimum number of operations to make num1 equal to 0.
    
    Args:
    num1 (int): The initial integer.
    num2 (int): The multiplier for the operation.
    
    Returns:
    int: The minimum number of operations, or -1 if impossible.
    """
    if num2 == 0:
        return -1  # Impossible to make num1 zero if num2 is zero.

    operations = 0
    while num1 > 0:
        # Check if num1 is divisible by num2
        if num1 % num2 != 0:
            return -1  # If num1 is not divisible by num2, it's impossible to make it zero.
        
        # Find the largest power of 2 that can be subtracted
        power = 0
        while num1 >= num2 * (2 ** power):
            power += 1
        power -= 1  # Adjust to the largest valid power
        
        # Subtract num2 * 2^power from num1
        num1 -= num2 * (2 ** power)
        operations += 1
    
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    num1 = 10
    num2 = 2
    print(minOperations(num1, num2))  # Expected output: 2

    # Test Case 2: Impossible case
    num1 = 7
    num2 = 3
    print(minOperations(num1, num2))  # Expected output: -1

    # Test Case 3: Large numbers
    num1 = 1024
    num2 = 2
    print(minOperations(num1, num2))  # Expected output: 10

    # Test Case 4: Edge case where num1 is already 0
    num1 = 0
    num2 = 5
    print(minOperations(num1, num2))  # Expected output: 0

    # Test Case 5: Edge case with num2 = 1
    num1 = 15
    num2 = 1
    print(minOperations(num1, num2))  # Expected output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `num1` becomes 0. In each iteration, we find the largest power of 2 that can be subtracted.
- The number of iterations is proportional to the number of operations required to reduce `num1` to 0.
- Finding the largest power of 2 involves logarithmic operations, so the complexity is O(log(num1)).
- Overall time complexity: O(log(num1)).

Space Complexity:
- The algorithm uses a constant amount of space for variables.
- Overall space complexity: O(1).

Topic: Math, Bit Manipulation
"""