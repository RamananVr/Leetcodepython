"""
LeetCode Problem #961: N-Repeated Element in Size 2N Array

Problem Statement:
You are given an integer array `nums` with a length of `2n` where `n >= 2`.
The array contains `n + 1` unique elements, and exactly one of these elements is repeated `n` times.

Return the element that is repeated `n` times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

Constraints:
- 2 <= n <= 5000
- nums.length == 2 * n
- 0 <= nums[i] <= 10^4
- nums contains `n + 1` unique elements and one of them is repeated exactly `n` times.
"""

# Clean and Correct Python Solution
def repeatedNTimes(nums):
    """
    Finds the element that is repeated n times in the array.

    :param nums: List[int] - The input array of size 2n
    :return: int - The element repeated n times
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # This line should never be reached due to problem constraints.

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 3]
    print(repeatedNTimes(nums1))  # Output: 3

    # Test Case 2
    nums2 = [2, 1, 2, 5, 3, 2]
    print(repeatedNTimes(nums2))  # Output: 2

    # Test Case 3
    nums3 = [5, 1, 5, 2, 5, 3, 5, 4]
    print(repeatedNTimes(nums3))  # Output: 5

    # Test Case 4
    nums4 = [9, 9, 1, 2, 3, 4, 5, 6]
    print(repeatedNTimes(nums4))  # Output: 9

    # Test Case 5
    nums5 = [7, 8, 7, 9, 10, 7, 11, 7]
    print(repeatedNTimes(nums5))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a set to store seen elements. In the worst case, the set will contain n unique elements.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays