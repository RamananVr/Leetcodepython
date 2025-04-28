"""
LeetCode Problem #1262: Greatest Sum Divisible by Three

Problem Statement:
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1, 8, their sum is 18 (maximum sum divisible by 3).

Example 2:
Input: nums = [4,1,5,3,1]
Output: 12
Explanation: Pick numbers 4, 1, 5, 3, their sum is 12 (maximum sum divisible by 3).

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 2, 3, 4, 4, their sum is 12 (maximum sum divisible by 3).

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4
"""

# Solution
def maxSumDivThree(nums):
    """
    Function to calculate the maximum sum divisible by three.
    
    Args:
    nums (List[int]): List of integers.
    
    Returns:
    int: Maximum sum divisible by three.
    """
    # Initialize dp array to store the maximum sums with remainders 0, 1, and 2
    dp = [0, 0, 0]
    
    for num in nums:
        # Create a copy of the current dp array to avoid overwriting during iteration
        dp_copy = dp[:]
        for remainder in dp_copy:
            # Update the dp array for the current number
            dp[(remainder + num) % 3] = max(dp[(remainder + num) % 3], remainder + num)
    
    # Return the maximum sum divisible by 3 (remainder 0)
    return dp[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 6, 5, 1, 8]
    print(maxSumDivThree(nums1))  # Output: 18

    # Test Case 2
    nums2 = [4, 1, 5, 3, 1]
    print(maxSumDivThree(nums2))  # Output: 12

    # Test Case 3
    nums3 = [1, 2, 3, 4, 4]
    print(maxSumDivThree(nums3))  # Output: 12

    # Additional Test Case
    nums4 = [2, 2, 2, 2, 2]
    print(maxSumDivThree(nums4))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the input array `nums` once, and for each number, it updates the `dp` array (of fixed size 3).
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a fixed-size array `dp` of size 3 to store the maximum sums for remainders 0, 1, and 2.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""