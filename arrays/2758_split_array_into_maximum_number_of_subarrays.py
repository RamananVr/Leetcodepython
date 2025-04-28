"""
LeetCode Question #2758: Split Array Into Maximum Number of Subarrays

Problem Statement:
You are given an integer array `nums`. You want to split the array into the maximum number of subarrays such that:
1. Each subarray is non-empty.
2. The sum of the elements in each subarray is strictly less than a given integer `k`.

Return the maximum number of subarrays you can achieve.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^9
"""

def maxSubarrays(nums, k):
    """
    Function to split the array into the maximum number of subarrays
    such that the sum of each subarray is strictly less than k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The threshold value for subarray sums.
    :return: int - The maximum number of subarrays.
    """
    # Initialize variables
    current_sum = 0
    subarray_count = 0

    # Iterate through the array
    for num in nums:
        # If adding the current number exceeds k, start a new subarray
        if current_sum + num >= k:
            subarray_count += 1
            current_sum = 0  # Reset the sum for the new subarray
        current_sum += num

    # Count the last subarray if it exists
    if current_sum > 0:
        subarray_count += 1

    return subarray_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 5
    print(maxSubarrays(nums1, k1))  # Expected Output: 4

    # Test Case 2
    nums2 = [10, 20, 30, 40]
    k2 = 50
    print(maxSubarrays(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    k3 = 3
    print(maxSubarrays(nums3, k3))  # Expected Output: 2

    # Test Case 4
    nums4 = [100, 200, 300]
    k4 = 1000
    print(maxSubarrays(nums4, k4))  # Expected Output: 1

    # Test Case 5
    nums5 = [5, 5, 5, 5, 5]
    k5 = 10
    print(maxSubarrays(nums5, k5))  # Expected Output: 5


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity:
- The function uses a constant amount of extra space for variables (`current_sum` and `subarray_count`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""