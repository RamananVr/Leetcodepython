"""
LeetCode Problem #27: Remove Element

Problem Statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead 
have the result be placed in the first part of the array nums. More formally, if there are k 
elements after removing the duplicates, then the first k elements of nums should hold the final 
result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array 
in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:

    nums = [...]; val = ...
    k = removeElement(nums, val)
    assert k == expected_k
    assert sorted(nums[:k]) == sorted(expected_result)

If all assertions pass, then your solution will be accepted.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""

def removeElement(nums, val):
    """
    Removes all occurrences of val from nums in-place and returns the new length of the array.

    Args:
    nums (List[int]): The input array of integers.
    val (int): The value to be removed.

    Returns:
    int: The new length of the array after removing val.
    """
    # Initialize a pointer for the position of the next valid element
    k = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is not equal to val, move it to the k-th position
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    # Return the new length of the array
    return k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = removeElement(nums1, val1)
    print(f"Output: {k1}, Modified Array: {nums1[:k1]}")  # Output: 2, Modified Array: [2, 2]

    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = removeElement(nums2, val2)
    print(f"Output: {k2}, Modified Array: {nums2[:k2]}")  # Output: 5, Modified Array: [0, 1, 3, 0, 4]

    # Test Case 3
    nums3 = []
    val3 = 1
    k3 = removeElement(nums3, val3)
    print(f"Output: {k3}, Modified Array: {nums3[:k3]}")  # Output: 0, Modified Array: []

    # Test Case 4
    nums4 = [4, 4, 4, 4]
    val4 = 4
    k4 = removeElement(nums4, val4)
    print(f"Output: {k4}, Modified Array: {nums4[:k4]}")  # Output: 0, Modified Array: []

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    val5 = 6
    k5 = removeElement(nums5, val5)
    print(f"Output: {k5}, Modified Array: {nums5[:k5]}")  # Output: 5, Modified Array: [1, 2, 3, 4, 5]

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the length of the input array nums. We iterate through the array once.
# Space Complexity: O(1), as we do not use any additional space and modify the array in-place.

# Topic: Arrays