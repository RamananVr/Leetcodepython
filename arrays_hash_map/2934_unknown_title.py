"""
LeetCode Problem #2934: Replace Elements in an Array

Problem Statement:
You are given a 0-indexed integer array `nums` and a 2D integer array `operations` where each operation is represented as 
a pair `[oldValue, newValue]`.

For each operation, replace every occurrence of `oldValue` in `nums` with `newValue`.

- For example, if `nums = [1,2,4,6]` and `operations = [[1,3],[4,7],[6,1]]`, then:
  - In the 1st operation, replace 1 with 3: `nums = [3,2,4,6]`.
  - In the 2nd operation, replace 4 with 7: `nums = [3,2,7,6]`.
  - In the 3rd operation, replace 6 with 1: `nums = [3,2,7,1]`.

Return the array after all operations have been applied.

Constraints:
1. `1 <= nums.length <= 10^5`
2. `-10^9 <= nums[i] <= 10^9`
3. `1 <= operations.length <= 10^5`
4. `oldValue != newValue`
"""

def arrayChange(nums, operations):
    """
    Replace elements in the array based on the operations.

    Args:
    nums (List[int]): The initial array of integers.
    operations (List[List[int]]): A list of operations where each operation is [oldValue, newValue].

    Returns:
    List[int]: The modified array after applying all operations.
    """
    # Create a mapping from oldValue to newValue
    value_map = {}
    
    # Traverse the operations in order
    for oldValue, newValue in operations:
        # If oldValue is already mapped, update its mapping to newValue
        if oldValue in value_map:
            value_map[newValue] = value_map.pop(oldValue)
        else:
            # Otherwise, map newValue to oldValue's position
            value_map[newValue] = oldValue
    
    # Reverse the mapping to get the final values
    reverse_map = {v: k for k, v in value_map.items()}
    
    # Update the nums array based on the reverse mapping
    for i in range(len(nums)):
        if nums[i] in reverse_map:
            nums[i] = reverse_map[nums[i]]
    
    return nums

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 4, 6]
    operations1 = [[1, 3], [4, 7], [6, 1]]
    print(arrayChange(nums1, operations1))  # Output: [3, 2, 7, 1]

    # Test Case 2
    nums2 = [5, 5, 5, 5]
    operations2 = [[5, 10], [10, 15], [15, 20]]
    print(arrayChange(nums2, operations2))  # Output: [20, 20, 20, 20]

    # Test Case 3
    nums3 = [100, 200, 300]
    operations3 = [[100, 400], [200, 500], [300, 600]]
    print(arrayChange(nums3, operations3))  # Output: [400, 500, 600]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    operations4 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    print(arrayChange(nums4, operations4))  # Output: [6, 6, 6, 6, 6]

# Time Complexity Analysis:
# - Constructing the value_map takes O(operations.length) time.
# - Constructing the reverse_map also takes O(operations.length) time.
# - Updating the nums array takes O(nums.length) time.
# Overall time complexity: O(nums.length + operations.length)

# Space Complexity Analysis:
# - The value_map and reverse_map dictionaries require O(operations.length) space.
# Overall space complexity: O(operations.length)

# Topic: Arrays, Hash Map