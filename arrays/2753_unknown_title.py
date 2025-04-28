"""
LeetCode Problem #2753: Check if Array Is Sorted and Rotated

Problem Statement:
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return `false`.

A sorted array is defined as an array that is in non-decreasing order. A rotation means taking 
an array and moving some number of elements from the front to the back. For example, 
rotating `[3, 4, 5, 1, 2]` results in `[1, 2, 3, 4, 5]`.

Note:
- An array `nums` is considered sorted and rotated if there exists some pivot index `k` such that:
  - The array can be split into two subarrays: `nums[0:k]` and `nums[k:]`.
  - The subarray `nums[k:]` is followed by the subarray `nums[0:k]`.
  - Both subarrays are individually sorted in non-decreasing order.

Constraints:
- `1 <= nums.length <= 100`
- `-10^3 <= nums[i] <= 10^3`

Example 1:
Input: nums = [3, 4, 5, 1, 2]
Output: true
Explanation: The array is sorted and rotated. The original sorted array is [1, 2, 3, 4, 5].

Example 2:
Input: nums = [2, 1, 3, 4]
Output: false
Explanation: The array is not sorted and rotated.

Example 3:
Input: nums = [1, 2, 3]
Output: true
Explanation: The array is sorted and rotated (with zero rotations).

"""

def check(nums):
    """
    Function to check if the array is sorted and rotated.

    Args:
    nums (List[int]): The input array.

    Returns:
    bool: True if the array is sorted and rotated, False otherwise.
    """
    n = len(nums)
    count_breaks = 0

    for i in range(n):
        # Check if the current element is greater than the next element
        if nums[i] > nums[(i + 1) % n]:
            count_breaks += 1

        # If there is more than one break, the array is not sorted and rotated
        if count_breaks > 1:
            return False

    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 5, 1, 2]
    print(check(nums1))  # Output: True

    # Test Case 2
    nums2 = [2, 1, 3, 4]
    print(check(nums2))  # Output: False

    # Test Case 3
    nums3 = [1, 2, 3]
    print(check(nums3))  # Output: True

    # Test Case 4
    nums4 = [1]
    print(check(nums4))  # Output: True

    # Test Case 5
    nums5 = [2, 3, 4, 5, 1]
    print(check(nums5))  # Output: True

    # Test Case 6
    nums6 = [5, 1, 2, 3, 4]
    print(check(nums6))  # Output: True

    # Test Case 7
    nums7 = [3, 2, 1]
    print(check(nums7))  # Output: False


"""
Time Complexity Analysis:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The function uses a constant amount of extra space (for variables like `count_breaks`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""