"""
LeetCode Question #1920: Build Array from Permutation

Problem Statement:
------------------
Given a zero-based permutation `nums` (0-indexed), build an array `ans` of the same length where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and return it.

A zero-based permutation `nums` is an array of distinct integers from `0` to `nums.length - 1` (inclusive).

Example 1:
----------
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]

Example 2:
----------
Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]

Constraints:
------------
- 1 <= nums.length <= 1000
- 0 <= nums[i] < nums.length
- The elements in `nums` are distinct.

Follow-up:
----------
Can you solve it without using an extra space (i.e., O(1) memory)?

"""

# Clean, Correct Python Solution
def buildArray(nums):
    """
    Build an array from the given permutation.

    Args:
    nums (List[int]): A zero-based permutation array.

    Returns:
    List[int]: The resulting array built from the permutation.
    """
    return [nums[nums[i]] for i in range(len(nums))]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 2, 1, 5, 3, 4]
    print(buildArray(nums1))  # Output: [0, 1, 2, 4, 5, 3]

    # Test Case 2
    nums2 = [5, 0, 1, 2, 3, 4]
    print(buildArray(nums2))  # Output: [4, 5, 0, 1, 2, 3]

    # Test Case 3
    nums3 = [3, 2, 1, 0]
    print(buildArray(nums3))  # Output: [0, 1, 2, 3]

    # Test Case 4
    nums4 = [0]
    print(buildArray(nums4))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
----------------
The solution iterates through the array `nums` once to construct the result array `ans`. 
Accessing `nums[nums[i]]` is an O(1) operation. Therefore, the time complexity is O(n), 
where n is the length of the input array `nums`.

Space Complexity:
-----------------
The solution uses a list comprehension to construct the result array `ans`, which requires 
O(n) space to store the output. Thus, the space complexity is O(n).

Follow-up Note:
---------------
The follow-up asks for an O(1) space solution. This can be achieved by modifying the input 
array in-place using mathematical encoding techniques, but the current solution does not 
address that.

Topic: Arrays
"""