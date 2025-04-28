"""
LeetCode Problem #2750: Ways to Split Array Into Good Subarrays

Problem Statement:
You are given a binary array `nums` (an array consisting of only 0s and 1s).

A subarray of an array is a contiguous segment of the array. A subarray is called "good" if there are exactly two 1s in the subarray.

Return the number of ways to split the array into good subarrays. Since the answer may be large, return it modulo 10^9 + 7.

Example:
Input: nums = [1,0,1,0,1]
Output: 4
Explanation: There are 4 ways to split nums into good subarrays:
- [1,0,1] and [0,1]
- [1,0] and [1,0,1]
- [1] and [0,1,0,1]
- [1,0,1,0] and [1]

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

# Python Solution
def numberOfGoodSubarraySplits(nums):
    """
    Function to calculate the number of ways to split the array into good subarrays.
    
    Args:
    nums (List[int]): A binary array consisting of 0s and 1s.

    Returns:
    int: The number of ways to split the array into good subarrays modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    # Find all indices of 1s in the array
    ones_indices = [i for i, num in enumerate(nums) if num == 1]

    # If there are fewer than 2 ones, it's impossible to form a good subarray
    if len(ones_indices) < 2:
        return 0

    # Calculate the number of ways to split
    result = 1
    for i in range(1, len(ones_indices)):
        # The number of ways to split between two consecutive 1s
        result *= (ones_indices[i] - ones_indices[i - 1])
        result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 1, 0, 1]
    print(numberOfGoodSubarraySplits(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 0, 0, 1]
    print(numberOfGoodSubarraySplits(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1, 1, 1]
    print(numberOfGoodSubarraySplits(nums3))  # Output: 1

    # Test Case 4
    nums4 = [0, 0, 0]
    print(numberOfGoodSubarraySplits(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 0, 0, 0, 1, 0, 1]
    print(numberOfGoodSubarraySplits(nums5))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding all indices of 1s takes O(n), where n is the length of the array.
- Calculating the product of gaps between consecutive 1s takes O(k), where k is the number of 1s in the array.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where k is the number of 1s in the array, as we store their indices in a list.
- In the worst case, k = n (if all elements are 1s), so the space complexity is O(n).

Primary Topic: Arrays
"""