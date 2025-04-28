"""
LeetCode Problem #1304: Find N Unique Integers Sum up to Zero

Problem Statement:
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7, -1, 1, 3, 4]
Explanation: These integers add up to 0. There are other possible outputs.

Example 2:
Input: n = 3
Output: [-1, 0, 1]

Example 3:
Input: n = 1
Output: [0]

Constraints:
1 <= n <= 1000
"""

def sumZero(n: int) -> list[int]:
    """
    Generate an array of n unique integers that sum up to zero.

    Args:
    n (int): The number of integers to generate.

    Returns:
    list[int]: A list of n unique integers summing to zero.
    """
    # If n is odd, include 0 in the result. Otherwise, use pairs of positive and negative integers.
    return list(range(1 - n, n, 2))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    print(f"Input: n = {n}")
    print(f"Output: {sumZero(n)}")  # Example output: [-2, -1, 0, 1, 2]

    # Test Case 2
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {sumZero(n)}")  # Example output: [-1, 0, 1]

    # Test Case 3
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {sumZero(n)}")  # Example output: [0]

    # Test Case 4
    n = 4
    print(f"Input: n = {n}")
    print(f"Output: {sumZero(n)}")  # Example output: [-3, -1, 1, 3]

"""
Time Complexity Analysis:
The function generates a range of integers from 1 - n to n with a step of 2. 
This operation takes O(n) time since the range function generates n elements.

Space Complexity Analysis:
The function returns a list of n integers, so the space complexity is O(n).

Topic: Arrays
"""