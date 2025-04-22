"""
LeetCode Problem #611: Valid Triangle Number

Problem Statement:
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

A triangle is valid if the sum of any two sides is greater than the third side.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
- (2, 3, 4) using the first 2.
- (2, 3, 4) using the second 2.
- (2, 2, 3)

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

# Solution
def triangleNumber(nums):
    """
    Function to count the number of valid triangles that can be formed
    from the given array of integers.

    :param nums: List[int] - Array of integers representing side lengths
    :return: int - Number of valid triangles
    """
    nums.sort()  # Sort the array to simplify the triangle inequality check
    n = len(nums)
    count = 0

    # Iterate through the array, treating nums[k] as the largest side
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            # Check if nums[i] + nums[j] > nums[k]
            if nums[i] + nums[j] > nums[k]:
                # If true, all pairs (i, j), (i, j-1), ..., (i, i+1) are valid
                count += j - i
                j -= 1
            else:
                i += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 3, 4]
    print(triangleNumber(nums1))  # Output: 3

    # Test Case 2
    nums2 = [4, 2, 3, 4]
    print(triangleNumber(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(triangleNumber(nums3))  # Output: 4

    # Test Case 4
    nums4 = [0, 0, 0]
    print(triangleNumber(nums4))  # Output: 0

    # Test Case 5
    nums5 = [5, 10, 15, 20]
    print(triangleNumber(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- The main loop iterates through the array, and for each k, the two-pointer approach runs in O(n).
- Overall complexity: O(n^2).

Space Complexity:
- The algorithm uses O(1) additional space, as it operates directly on the sorted array.
- Overall complexity: O(1).
"""

# Topic: Arrays, Two Pointers