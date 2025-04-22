"""
LeetCode Problem #713: Subarray Product Less Than K

Problem Statement:
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

Constraints:
1. 1 <= nums.length <= 3 * 10^4
2. 1 <= nums[i] <= 1000
3. 0 <= k <= 10^6
"""

def numSubarrayProductLessThanK(nums, k):
    """
    Function to calculate the number of contiguous subarrays where the product of all elements is less than k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The threshold for the product.

    Returns:
    int: The count of subarrays with product less than k.
    """
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 5, 2, 6]
    k1 = 100
    print(numSubarrayProductLessThanK(nums1, k1))  # Expected Output: 8

    # Test Case 2
    nums2 = [1, 2, 3]
    k2 = 0
    print(numSubarrayProductLessThanK(nums2, k2))  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 1, 1]
    k3 = 2
    print(numSubarrayProductLessThanK(nums3, k3))  # Expected Output: 6

    # Test Case 4
    nums4 = [10, 5, 2, 6]
    k4 = 10
    print(numSubarrayProductLessThanK(nums4, k4))  # Expected Output: 3

"""
Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once.
- The `left` pointer also moves forward, but each element is processed at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays, Sliding Window
"""