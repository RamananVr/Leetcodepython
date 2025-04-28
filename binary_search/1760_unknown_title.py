"""
LeetCode Problem #1760: Minimum Limit of Balls in a Bag

Problem Statement:
You are given an integer array `nums` where the `i-th` bag contains `nums[i]` balls. 
You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:
- Take any bag of balls and divide it into two new bags, with a positive number of balls in each. 
  For example, if you have a bag of 5 balls, you can divide it into two new bags of size 1 and 4, 
  or size 2 and 3.

Your goal is to minimize the maximum number of balls in a bag. Return the minimum possible value 
of the maximum number of balls in a bag after performing the operations.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= maxOperations <= 10^9
- 1 <= nums[i] <= 10^9
"""

# Solution
def minimumSize(nums, maxOperations):
    def canDivide(mid):
        # Check if we can make all bags <= mid with maxOperations
        operations = 0
        for num in nums:
            if num > mid:
                operations += (num - 1) // mid
        return operations <= maxOperations

    # Binary search for the minimum possible maximum size
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if canDivide(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [9]
    maxOperations1 = 2
    print(minimumSize(nums1, maxOperations1))  # Output: 3

    # Test Case 2
    nums2 = [2, 4, 8, 2]
    maxOperations2 = 4
    print(minimumSize(nums2, maxOperations2))  # Output: 2

    # Test Case 3
    nums3 = [7, 17]
    maxOperations3 = 2
    print(minimumSize(nums3, maxOperations3))  # Output: 7

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    maxOperations4 = 0
    print(minimumSize(nums4, maxOperations4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max(nums))) iterations, where max(nums) is the largest number in the array.
- For each iteration, we check if we can divide the bags using the `canDivide` function, which takes O(n) time, 
  where n is the length of the array `nums`.
- Therefore, the overall time complexity is O(n * log(max(nums))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""