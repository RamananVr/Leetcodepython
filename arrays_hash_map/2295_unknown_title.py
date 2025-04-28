"""
LeetCode Problem #2295: Replace Elements in an Array

Problem Statement:
You are given a 0-indexed array `nums` that consists of `n` distinct integers. You are also given a 2D array `operations` where `operations[i] = [oldValue, newValue]` indicates that you should replace the value `oldValue` in `nums` with `newValue`.

- There will be exactly one `oldValue` in `nums` for each `operation[i]`.
- Perform all the operations in order, and return the resulting array.

Constraints:
1. `n == nums.length`
2. `1 <= n, operations.length <= 10^5`
3. `-10^9 <= nums[i], oldValue, newValue <= 10^9`
4. All the values of `nums` are distinct.
5. Each `oldValue` in `operations` exists in `nums`.

Example:
Input: nums = [1, 2, 4, 6], operations = [[1, 3], [4, 7], [6, 1]]
Output: [3, 2, 7, 1]
Explanation:
- Replace 1 with 3: [3, 2, 4, 6]
- Replace 4 with 7: [3, 2, 7, 6]
- Replace 6 with 1: [3, 2, 7, 1]
"""

# Python Solution
def arrayChange(nums, operations):
    # Create a mapping from the current value to its index in nums
    value_to_index = {value: idx for idx, value in enumerate(nums)}
    
    # Process each operation
    for old_value, new_value in operations:
        # Find the index of the old value
        index = value_to_index[old_value]
        
        # Update nums at the found index
        nums[index] = new_value
        
        # Update the mapping to reflect the new value
        value_to_index[new_value] = index
        
        # Remove the old value from the mapping
        del value_to_index[old_value]
    
    return nums

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 4, 6]
    operations1 = [[1, 3], [4, 7], [6, 1]]
    print(arrayChange(nums1, operations1))  # Output: [3, 2, 7, 1]

    # Test Case 2
    nums2 = [10, 20, 30, 40]
    operations2 = [[10, 15], [20, 25], [30, 35], [40, 45]]
    print(arrayChange(nums2, operations2))  # Output: [15, 25, 35, 45]

    # Test Case 3
    nums3 = [5, 6, 7, 8]
    operations3 = [[5, 9], [9, 10], [10, 11]]
    print(arrayChange(nums3, operations3))  # Output: [11, 6, 7, 8]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `value_to_index` dictionary takes O(n), where n is the length of `nums`.
- Processing each operation takes O(1) for lookup, update, and deletion in the dictionary.
- Since there are m operations, the total time complexity is O(n + m).

Space Complexity:
- The `value_to_index` dictionary requires O(n) space to store the mapping of values to indices.
- The space complexity is O(n).
"""

# Topic: Arrays, Hash Map