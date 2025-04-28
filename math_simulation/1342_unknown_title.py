"""
LeetCode Problem #1342: Number of Steps to Reduce a Number to Zero

Problem Statement:
Given an integer `num`, return the number of steps to reduce it to zero. 
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:
Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:
Input: num = 123
Output: 12

Constraints:
- 0 <= num <= 10^6
"""

def numberOfSteps(num: int) -> int:
    """
    Function to calculate the number of steps to reduce a number to zero.
    
    :param num: The input integer.
    :return: The number of steps to reduce the number to zero.
    """
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 14
    print(f"Input: {num1}, Output: {numberOfSteps(num1)}")  # Expected Output: 6

    # Test Case 2
    num2 = 8
    print(f"Input: {num2}, Output: {numberOfSteps(num2)}")  # Expected Output: 4

    # Test Case 3
    num3 = 123
    print(f"Input: {num3}, Output: {numberOfSteps(num3)}")  # Expected Output: 12

    # Test Case 4
    num4 = 0
    print(f"Input: {num4}, Output: {numberOfSteps(num4)}")  # Expected Output: 0

    # Test Case 5
    num5 = 1
    print(f"Input: {num5}, Output: {numberOfSteps(num5)}")  # Expected Output: 1

"""
Time Complexity Analysis:
- The time complexity of the solution is O(log(num)).
  This is because in each step, the number is either divided by 2 (for even numbers) or decremented by 1 (for odd numbers).
  The number of steps is proportional to the number of bits in the binary representation of `num`, which is O(log(num)).

Space Complexity Analysis:
- The space complexity of the solution is O(1).
  We are using a constant amount of extra space to store the `steps` variable.

Topic: Math, Simulation
"""