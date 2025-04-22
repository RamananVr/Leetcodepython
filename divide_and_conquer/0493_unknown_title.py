"""
LeetCode Problem #493: Reverse Pairs

Problem Statement:
Given an integer array `nums`, return the number of reverse pairs in the array.

A reverse pair is a pair `(i, j)` where:
- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""

# Solution
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start: int, end: int) -> int:
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Count reverse pairs
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Merge the two halves
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            # Copy sorted elements back to nums
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            
            return count
        
        return merge_sort(0, len(nums) - 1)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 3, 2, 3, 1]
    print(solution.reversePairs(nums1))  # Output: 2
    
    # Test Case 2
    nums2 = [2, 4, 3, 5, 1]
    print(solution.reversePairs(nums2))  # Output: 3
    
    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(solution.reversePairs(nums3))  # Output: 4
    
    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(solution.reversePairs(nums4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The merge sort algorithm divides the array into halves recursively, which takes O(log n) levels of recursion.
- At each level, we count reverse pairs and merge the two halves, which takes O(n) time.
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The algorithm uses a temporary array for merging, which takes O(n) space.
- The recursion stack depth is O(log n).
- Therefore, the overall space complexity is O(n).

Topic: Divide and Conquer
"""