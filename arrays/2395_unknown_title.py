"""
LeetCode Problem #2395: Find Subarrays With Equal Sum

Problem Statement:
Given a 0-indexed integer array `nums`, determine if there exist two subarrays of length 2 with equal sum. 
Note that the two subarrays must begin at different indices.

Return `true` if such subarrays exist, otherwise return `false`.

Example 1:
Input: nums = [4, 2, 4]
Output: true
Explanation: The subarrays [4, 2] and [2, 4] have the same sum of 6.

Example 2:
Input: nums = [1, 2, 3, 4, 5]
Output: false
Explanation: No two subarrays of length 2 have the same sum.

Example 3:
Input: nums = [0, 0, 0]
Output: true
Explanation: The subarrays [0, 0] and [0, 0] have the same sum of 0.

Constraints:
- 2 <= nums.length <= 100
- -10^9 <= nums[i] <= 10^9
"""

def findSubarrays(nums):
    """
    Determines if there exist two subarrays of length 2 with equal sum.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if such subarrays exist, otherwise False.
    """
    seen_sums = set()
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 4]
    print(findSubarrays(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(findSubarrays(nums2))  # Output: False

    # Test Case 3
    nums3 = [0, 0, 0]
    print(findSubarrays(nums3))  # Output: True

    # Additional Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    print(findSubarrays(nums4))  # Output: False

    # Additional Test Case 5
    nums5 = [1, 1, 1, 1]
    print(findSubarrays(nums5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, calculating the sum of adjacent elements.
- This results in a time complexity of O(n), where n is the length of the input array.

Space Complexity:
- A set is used to store the sums of subarrays of length 2. In the worst case, the set could contain up to n-1 elements.
- This results in a space complexity of O(n).

Topic: Arrays
"""