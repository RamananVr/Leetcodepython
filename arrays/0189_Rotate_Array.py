"""
LeetCode Problem #189: Rotate Array

Problem Statement:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem. Could you do it in-place with O(1) extra space?
"""

# Clean, Correct Python Solution
def rotate(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps in-place.

    Args:
    nums (List[int]): The input array to rotate.
    k (int): The number of steps to rotate the array.

    Returns:
    None: The function modifies the input array in-place.
    """
    n = len(nums)
    k %= n  # Handle cases where k >= n

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate(nums1, k1)
    print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(nums2, k2)
    print(nums2)  # Output: [3, 99, -1, -100]

    # Test Case 3
    nums3 = [1, 2]
    k3 = 3
    rotate(nums3, k3)
    print(nums3)  # Output: [2, 1]

    # Test Case 4
    nums4 = [1]
    k4 = 10
    rotate(nums4, k4)
    print(nums4)  # Output: [1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `reverse` function is called three times, and each call takes O(n) time to reverse a portion of the array.
- Therefore, the overall time complexity is O(n), where n is the length of the array.

Space Complexity:
- The solution uses O(1) extra space since the rotation is performed in-place without using any additional data structures.

Topic: Arrays
"""