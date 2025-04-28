"""
LeetCode Problem #1589: Maximum Sum Obtained of Any Permutation

Problem Statement:
You are given an array of integers `nums` (0-indexed) and an array of integer pairs `requests` where `requests[i] = [start_i, end_i]`. 
The `i-th` request asks for the sum of `nums[start_i] + nums[start_i+1] + ... + nums[end_i]` (inclusive). 
You can rearrange `nums` in any order. You want to maximize the total sum of all requests among all permutations of `nums`.

Return the maximum total sum of all requests modulo 10^9 + 7.

Example 1:
Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [5,2,3,4,1]. The sum of the requests is:
- requests[0] -> nums[1] + nums[2] + nums[3] = 2 + 3 + 4 = 9
- requests[1] -> nums[0] + nums[1] = 5 + 2 = 7
Total sum = 9 + 7 = 16, which is the maximum.

Example 2:
Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation of nums is [6,5,4,3,2,1]. The sum of the requests is:
- requests[0] -> nums[0] + nums[1] = 6 + 5 = 11
Total sum = 11, which is the maximum.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= requests.length <= 10^5
- requests[i].length == 2
- 0 <= start_i <= end_i < nums.length
"""

from typing import List

def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # Step 1: Create a frequency array to count how many times each index is requested
    freq = [0] * (n + 1)
    for start, end in requests:
        freq[start] += 1
        if end + 1 < n:
            freq[end + 1] -= 1
    
    # Step 2: Compute the prefix sum of the frequency array
    for i in range(1, n):
        freq[i] += freq[i - 1]
    
    # Step 3: Remove the extra element and sort the frequency array
    freq.pop()
    freq.sort(reverse=True)
    
    # Step 4: Sort nums in descending order
    nums.sort(reverse=True)
    
    # Step 5: Compute the maximum sum
    max_sum = 0
    for i in range(n):
        max_sum += freq[i] * nums[i]
        max_sum %= MOD
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    requests1 = [[1, 3], [0, 1]]
    print(maxSumRangeQuery(nums1, requests1))  # Output: 19

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5, 6]
    requests2 = [[0, 1]]
    print(maxSumRangeQuery(nums2, requests2))  # Output: 11

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6]
    requests3 = [[0, 3], [2, 5], [1, 4]]
    print(maxSumRangeQuery(nums3, requests3))  # Output: 47

"""
Time Complexity Analysis:
1. Constructing the frequency array takes O(requests.length).
2. Computing the prefix sum of the frequency array takes O(nums.length).
3. Sorting the frequency array and nums both take O(nums.length * log(nums.length)).
4. Calculating the maximum sum takes O(nums.length).

Overall Time Complexity: O(n log n + m), where n = len(nums) and m = len(requests).

Space Complexity Analysis:
1. The frequency array takes O(nums.length) space.
2. Other auxiliary variables take O(1) space.

Overall Space Complexity: O(n), where n = len(nums).

Topic: Arrays, Sorting, Prefix Sum
"""