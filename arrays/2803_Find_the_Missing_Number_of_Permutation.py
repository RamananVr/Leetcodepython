"""
LeetCode Problem #2803: Find the Missing Number of Permutation

Problem Statement:
You are given an integer array `nums` of length `n` containing all the numbers from `0` to `n` except one. 
Find and return the missing number.

Example 1:
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number in the array.

Example 2:
Input: nums = [0, 1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2]. 2 is the missing number in the array.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0, 9]. 8 is the missing number in the array.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Follow up:
Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

# Solution
def missingNumber(nums):
    """
    Finds the missing number in the permutation array.

    Args:
    nums (List[int]): The input array containing numbers from 0 to n except one.

    Returns:
    int: The missing number.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
    actual_sum = sum(nums)          # Sum of numbers in the array
    return expected_sum - actual_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 0, 1]
    print(missingNumber(nums1))  # Output: 2

    # Test Case 2
    nums2 = [0, 1]
    print(missingNumber(nums2))  # Output: 2

    # Test Case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums3))  # Output: 8

    # Test Case 4
    nums4 = [0]
    print(missingNumber(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1]
    print(missingNumber(nums5))  # Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of the array takes O(n) time.
- Calculating the expected sum using the formula is O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses only a constant amount of extra space (O(1)).
- No additional data structures are used.
"""

# Topic: Arrays