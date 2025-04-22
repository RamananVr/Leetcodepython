"""
LeetCode Problem #26: Remove Duplicates from Sorted Array

Problem Statement:
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:
1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. 
   The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

Custom Judge:
The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.
"""

# Clean, Correct Python Solution
def removeDuplicates(nums):
    """
    Removes duplicates from a sorted array in-place and returns the number of unique elements.

    :param nums: List[int] - A sorted list of integers
    :return: int - The number of unique elements in the array
    """
    if not nums:
        return 0

    # Pointer for the position of the last unique element
    unique_index = 0

    # Iterate through the array
    for i in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    # The number of unique elements is unique_index + 1
    return unique_index + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2]
    k1 = removeDuplicates(nums1)
    print(f"Output: {k1}, Modified Array: {nums1[:k1]}")  # Output: 2, Modified Array: [1, 2]

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = removeDuplicates(nums2)
    print(f"Output: {k2}, Modified Array: {nums2[:k2]}")  # Output: 5, Modified Array: [0, 1, 2, 3, 4]

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = removeDuplicates(nums3)
    print(f"Output: {k3}, Modified Array: {nums3[:k3]}")  # Output: 5, Modified Array: [1, 2, 3, 4, 5]

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = removeDuplicates(nums4)
    print(f"Output: {k4}, Modified Array: {nums4[:k4]}")  # Output: 1, Modified Array: [1]

    # Test Case 5
    nums5 = []
    k5 = removeDuplicates(nums5)
    print(f"Output: {k5}, Modified Array: {nums5[:k5]}")  # Output: 0, Modified Array: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few variables).
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays