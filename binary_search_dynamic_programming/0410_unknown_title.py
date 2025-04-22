"""
LeetCode Problem #410: Split Array Largest Sum

Problem Statement:
Given an array `nums` which consists of non-negative integers and an integer `m`, you can split the array into `m` non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these `m` subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9
Explanation:
There are several ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
Explanation:
Each subarray will contain one element, and the largest sum is 4.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= m <= min(50, nums.length)
"""

# Solution
def splitArray(nums, m):
    """
    Function to minimize the largest sum among m subarrays.
    
    Args:
    nums (List[int]): The input array of non-negative integers.
    m (int): The number of subarrays to split into.
    
    Returns:
    int: The minimized largest sum among the m subarrays.
    """
    def can_split(max_sum):
        # Helper function to check if we can split the array into m subarrays
        # such that the largest sum of any subarray is <= max_sum.
        current_sum = 0
        splits = 1
        for num in nums:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
                if splits > m:
                    return False
            else:
                current_sum += num
        return True

    # Binary search for the minimum largest sum
    left, right = max(nums), sum(nums)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_split(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 2, 5, 10, 8]
    m1 = 2
    print(splitArray(nums1, m1))  # Output: 18

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    m2 = 2
    print(splitArray(nums2, m2))  # Output: 9

    # Test Case 3
    nums3 = [1, 4, 4]
    m3 = 3
    print(splitArray(nums3, m3))  # Output: 4

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m4 = 3
    print(splitArray(nums4, m4))  # Output: 17

    # Test Case 5
    nums5 = [2, 3, 1, 2, 4, 3]
    m5 = 3
    print(splitArray(nums5, m5))  # Output: 6

"""
Time Complexity:
- The binary search runs in O(log(sum(nums) - max(nums))).
- The `can_split` function iterates through the array, which takes O(n).
- Therefore, the overall time complexity is O(n * log(sum(nums) - max(nums))).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search, Dynamic Programming
"""