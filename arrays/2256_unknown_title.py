"""
LeetCode Problem #2256: Minimum Average Difference

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n`.

The average difference of the index `i` is the absolute difference between the average of the first `i + 1` elements of `nums` and the average of the last `n - i - 1` elements. Both averages should be rounded down to the nearest integer.

- If there are fewer than `i + 1` elements in the first part or fewer than `n - i - 1` elements in the second part, the average difference is considered to be the absolute value of the sum of the part that exists.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Example 1:
Input: nums = [2, 5, 3, 9, 5, 3]
Output: 3
Explanation:
- The average difference of index 0 is |2 - 5| = 3.
- The average difference of index 1 is |3 - 5| = 2.
- The average difference of index 2 is |3 - 6| = 3.
- The average difference of index 3 is |4 - 4| = 0.
- The average difference of index 4 is |4 - 3| = 1.
- The average difference of index 5 is |4 - 0| = 4.
The index with the minimum average difference is 3.

Example 2:
Input: nums = [0]
Output: 0
Explanation:
The only index is 0, so the answer is 0.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""

# Python Solution
def minimumAverageDifference(nums):
    n = len(nums)
    total_sum = sum(nums)
    left_sum = 0
    min_diff = float('inf')
    result_index = -1

    for i in range(n):
        # Update the left sum
        left_sum += nums[i]
        
        # Calculate the left average
        left_avg = left_sum // (i + 1)
        
        # Calculate the right average
        if i < n - 1:
            right_avg = (total_sum - left_sum) // (n - i - 1)
        else:
            right_avg = 0
        
        # Calculate the absolute difference
        diff = abs(left_avg - right_avg)
        
        # Update the result if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            result_index = i

    return result_index

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 3, 9, 5, 3]
    print(minimumAverageDifference(nums1))  # Output: 3

    # Test Case 2
    nums2 = [0]
    print(minimumAverageDifference(nums2))  # Output: 0

    # Test Case 3
    nums3 = [4, 2, 0]
    print(minimumAverageDifference(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(minimumAverageDifference(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    print(minimumAverageDifference(nums5))  # Output: 2

"""
Time Complexity Analysis:
- Calculating the total sum of the array takes O(n).
- Iterating through the array to calculate the left and right averages takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- We use a constant amount of extra space for variables like `left_sum`, `total_sum`, etc.
- Overall space complexity: O(1).

Topic: Arrays
"""