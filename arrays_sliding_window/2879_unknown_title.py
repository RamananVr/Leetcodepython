"""
LeetCode Problem #2879: Maximum Beauty of an Array After Applying Operation

Problem Statement:
You are given an array `nums` consisting of positive integers and an integer `k`. You can apply the following operation on the array any number of times:

- Choose an index `i` in the array and replace `nums[i]` with any integer in the range `[nums[i] - k, nums[i] + k]`.

The beauty of the array is the length of the longest subsequence consisting of equal elements. Return the maximum possible beauty of the array after applying the operation any number of times.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= k <= 10^9
"""

# Solution
def maximumBeauty(nums, k):
    """
    Finds the maximum possible beauty of the array after applying the operation.

    :param nums: List[int] - The input array of positive integers.
    :param k: int - The range modifier for the operation.
    :return: int - The maximum possible beauty of the array.
    """
    # Sort the array to group numbers that can be made equal
    nums.sort()
    
    # Use a sliding window to find the longest subsequence of equal elements
    left = 0
    max_beauty = 0
    
    for right in range(len(nums)):
        # Check if the current window satisfies the condition
        while nums[right] - nums[left] > 2 * k:
            left += 1
        # Update the maximum beauty
        max_beauty = max(max_beauty, right - left + 1)
    
    return max_beauty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 6, 1, 2]
    k1 = 2
    print(maximumBeauty(nums1, k1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    k2 = 0
    print(maximumBeauty(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [10, 20, 30, 40]
    k3 = 5
    print(maximumBeauty(nums3, k3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 3, 5, 7, 9]
    k4 = 4
    print(maximumBeauty(nums4, k4))  # Expected Output: 5

    # Test Case 5
    nums5 = [1000000000, 999999999, 999999998]
    k5 = 1
    print(maximumBeauty(nums5, k5))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The sliding window traversal takes O(n), as each element is processed at most twice (once by the right pointer and once by the left pointer).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it operates directly on the input array and uses a few variables.
- Overall space complexity: O(1).

Topic: Arrays, Sliding Window
"""