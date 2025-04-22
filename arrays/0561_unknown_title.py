"""
LeetCode Problem #561: Array Partition

Problem Statement:
Given an integer array `nums` of 2n integers, group these integers into n pairs 
such that the sum of the minimum of each pair is maximized. Return the maximized sum.

Example:
Input: nums = [1,4,3,2]
Output: 4
Explanation: The optimal pairing is (1, 2) and (3, 4). The sum of the minimums is 1 + 3 = 4.

Constraints:
- 1 <= n <= 10^4
- nums.length == 2 * n
- -10^4 <= nums[i] <= 10^4
"""

# Solution
def arrayPairSum(nums):
    """
    Function to calculate the maximum sum of the minimums of pairs.
    
    Args:
    nums (List[int]): List of integers of length 2n.
    
    Returns:
    int: Maximized sum of the minimums of pairs.
    """
    # Sort the array
    nums.sort()
    
    # Sum up every alternate element starting from the first
    return sum(nums[i] for i in range(0, len(nums), 2))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 3, 2]
    print(arrayPairSum(nums1))  # Output: 4

    # Test Case 2
    nums2 = [6, 2, 6, 5, 1, 2]
    print(arrayPairSum(nums2))  # Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(arrayPairSum(nums3))  # Output: 2

    # Test Case 4
    nums4 = [-1, -2, -3, -4]
    print(arrayPairSum(nums4))  # Output: -6

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Summing up every alternate element takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so no additional space is used.
- Overall space complexity: O(1).
"""

# Topic: Arrays