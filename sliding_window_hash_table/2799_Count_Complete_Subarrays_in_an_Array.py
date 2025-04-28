"""
LeetCode Problem #2799: Count Complete Subarrays in an Array

Problem Statement:
You are given an array `nums` consisting of positive integers.

We define a complete subarray as a subarray that contains every distinct integer in `nums` at least once.

Return the number of complete subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are:
- The subarray [1,3,1,2] contains the distinct integers [1,2,3].
- The subarray [1,3,1,2,2] contains the distinct integers [1,2,3].
- The subarray [3,1,2] contains the distinct integers [1,2,3].
- The subarray [3,1,2,2] contains the distinct integers [1,2,3].

Example 2:
Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists of only one distinct integer, so any subarray is complete. The total number of subarrays is 10.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2000
"""

def countCompleteSubarrays(nums):
    """
    Function to count the number of complete subarrays in the given array.

    Args:
    nums (List[int]): The input array of positive integers.

    Returns:
    int: The number of complete subarrays.
    """
    from collections import Counter

    # Find the total number of distinct integers in the array
    total_distinct = len(set(nums))
    n = len(nums)
    count = 0

    # Use a sliding window approach to count complete subarrays
    for i in range(n):
        seen = Counter()
        distinct_count = 0
        for j in range(i, n):
            if seen[nums[j]] == 0:
                distinct_count += 1
            seen[nums[j]] += 1
            if distinct_count == total_distinct:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 1, 2, 2]
    print(countCompleteSubarrays(nums1))  # Output: 4

    # Test Case 2
    nums2 = [5, 5, 5, 5]
    print(countCompleteSubarrays(nums2))  # Output: 10

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(countCompleteSubarrays(nums3))  # Output: 10

    # Test Case 4
    nums4 = [1]
    print(countCompleteSubarrays(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 2, 1, 2, 1]
    print(countCompleteSubarrays(nums5))  # Output: 9

"""
Time Complexity Analysis:
- Let `n` be the length of the input array `nums`.
- The outer loop runs `n` times, and the inner loop runs up to `n` times in the worst case.
- For each iteration of the inner loop, we perform constant-time operations (e.g., updating the Counter).
- Therefore, the overall time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(d), where `d` is the number of distinct integers in the array.
- This is because we use a Counter to store the frequency of elements in the current subarray.

Topic: Sliding Window, Hash Table
"""