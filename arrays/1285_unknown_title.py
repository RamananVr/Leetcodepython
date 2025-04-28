"""
LeetCode Problem #1285: Find the Start and End Number of Continuous Ranges

Problem Statement:
You are given a sorted, strictly increasing integer array `nums` and an integer `k`. 
The array `nums` represents a set of numbers that are already included in a range. 
Your task is to find the `k-th` missing number in the range `[1, nums[-1] + k]`.

Example:
Input: nums = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: The missing numbers are [1, 5, 6, 8, 9]. The 5th missing number is 9.

Constraints:
1. 1 <= nums.length <= 1000
2. 1 <= nums[i] <= 1000
3. 1 <= k <= 1000
4. nums is sorted in strictly increasing order.

"""

# Solution
def findKthPositive(nums, k):
    """
    Finds the k-th missing positive integer from the sorted array nums.

    :param nums: List[int] - A sorted, strictly increasing list of integers.
    :param k: int - The k-th missing number to find.
    :return: int - The k-th missing positive integer.
    """
    missing_count = 0
    current = 1
    index = 0

    while True:
        if index < len(nums) and nums[index] == current:
            # If the current number is in nums, move to the next number in nums
            index += 1
        else:
            # If the current number is missing, increment the missing count
            missing_count += 1
            if missing_count == k:
                return current
        current += 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4, 7, 11]
    k1 = 5
    print(findKthPositive(nums1, k1))  # Output: 9

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 2
    print(findKthPositive(nums2, k2))  # Output: 6

    # Test Case 3
    nums3 = [3, 10, 20]
    k3 = 15
    print(findKthPositive(nums3, k3))  # Output: 18

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(findKthPositive(nums4, k4))  # Output: 6

    # Test Case 5
    nums5 = [5, 6, 7, 8, 9]
    k5 = 3
    print(findKthPositive(nums5, k5))  # Output: 3


# Time and Space Complexity Analysis
"""
Time Complexity:
- The while loop iterates through the range of numbers until the k-th missing number is found.
- In the worst case, the loop runs for O(k + n), where n is the length of nums. 
  This is because we may need to iterate through all the missing numbers and the elements in nums.

Space Complexity:
- The algorithm uses O(1) additional space since it only uses a few variables to track the current number, index, and missing count.

Overall Complexity:
- Time: O(k + n)
- Space: O(1)
"""

# Topic: Arrays