"""
LeetCode Problem #334: Increasing Triplet Subsequence

Problem Statement:
Given an integer array `nums`, return true if there exists a triple of indices (i, j, k) such that 
i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No such triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (2, 4, 6) satisfies the conditions.

Constraints:
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1

Follow up:
Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

def increasingTriplet(nums):
    """
    Determines if there exists a triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

    :param nums: List[int] - The input array of integers.
    :return: bool - True if such a triplet exists, otherwise False.
    """
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num  # Update the smallest number
        elif num <= second:
            second = num  # Update the second smallest number
        else:
            # If we find a number greater than both `first` and `second`, we have a triplet
            return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Increasing sequence
    nums1 = [1, 2, 3, 4, 5]
    print(increasingTriplet(nums1))  # Expected Output: True

    # Test Case 2: Decreasing sequence
    nums2 = [5, 4, 3, 2, 1]
    print(increasingTriplet(nums2))  # Expected Output: False

    # Test Case 3: Mixed sequence with a valid triplet
    nums3 = [2, 1, 5, 0, 4, 6]
    print(increasingTriplet(nums3))  # Expected Output: True

    # Test Case 4: Short array (no triplet possible)
    nums4 = [1, 2]
    print(increasingTriplet(nums4))  # Expected Output: False

    # Test Case 5: Array with duplicates
    nums5 = [1, 1, 1, 1, 1]
    print(increasingTriplet(nums5))  # Expected Output: False

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses only two variables (`first` and `second`) to track the smallest and second smallest numbers.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""