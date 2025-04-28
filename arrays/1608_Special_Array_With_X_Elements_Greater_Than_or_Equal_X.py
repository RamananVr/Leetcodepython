"""
LeetCode Problem #1608: Special Array With X Elements Greater Than or Equal X

Problem Statement:
You are given an array `nums` of non-negative integers. `nums` is considered special if there exists a number `x` such that there are exactly `x` numbers in `nums` that are greater than or equal to `x`.

Notice that `x` does not have to be an element in `nums`.

Return `x` if the array is special, otherwise, return `-1`. It can be proven that if `x` is valid, it is unique.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""

def specialArray(nums):
    """
    Function to find the special number x in the array nums.
    """
    nums.sort(reverse=True)  # Sort in descending order
    for x in range(1, len(nums) + 1):
        if nums[x - 1] >= x and (x == len(nums) or nums[x] < x):
            return x
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5]
    print(specialArray(nums1))  # Output: 2

    # Test Case 2
    nums2 = [0, 0]
    print(specialArray(nums2))  # Output: -1

    # Test Case 3
    nums3 = [0, 4, 3, 0, 4]
    print(specialArray(nums3))  # Output: 3

    # Test Case 4
    nums4 = [3, 6, 7, 7, 0]
    print(specialArray(nums4))  # Output: -1

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop runs at most n times, so the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(1) as we are sorting the array in place and using a constant amount of extra space.

Topic: Arrays
"""