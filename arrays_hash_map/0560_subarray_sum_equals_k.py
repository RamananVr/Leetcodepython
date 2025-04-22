"""
LeetCode Question #560: Subarray Sum Equals K

Problem Statement:
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10^7 <= nums[i] <= 10^7
- -10^7 <= k <= 10^7
"""

# Solution
def subarraySum(nums, k):
    """
    Function to find the total number of continuous subarrays whose sum equals k.

    Args:
    nums (List[int]): List of integers.
    k (int): Target sum.

    Returns:
    int: Total number of subarrays whose sum equals k.
    """
    count = 0
    prefix_sum = 0
    prefix_sum_map = {0: 1}  # Dictionary to store prefix sums and their frequencies

    for num in nums:
        prefix_sum += num
        # Check if (prefix_sum - k) exists in the map
        if prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[prefix_sum - k]
        # Update the prefix_sum_map
        prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1]
    k1 = 2
    print(subarraySum(nums1, k1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3]
    k2 = 3
    print(subarraySum(nums2, k2))  # Output: 2

    # Test Case 3
    nums3 = [1, -1, 1, -1, 1]
    k3 = 0
    print(subarraySum(nums3, k3))  # Output: 5

    # Test Case 4
    nums4 = [3, 4, 7, 2, -3, 1, 4, 2]
    k4 = 7
    print(subarraySum(nums4, k4))  # Output: 4

    # Test Case 5
    nums5 = [1]
    k5 = 1
    print(subarraySum(nums5, k5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The space complexity is O(n) in the worst case, as we store prefix sums in the dictionary.
- In the best case, the dictionary size is smaller, but the worst-case space complexity is O(n).

Topic: Arrays, Hash Map
"""