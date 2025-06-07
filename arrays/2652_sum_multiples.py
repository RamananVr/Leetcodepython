"""
LeetCode Question #2652: Sum Multiples

Problem Statement:
Given a positive integer n, find the sum of all integers in the range [1, n] that are divisible by 3, 5, or 7.

Return an integer representing the sum of all integers in the range [1, n] divisible by 3, 5, or 7.

Examples:
Example 1:
Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.

Example 2:
Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.

Example 3:
Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.

Constraints:
- 1 <= n <= 1000
"""

def sumOfMultiples(n: int) -> int:
    """
    Find the sum of all integers in the range [1, n] divisible by 3, 5, or 7.
    
    Approach: Iterate through all numbers and check divisibility.
    """
    total_sum = 0
    
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total_sum += i
    
    return total_sum

def sumOfMultiplesOptimized(n: int) -> int:
    """
    Optimized approach using inclusion-exclusion principle.
    
    Sum of multiples of A or B or C = 
    Sum(A) + Sum(B) + Sum(C) - Sum(LCM(A,B)) - Sum(LCM(A,C)) - Sum(LCM(B,C)) + Sum(LCM(A,B,C))
    """
    def sum_of_multiples(divisor, limit):
        """Calculate sum of multiples of divisor up to limit."""
        if divisor > limit:
            return 0
        count = limit // divisor
        return divisor * count * (count + 1) // 2
    
    def gcd(a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        """Calculate least common multiple."""
        return a * b // gcd(a, b)
    
    # Sum of multiples of 3, 5, 7
    sum3 = sum_of_multiples(3, n)
    sum5 = sum_of_multiples(5, n)
    sum7 = sum_of_multiples(7, n)
    
    # Sum of multiples of LCM pairs
    sum15 = sum_of_multiples(lcm(3, 5), n)  # LCM(3,5) = 15
    sum21 = sum_of_multiples(lcm(3, 7), n)  # LCM(3,7) = 21
    sum35 = sum_of_multiples(lcm(5, 7), n)  # LCM(5,7) = 35
    
    # Sum of multiples of LCM of all three
    sum105 = sum_of_multiples(lcm(lcm(3, 5), 7), n)  # LCM(3,5,7) = 105
    
    # Apply inclusion-exclusion principle
    return sum3 + sum5 + sum7 - sum15 - sum21 - sum35 + sum105

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (7, 21),
        (10, 40),
        (9, 30),
        (1, 0),
        (15, 60),
        (21, 119)
    ]
    
    print("Testing brute force approach:")
    for n, expected in test_cases:
        result = sumOfMultiples(n)
        print(f"sumOfMultiples({n}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for n, expected in test_cases:
        result = sumOfMultiplesOptimized(n)
        print(f"sumOfMultiplesOptimized({n}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Brute Force Approach:
Time Complexity: O(n) - iterate through all numbers from 1 to n
Space Complexity: O(1) - only using constant extra space

Optimized Approach (Inclusion-Exclusion):
Time Complexity: O(1) - constant number of arithmetic operations
Space Complexity: O(1) - only using constant extra space

Topic: Arrays, Math, Number Theory
"""
