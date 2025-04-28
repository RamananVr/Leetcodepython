"""
LeetCode Problem #532: K-diff Pairs in an Array

Problem Statement:
Given an array of integers `nums` and an integer `k`, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where:
- 0 <= i, j < nums.length
- i != j
- |nums[i] - nums[j]| == k

Notice that |x| denotes the absolute value of x.

Example 1:
Input: nums = [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array: (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array: (1, 2), (2, 3), (3, 4), and (4, 5).

Example 3:
Input: nums = [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array: (1, 1).

Constraints:
- 1 <= nums.length <= 10^4
- -10^7 <= nums[i] <= 10^7
- 0 <= k <= 10^7
"""

# Clean and Correct Python Solution
def findPairs(nums, k):
    if k < 0:
        return 0  # k-diff pairs cannot exist for negative k

    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    count = 0
    if k == 0:
        # For k = 0, we need to find elements that appear more than once
        for num in num_count:
            if num_count[num] > 1:
                count += 1
    else:
        # For k > 0, we need to find unique pairs (num, num + k)
        for num in num_count:
            if num + k in num_count:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 4, 1, 5]
    k1 = 2
    print(findPairs(nums1, k1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    print(findPairs(nums2, k2))  # Output: 4

    # Test Case 3
    nums3 = [1, 3, 1, 5, 4]
    k3 = 0
    print(findPairs(nums3, k3))  # Output: 1

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = -1
    print(findPairs(nums4, k4))  # Output: 0 (k cannot be negative)

    # Test Case 5
    nums5 = [1, 1, 1, 2, 2]
    k5 = 1
    print(findPairs(nums5, k5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- O(n): We iterate through the array once to build the frequency dictionary (O(n)).
- For k > 0, we iterate through the keys of the dictionary to check for pairs (O(n)).
- Overall, the time complexity is O(n).

Space Complexity:
- O(n): We use a dictionary to store the frequency of each number in the array.
"""

# Topic: Arrays, Hash Table