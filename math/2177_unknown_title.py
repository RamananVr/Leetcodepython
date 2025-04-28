"""
LeetCode Problem #2177: Find Three Consecutive Integers That Sum to a Given Number

Problem Statement:
Given an integer `num`, return three consecutive integers (as a list) whose sum is equal to `num`. 
If it is impossible to find such integers, return an empty list.

Example:
Input: num = 33
Output: [10, 11, 12]
Explanation: 10 + 11 + 12 = 33

Input: num = 4
Output: []
Explanation: It is impossible to find three consecutive integers that sum to 4.

Constraints:
- -10^15 <= num <= 10^15
"""

def sumOfThree(num):
    """
    Find three consecutive integers whose sum equals the given number.

    :param num: int - The target sum.
    :return: List[int] - A list of three consecutive integers if possible, otherwise an empty list.
    """
    # Check if num is divisible by 3
    if num % 3 != 0:
        return []
    
    # Calculate the middle integer
    middle = num // 3
    
    # Return the three consecutive integers
    return [middle - 1, middle, middle + 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: num = 33
    print(sumOfThree(33))  # Expected Output: [10, 11, 12]

    # Test Case 2: num = 4
    print(sumOfThree(4))  # Expected Output: []

    # Test Case 3: num = 0
    print(sumOfThree(0))  # Expected Output: [-1, 0, 1]

    # Test Case 4: num = -3
    print(sumOfThree(-3))  # Expected Output: [-2, -1, 0]

    # Test Case 5: num = 15
    print(sumOfThree(15))  # Expected Output: [4, 5, 6]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a constant-time check (num % 3) and a simple arithmetic operation (num // 3).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a fixed amount of space to store the result (a list of three integers).
- Therefore, the space complexity is O(1).

Topic: Math
"""