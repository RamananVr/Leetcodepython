"""
LeetCode Problem #908: Smallest Range I

Problem Statement:
You are given an integer array nums and an integer k.

In one operation, you can choose any element of nums and subtract or add k to it. 
For example, if nums = [1,2,3] and k = 1, you can change 2 to 1 or 3.

The smallest range of nums after performing the above operation any number of times is the difference 
between the maximum and minimum elements in nums.

Return the smallest range that can be achieved.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^4
- 0 <= k <= 10^4
"""

# Solution
def smallestRangeI(nums, k):
    """
    Calculate the smallest range after modifying the array with +/- k operations.

    :param nums: List[int] - The input array of integers.
    :param k: int - The maximum value to add or subtract from each element.
    :return: int - The smallest range achievable.
    """
    max_num = max(nums)
    min_num = min(nums)
    return max(0, max_num - min_num - 2 * k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 6]
    k1 = 3
    print(smallestRangeI(nums1, k1))  # Expected Output: 0

    # Test Case 2
    nums2 = [0, 10]
    k2 = 2
    print(smallestRangeI(nums2, k2))  # Expected Output: 6

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    k3 = 1
    print(smallestRangeI(nums3, k3))  # Expected Output: 2

    # Test Case 4
    nums4 = [5, 5, 5]
    k4 = 10
    print(smallestRangeI(nums4, k4))  # Expected Output: 0

    # Test Case 5
    nums5 = [1]
    k5 = 0
    print(smallestRangeI(nums5, k5))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the maximum and minimum of the array takes O(n), where n is the length of nums.
- The rest of the operations are O(1).
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables like max_num and min_num.
- Overall space complexity: O(1).
"""

# Topic: Arrays