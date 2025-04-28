"""
LeetCode Problem #264: Ugly Number II

Problem Statement:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example:
Input: n = 10
Output: 12
Explanation: The sequence of ugly numbers is [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]. The 10th ugly number is 12.

Constraints:
1 <= n <= 1690
"""

# Solution
def nthUglyNumber(n: int) -> int:
    # Initialize pointers for multiples of 2, 3, and 5
    p2, p3, p5 = 0, 0, 0
    # Initialize the list to store ugly numbers
    ugly_numbers = [1] * n
    
    for i in range(1, n):
        # Calculate the next ugly number candidates
        next2 = ugly_numbers[p2] * 2
        next3 = ugly_numbers[p3] * 3
        next5 = ugly_numbers[p5] * 5
        
        # Choose the smallest candidate as the next ugly number
        next_ugly = min(next2, next3, next5)
        ugly_numbers[i] = next_ugly
        
        # Increment the pointer(s) that contributed to the next ugly number
        if next_ugly == next2:
            p2 += 1
        if next_ugly == next3:
            p3 += 1
        if next_ugly == next5:
            p5 += 1
    
    return ugly_numbers[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(nthUglyNumber(n))  # Output: 12

    # Test Case 2
    n = 1
    print(nthUglyNumber(n))  # Output: 1

    # Test Case 3
    n = 15
    print(nthUglyNumber(n))  # Output: 24

    # Test Case 4
    n = 100
    print(nthUglyNumber(n))  # Output: 1536

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm iterates `n` times to compute the nth ugly number. Each iteration involves constant-time operations to calculate the next multiples of 2, 3, and 5, and to update the pointers. Therefore, the time complexity is O(n).

Space Complexity:
The algorithm uses a list `ugly_numbers` of size `n` to store the ugly numbers. Thus, the space complexity is O(n).

Topic: Dynamic Programming
"""