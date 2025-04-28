"""
LeetCode Problem #2488: Count Subarrays With Median K

Problem Statement:
You are given an array `nums` of size `n` consisting of distinct integers from `1` to `n` and a positive integer `k`.

A subarray is a contiguous part of an array.

A subarray is said to have a median equal to `k` if the following conditions are met:
1. It is of odd length.
2. The median of the subarray is equal to `k`.

Note:
- The median of an array is the middle element after sorting the array in ascending order. 
  - For example, the median of `[2,3,1]` is `2`, and the median of `[8,4,3,5,1]` is `4`.

Return the number of subarrays that have a median equal to `k`.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i], k <= n`
- The integers in `nums` are distinct.

"""

def countSubarrays(nums, k):
    """
    Function to count the number of subarrays with median equal to k.
    """
    # Find the index of k in the array
    k_index = nums.index(k)
    
    # Initialize a dictionary to store prefix sums
    prefix_count = {0: 1}
    balance = 0
    result = 0

    # Traverse the array
    for i, num in enumerate(nums):
        # Update the balance based on the current number
        if num > k:
            balance += 1
        elif num < k:
            balance -= 1

        # If we are at or past the index of k
        if i >= k_index:
            # Check for subarrays with odd length
            result += prefix_count.get(balance, 0)
            result += prefix_count.get(balance - 1, 0)
        
        # Update the prefix count
        if i < k_index:
            prefix_count[balance] = prefix_count.get(balance, 0) + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 1, 4, 5]
    k1 = 4
    print(countSubarrays(nums1, k1))  # Output: 3

    # Test Case 2
    nums2 = [2, 3, 1]
    k2 = 3
    print(countSubarrays(nums2, k2))  # Output: 1

    # Test Case 3
    nums3 = [1, 4, 3, 2, 5]
    k3 = 3
    print(countSubarrays(nums3, k3))  # Output: 4

    # Test Case 4
    nums4 = [5, 1, 3, 2, 4]
    k4 = 2
    print(countSubarrays(nums4, k4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once, making it O(n), where n is the length of the array.
- Dictionary operations (get and update) are O(1) on average.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(n) in the worst case due to the prefix_count dictionary, which can store up to n keys.

Topic: Arrays, Prefix Sum, Hash Map
"""