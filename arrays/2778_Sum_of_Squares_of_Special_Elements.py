"""
LeetCode Problem #2778: Sum of Squares of Special Elements

Problem Statement:
You are given a 1-indexed integer array `nums` of length `n`.

An element `nums[i]` of `nums` is called special if `i` divides `n`, i.e., `n % i == 0`.

Return the sum of the squares of all special elements of `nums`.

Example:
Input: nums = [2, 7, 1, 19, 18, 3], Output: 63
Explanation:
- The length of nums is n = 6.
- The special elements are nums[1] = 2, nums[2] = 7, nums[3] = 1, and nums[6] = 3.
- Their squares are 2^2 = 4, 7^2 = 49, 1^2 = 1, and 3^2 = 9.
- The sum of squares is 4 + 49 + 1 + 9 = 63.

Constraints:
- 1 <= nums.length == n <= 50
- 1 <= nums[i] <= 100
"""

def sum_of_squares(nums):
    """
    Calculate the sum of squares of special elements in the array.

    Args:
    nums (List[int]): A 1-indexed list of integers.

    Returns:
    int: The sum of squares of special elements.
    """
    n = len(nums)
    result = 0
    for i in range(1, n + 1):  # 1-indexed
        if n % i == 0:  # Check if i divides n
            result += nums[i - 1] ** 2  # Add the square of the special element
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 1, 19, 18, 3]
    print(sum_of_squares(nums1))  # Output: 63

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(sum_of_squares(nums2))  # Output: 26

    # Test Case 3
    nums3 = [10, 20, 30, 40, 50, 60, 70]
    print(sum_of_squares(nums3))  # Output: 4900

    # Test Case 4
    nums4 = [1]
    print(sum_of_squares(nums4))  # Output: 1

    # Test Case 5
    nums5 = [5, 10, 15, 20, 25, 30]
    print(sum_of_squares(nums5))  # Output: 1300

"""
Time Complexity:
- The loop iterates from 1 to n (inclusive), where n is the length of the array.
- For each iteration, we perform a constant-time operation (checking divisibility and squaring).
- Therefore, the time complexity is O(n).

Space Complexity:
- We use a single integer variable `result` to store the sum.
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""