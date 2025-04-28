"""
LeetCode Question #2321: Maximum Score Of Spliced Array

Problem Statement:
You are given two 0-indexed integer arrays nums1 and nums2, both of length n.

You can choose any number of elements (possibly zero) from nums1 and replace them with the corresponding elements from nums2. This operation is called "splicing". The score of nums1 after splicing is the sum of its elements.

Return the maximum possible score you can achieve after splicing nums1.

Example 1:
Input: nums1 = [60, 60, 60], nums2 = [10, 90, 10]
Output: 210
Explanation: Choose the second element of nums1 to splice with nums2. 
The resulting nums1 is [60, 90, 60], and its score is 210.

Example 2:
Input: nums1 = [20, 40, 20, 70, 30], nums2 = [50, 20, 50, 40, 20]
Output: 220
Explanation: Choose the first and third elements of nums1 to splice with nums2. 
The resulting nums1 is [50, 40, 50, 70, 30], and its score is 220.

Example 3:
Input: nums1 = [7, 11, 13], nums2 = [1, 1, 1]
Output: 31
Explanation: No splicing is needed. The resulting nums1 is [7, 11, 13], and its score is 31.

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^4
"""

# Python Solution
def maximumsSplicedArray(nums1, nums2):
    def maxSubarraySumDifference(arr1, arr2):
        # Calculate the maximum subarray sum of the difference between arr2 and arr1
        max_diff = 0
        current_diff = 0
        for i in range(len(arr1)):
            current_diff += arr2[i] - arr1[i]
            if current_diff < 0:
                current_diff = 0
            max_diff = max(max_diff, current_diff)
        return max_diff

    # Calculate the total sum of nums1 and nums2
    sum_nums1 = sum(nums1)
    sum_nums2 = sum(nums2)

    # Calculate the maximum score by splicing nums1 with nums2 and vice versa
    max_score_from_nums1 = sum_nums1 + maxSubarraySumDifference(nums1, nums2)
    max_score_from_nums2 = sum_nums2 + maxSubarraySumDifference(nums2, nums1)

    # Return the maximum score
    return max(max_score_from_nums1, max_score_from_nums2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [60, 60, 60]
    nums2 = [10, 90, 10]
    print(maximumsSplicedArray(nums1, nums2))  # Output: 210

    # Test Case 2
    nums1 = [20, 40, 20, 70, 30]
    nums2 = [50, 20, 50, 40, 20]
    print(maximumsSplicedArray(nums1, nums2))  # Output: 220

    # Test Case 3
    nums1 = [7, 11, 13]
    nums2 = [1, 1, 1]
    print(maximumsSplicedArray(nums1, nums2))  # Output: 31

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function maxSubarraySumDifference iterates through the arrays once, which takes O(n) time.
- The main function calls maxSubarraySumDifference twice, so the overall time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Overall Complexity:
Time: O(n)
Space: O(1)
"""

# Topic: Arrays, Dynamic Programming (Kadane's Algorithm)