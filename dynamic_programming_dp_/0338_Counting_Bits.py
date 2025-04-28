"""
LeetCode Problem #338: Counting Bits

Problem Statement:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
- 0 <= n <= 10^5

Follow-up:
It is very straightforward to solve the problem with a simple for loop and check each number. 
Can you do it in a way that is both space and time efficient?
"""

def countBits(n: int) -> list[int]:
    """
    Returns an array where each element at index i represents the number of 1's in the binary representation of i.
    
    :param n: An integer representing the maximum number to calculate the binary representation for.
    :return: A list of integers where each element is the count of 1's in the binary representation of the index.
    """
    # Initialize the result array with 0's
    ans = [0] * (n + 1)
    
    # Use the relationship: ans[i] = ans[i >> 1] + (i & 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    
    return ans

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {countBits(n1)}")  # Expected Output: [0, 1, 1]

    # Test Case 2
    n2 = 5
    print(f"Input: n = {n2}")
    print(f"Output: {countBits(n2)}")  # Expected Output: [0, 1, 1, 2, 1, 2]

    # Test Case 3
    n3 = 0
    print(f"Input: n = {n3}")
    print(f"Output: {countBits(n3)}")  # Expected Output: [0]

    # Test Case 4
    n4 = 10
    print(f"Input: n = {n4}")
    print(f"Output: {countBits(n4)}")  # Expected Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through all integers from 1 to n, performing constant-time operations for each integer.
- Therefore, the time complexity is O(n).

Space Complexity:
- The algorithm uses an array `ans` of size n + 1 to store the results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""