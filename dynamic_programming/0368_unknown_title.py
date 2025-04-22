"""
LeetCode Problem #368: Largest Divisible Subset

Problem Statement:
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
    answer[i] % answer[j] == 0 or answer[j] % answer[i] == 0.

If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 10^9
- All the integers in nums are unique.
"""

def largestDivisibleSubset(nums):
    """
    Finds the largest divisible subset of a given list of distinct positive integers.

    :param nums: List[int] - A list of distinct positive integers.
    :return: List[int] - The largest divisible subset.
    """
    if not nums:
        return []

    # Step 1: Sort the numbers
    nums.sort()

    # Step 2: Initialize DP arrays
    dp = [1] * len(nums)  # dp[i] will store the size of the largest subset ending with nums[i]
    prev = [-1] * len(nums)  # prev[i] will store the index of the previous element in the subset

    # Step 3: Fill DP arrays
    max_size = 0
    max_index = -1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_size:
            max_size = dp[i]
            max_index = i

    # Step 4: Reconstruct the largest divisible subset
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev[max_index]

    return result[::-1]  # Reverse the result to get the correct order

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print("Input:", nums1)
    print("Output:", largestDivisibleSubset(nums1))  # Expected: [1, 2] or [1, 3]

    # Test Case 2
    nums2 = [1, 2, 4, 8]
    print("Input:", nums2)
    print("Output:", largestDivisibleSubset(nums2))  # Expected: [1, 2, 4, 8]

    # Test Case 3
    nums3 = [4, 8, 10, 240]
    print("Input:", nums3)
    print("Output:", largestDivisibleSubset(nums3))  # Expected: [4, 8, 240]

    # Test Case 4
    nums4 = [3, 5, 10, 20, 21]
    print("Input:", nums4)
    print("Output:", largestDivisibleSubset(nums4))  # Expected: [5, 10, 20]

    # Test Case 5
    nums5 = [1]
    print("Input:", nums5)
    print("Output:", largestDivisibleSubset(nums5))  # Expected: [1]

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of nums.
- The nested loops to fill the dp array take O(n^2).
- Reconstructing the subset takes O(n).
- Overall time complexity: O(n^2).

Space Complexity:
- The dp and prev arrays each take O(n) space.
- The result array takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Dynamic Programming
"""