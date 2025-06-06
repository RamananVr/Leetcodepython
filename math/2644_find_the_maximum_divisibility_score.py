"""
LeetCode Problem #2644: Find the Maximum Divisibility Score

Problem Statement:
You are given two 0-indexed integer arrays nums and divisors.

The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

Return the integer divisors[i] with the maximum divisibility score. If there is more than one integer with the maximum score, return the minimum one.

Example 1:
Input: nums = [4,7,9,3,9], divisors = [5,2,3]
Output: 3
Explanation: The divisibility scores for each element in divisors are:
- The divisibility score of divisors[0] = 5 is 0 since no number in nums is divisible by 5.
- The divisibility score of divisors[1] = 2 is 1 since nums[0] = 4 is divisible by 2.
- The divisibility score of divisors[2] = 3 is 3 since nums[2] = 9, nums[3] = 3, and nums[4] = 9 are divisible by 3.
Since divisors[2] has the maximum score, we return it.

Example 2:
Input: nums = [20,14,21,10], divisors = [5,7,5]
Output: 5
Explanation: The divisibility scores for each element in divisors are:
- The divisibility score of divisors[0] = 5 is 2 since nums[0] = 20 and nums[3] = 10 are divisible by 5.
- The divisibility score of divisors[1] = 7 is 2 since nums[1] = 14 and nums[2] = 21 are divisible by 7.
- The divisibility score of divisors[2] = 5 is 2 since nums[0] = 20 and nums[3] = 10 are divisible by 5.
Since divisors[0], divisors[1], and divisors[2] all have the maximum score, we return the minimum one which is 5.

Example 3:
Input: nums = [12], divisors = [10,16]
Output: 10
Explanation: The divisibility scores for each element in divisors are:
- The divisibility score of divisors[0] = 10 is 0 since no number in nums is divisible by 10.
- The divisibility score of divisors[1] = 16 is 0 since no number in nums is divisible by 16.
Since divisors[0] and divisors[1] both have the maximum score, we return the minimum one which is 10.

Constraints:
- 1 <= nums.length, divisors.length <= 1000
- 1 <= nums[i], divisors[i] <= 10^9
"""

from typing import List

def maxDivScore(nums: List[int], divisors: List[int]) -> int:
    """
    Find the divisor with the maximum divisibility score.
    If there are ties, return the minimum divisor.
    
    Args:
    nums: List of integers to be divided
    divisors: List of potential divisors
    
    Returns:
    The divisor with maximum divisibility score (minimum if tie)
    """
    max_score = -1
    result = float('inf')
    
    for divisor in divisors:
        # Calculate divisibility score for current divisor
        score = 0
        for num in nums:
            if num % divisor == 0:
                score += 1
        
        # Update result if we found a better score or same score with smaller divisor
        if score > max_score or (score == max_score and divisor < result):
            max_score = score
            result = divisor
    
    return result

def maxDivScoreOptimized(nums: List[int], divisors: List[int]) -> int:
    """
    Optimized version using list comprehension and built-in functions.
    
    Args:
    nums: List of integers to be divided
    divisors: List of potential divisors
    
    Returns:
    The divisor with maximum divisibility score (minimum if tie)
    """
    def get_score(divisor):
        return sum(1 for num in nums if num % divisor == 0)
    
    # Find maximum score first
    max_score = max(get_score(divisor) for divisor in divisors)
    
    # Among divisors with max score, return the minimum
    return min(divisor for divisor in divisors if get_score(divisor) == max_score)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 7, 9, 3, 9]
    divisors1 = [5, 2, 3]
    print(maxDivScore(nums1, divisors1))  # Output: 3
    
    # Test Case 2
    nums2 = [20, 14, 21, 10]
    divisors2 = [5, 7, 5]
    print(maxDivScore(nums2, divisors2))  # Output: 5
    
    # Test Case 3
    nums3 = [12]
    divisors3 = [10, 16]
    print(maxDivScore(nums3, divisors3))  # Output: 10
    
    # Test Case 4: Edge case - single element arrays
    nums4 = [6]
    divisors4 = [3]
    print(maxDivScore(nums4, divisors4))  # Output: 3
    
    # Test Case 5: Multiple divisors with same score
    nums5 = [2, 4, 6, 8]
    divisors5 = [2, 4, 8, 1]
    print(maxDivScore(nums5, divisors5))  # Output: 1 (all numbers divisible by 1)
    
    # Test Case 6: No divisibility
    nums6 = [7, 11, 13]
    divisors6 = [2, 3, 5]
    print(maxDivScore(nums6, divisors6))  # Output: 2 (minimum among equal scores of 0)
    
    # Test optimized version
    print("\nOptimized version results:")
    print(maxDivScoreOptimized(nums1, divisors1))  # Output: 3
    print(maxDivScoreOptimized(nums2, divisors2))  # Output: 5
    print(maxDivScoreOptimized(nums3, divisors3))  # Output: 10

"""
Time Complexity:
- For each divisor in divisors (O(d) where d = len(divisors))
- We check divisibility for each number in nums (O(n) where n = len(nums))
- Overall time complexity: O(d * n)

Space Complexity:
- We use only a constant amount of extra space for variables
- Space complexity: O(1)

The optimized version has the same time complexity but uses more functional programming style.
It might be slightly slower due to multiple passes but is more readable.
"""

# Topic: Math
