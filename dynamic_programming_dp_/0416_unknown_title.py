"""
LeetCode Problem #416: Partition Equal Subset Sum

Problem Statement:
Given a non-empty array nums containing only positive integers, determine if the array can be partitioned into two subsets such that the sum of the elements in both subsets is equal.

Example 1:
Input: nums = [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
"""

def canPartition(nums):
    """
    Determines if the array can be partitioned into two subsets with equal sum.

    :param nums: List[int] - The input array of positive integers.
    :return: bool - True if the array can be partitioned, False otherwise.
    """
    total_sum = sum(nums)
    
    # If the total sum is odd, it's impossible to split into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Initialize a DP array where dp[i] means whether a subset sum of i is possible
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: A subset sum of 0 is always possible (empty subset)
    
    for num in nums:
        # Traverse dp array from right to left to avoid overwriting results
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 5, 11, 5]
    print(f"Input: {nums1} -> Output: {canPartition(nums1)}")  # Expected: True

    # Test Case 2
    nums2 = [1, 2, 3, 5]
    print(f"Input: {nums2} -> Output: {canPartition(nums2)}")  # Expected: False

    # Test Case 3
    nums3 = [2, 2, 3, 5]
    print(f"Input: {nums3} -> Output: {canPartition(nums3)}")  # Expected: False

    # Test Case 4
    nums4 = [1, 2, 5]
    print(f"Input: {nums4} -> Output: {canPartition(nums4)}")  # Expected: False

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Input: {nums5} -> Output: {canPartition(nums5)}")  # Expected: True

"""
Time Complexity:
- Let n be the number of elements in the array and S be the total sum of the array.
- The time complexity is O(n * S/2), where S/2 is the target subset sum. This is because we iterate over the array and for each element, we update the dp array of size S/2.

Space Complexity:
- The space complexity is O(S/2) because we use a 1D dp array of size S/2 to store whether a subset sum is possible.

Topic: Dynamic Programming (DP)
"""