"""
LeetCode Question #2281: Sum of Total Strength of Wizards

Problem Statement:
You are given an integer array `strength`, where `strength[i]` represents the strength of the i-th wizard. 
The total strength of a group of wizards is defined as the product of the sum of their strengths and 
the minimum strength within the group.

Return the sum of the total strength of all contiguous subgroups of wizards modulo 10^9 + 7.

Example:
Input: strength = [1,3,1,2]
Output: 44

Explanation:
The following are all the contiguous subgroups:
- The group [1] has sum 1 and minimum 1, so its total strength is 1 * 1 = 1.
- The group [3] has sum 3 and minimum 3, so its total strength is 3 * 3 = 9.
- The group [1] has sum 1 and minimum 1, so its total strength is 1 * 1 = 1.
- The group [2] has sum 2 and minimum 2, so its total strength is 2 * 2 = 4.
- The group [1,3] has sum 4 and minimum 1, so its total strength is 4 * 1 = 4.
- The group [3,1] has sum 4 and minimum 1, so its total strength is 4 * 1 = 4.
- The group [1,2] has sum 3 and minimum 1, so its total strength is 3 * 1 = 3.
- The group [1,3,1] has sum 5 and minimum 1, so its total strength is 5 * 1 = 5.
- The group [3,1,2] has sum 6 and minimum 1, so its total strength is 6 * 1 = 6.
- The group [1,3,1,2] has sum 7 and minimum 1, so its total strength is 7 * 1 = 7.

The sum of all these total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
"""

# Python Solution
from typing import List

def totalStrength(strength: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(strength)
    
    # Precompute prefix sums and prefix of prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MOD
    
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MOD
    
    # Monotonic stack to find previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            next_smaller[stack.pop()] = i
        stack.append(i)
    
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            prev_smaller[stack.pop()] = i
        stack.append(i)
    
    # Calculate total strength
    result = 0
    for i in range(n):
        left = prev_smaller[i]
        right = next_smaller[i]
        
        # Sum of subarray sums on the left
        left_sum = prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[left + 1]
        left_count = i - left
        
        # Sum of subarray sums on the right
        right_sum = prefix_of_prefix_sum[right + 1] - prefix_of_prefix_sum[i + 1]
        right_count = right - i
        
        # Contribution of strength[i] as the minimum
        total = strength[i] * (right_sum * left_count - left_sum * right_count) % MOD
        result = (result + total) % MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strength = [1, 3, 1, 2]
    print(totalStrength(strength))  # Output: 44

    # Test Case 2
    strength = [5, 4, 6]
    print(totalStrength(strength))  # Output: 213

    # Test Case 3
    strength = [1]
    print(totalStrength(strength))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing prefix sums: O(n)
- Finding previous and next smaller elements using monotonic stack: O(n)
- Calculating total strength: O(n)
Overall: O(n)

Space Complexity:
- Prefix sums and prefix of prefix sums: O(n)
- Monotonic stack: O(n)
Overall: O(n)

Topic: Arrays, Monotonic Stack, Prefix Sum
"""