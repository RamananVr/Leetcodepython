"""
LeetCode Question #2868: Find the Maximum Divisibility Score

Problem Statement:
You are given two integer arrays `nums` and `divisors`. The divisibility score of `divisors[i]` is defined as the number of elements in `nums` that are divisible by `divisors[i]`.

Return the divisor with the maximum divisibility score. If there is a tie, return the smallest divisor.

Example:
Input: nums = [4, 7, 9, 3, 9], divisors = [5, 10, 3]
Output: 3
Explanation: The divisibility scores are:
- For divisor 5: score = 0 (no elements in nums are divisible by 5)
- For divisor 10: score = 0 (no elements in nums are divisible by 10)
- For divisor 3: score = 3 (elements 9, 9, and 3 are divisible by 3)
Since 3 has the highest score, we return it.

Constraints:
- 1 <= nums.length, divisors.length <= 1000
- 1 <= nums[i], divisors[i] <= 10^9
"""

# Python Solution
def maxDivScore(nums, divisors):
    """
    Finds the divisor with the maximum divisibility score.
    If there is a tie, returns the smallest divisor.

    :param nums: List[int] - Array of integers
    :param divisors: List[int] - Array of divisors
    :return: int - Divisor with the maximum divisibility score
    """
    max_score = 0
    best_divisor = float('inf')

    for divisor in divisors:
        score = sum(1 for num in nums if num % divisor == 0)
        if score > max_score or (score == max_score and divisor < best_divisor):
            max_score = score
            best_divisor = divisor

    return best_divisor

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [4, 7, 9, 3, 9]
    divisors = [5, 10, 3]
    print(maxDivScore(nums, divisors))  # Output: 3

    # Test Case 2
    nums = [8, 16, 32, 64]
    divisors = [2, 4, 8]
    print(maxDivScore(nums, divisors))  # Output: 8

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    divisors = [6, 7, 8]
    print(maxDivScore(nums, divisors))  # Output: 6

    # Test Case 4
    nums = [10, 20, 30, 40]
    divisors = [5, 10, 20]
    print(maxDivScore(nums, divisors))  # Output: 10

    # Test Case 5
    nums = [100, 200, 300]
    divisors = [50, 100, 150]
    print(maxDivScore(nums, divisors))  # Output: 100

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each divisor in `divisors`, we iterate through all elements in `nums` to calculate the divisibility score.
- This results in a time complexity of O(m * n), where m is the length of `divisors` and n is the length of `nums`.

Space Complexity:
- The solution uses constant space, as we only store a few variables (`max_score`, `best_divisor`, and `score`).
- Thus, the space complexity is O(1).

Overall Complexity:
- Time: O(m * n)
- Space: O(1)
"""

# Topic: Arrays