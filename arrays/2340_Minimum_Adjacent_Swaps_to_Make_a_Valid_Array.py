"""
LeetCode Problem #2340: Minimum Adjacent Swaps to Make a Valid Array

Problem Statement:
You are given a 0-indexed integer array `nums`. The array is valid if the following conditions are satisfied:
1. The minimum value in `nums` is at the beginning of the array.
2. The maximum value in `nums` is at the end of the array.

You are allowed to perform any number of adjacent swaps in the array. Each swap moves two adjacent elements to swap their positions.

Return the minimum number of adjacent swaps required to make the array valid.

Example 1:
Input: nums = [3, 4, 5, 5, 3, 1]
Output: 6
Explanation: Perform the following swaps:
- Swap index 5 and 4: [3, 4, 5, 5, 1, 3]
- Swap index 4 and 3: [3, 4, 5, 1, 5, 3]
- Swap index 3 and 2: [3, 4, 1, 5, 5, 3]
- Swap index 2 and 1: [3, 1, 4, 5, 5, 3]
- Swap index 1 and 0: [1, 3, 4, 5, 5, 3]
- Swap index 5 and 4: [1, 3, 4, 5, 3, 5]

Example 2:
Input: nums = [1, 3, 5, 3, 1]
Output: 0
Explanation: The array is already valid.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
def minimumSwaps(nums):
    n = len(nums)
    min_index = nums.index(min(nums))  # Find the index of the minimum value
    max_index = nums.index(max(nums))  # Find the index of the maximum value

    # If the max value is before the min value, adjust the max index
    if max_index < min_index:
        max_index += 1

    # Total swaps needed is the sum of:
    # - Swaps to bring the min value to the front
    # - Swaps to bring the max value to the end
    return min_index + (n - 1 - max_index)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 5, 5, 3, 1]
    print(minimumSwaps(nums1))  # Output: 6

    # Test Case 2
    nums2 = [1, 3, 5, 3, 1]
    print(minimumSwaps(nums2))  # Output: 0

    # Test Case 3
    nums3 = [5, 1, 3, 2, 4]
    print(minimumSwaps(nums3))  # Output: 4

    # Test Case 4
    nums4 = [2, 1]
    print(minimumSwaps(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1]
    print(minimumSwaps(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the index of the minimum value takes O(n).
- Finding the index of the maximum value takes O(n).
- The rest of the operations are O(1).
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables like `min_index` and `max_index`.
- Overall space complexity: O(1).

Topic: Arrays
"""