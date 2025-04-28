"""
LeetCode Problem #2044: Count Number of Maximum Bitwise-OR Subsets

Problem Statement:
Given an integer array `nums`, find the number of non-empty subsets of `nums` such that the bitwise OR of every element in the subset is equal to the maximum possible bitwise OR of `nums`.

A subset is a selection of elements (possibly none) of the array such that the order of the elements is not changed. Two subsets are different if the indices of the elements chosen are different.

Return the number of subsets with the maximum bitwise OR.

Example 1:
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR is 3. There are 2 subsets with a bitwise OR equal to 3: [3] and [3,1].

Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets have a bitwise OR of 2. There are 7 subsets in total.

Example 3:
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR is 7. There are 6 subsets with a bitwise OR equal to 7.

Constraints:
- 1 <= nums.length <= 16
- 1 <= nums[i] <= 10^5
"""

# Python Solution
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Calculate the maximum possible bitwise OR
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Step 2: Use backtracking to count subsets with the maximum OR
        count = 0

        def backtrack(index: int, current_or: int):
            nonlocal count
            # Base case: if we've considered all elements
            if index == len(nums):
                if current_or == max_or:
                    count += 1
                return
            
            # Include the current element in the subset
            backtrack(index + 1, current_or | nums[index])
            # Exclude the current element from the subset
            backtrack(index + 1, current_or)
        
        # Start backtracking from the first index with an initial OR of 0
        backtrack(0, 0)
        return count

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [3, 1]
    print(solution.countMaxOrSubsets(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 2, 2]
    print(solution.countMaxOrSubsets(nums2))  # Output: 7

    # Test Case 3
    nums3 = [3, 2, 1, 5]
    print(solution.countMaxOrSubsets(nums3))  # Output: 6

    # Additional Test Case 4
    nums4 = [1, 2, 4]
    print(solution.countMaxOrSubsets(nums4))  # Output: 4

    # Additional Test Case 5
    nums5 = [1]
    print(solution.countMaxOrSubsets(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The total number of subsets of an array of size `n` is `2^n`.
   - For each subset, we compute the bitwise OR, which takes O(1) time.
   - Therefore, the time complexity is O(2^n).

2. Space Complexity:
   - The recursion stack can go as deep as `n` (the size of the input array).
   - Thus, the space complexity is O(n).

Topic: Backtracking
"""