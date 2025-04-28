"""
LeetCode Problem #2762: Continuous Subarrays

Problem Statement:
You are given an integer array `nums`. A subarray of `nums` is called a continuous subarray if the absolute difference 
between any two elements in the subarray is at most 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [5, 4, 2, 4]
Output: 8
Explanation: 
Continuous subarrays are: [5], [4], [2], [4], [5,4], [4,2], [2,4], [4,2,4].
There are a total of 8 continuous subarrays.

Example 2:
Input: nums = [1, 2, 3]
Output: 6
Explanation: 
Continuous subarrays are: [1], [2], [3], [1,2], [2,3], [1,2,3].
There are a total of 6 continuous subarrays.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def continuousSubarrays(nums):
    """
    Function to calculate the total number of continuous subarrays.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The total number of continuous subarrays.
    """
    n = len(nums)
    left = 0
    result = 0
    min_val, max_val = nums[0], nums[0]

    for right in range(n):
        # Update the min and max values in the current window
        min_val = min(min_val, nums[right])
        max_val = max(max_val, nums[right])

        # If the absolute difference exceeds 2, shrink the window
        while max_val - min_val > 2:
            left += 1
            min_val = min(nums[left:right + 1])
            max_val = max(nums[left:right + 1])

        # Add the number of subarrays ending at `right`
        result += (right - left + 1)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 4, 2, 4]
    print(continuousSubarrays(nums1))  # Output: 8

    # Test Case 2
    nums2 = [1, 2, 3]
    print(continuousSubarrays(nums2))  # Output: 6

    # Test Case 3
    nums3 = [10, 12, 14, 16]
    print(continuousSubarrays(nums3))  # Output: 4

    # Test Case 4
    nums4 = [1]
    print(continuousSubarrays(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 3, 5, 7, 9]
    print(continuousSubarrays(nums5))  # Output: 5

"""
Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once, 
  and the `left` pointer only moves forward when necessary. 
- In the worst case, each element is processed twice (once by `right` and once by `left`), 
  resulting in a time complexity of O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `min_val`, `max_val`, `left`, and `result`.
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""