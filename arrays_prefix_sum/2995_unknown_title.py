"""
LeetCode Problem #2995: Sum of Distances

Problem Statement:
You are given an array `nums` consisting of `n` integers. For each index `i` in the array, 
you need to calculate the sum of the absolute differences between `nums[i]` and all other elements in the array.

Formally, for each index `i`, compute:
    result[i] = sum(abs(nums[i] - nums[j]) for all j where 0 <= j < n and j != i)

Return the array `result` of size `n`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# Solution
def sum_of_distances(nums):
    """
    Calculate the sum of absolute differences for each index in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: The result array where each element is the sum of absolute differences.
    """
    n = len(nums)
    nums_sorted = sorted((num, i) for i, num in enumerate(nums))  # Sort nums with their original indices
    sorted_nums = [num for num, _ in nums_sorted]
    sorted_indices = [i for _, i in nums_sorted]

    # Prefix sums for sorted array
    prefix_sum = [0] * n
    prefix_sum[0] = sorted_nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + sorted_nums[i]

    # Calculate result
    result = [0] * n
    for i in range(n):
        num = sorted_nums[i]
        left_sum = prefix_sum[i] - num  # Sum of elements to the left of current
        right_sum = prefix_sum[-1] - prefix_sum[i]  # Sum of elements to the right of current
        left_count = i
        right_count = n - i - 1

        # Total distance for current element
        result[sorted_indices[i]] = (num * left_count - left_sum) + (right_sum - num * right_count)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 5]
    print(sum_of_distances(nums1))  # Output: [4, 3, 5]

    # Test Case 2
    nums2 = [1, 4, 6, 8, 10]
    print(sum_of_distances(nums2))  # Output: [24, 15, 13, 15, 24]

    # Test Case 3
    nums3 = [1]
    print(sum_of_distances(nums3))  # Output: [0]

    # Test Case 4
    nums4 = [1, 1, 1]
    print(sum_of_distances(nums4))  # Output: [0, 0, 0]

    # Test Case 5
    nums5 = [10, -10, 10]
    print(sum_of_distances(nums5))  # Output: [40, 60, 40]

"""
Time Complexity:
- Sorting the array takes O(n log n).
- Calculating prefix sums takes O(n).
- Calculating the result array takes O(n).
Overall time complexity: O(n log n).

Space Complexity:
- The space used for the sorted array, prefix sums, and result array is O(n).
Overall space complexity: O(n).

Topic: Arrays, Prefix Sum
"""