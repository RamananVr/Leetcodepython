"""
LeetCode Problem #15: 3Sum

Problem Statement:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i`, `j`, and `k` are distinct indices.
- `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[0] + nums[4] + nums[5] = (-1) + (-1) + 2 = 0.
The distinct triplets are [-1, 0, 1] and [-1, -1, 2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0, 1, 1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
"""

def threeSum(nums):
    """
    Finds all unique triplets in the array that sum up to zero.

    :param nums: List[int] - The input array of integers.
    :return: List[List[int]] - A list of unique triplets that sum to zero.
    """
    nums.sort()  # Sort the array to make it easier to avoid duplicates
    result = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers to find the other two numbers
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate values for the second and third numbers
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Input:", nums1)
    print("Output:", threeSum(nums1))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

    # Test Case 2
    nums2 = [0, 1, 1]
    print("Input:", nums2)
    print("Output:", threeSum(nums2))  # Expected: []

    # Test Case 3
    nums3 = [0, 0, 0]
    print("Input:", nums3)
    print("Output:", threeSum(nums3))  # Expected: [[0, 0, 0]]

    # Test Case 4
    nums4 = [-2, 0, 1, 1, 2]
    print("Input:", nums4)
    print("Output:", threeSum(nums4))  # Expected: [[-2, 0, 2], [-2, 1, 1]]

    # Test Case 5
    nums5 = []
    print("Input:", nums5)
    print("Output:", threeSum(nums5))  # Expected: []

# Topic: Arrays