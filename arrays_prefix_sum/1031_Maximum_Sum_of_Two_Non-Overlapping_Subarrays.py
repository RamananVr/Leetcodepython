"""
LeetCode Problem #1031: Maximum Sum of Two Non-Overlapping Subarrays

Problem Statement:
Given an integer array `nums` and two integers `firstLen` and `secondLen`, return the maximum sum of the elements in two non-overlapping subarrays with lengths `firstLen` and `secondLen`.

The subarrays should not overlap, and the order of the subarrays does not matter. For example, a `firstLen`-length subarray followed by a `secondLen`-length subarray or vice versa is valid.

Example:
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1 and [6,5] with length 2.

Constraints:
- 1 <= firstLen, secondLen <= 1000
- firstLen + secondLen <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    """
    Function to calculate the maximum sum of two non-overlapping subarrays.

    Args:
    nums (List[int]): The input array of integers.
    firstLen (int): The length of the first subarray.
    secondLen (int): The length of the second subarray.

    Returns:
    int: The maximum sum of the two non-overlapping subarrays.
    """
    def maxSum(L, M):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        maxL, maxSum = 0, 0
        
        # Iterate through the array to find the maximum sum
        for i in range(L + M, n + 1):
            maxL = max(maxL, prefix_sum[i - M] - prefix_sum[i - M - L])
            maxSum = max(maxSum, maxL + prefix_sum[i] - prefix_sum[i - M])
        
        return maxSum

    # Try both orders: firstLen followed by secondLen, and secondLen followed by firstLen
    return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    firstLen = 1
    secondLen = 2
    print(maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 20

    # Test Case 2
    nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    firstLen = 3
    secondLen = 2
    print(maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 29

    # Test Case 3
    nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    firstLen = 4
    secondLen = 3
    print(maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 31


"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing the prefix sum takes O(n), where n is the length of the input array `nums`.
- The main loop iterates through the array once, performing constant-time operations for each index. This also takes O(n).
- Since we compute the result for two different orders (firstLen followed by secondLen, and vice versa), the total time complexity is O(n).

Space Complexity:
- The prefix sum array requires O(n) additional space.
- The overall space complexity is O(n).

Topic: Arrays, Prefix Sum
"""