"""
LeetCode Problem #80: Remove Duplicates from Sorted Array II

Problem Statement:
Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. 
More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. 
It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];

If all assertions pass, then your solution is correct.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    """
    Removes duplicates from the sorted array such that each unique element appears at most twice.
    Modifies the array in-place and returns the new length.

    :param nums: List[int] - The input sorted array
    :return: int - The length of the modified array
    """
    if not nums:
        return 0

    # Pointer to place the next valid element
    write_index = 0

    # Iterate through the array
    for num in nums:
        # If we are at the start or the current number can be added without exceeding the "at most twice" condition
        if write_index < 2 or num != nums[write_index - 2]:
            nums[write_index] = num
            write_index += 1

    return write_index


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = removeDuplicates(nums1)
    print(nums1[:k1])  # Output: [1, 1, 2, 2, 3]
    print(k1)          # Output: 5

    # Test Case 2
    nums2 = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3]
    k2 = removeDuplicates(nums2)
    print(nums2[:k2])  # Output: [0, 0, 1, 1, 2, 2, 3, 3]
    print(k2)          # Output: 8

    # Test Case 3
    nums3 = [1, 1, 2, 2, 2, 3, 3, 3, 3]
    k3 = removeDuplicates(nums3)
    print(nums3[:k3])  # Output: [1, 1, 2, 2, 3, 3]
    print(k3)          # Output: 6

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = removeDuplicates(nums4)
    print(nums4[:k4])  # Output: [1, 1]
    print(k4)          # Output: 2

    # Test Case 5
    nums5 = []
    k5 = removeDuplicates(nums5)
    print(nums5[:k5])  # Output: []
    print(k5)          # Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm modifies the array in-place and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""