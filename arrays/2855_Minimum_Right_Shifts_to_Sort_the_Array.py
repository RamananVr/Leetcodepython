"""
LeetCode Problem #2855: Minimum Right Shifts to Sort the Array

Problem Statement:
You are given a 0-indexed array `nums` of length `n`. The array `nums` is circular, meaning that the first element of the array is the next element of the last element, and the last element of the array is the previous element of the first element.

You need to find the minimum number of right shifts required to sort the array in non-decreasing order. A right shift means moving the last element of the array to the first position. If the array is already sorted, no right shifts are needed, and you should return `0`. If it is impossible to sort the array using any number of right shifts, return `-1`.

Example:
Input: nums = [3, 4, 5, 1, 2]
Output: 2
Explanation: After 2 right shifts, the array becomes [1, 2, 3, 4, 5], which is sorted.

Constraints:
- `n == nums.length`
- `1 <= n <= 100`
- `1 <= nums[i] <= 100`
"""

def minimumRightShifts(nums):
    """
    Function to calculate the minimum number of right shifts required to sort the array.
    
    :param nums: List[int] - The input array
    :return: int - Minimum number of right shifts required, or -1 if not possible
    """
    n = len(nums)
    
    # Check if the array is already sorted
    if nums == sorted(nums):
        return 0
    
    # Find the index where the array can be split into two sorted parts
    for i in range(1, n):
        if nums[i:] + nums[:i] == sorted(nums):
            return n - i
    
    # If no valid split is found, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 5, 1, 2]
    print(minimumRightShifts(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(minimumRightShifts(nums2))  # Output: 0

    # Test Case 3
    nums3 = [2, 1, 3, 4]
    print(minimumRightShifts(nums3))  # Output: -1

    # Test Case 4
    nums4 = [5, 1, 2, 3, 4]
    print(minimumRightShifts(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1]
    print(minimumRightShifts(nums5))  # Output: 0

"""
Time Complexity Analysis:
- The function iterates through the array to check for valid splits. For each split, it creates a new array by concatenating two parts and compares it with the sorted version of the array.
- Sorting the array takes O(n log n), and checking equality for each split takes O(n). Since there are n possible splits, the overall complexity is O(n^2 + n log n), which simplifies to O(n^2) for large n.

Space Complexity Analysis:
- The function creates a sorted version of the array, which takes O(n) space.
- Additionally, for each split, a new array of size n is created, but this is temporary and does not affect the overall space complexity.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""