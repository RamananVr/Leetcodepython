"""
LeetCode Problem #2970: Maximum Number of K-Pairs

Problem Statement:
You are given an integer array `nums` and an integer `k`. A pair `(i, j)` is called a k-pair if:
- `nums[i] + nums[j] == k`
- `i != j`

Return the maximum number of k-pairs you can form. Each element in the array can be used at most once in a pair.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: The pairs are (1, 4) and (2, 3).

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: The only pair is (3, 3).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
"""

from collections import Counter

def maxOperations(nums, k):
    """
    Function to calculate the maximum number of k-pairs in the array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The target sum for pairs.

    Returns:
    int: The maximum number of k-pairs.
    """
    count = Counter(nums)
    operations = 0

    for num in count:
        complement = k - num
        if complement in count:
            if num == complement:
                # If num and complement are the same, we can only form pairs within the count of num
                operations += count[num] // 2
            else:
                # Otherwise, take the minimum count of num and its complement
                operations += min(count[num], count[complement])
    
    return operations // 2 if num==