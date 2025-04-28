"""
LeetCode Problem #740: Delete and Earn

Problem Statement:
You are given an integer array `nums`. You want to maximize the number of points you get by performing the following operation any number of times:

- Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterward, you must delete every element equal to `nums[i] - 1` and every element equal to `nums[i] + 1`.

You start with 0 points. Return the maximum number of points you can earn by applying the above operation.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
- Delete 4 to earn 4 points, resulting in nums = [3, 2].
- Delete 2 to earn 2 points, resulting in nums = [3].
- There are no more elements to delete.
- Total points earned = 6.

Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
- Delete 3 to earn 3 points, resulting in nums = [2, 2, 4].
- Delete 4 to earn 4 points, resulting in nums = [2, 2].
- Delete 2 to earn 2 points, resulting in an empty array.
- Total points earned = 9.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^4
"""

# Solution
def deleteAndEarn(nums):
    """
    Function to calculate the maximum points that can be earned by deleting elements from the array.
    
    :param nums: List[int] - Input array of integers
    :return: int - Maximum points that can be earned
    """
    if not nums:
        return 0

    # Create a frequency map to calculate the total points for each number
    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num

    # Use dynamic programming to solve the problem (similar to "House Robber" problem)
    dp = [0] * (max_num + 1)
    dp[0] = points[0]
    dp[1] = max(points[0], points[1])

    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

    return dp[max_num]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 2]
    print(deleteAndEarn(nums1))  # Output: 6

    # Test Case 2
    nums2 = [2, 2, 3, 3, 3, 4]
    print(deleteAndEarn(nums2))  # Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 2, 2, 3]
    print(deleteAndEarn(nums3))  # Output: 6

    # Test Case 4
    nums4 = [10, 10, 10, 11, 12]
    print(deleteAndEarn(nums4))  # Output: 30

    # Test Case 5
    nums5 = [1]
    print(deleteAndEarn(nums5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `points` array takes O(n), where n is the length of the input array `nums`.
- The dynamic programming step iterates through the `points` array, which has a size of max(nums). This takes O(max(nums)).
- Overall time complexity: O(n + max(nums)).

Space Complexity:
- The `points` array and `dp` array both have a size of max(nums) + 1.
- Overall space complexity: O(max(nums)).
"""

# Topic: Dynamic Programming