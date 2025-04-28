"""
LeetCode Problem #327: Count of Range Sum

Problem Statement:
Given an integer array `nums` and two integers `lower` and `upper`, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where `i <= j`.

Example 1:
Input: nums = [-2, 5, -1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are:
- [0, 0] -> -2
- [2, 2] -> -1
- [0, 2] -> 2

Example 2:
Input: nums = [0], lower = 0, upper = 0
Output: 1

Constraints:
- 1 <= nums.length <= 100,000
- -2^31 <= nums[i] <= 2^31 - 1
- -10^5 <= lower <= upper <= 10^5
"""

# Solution
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(start, end):
            if start == end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Count the valid range sums
            j = k = mid + 1
            for left in prefix_sums[start:mid + 1]:
                while k <= end and prefix_sums[k] - left < lower:
                    k += 1
                while j <= end and prefix_sums[j] - left <= upper:
                    j += 1
                count += j - k
            
            # Merge the two halves
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if prefix_sums[i] <= prefix_sums[j]:
                    temp.append(prefix_sums[i])
                    i += 1
                else:
                    temp.append(prefix_sums[j])
                    j += 1
            while i <= mid:
                temp.append(prefix_sums[i])
                i += 1
            while j <= end:
                temp.append(prefix_sums[j])
                j += 1
            
            # Copy the sorted array back
            for i in range(len(temp)):
                prefix_sums[start + i] = temp[i]
            
            return count
        
        # Compute prefix sums
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        # Perform merge sort and count range sums
        return merge_sort(0, len(prefix_sums) - 1)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(solution.countRangeSum(nums, lower, upper))  # Output: 3
    
    # Test Case 2
    nums = [0]
    lower = 0
    upper = 0
    print(solution.countRangeSum(nums, lower, upper))  # Output: 1
    
    # Test Case 3
    nums = [1, 2, 3, 4]
    lower = 3
    upper = 6
    print(solution.countRangeSum(nums, lower, upper))  # Output: 4

"""
Time Complexity:
- The merge sort algorithm runs in O(n log n), where n is the length of the prefix sums array.
- Counting the valid range sums during the merge step takes O(n) for each level of recursion.
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(n) space for the prefix sums array and O(n) additional space for the temporary array during merging.
- Overall space complexity: O(n).

Topic: Divide and Conquer
"""