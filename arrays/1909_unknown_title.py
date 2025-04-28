"""
LeetCode Problem #1909: Remove One Element to Make the Array Strictly Increasing

Problem Statement:
Given a 0-indexed integer array `nums`, return `true` if it can be made strictly increasing 
after removing exactly one element, or `false` otherwise. If the array is already strictly 
increasing, return `true`.

The array `nums` is strictly increasing if `nums[i - 1] < nums[i]` for every index `i` 
(1 <= i < nums.length).

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def canBeIncreasing(nums):
    """
    Determines if the array can be made strictly increasing by removing one element.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if the array can be made strictly increasing, False otherwise.
    """
    def is_strictly_increasing(arr):
        """Helper function to check if an array is strictly increasing."""
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                return False
        return True

    for i in range(len(nums)):
        # Create a new array by removing the element at index i
        new_nums = nums[:i] + nums[i+1:]
        if is_strictly_increasing(new_nums):
            return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Removing 1 makes the array strictly increasing
    nums1 = [1, 2, 10, 5, 7]
    print(canBeIncreasing(nums1))  # Expected Output: True

    # Test Case 2: Array is already strictly increasing
    nums2 = [1, 2, 3, 4]
    print(canBeIncreasing(nums2))  # Expected Output: True

    # Test Case 3: Removing any single element cannot make the array strictly increasing
    nums3 = [2, 3, 1, 2]
    print(canBeIncreasing(nums3))  # Expected Output: False

    # Test Case 4: Removing the last element makes the array strictly increasing
    nums4 = [1, 2, 3, 2]
    print(canBeIncreasing(nums4))  # Expected Output: True

    # Test Case 5: Removing the first element makes the array strictly increasing
    nums5 = [5, 1, 2, 3]
    print(canBeIncreasing(nums5))  # Expected Output: True

"""
Time Complexity Analysis:
- The outer loop iterates over the array `nums` of size `n`, so it runs `O(n)` times.
- For each iteration, the helper function `is_strictly_increasing` is called, which checks 
  the array in `O(n)` time.
- Therefore, the overall time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n) due to the creation of a new array `new_nums` in each iteration.

Topic: Arrays
"""