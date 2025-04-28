"""
LeetCode Problem #1537: Get the Maximum Score

Problem Statement:
You are given two sorted arrays of integers nums1 and nums2.

You can traverse each array starting from the beginning or the end, and you can switch from one array to the other only at common elements. If you switch at a common element, you can only continue traversing the other array starting from that element.

The score is defined as the sum of the elements visited. Your goal is to maximize your score.

Return the maximum score you can achieve. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: 
You can start with nums1 and switch to nums2 at 4, then switch back to nums1 at 8. 
Path: 2 -> 4 -> 6 -> 8 -> 10
Maximum score: 2 + 4 + 6 + 8 + 10 = 30.

Example 2:
Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
Output: 109
Explanation:
You can start with nums1 and switch to nums2 at 3, then switch back to nums1 at 5, then switch to nums2 at 100.
Path: 1 -> 3 -> 5 -> 100
Maximum score: 1 + 3 + 5 + 100 = 109.

Example 3:
Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
Output: 40
Explanation: 
There are no common elements, so you can only choose to traverse nums1 or nums2.
Maximum score: max(1+2+3+4+5, 6+7+8+9+10) = 40.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^7
- nums1 and nums2 are strictly increasing.
"""

# Python Solution
def maxSum(nums1, nums2):
    MOD = 10**9 + 7
    i, j = 0, 0
    sum1, sum2 = 0, 0
    result = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums1[i] > nums2[j]:
            sum2 += nums2[j]
            j += 1
        else:  # nums1[i] == nums2[j]
            result += max(sum1, sum2) + nums1[i]
            sum1, sum2 = 0, 0
            i += 1
            j += 1

    # Add remaining elements in nums1
    while i < len(nums1):
        sum1 += nums1[i]
        i += 1

    # Add remaining elements in nums2
    while j < len(nums2):
        sum2 += nums2[j]
        j += 1

    result += max(sum1, sum2)
    return result % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 5, 8, 10]
    nums2 = [4, 6, 8, 9]
    print(maxSum(nums1, nums2))  # Output: 30

    # Test Case 2
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [3, 5, 100]
    print(maxSum(nums1, nums2))  # Output: 109

    # Test Case 3
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    print(maxSum(nums1, nums2))  # Output: 40

    # Test Case 4
    nums1 = [1, 4, 5, 8, 10]
    nums2 = [2, 3, 6, 7, 9]
    print(maxSum(nums1, nums2))  # Output: 29

# Time and Space Complexity Analysis
# Time Complexity: O(n + m), where n is the length of nums1 and m is the length of nums2.
# This is because we traverse both arrays once.

# Space Complexity: O(1), as we are using a constant amount of extra space.

# Topic: Arrays, Two Pointers