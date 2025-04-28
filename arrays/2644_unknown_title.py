"""
LeetCode Problem #2644: Find the Maximum Divisibility Score

Problem Statement:
You are given two integer arrays `nums` and `divisors`. The divisibility score of `divisors[i]` is the number of elements in `nums` that are divisible by `divisors[i]`.

Return the divisor with the maximum divisibility score. If there is more than one divisor with the maximum score, return the smallest one.

Example:
Input: nums = [4, 7, 9, 3, 9], divisors = [5, 10, 3]
Output: 3
Explanation: The divisibility scores are:
- For divisor 5: score = 0 (no elements in nums are divisible by 5)
- For divisor 10: score = 0 (no elements in nums are divisible by 10)
- For divisor 3: score = 3 (elements 9, 9, and 3 are divisible by 3)
The maximum score is 3, and the smallest divisor with this score is 3.

Constraints:
- 1 <= nums.length, divisors.length <= 1000
- 1 <= nums[i], divisors[i] <= 10^9
"""

# Python Solution
def maxDivScore(nums, divisors):
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
    nums1 = [4, 7, 9, 3, 9]
    divisors1 = [5, 10, 3]
    print(maxDivScore(nums1, divisors1))  # Output: 3

    # Test Case 2
    nums2 = [20, 30, 50, 70]
    divisors2 = [2, 5, 10]
    print(maxDivScore(nums2, divisors2))  # Output: 5

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    divisors3 = [1, 2, 3]
    print(maxDivScore(nums3, divisors3))  # Output: 1

    # Test Case 4
    nums4 = [100, 200, 300]
    divisors4 = [10, 20, 30]
    print(maxDivScore(nums4, divisors4))  # Output: 10

    # Test Case 5
    nums5 = [6, 12, 18, 24]
    divisors5 = [6, 12, 18]
    print(maxDivScore(nums5, divisors5))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each divisor in `divisors`, we iterate through all elements in `nums` to calculate the score.
- Let `n` be the length of `nums` and `m` be the length of `divisors`.
- The time complexity is O(n * m).

Space Complexity:
- We use a constant amount of extra space for variables like `max_score` and `best_divisor`.
- The space complexity is O(1).
"""

# Topic: Arrays