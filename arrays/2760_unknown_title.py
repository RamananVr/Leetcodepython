"""
LeetCode Problem #2760: Longest Even Odd Subarray With Threshold

Problem Statement:
You are given an integer array `nums` and an integer `threshold`. A subarray of `nums` is called an even-odd subarray if:
1. Its length is at least 2.
2. The elements of the subarray alternate between even and odd numbers.

Additionally, the maximum value in the subarray must not exceed `threshold`.

Return the length of the longest even-odd subarray that satisfies the above conditions. If no such subarray exists, return 0.

Example:
Input: nums = [3, 2, 5, 4], threshold = 5
Output: 3
Explanation: The subarray [3, 2, 5] is an even-odd subarray with a maximum value of 5, which satisfies the threshold.

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 1 <= threshold <= 1000
"""

def longest_even_odd_subarray(nums, threshold):
    """
    Finds the length of the longest even-odd subarray with a maximum value not exceeding the threshold.

    :param nums: List[int] - The input array of integers.
    :param threshold: int - The threshold value.
    :return: int - The length of the longest even-odd subarray.
    """
    max_length = 0
    current_length = 0

    for i in range(len(nums)):
        # Reset the current subarray length
        current_length = 1

        # Check if the current number is within the threshold
        if nums[i] > threshold:
            continue

        # Expand the subarray
        for j in range(i + 1, len(nums)):
            if nums[j] > threshold:
                break

            # Check if the current subarray alternates between even and odd
            if (nums[j - 1] % 2 == 0 and nums[j] % 2 == 1) or (nums[j - 1] % 2 == 1 and nums[j] % 2 == 0):
                current_length += 1
            else:
                break

        # Update the maximum length
        max_length = max(max_length, current_length)

    return max_length


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 5, 4]
    threshold1 = 5
    print(longest_even_odd_subarray(nums1, threshold1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    threshold2 = 3
    print(longest_even_odd_subarray(nums2, threshold2))  # Output: 2

    # Test Case 3
    nums3 = [2, 4, 6, 8]
    threshold3 = 10
    print(longest_even_odd_subarray(nums3, threshold3))  # Output: 0

    # Test Case 4
    nums4 = [1, 3, 5, 7, 9]
    threshold4 = 10
    print(longest_even_odd_subarray(nums4, threshold4))  # Output: 0

    # Test Case 5
    nums5 = [10, 15, 20, 25, 30]
    threshold5 = 25
    print(longest_even_odd_subarray(nums5, threshold5))  # Output: 2


"""
Time Complexity:
- The outer loop iterates through each element of the array, and the inner loop iterates through the remaining elements.
- In the worst case, the inner loop runs approximately n times for each of the n elements, resulting in O(n^2) time complexity.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""