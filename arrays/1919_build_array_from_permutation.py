# LeetCode Problem #1919: Build Array from Permutation

"""
Problem Statement:
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where:
    ans[i] = nums[nums[i]] for each 0 <= i < nums.length.
Return the array ans.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < nums.length
- The elements in nums are distinct.

Example:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
"""

class Solution:
    def buildArray(self, nums):
        """
        Build the array ans where ans[i] = nums[nums[i]].

        :param nums: List[int] - A zero-based permutation of integers.
        :return: List[int] - The resulting array.
        """
        # Using list comprehension to construct the result array
        return [nums[nums[i]] for i in range(len(nums))]

# Example test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [0, 2, 1, 5, 3, 4]
    print(solution.buildArray(nums1))  # Output: [0, 1, 2, 4, 5, 3]
    
    # Test case 2
    nums2 = [5, 0, 1, 2, 3, 4]
    print(solution.buildArray(nums2))  # Output: [4, 5, 0, 1, 2, 3]

    # Test case 3
    nums3 = [3, 2, 1, 0]
    print(solution.buildArray(nums3))  # Output: [0, 1, 2, 3]

"""
Time Complexity:
- The solution iterates through the nums array once, and for each index i, it accesses nums[i] and nums[nums[i]].
- Accessing elements in a list is O(1), so the overall time complexity is O(n), where n is the length of nums.

Space Complexity:
- The solution uses a new list to store the result, which requires O(n) space.
- No additional space is used apart from the output list, so the space complexity is O(n).

Topic: Arrays
"""