"""
LeetCode Problem #1389: Create Target Array in the Given Order

Problem Statement:
Given two arrays of integers `nums` and `index`. Your task is to create a target array under the following rules:
- Initially, the target array is empty.
- From left to right, read the elements of `nums` and `index`. Insert at index `index[i]` the value `nums[i]` in the target array.
- Repeat the above steps until there are no elements to read in `nums` and `index`.

Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]

Example 2:
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]

Constraints:
- 1 <= nums.length, index.length <= 100
- nums.length == index.length
- 0 <= nums[i] <= 100
- 0 <= index[i] <= i
"""

# Clean and Correct Python Solution
def createTargetArray(nums, index):
    """
    Create the target array based on the given nums and index arrays.

    Args:
    nums (List[int]): List of integers to insert into the target array.
    index (List[int]): List of indices specifying where to insert elements.

    Returns:
    List[int]: The resulting target array.
    """
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 2, 3, 4]
    index1 = [0, 1, 2, 2, 1]
    print(createTargetArray(nums1, index1))  # Output: [0, 4, 1, 3, 2]

    # Test Case 2
    nums2 = [1, 2, 3, 4, 0]
    index2 = [0, 1, 2, 3, 0]
    print(createTargetArray(nums2, index2))  # Output: [0, 1, 2, 3, 4]

    # Test Case 3
    nums3 = [1]
    index3 = [0]
    print(createTargetArray(nums3, index3))  # Output: [1]

    # Test Case 4
    nums4 = [4, 2, 3, 1]
    index4 = [0, 1, 2, 0]
    print(createTargetArray(nums4, index4))  # Output: [1, 4, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `insert` operation in a Python list takes O(n) in the worst case, where n is the size of the list.
- Since we perform the `insert` operation for each element in `nums` (of size m), the overall time complexity is O(m^2), where m is the length of the `nums` array.

Space Complexity:
- The space complexity is O(m), where m is the length of the `nums` array, as we are creating a new list `target` to store the result.

Topic: Arrays
"""