"""
LeetCode Problem #912: Sort an Array

Problem Statement:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using the built-in sort function in your programming language.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4
"""

# Solution: Merge Sort Implementation
def sortArray(nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        # Append remaining elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array
    
    return merge_sort(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 2, 3, 1]
    print(sortArray(nums1))  # Output: [1, 2, 3, 5]

    # Test Case 2
    nums2 = [5, 1, 1, 2, 0, 0]
    print(sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]

    # Test Case 3
    nums3 = [3, -1, 0, -5, 2, 4]
    print(sortArray(nums3))  # Output: [-5, -1, 0, 2, 3, 4]

    # Test Case 4
    nums4 = [1]
    print(sortArray(nums4))  # Output: [1]

    # Test Case 5
    nums5 = [10, -10, 0, 5, -5]
    print(sortArray(nums5))  # Output: [-10, -5, 0, 5, 10]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Merge Sort has a time complexity of O(n log n), where n is the number of elements in the array.
- The array is repeatedly divided into halves (log n levels), and merging takes O(n) time at each level.

Space Complexity:
- The space complexity is O(n) due to the auxiliary space required for merging the arrays.
- Additionally, the recursion stack depth is O(log n) for dividing the array.

Topic: Arrays
"""