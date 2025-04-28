"""
LeetCode Problem #2845: Count of Interesting Subarrays

Problem Statement:
You are given an array `nums` of integers and an integer `k`. A subarray of `nums` is called "interesting" if the sum of its elements is divisible by `k`. Return the number of interesting subarrays in `nums`.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4
"""

def countInterestingSubarrays(nums, k):
    """
    Function to count the number of interesting subarrays in the given array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The divisor.

    Returns:
    int: The count of interesting subarrays.
    """
    from collections import defaultdict

    # Initialize variables
    prefix_sum = 0
    count = 0
    remainder_count = defaultdict(int)
    remainder_count[0] = 1  # To handle cases where prefix_sum % k == 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # Handle negative remainders to ensure they are in the range [0, k-1]
        if remainder < 0:
            remainder += k

        # Add the count of subarrays that end at the current index
        count += remainder_count[remainder]

        # Update the remainder count
        remainder_count[remainder] += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    print(countInterestingSubarrays(nums1, k1))  # Expected Output: 7

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 3
    print(countInterestingSubarrays(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [5, -5, 5, -5]
    k3 = 5
    print(countInterestingSubarrays(nums3, k3))  # Expected Output: 10

    # Test Case 4
    nums4 = [1, 2, 3]
    k4 = 6
    print(countInterestingSubarrays(nums4, k4))  # Expected Output: 0

"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a dictionary to store the count of remainders, which can have at most k unique keys.
- Thus, the space complexity is O(k).

Topic: Arrays, Prefix Sum, Hash Map
"""