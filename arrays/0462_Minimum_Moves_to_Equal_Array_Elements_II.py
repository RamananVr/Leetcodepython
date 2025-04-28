"""
LeetCode Problem #462: Minimum Moves to Equal Array Elements II

Problem Statement:
Given an integer array `nums` of size `n`, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.

Test cases are designed such that the answer will fit in a 32-bit integer.

Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
"""

from typing import List

def minMoves2(nums: List[int]) -> int:
    """
    This function calculates the minimum number of moves required to make all elements in the array equal.
    The optimal solution involves aligning all elements to the median of the array.
    """
    nums.sort()
    median = nums[len(nums) // 2]  # Median minimizes the sum of absolute differences
    return sum(abs(num - median) for num in nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(minMoves2(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 10, 2, 9]
    print(minMoves2(nums2))  # Output: 16

    # Test Case 3
    nums3 = [1, 0, 0, 8, 6]
    print(minMoves2(nums3))  # Output: 14

    # Test Case 4
    nums4 = [1]
    print(minMoves2(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 2, 2, 2, 3]
    print(minMoves2(nums5))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Calculating the sum of absolute differences takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation may require O(n) additional space depending on the sorting algorithm used.
- The function itself uses O(1) additional space.
- Overall space complexity: O(n) (due to sorting).

Topic: Arrays
"""