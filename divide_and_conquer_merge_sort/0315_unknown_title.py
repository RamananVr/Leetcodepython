"""
LeetCode Problem #315: Count of Smaller Numbers After Self

Problem Statement:
You are given an integer array `nums` and you have to return a new counts array. 
The counts array has the property where `counts[i]` is the number of smaller elements 
to the right of `nums[i]`.

Example:
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is only 1 smaller element (1).
To the right of 1 there are no smaller elements.
"""

# Solution
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return smaller

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [5, 2, 6, 1]
    print(solution.countSmaller(nums1))  # Output: [2, 1, 1, 0]
    
    # Test Case 2
    nums2 = [3, 4, 9, 6, 1]
    print(solution.countSmaller(nums2))  # Output: [1, 1, 2, 1, 0]
    
    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(solution.countSmaller(nums3))  # Output: [0, 0, 0, 0]
    
    # Test Case 4
    nums4 = [4, 3, 2, 1]
    print(solution.countSmaller(nums4))  # Output: [3, 2, 1, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
The solution uses a modified merge sort algorithm, which has a time complexity of O(n log n), 
where n is the length of the input array `nums`. The merge step involves comparing elements 
and updating the `smaller` array, which is efficient due to the sorted nature of the subarrays.

Space Complexity:
The space complexity is O(n), where n is the length of the input array `nums`. This is due to 
the auxiliary space used for the `enum` list and the `smaller` array.

Topic: Divide and Conquer, Merge Sort
"""