"""
LeetCode Problem #2797: "Split Array into Maximum Number of Subarrays"

Problem Statement:
You are given an integer array `nums`. You want to split the array into the maximum number of non-empty subarrays such that:
1. Each subarray has a strictly increasing order of elements.
2. The concatenation of all subarrays in order results in the original array.

Return the maximum number of subarrays you can split `nums` into.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def maxSubarrays(nums):
    """
    Function to calculate the maximum number of subarrays that can be split
    from the given array such that each subarray is strictly increasing.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum number of subarrays.
    """
    # Initialize the count of subarrays
    subarray_count = 1

    # Iterate through the array to find points where the order is not strictly increasing
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            # Start a new subarray
            subarray_count += 1

    return subarray_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 2, 4, 5]
    print(maxSubarrays(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(maxSubarrays(nums2))  # Expected Output: 1

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(maxSubarrays(nums3))  # Expected Output: 5

    # Test Case 4
    nums4 = [1, 3, 2, 4, 6, 5, 7]
    print(maxSubarrays(nums4))  # Expected Output: 4

    # Test Case 5
    nums5 = [10]
    print(maxSubarrays(nums5))  # Expected Output: 1

"""
Time Complexity Analysis:
- The function iterates through the array once, performing a constant-time comparison at each step.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The function uses a constant amount of extra space (only a single integer variable for the count).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""