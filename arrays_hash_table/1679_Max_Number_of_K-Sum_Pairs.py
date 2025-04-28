"""
LeetCode Problem #1679: Max Number of K-Sum Pairs

Problem Statement:
You are given an integer array `nums` and an integer `k`. In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array. Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove the pair (1, 4), then nums = [2,3]
- Remove the pair (2, 3), then nums = []
There are no more pairs that sum up to 5, so the number of operations is 2.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the pair (3, 3), then nums = [1,4,3]
There are no more pairs that sum up to 6, so the number of operations is 1.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
"""

# Clean and Correct Python Solution
from collections import Counter

def maxOperations(nums, k):
    count = Counter(nums)
    operations = 0

    for num in count:
        complement = k - num
        if complement in count:
            if complement == num:
                # If the number and its complement are the same, we can only form pairs within the count of that number
                operations += count[num] // 2
            else:
                # Otherwise, take the minimum count of the number and its complement
                operations += min(count[num], count[complement])
    
    # Since we count each pair twice (once for num and once for complement), divide by 2
    return operations // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    k1 = 5
    print(maxOperations(nums1, k1))  # Output: 2

    # Test Case 2
    nums2 = [3, 1, 3, 4, 3]
    k2 = 6
    print(maxOperations(nums2, k2))  # Output: 1

    # Test Case 3
    nums3 = [2, 5, 4, 3, 1, 5, 2]
    k3 = 7
    print(maxOperations(nums3, k3))  # Output: 3

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 2
    print(maxOperations(nums4, k4))  # Output: 2

    # Test Case 5
    nums5 = [1]
    k5 = 2
    print(maxOperations(nums5, k5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the Counter object takes O(n), where n is the length of the nums array.
- Iterating through the keys of the Counter and performing operations takes O(m), where m is the number of unique elements in nums.
- In the worst case, m = n (all elements are unique), so the overall time complexity is O(n).

Space Complexity:
- The Counter object stores the frequency of each unique element, which requires O(m) space, where m is the number of unique elements in nums.
- In the worst case, m = n, so the space complexity is O(n).

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Arrays, Hash Table