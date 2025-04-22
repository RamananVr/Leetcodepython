"""
LeetCode Problem #312: Burst Balloons

Problem Statement:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons. If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,1,8] --> [3,8] --> [8] --> []
coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15 + 120 + 24 + 8 = 167

Example 2:
Input: nums = [1,5]
Output: 10

Constraints:
- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100
"""

# Clean and Correct Python Solution
def maxCoins(nums):
    # Add virtual balloons with value 1 at both ends
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Create a DP table
    dp = [[0] * n for _ in range(n)]
    
    # Iterate over the length of the subarray
    for length in range(2, n):  # length is the distance between left and right
        for left in range(0, n - length):  # left boundary of the subarray
            right = left + length  # right boundary of the subarray
            # Iterate over all possible balloons to burst last in the subarray
            for i in range(left + 1, right):
                # Calculate coins if balloon i is the last to burst
                coins = nums[left] * nums[i] * nums[right]
                # Add coins from previously solved subproblems
                coins += dp[left][i] + dp[i][right]
                # Update the DP table
                dp[left][right] = max(dp[left][right], coins)
    
    # The result is stored in dp[0][n-1], which considers the entire range
    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 5, 8]
    print("Test Case 1 Output:", maxCoins(nums1))  # Expected Output: 167

    # Test Case 2
    nums2 = [1, 5]
    print("Test Case 2 Output:", maxCoins(nums2))  # Expected Output: 10

    # Test Case 3
    nums3 = [7, 9, 8, 0, 7]
    print("Test Case 3 Output:", maxCoins(nums3))  # Expected Output: 1654

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print("Test Case 4 Output:", maxCoins(nums4))  # Expected Output: 110

    # Test Case 5
    nums5 = [8]
    print("Test Case 5 Output:", maxCoins(nums5))  # Expected Output: 8

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DP table has dimensions n x n, where n is the length of nums after adding the virtual balloons (n = original length + 2).
- For each subarray (left, right), we iterate over all possible balloons to burst last, which takes O(n) time.
- Thus, the total time complexity is O(n^3).

Space Complexity:
- The space complexity is O(n^2) due to the DP table.
- The additional space used for variables is negligible compared to the DP table.
"""

# Topic: Dynamic Programming