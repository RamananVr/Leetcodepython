"""
LeetCode Problem #390: Elimination Game

Problem Statement:
You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. 
Applying the following algorithm repeatedly on the list until only one number remains:

1. Starting from the left, remove the first number and every other number afterward until the end of the list.
2. Repeat the above step again, but this time from the right to the left, remove the rightmost number and every other number from the remaining numbers.
3. Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return the last number that remains in the list.

Constraints:
- 1 <= n <= 10^9

Example:
Input: n = 9
Output: 6

Explanation:
Initial list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Step 1: Remove every second number starting from the left: [2, 4, 6, 8]
Step 2: Remove every second number starting from the right: [2, 6]
Step 3: Remove every second number starting from the left: [6]
The last remaining number is 6.
"""

def lastRemaining(n: int) -> int:
    """
    This function calculates the last remaining number in the elimination game.
    """
    left_to_right = True
    step = 1
    head = 1
    remaining = n

    while remaining > 1:
        if left_to_right or remaining % 2 == 1:
            head += step
        step *= 2
        remaining //= 2
        left_to_right = not left_to_right

    return head

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 9
    print(f"Input: n = {n}, Output: {lastRemaining(n)}")  # Expected Output: 6

    # Test Case 2
    n = 1
    print(f"Input: n = {n}, Output: {lastRemaining(n)}")  # Expected Output: 1

    # Test Case 3
    n = 10
    print(f"Input: n = {n}, Output: {lastRemaining(n)}")  # Expected Output: 8

    # Test Case 4
    n = 100
    print(f"Input: n = {n}, Output: {lastRemaining(n)}")  # Expected Output: 54

    # Test Case 5
    n = 1000
    print(f"Input: n = {n}, Output: {lastRemaining(n)}")  # Expected Output: 510

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm runs in O(log n) time because the number of elements is halved in each iteration.

Space Complexity:
- The algorithm uses O(1) space as it only uses a few variables to track the state of the computation.

Topic: Math, Simulation
"""